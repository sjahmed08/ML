from turtle import *
import time
import re

def get_walls(warehouse):
    walls=[]
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j]=='#':
                wall_center=j+.5,(i+.5)*-1
                print wall_center
                walls.append(wall_center)
            if warehouse[i][j]=='@':
                start_loc=j+.5,(i+.5)*-1
                start=start_loc
    return walls,start
    
def obstacles(length,x,y):
    #print 'x,y',x,y
    size=length*.5
    #print 'size',size
    #loop for each side of the square
    penup()
    #print 'corner',x-size,y+size
    #goto(x,y)
    goto(x-size,y+size)
    pendown()
    if length==.3:
        color("green")
    if length==.2:
        color("red")
    if length==1.5:
        color("black")
    fill(True)
    for i in range(4):
        #move forwards and turn at right angle
        write(position())
        forward(length)
        right(90)
    fill(False)
    penup()

def draw_path_moves(start, moves):
    hold=0
    fill(False)
    color("blue")
    radians()
    penup()
    setposition(start[0],start[1])
    pendown()
    
    for i in range(len(moves)):
        move_parts=re.split(" ",moves[i])
        if move_parts[0]!='move':
            time.sleep(3)
            #write('lift/down')
            hold=1
        if move_parts[0]=='move':
            left(float(move_parts[1]))
            forward(float(move_parts[2]))
            if hold==0:
                write(position())

def draw_path_coords(start,coords):
    fill(False)
    color("orange")
    radians()
    penup()
    setposition(start[0],start[1])
    pendown()
    for i in range(len(coords)):
        setposition(coords[i][0],coords[i][1])
        
############## MAIN ########################
warehouse=['..#..',
                                '.....',
                                '..#..',
                                '.....',
                                '....@']
