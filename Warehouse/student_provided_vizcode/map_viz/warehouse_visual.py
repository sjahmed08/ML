import pygame
import sys
from math import * 

PI = pi

def print_array(s, a):
    print s
    for i in a:
        print i

# colors
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0,0)
RED = pygame.Color(255, 0, 0) 
COLOR_ROBOT = pygame.Color(204, 0, 0) 
COLOR_DROPAREA = pygame.Color(102, 255, 102) 
COLOR_TARGET = pygame.Color(255, 153, 51) 

class warehouse_visualizer:    
    
    params = None
    
    def __init__(self):
        pass

    def visualize(self, params, sub_cell_div = 3):
        # decalare 
        warehouse = None
        grid = []
        todo = []
        droparea = []
        max_distance = 100.0
        max_steering = 0.0
        heading = 0.0
        current_x = 0.0
        current_y = 0.0
        current_cell = [0.0, 0.0]
        path = []
        backpath = []
        
        #init
        warehouse = params['warehouse']
        todo = params['todo']

        grid = [[0 for row in range(len(warehouse[0])*sub_cell_div)]
                        for col in range(len(warehouse)*sub_cell_div)]

        # Setup the grid
        for i in range(len(warehouse)):
            for j in range(len(warehouse[i])):
                if warehouse[i][j] == '@':
                    droparea = [i * sub_cell_div + 1, j * sub_cell_div + 1]
                elif warehouse[i][j] == '#':
                    for w in range(sub_cell_div):
                            for h in range(sub_cell_div):
                                r = i * sub_cell_div + w
                                c = j * sub_cell_div + h                        
                                if r >=0 and c >=0 and r < len(grid) and c < len(grid[0]):
                                    grid[r][c] = 1

        # print out for debug
        #print_array('grid', grid)
        
        # margin
        margin = [50, 50]
        size = [len(grid), len(grid[0])]
        cell_size = [100.0/sub_cell_div, 100.0/sub_cell_div]

        # init pygame
        pygame.init()
        w = int(margin[0] * 2 + cell_size[0] * (size[1]))
        h = int(margin[1] * 2 + cell_size[1] *(size[0]))
        screen = pygame.display.set_mode((w, h))
        screen.fill(WHITE)
        
        # Draw cells
        for i in range(len(grid)):     
            for j in range(len(grid[0])):
                start_x = cell_size[0] * (j) 
                start_y = cell_size[1] * (i)                
                color = BLACK
                width = 1
                
                if grid[i][j] == 1:
                    width = 0
                    
                pygame.draw.rect(screen, BLACK, (margin[0] + start_x, margin[1] + start_y, cell_size[0], cell_size[1] ), width)

        # Draw boxes         
        for i in todo:
                pygame.draw.rect(screen, COLOR_TARGET, (margin[0] + i[0] * 100 -10, margin[1] + i[1] * -100 -10 ,20,20), 0)

        # Captions
        pygame.draw.rect(screen, COLOR_DROPAREA, (margin[0] + (droparea[1]-1) * (cell_size[0]), margin[1] + (droparea[0] -1 )* (cell_size[1]) ,100,100), 0)    
        
        x = margin[0] + (droparea[1] - 1 + sub_cell_div/4.0 ) * (cell_size[0])
        y = margin[1] + (droparea[0] - 1 + sub_cell_div/4.0 ) * (cell_size[1])
        r = pygame.draw.rect(screen, RED, (x,y,50,50), 0)

        font = pygame.font.Font('freesansbold.ttf', 12) 
        text = font.render('Test Case' + str(params['test_case']), True, BLACK) 
        textRect = text.get_rect()  
        textRect.center = (w/2., margin[1] - 40) 
        screen.blit(text, textRect)  
        
        # draw x and y axis
        for i in range(len(grid) + 1):
            if i % sub_cell_div == 0:                
                text = font.render(str(i/sub_cell_div), True, BLACK) 
                textRect = text.get_rect()  
                textRect.center = (margin[0] - 20, margin[1] + cell_size[1] * (i)) 
                screen.blit(text, textRect)   
                
        for i in range(len(grid[0]) + 1):
            if i % sub_cell_div == 0:
                text = font.render(str(i/sub_cell_div), True, BLACK) 
                textRect = text.get_rect()  
                textRect.center = (margin[0] + cell_size[1] * (i), margin[1] -20 ) 
                screen.blit(text, textRect)   
                
        while True: # main game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                else:
                    pygame.display.update()
                    
    
    def run_with_params(self, params):
        self.params = params

    #------------------------------------------------
    # test cases copy and paste from Part B
    #------------------------------------------------
    def test_case1(self):
        params = {'test_case': 1,
                  'warehouse': ['..#..',
                                '.....',
                                '..#..',
                                '.....',
                                '....@'],
                  'todo': [(1.5, -0.5),
                           (4.0, -2.5)],
                  'max_distance': 5.0,
                  'max_steering': PI / 2. + 0.01,
                  'min_cost': 38.}

        self.run_with_params(params)
    
    def test_case2(self):
        params = {'test_case': 2,
                  'warehouse': ['..#..@',
                                '......',
                                '..####',
                                '..#...',
                                '......'],
                  'todo': [(3.5,-3.5),
                           (0.5,-1.0)],
                  'max_distance': 5.0,
                  'max_steering': PI / 2. + 0.01,
                  'min_cost': 56.}

        self.run_with_params(params)
    
    def test_case3(self):
        params = {'test_case': 3,
                  'warehouse': ['..#...',
                                '......',
                                '..####',
                                '..#..#',
                                '.....@'],
                  'todo': [(4.5, -1.0),
                           (3.5, -3.5)],
                  'max_distance': 5.0,
                  'max_steering': PI/2.+0.01,
                  'min_cost': 43.0}

        self.run_with_params(params)

    def test_case4(self):
        params = {'test_case': 4,
                  'warehouse': ['..#...',
                                '......',
                                '..##.#',
                                '..#..#',
                                '.....@'],
                  'todo': [(4.5, -1.0),
                           (3.5, -3.5)],
                  'max_distance': 5.0,
                  'max_steering': PI / 2. + 0.01,
                  'min_cost': 30.0}

        self.run_with_params(params)

    def test_case5(self):
        params = {'test_case': 5,
                  'warehouse': ['..#...',
                                '#....#',
                                '..##.#',
                                '..#..#',
                                '#....@'],
                  'todo': [(1.0, -.5),
                           (0.5, -3.5)],
                  'max_distance': 5.0,
                  'max_steering': PI / 2. + 0.01,
                  'min_cost': 50.0}

        self.run_with_params(params)

    def test_case6(self):
        params = {'test_case': 6,
                  'warehouse': ['@.#...#',
                                '#...#..'],
                  'todo': [(4.5, -.5),
                           (6.0, -1.5)],
                  'max_distance': 5.0,
                  'max_steering': PI / 2. + 0.01,
                  'min_cost': 61.5}

        self.run_with_params(params)

    # ## CREDIT TO: James Corbitt for the following test cases
    def test_case7(self):
        params = {'test_case': 7,
                  'warehouse': ['#.@.#',
                                '..#..'],
                  'todo': [(0.5, -1.5),
                           (4.5, -1.5)],
                  'max_distance': 5.0,
                  'max_steering': PI / 2. + 0.01,
                  'min_cost': 29.4857865623}

        self.run_with_params(params)
    
    def test_case8(self):
        params = {'test_case': 8,
                  'warehouse': ['#.@.#'],
                  'todo': [(1.5, -0.5),
                           (3.5, -0.5)],
                  'max_distance': 5.0,
                  'max_steering': PI / 2. + 0.01,
                  'min_cost': 15.9980798485}

        self.run_with_params(params)

    def test_case9(self):
        params = {'test_case': 9,
                  'warehouse': ['#.######',
                                '#.#....#',
                                '#.#.##.#',
                                '#.#.@#.#',
                                '#.####.#',
                                '#......#',
                                '########'],
                  'todo': [(3.5, -3.5),
                           (3.5, -2.5),
                           (3.5, -1.5),
                           (4.5, -1.5),
                           (5.5, -1.5),
                           (6.5, -2.5),
                           (6.5, -3.5),
                           (6.5, -4.5),
                           (6.5, -5.5),
                           (5.5, -5.5),
                           (4.5, -5.5),
                           (3.5, -5.5),
                           (2.5, -5.5),
                           (1.5, -4.5),
                           (1.5, -3.5),
                           (1.5, -2.5),
                           (1.5, -1.5),
                           (1.5, -0.5)],
                  'max_distance': 3.0,
                  'max_steering': PI / 2. + 0.01,
                  'min_cost': 603.432133513}

        self.run_with_params(params)

    def test_case10(self):
        params = {'test_case': 10,
                  'warehouse': ['#######.',
                                '#.......',
                                '#@......'],
                  'todo': [(7.5, -1.5),
                           (7.5, -0.5)],
                  'max_distance': 3.0,
                  'max_steering': PI / 2. + 0.01,
                  'min_cost': 42.8704538273}

        self.run_with_params(params)
    
# ---------------------------------
#  end copy & paste
# --------------------------------- 
    
def main():   
    v = warehouse_visualizer()
    if len(sys.argv) > 2:
        f = getattr(v, 'test_case' + sys.argv[1])
        f()
        v.visualize(v.params, 3)
    else:
        for i in range(1, 11):
            f = getattr(v, 'test_case' + str(i))
            f()
            v.visualize(v.params, 3)

if __name__ == '__main__':
    main()