todo=[(1.5, -0.5),(4.0, -2.5)]
moves = ['move 1.58079632679 0 ', 'move 0.775398163397 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move -0.785398163397 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.785398163397 0.141421356237', 'move 8.881784197e-16 0.141421356237', 'move 0.0 0.141421356237', 'move 1.33226762955e-15 0.141421356237', 'move 0.785398163397 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move -0.785398163397 0.141421356237', 'move 2.22044604925e-15 0.141421356237', 'move -1.33226762955e-15 0.141421356237', 'lift 0', 'move -1.58079632679 0 ', 'move -1.56079632679 0.141421356237', 'move 8.881784197e-16 0.141421356237', 'move -2.22044604925e-15 0.141421356237', 'move 0.785398163397 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move -0.785398163397 0.141421356237', 'move -8.881784197e-16 0.141421356237', 'move 0.0 0.141421356237', 'move -8.881784197e-16 0.141421356237', 'move -0.785398163397 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move -0.785398163397 0.141421356237', 'move 1.57079632679 0.141421356237', 'move 2.22044604925e-15 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move 2.22044604925e-15 0.141421356237', 'move -4.4408920985e-15 0.141421356237', 'move 2.22044604925e-15 0.141421356237', 'move 2.22044604925e-15 0.141421356237', 'move -6.66133814775e-15 0.141421356237', 'move 8.881784197e-15 0.141421356237', 'move -8.881784197e-15 0.141421356237', 'move 8.881784197e-15 0.141421356237', 'move 0.785398163397 0.1', 'down 4.5 -4.5', 'move 1.58079632679 0 ', 'move 0.775398163397 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move -1.57079632679 0.141421356237', 'move -2.22044604925e-15 0.141421356237', 'move 0.0 0.141421356237', 'move 1.57079632679 0.141421356237', 'move 2.22044604925e-15 0.141421356237', 'move -4.4408920985e-15 0.141421356237', 'move 2.22044604925e-15 0.141421356237', 'move 0.0 0.141421356237', 'move -1.57079632679 0.141421356237', 'move -2.22044604925e-15 0.141421356237', 'move 4.4408920985e-15 0.141421356237', 'move -2.22044604925e-15 0.141421356237', 'move 0.0 0.141421356237', 'move 1.57079632679 0.141421356237', 'move 2.22044604925e-15 0.141421356237', 'move -4.4408920985e-15 0.141421356237', 'move 2.22044604925e-15 0.141421356237', 'move 0.0 0.141421356237', 'lift 1', 'move -1.58079632679 0 ', 'move -1.56079632679 0.141421356237', 'move 0.0 0.141421356237', 'move 0.785398163397 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move 0.785398163397 0.141421356237', 'move -1.57079632679 0.141421356237', 'move 0.785398163397 0.1', 'move 0.0 0.1', 'move 0.0 0.1', 'move -0.785398163397 0.141421356237', 'move 1.57079632679 0.141421356237', 'move 2.22044604925e-15 0.141421356237', 'move 0.0 0.141421356237', 'move 0.0 0.141421356237', 'move 2.22044604925e-15 0.141421356237', 'move -4.4408920985e-15 0.141421356237', 'move 2.22044604925e-15 0.141421356237', 'move 2.22044604925e-15 0.141421356237', 'move -6.66133814775e-15 0.141421356237', 'move 8.881784197e-15 0.141421356237', 'move -8.881784197e-15 0.141421356237', 'move 8.881784197e-15 0.141421356237', 'move 0.785398163397 0.1', 'down 4.5 -4.5']
# moves=['move 1.58079632679 0' , 'move 1.56079632679 .50', 'move -1.56079632679 2'] #, 'move 1.58079632679 0', 'move 1.58079632679 0', 'move 0.558002603548 1.80277563773', 'move -1.58079632679 0', 'move -1.58079632679 0', 'move -1.55079632679 1.60118641699e-15', 'move 1.58079632679 0', 'move 1.58079632679 0', 'move 0.962793723247 2.5', 'move 1.57079632679 2.22044604925e-16', 'move 1.57079632679 2.5', 'move 1.58079632679 0', 'move 1.58079632679 0', 'move 1.55079632679 2.22044604925e-16', 'move 1.58079632679 0', 'move 0.578002603548 1.80277563773', 'move 0.982793723247 2.22044604925e-16', 'move 0.0 2.5']
# moves = ['move 1.570963 2.0',  # rotate and move north 2 spaces
#                   'move 1.570963 0.1',  # rotate west and move closer to second box
#                   'lift 1',             # lift the second box
#                   'move 0.785398 1.5',  # rotate to sw and move down 1.5 squares
#                   'down 3.5 -4.0',      # set the box out of the way
#                   'move -0.785398 2.0',  # rotate to west and move 2.5 squares
#                   'move -1.570963 2.7',  # rotate to north and move to pick up box 0
#                   'lift 0',             # lift the first box
#                   'move -1.570963 0.0',  # rotate to the south east
#                   'move -0.785398 1.0',  # finish rotation
#                   'move 0.785398 2.5',  # rotate to east and move
#                   'move -1.570963 2.5',  # rotate and move south
#                   'down 4.5 -4.5',      # set down the box in the dropzone
#                   'move -1.570963 0.6',  # rotate to west and move towards box 1
#                   'lift 1',             # lift the second box
#                   'move 1.570963 0.0',  # rotate north
#                   'move 1.570963 0.6',  # rotate east and move back towards dropzone
#                   'down 4.5 -4.5']      # deliver second box
coords=[[4.5, -4.5], (2.0, -4.5), (1.0, -3.0), (1.0, -0.5), (1.0, -3.0), (2.0, -4.5), [4.5, -4.5]]

##### set coordinates to match warehouse
setworldcoordinates(0, (len(warehouse[0]))*-1, len(warehouse), 0)
turtlesize(stretch_wid=5, stretch_len=5)

# get walls and start from warehouse
walls, start = get_walls(warehouse)

#draw walls on turtle display
for i in range(len(walls)):
    #print walls[i][0],walls[i][1]
    obstacles(1.5,walls[i][0],walls[i][1])

## draw boxes from todo
for i in range(len(todo)):
    obstacles(.3,todo[i][0],todo[i][1])
    
# mark your collisons
###put your collisons in this list to be drawn in red
collisions=[[3.20,-3.20]]
for i in range(len(collisions)):
    obstacles(.2,collisions[i][0],collisions[i][1])

###### draw path - from start and moves list
draw_path_moves(start, moves)

##### draw path form coords

draw_path_coords(start,coords)


print window_width()
print window_height()
exitonclick()