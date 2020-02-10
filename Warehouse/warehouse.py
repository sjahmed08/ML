######################################################################
# This file copyright the Georgia Institute of Technology
#
# Permission is given to students to use or modify this file (only)
# to work on their assignments.
#
# You may NOT publish this file or make it available to others not in
# the course.
#
######################################################################

'''
=== Introduction ===

Your file must be called `warehouse.py` and must have two classes
  called `DeliveryPlanner_PartA` and `DeliveryPlanner_PartB`.

- You may add additional classes and functions as needed provided they are all in this file `warehouse.py`.
- You may share code between partA and partB but it MUST BE IN THIS FILE
- Upload warehouse.py to Canvas in the Assignments section. Do NOT put it into an 
  archive with other files.
- Your warehouse.py file must not execute any code when imported.
- Ask any questions about the directions or specifications on Piazza.

=== Grading ===

- Your planner will be graded against a set of test cases, each equally weighted.
- If your planner returns a list of moves of total cost that is K times the minimum cost of 
  successfully completing the task, you will receive 1/K of the credit for that test case.
- Otherwise, you will receive no credit for that test case. This could happen for one of several 
  reasons including (but not necessarily limited to):
  - plan_delivery's moves do not deliver the boxes in the correct order.
  - plan_delivery's output is not a list of strings in the prescribed format.
  - plan_delivery does not return an output within the prescribed time limit.
  - Your code raises an exception.

=== Part A ===

In this Part A, you will build a planner that helps a robot
  find the best path through a warehouse filled with boxes
  that it has to pick up and deliver to a dropzone.

`DeliveryPlanner_PartA` must have an `__init__` function that takes three 
  arguments: `self`, `warehouse`, and `todo`.
`DeliveryPlanner_PartA` must also have a function called `plan_delivery` that 
  takes a single argument, `self`.

=== Part A Input Specifications ===

`warehouse` will be a list of m strings, each with n characters,
  corresponding to the layout of the warehouse. The warehouse is an
  m x n grid. warehouse[i][j] corresponds to the spot in the ith row
  and jth column of the warehouse, where the 0th row is the northern
  end of the warehouse and the 0th column is the western end.

The characters in each string will be one of the following:

'.' (period) : traversable space. The robot may enter from any adjacent space.
'#' (hash) : a wall. The robot cannot enter this space.
'@' (dropzone): the starting point for the robot and the space where all boxes must be delivered.
  The dropzone may be traversed like a '.' space.
[0-9a-zA-Z] (any alphanumeric character) : a box. At most one of each alphanumeric character 
  will be present in the warehouse (meaning there will be at most 62 boxes). A box may not
  be traversed, but if the robot is adjacent to the box, the robot can pick up the box.
  Once the box has been removed, the space functions as a '.' space.

For example, 
  warehouse = ['1#2',
               '.#.',
               '..@']
  is a 3x3 warehouse.
  - The dropzone is at the warehouse cell in row 2, column 2.
  - Box '1' is located in the warehouse cell in row 0, column 0.
  - Box '2' is located in the warehouse cell in row 0, column 2.
  - There are walls in the warehouse cells in row 0, column 1 and row 1, column 1.
  - The remaining five warehouse cells contain empty space. (The dropzone is empty space)
#
The argument `todo` is a list of alphanumeric characters giving the order in which the 
  boxes must be delivered to the dropzone. For example, if 
  todo = ['1','2']
  is given with the above example `warehouse`, then the robot must first deliver box '1'
  to the dropzone, and then the robot must deliver box '2' to the dropzone.

=== Part A Rules for Movement ===

- Two spaces are considered adjacent if they share an edge or a corner.
- The robot may move horizontally or vertically at a cost of 2 per move.
- The robot may move diagonally at a cost of 3 per move.
- The robot may not move outside the warehouse.
- The warehouse does not "wrap" around.
- As described earlier, the robot may pick up a box that is in an adjacent square.
- The cost to pick up a box is 4, regardless of the direction the box is relative to the robot.
- While holding a box, the robot may not pick up another box.
- The robot may put a box down on an adjacent empty space ('.') or the dropzone ('@') at a cost
  of 2 (regardless of the direction in which the robot puts down the box).
- If a box is placed on the '@' space, it is considered delivered and is removed from the ware-
  house.
- The warehouse will be arranged so that it is always possible for the robot to move to the 
  next box on the todo list without having to rearrange any other boxes.

An illegal move will incur a cost of 100, and the robot will not move (the standard costs for a 
  move will not be additionally incurred). Illegal moves include:
- attempting to move to a nonadjacent, nonexistent, or occupied space
- attempting to pick up a nonadjacent or nonexistent box
- attempting to pick up a box while holding one already
- attempting to put down a box on a nonadjacent, nonexistent, or occupied space
- attempting to put down a box while not holding one

=== Part A Output Specifications ===

`plan_delivery` should return a LIST of moves that minimizes the total cost of completing
  the task successfully.
Each move should be a string formatted as follows:

'move {i} {j}', where '{i}' is replaced by the row-coordinate of the space the robot moves
  to and '{j}' is replaced by the column-coordinate of the space the robot moves to

'lift {x}', where '{x}' is replaced by the alphanumeric character of the box being picked up

'down {i} {j}', where '{i}' is replaced by the row-coordinate of the space the robot puts 
  the box, and '{j}' is replaced by the column-coordinate of the space the robot puts the box

For example, for the values of `warehouse` and `todo` given previously (reproduced below):
  warehouse = ['1#2',
               '.#.',
               '..@']
  todo = ['1','2']
`plan_delivery` might return the following:
  ['move 2 1',
   'move 1 0',
   'lift 1',
   'move 2 1',
   'down 2 2',
   'move 1 2',
   'lift 2',
   'down 2 2']

=== Part B ===

In this Part B, you will again build a planner that helps a robot
  find the best path through a warehouse filled with boxes
  that it has to pick up and deliver to a dropzone. Unlike Part A,
  however, in this problem the robot is moving in a continuous world
  (albeit in discrete time steps) and has constraints on the amount
  it can turn its wheels in a given time step.

`DeliveryPlanner_PartB` must have an `__init__` function that takes five 
  arguments: `self`, `warehouse`, `todo`, `max_distance`, and
  `max_steering`.
`DeliveryPlanner_PartB` must also have a function called `plan_delivery` that 
  takes a single argument, `self`.

=== Part B Input Specifications ===

`warehouse` will be a list of m strings, each with n characters,
  corresponding to the layout of the warehouse. The warehouse is an
  m x n grid. warehouse[i][j] corresponds to the spot in the ith row
  and jth column of the warehouse, where the 0th row is the northern
  end of the warehouse and the 0th column is the western end.

The characters in each string will be one of the following:

'.' (period) : traversable space.
'#' (hash) : a wall. If the robot contacts a wall space, it will crash.
'@' (dropzone): the space where all boxes must be delivered. The dropzone may be traversed like 
  a '.' space.

Each space is a 1 x 1 block. The upper-left corner of space warehouse[i][j] is at the point (j,-i) in
  the plane. Spaces outside the warehouse are considered walls; if any part of the robot leaves the 
  warehouse, it will be considered to have crashed into the exterior wall of the warehouse.

For example, 
  warehouse = ['.#.',
               '.#.',
               '..@']
  is a 3x3 warehouse. The dropzone is at space (2,-2) and there are walls at spaces (1,0) 
  and (1,-1). The rest of the warehouse is empty space.

The robot is a square of width 0.5. The robot begins centered in the dropzone space.
  The robot's initial bearing is 0.

The argument `todo` is a list of points representing the center point of each box.
  todo[0] is the first box which must be delivered, followed by todo[1], and so on.
  Each box is a square of size 0.2 x 0.2. If the robot contacts a box, it will crash.

The arguments `max_distance` and `max_steering` are parameters constraining the movement
  of the robot on a given time step. They are described more below.

=== Part B Rules for Movement ===

- The robot may move any distance between 0 and `max_distance` per time step.
- The robot may set its steering angle anywhere between -`max_steering` and 
  `max_steering` per time step. A steering angle of 0 means that the robot will
  move according to its current bearing. A positive angle means the robot will 
  turn counterclockwise by `steering_angle` radians; a negative steering_angle 
  means the robot will turn clockwise by abs(steering_angle) radians.
- Upon a movement, the robot will change its steering angle instantaneously to the 
  amount indicated by the move, and then it will move a distance in a straight line in its
  new bearing according to the amount indicated move.
- The cost per move is 1 plus the amount of distance traversed by the robot on that move.

- The robot may pick up a box whose center point is within 0.5 units of the robot's center point.
- If the robot picks up a box, it incurs a total cost of 2 for that move (this already includes 
  the 1-per-move cost incurred by the robot).
- While holding a box, the robot may not pick up another box.
- The robot may put a box down at a total cost of 1.5 for that move. The box must be placed so that:
  - The box is not contacting any walls, the exterior of the warehouse, any other boxes, or the robot
  - The box's center point is within 0.5 units of the robot's center point
- A box is always oriented so that two of its edges are horizontal and the other two are vertical.
- If a box is placed entirely within the '@' space, it is considered delivered and is removed from the 
  warehouse.
- The warehouse will be arranged so that it is always possible for the robot to move to the 
  next box on the todo list without having to rearrange any other boxes.

- If the robot crashes, it will stop moving and incur a cost of 100*distance, where distance
  is the length it attempted to move that move. (The regular movement cost will not apply.)
- If an illegal move is attempted, the robot will not move, but the standard cost will be incurred.
  Illegal moves include (but are not necessarily limited to):
    - picking up a box that doesn't exist or is too far away
    - picking up a box while already holding one
    - putting down a box too far away or so that it's touching a wall, the warehouse exterior, 
      another box, or the robot
    - putting down a box while not holding a box

=== Part B Output Specifications ===

`plan_delivery` should return a LIST of strings, each in one of the following formats.

'move {steering} {distance}', where '{steering}' is a floating-point number between
  -`max_steering` and `max_steering` (inclusive) and '{distance}' is a floating-point
  number between 0 and `max_distance`

'lift {b}', where '{b}' is replaced by the index in the list `todo` of the box being picked up
  (so if you intend to lift box 0, you would return the string 'lift 0')

'down {x} {y}', where '{x}' is replaced by the x-coordinate of the center point of where the box
  will be placed and where '{y}' is replaced by the y-coordinate of that center point
  (for example, 'down 1.5 -2.9' means to place the box held by the robot so that its center point
  is (1.5,-2.9)).

'''
import numpy as np
import math
from math import *
from collections import OrderedDict
PI = math.pi

class DeliveryPlanner_PartA:

    def __init__(self, warehouse, todo):
        self.warehouse = np.array(warehouse)
        self.todo = todo
        pass

    def findHeuristic(self, x, y, goalx, goaly):
      dx = abs(x - goalx)
      dy = abs(y - goaly)
      return 1 * math.sqrt(dx * dx + dy * dy)


    def plan_delivery(self):

        # moves = ['move 2 1',
        #          'move 1 0',
        #          'lift 1',
        #          'move 2 1',
        #          'down 2 2',
        #          'move 1 2',
        #          'lift 2',
        #          'down 2 2']

        moves = []

        goals = {}
        cost = 1
        delta = [[-1, 0], # go up
                 [ 0,-1], # go left
                 [ 1, 0], # go down
                 [ 0, 1], # go right
                 [ -1, -1], # diag up left
                 [ 1, 1], # diag down right
                 [ -1, 1], # diag up right
                 [ 1, -1]] # diag down left

        delta_name = np.array(['up', 'lf', 'dn', 'rt', 'dul', 
        'ddr', 'dur', 'ddl'])


        for row in range(len(self.warehouse)):
          for col in range(len(self.warehouse[0])):
            if self.warehouse[row][col] == '@':
              init = row,col
            elif self.warehouse[row][col].isalnum():
              goals[self.warehouse[row][col]] = row,col
        
        
        heuristic = np.array([[0 for col in range(len(self.warehouse[0]))] for row in range(len(self.warehouse))])
        previousTarget = []
        
        for target in self.todo:
          goal = goals.get(target)
          for row in range(len(self.warehouse)):
            for col in range(len(self.warehouse[0])):
              heuristic[row][col] = self.findHeuristic(row, col, goal[0], goal[1])
          # print "warehouse ", self.warehouse
          # print "closed ", closed
          # print goals

          closed = np.array([[0 for col in range(len(self.warehouse[0]))] for row in range(len(self.warehouse))])
          closed[[init[0]],[init[1]]] = 1
          action = np.array([[-1 for col in range(len(self.warehouse[0]))] for row in range(len(self.warehouse))])

          expand = np.array([[-1 for col in range(len(self.warehouse[0]))] for row in range(len(self.warehouse))])
          

          x = init[0]
          y = init[1]
          g = 0
          h = heuristic[x][y]
          f = g + h

          open = [[f, g, h, x, y]]

          found = False  # flag that is set when search is complete
          resign = False # flag set if we can't find expand
          count = 0
 

          # print "goal", goal
          # print "heuristic", heuristic
        
          while found is False and resign is False:
            if len(open) == 0:
                print "closed", closed
                resign = True
                print ("fail")
                
            else:
                open.sort()
                open.reverse()
                next = open.pop()
                # print "next ", next
                
                x = next[3]
                y = next[4]
                g = next[1]

                expand[x][y] = count
                count += 1

                if x == goal[0] and y == goal[1]:
                    found = True
                    # print "found", closed
                    # print next
                else:
                    # expand winning element and add to new open list
                    for i in range(len(delta)):
                        x2 = x + delta[i][0]
                        y2 = y + delta[i][1]
                        if x2 >= 0 and x2 < len(self.warehouse) and y2 >= 0 and y2 < len(self.warehouse[0]):                    
                            if closed[x2][y2] == 0 and (self.warehouse[x2][y2] == '.' or previousTarget.count(self.warehouse[x2][y2]) > 0) :
                                g2 = g + cost
                                h2 = heuristic[x2][y2]
                                f2 = g2 + h2
                                open.append([f2, g2, h2, x2, y2])
                                closed[x2][y2] = 1
                                # print "target ", target
                                # print "closed ", closed
                                action[x2][y2] = i
                            elif closed[x2][y2] == 0 and self.warehouse[x2][y2] == target:  # and self.warehouse[x][y] != '@':
                                g2 = g + cost
                                h2 = heuristic[x2][y2]
                                f2 = g2 + h2
                                open.append([f2, g2, h2, x2, y2])
                                print "target ", target 
                                # closed[x2][y2] = target
                                action[x2][y2] = i
          previousTarget.append(target)
          policy = np.array([["   " for col in range(len(self.warehouse[0]))] for row in range(len(self.warehouse))])
          reversePolicy = np.array([["   " for col in range(len(self.warehouse[0]))] for row in range(len(self.warehouse))])
          x = goal[0]
          y = goal[1]
          policy[x][y] = target
          while x != init[0] or y != init[1]:
            x2 = abs(x - delta[action[x][y]][0])
            y2 = abs(y - delta[action[x][y]][1])
            # print "x, y", x, y
            # print "x2, y2", x2, y2
            policy[x2][y2] = delta_name[action[x][y]]
            x = x2
            y = y2
          
          # while x != goal[0] or y != goal[1]:
          #   x2 = abs(x + delta[action[x][y]][0])
          #   y2 = abs(y + delta[action[x][y]][1])
          #   # print "x, y", x, y
          #   # print "x2, y2", x2, y2
          #   reversePolicy[x2][y2] = delta_name[action[x][y]]
          #   x = x2
          #   y = y2

          # print "warehouse", self.warehouse
          # print "------Policy: "
          # for i in range(len(policy)):
          #   print policy[i]


          # print "warehouse", self.warehouse
          # print "------Reverse Policy: "
          # for i in range(len(policy)):
          #   print reversePolicy[i]  
          # print "expansion", expand
          # print "action", action
          # for 
          x = init[0]
          y = init[1]

          reverse = []
          # bool nextToDz = False
          lastX = 1000
          lastY = 1000
        
          while x != goal[0] or y != goal[1]:
            if policy[x][y] == 'up':
              x = x - 1
              y = y 
              if policy[x][y] == target:
                moves.append('lift ' + target)
                lastX = x - 1
                lastY = y
                reverse.append('down ' + str(init[0]) + ' ' + str(init[1]))
                break
              else:
                moves.append('move ' + str(x) + ' ' + str(y))
                reverse.append('move ' + str(x + 1) + ' ' + str(y))

            elif policy[x][y] == 'lf':
              x = x
              y = y - 1
              if policy[x][y] == target:
                lastX = x
                lastY = y - 1
                moves.append('lift ' + target)
                reverse.append('down ' + str(init[0]) + ' ' + str(init[1]))
                break
              else:
                moves.append('move ' + str(x) + ' ' + str(y))
                reverse.append('move ' + str(x) + ' ' + str(y + 1))

            elif policy[x][y] == 'dn':
              x = x + 1
              y = y
              if policy[x][y] == target:
                lastX = x - 1
                lastY = y
                moves.append('lift ' + target)
                reverse.append('down ' + str(init[0]) + ' ' + str(init[1]))
                break
              else:
                moves.append('move ' + str(x) + ' ' + str(y))
                reverse.append('move ' + str(x - 1) + ' ' + str(y))

            elif policy[x][y] == 'rt':
              x = x
              y = y + 1
              if policy[x][y] == target:
                lastX = x
                lastY = y - 1
                moves.append('lift ' + target)
                reverse.append('down ' + str(init[0]) + ' ' + str(init[1]))
                break
              else:
                moves.append('move ' + str(x) + ' ' + str(y))
                reverse.append('move ' + str(x) + ' ' + str(y - 1))

            elif policy[x][y] == 'dul':
              x = x - 1
              y = y - 1
              if policy[x][y] == target:
                lastX = x + 1
                lastY = y + 1
                moves.append('lift ' + target)
                reverse.append('down ' + str(init[0]) + ' ' + str(init[1]))
                break
              else:
                moves.append('move ' + str(x) + ' ' + str(y))
                reverse.append('move ' + str(x + 1) + ' ' + str(y + 1))

            elif policy[x][y] == 'ddr':
              x = x + 1
              y = y + 1
              if policy[x][y] == target:
                lastX = x - 1
                lastY = y - 1
                moves.append('lift ' + target)
                reverse.append('down ' + str(init[0]) + ' ' + str(init[1]))
                break
              else:
                moves.append('move ' + str(x) + ' ' + str(y))
                reverse.append('move ' + str(x - 1) + ' ' + str(y - 1))

            elif policy[x][y] == 'dur':
              x = x - 1
              y = y + 1
              if policy[x][y] == target:
                lastX = x + 1
                lastY = y - 1
                moves.append('lift ' + target)
                reverse.append('down ' + str(init[0]) + ' ' + str(init[1]))
                break
              else:
                moves.append('move ' + str(x) + ' ' + str(y))
                reverse.append('move ' + str(x + 1) + ' ' + str(y - 1))

            elif policy[x][y] == 'ddl':
              x = x + 1
              y = y - 1
              if policy[x][y] == target:
                lastX = x - 1
                lastY = y + 1
                moves.append('lift ' + target)
                reverse.append('down ' + str(init[0]) + ' ' + str(init[1]))
                break
              else:
                moves.append('move ' + str(x) + ' ' + str(y))
                reverse.append('move ' + str(x - 1) + ' ' + str(y + 1))

          # print "moves", moves
          print "Reverse ", reverse
          temp = reverse[1:len(reverse) - 1]
          temp.reverse()
          # print "last ", reverse.pop()
          print "temp ", temp
          
          # if (moves[-1] == temp[0]):
          #   moves += temp[1:]
          # else:
          moves += temp
          moves.append(reverse.pop())
          # moves += reverse.pop()
        
        n = 0
        max_moves = len(moves)
        removeList = []
        dropLater = []
        addList = []
        
        while (n + 1 < max_moves):
          if moves[n].find('down') >= 0:
            # check moves[n-1] and moves[n+1]
            
            if moves[n - 1] == moves[n + 1]:
              # del moves[n + 1]
              removeList.append(n + 1)
              print "I am removing duplicate move", moves[n - 1], moves[n + 1]
              print "n", n

            elif moves[n - 1].find('lift') >= 0:
              # temp = moves[n + 1]
              
              # moves[n + 1] = moves[n]
              # moves[n] = temp
              dropLater.append(n)
              print "moves[n + 1] ", moves[n + 1]
              print "moves[n]", moves[n]
            else:
              # moves.insert(n+1, 'moves ' + str(init[0]) + ' ' + str(init[1]))
              addList.append(n)

            
          n += 1


        for i in dropLater:
          # moves.insert(i, 'drop ' + str(init[0]) + ' ' + str(init[1]))
          temp = moves[i + 1]    
          moves[i + 1] = moves[i]
          moves[i] = temp
          # print "print swapping"

        offset = 0
        for i in removeList:
          del moves[i - offset]
          offset += 1
        offset = 0
        for i in addList:
          if moves[i].find('down') < 0:
            moves.insert(i - offset, 'move ' + str(init[0]) + ' ' + str(init[1]))
            offset + 1



  

        print "moves after", moves

        # moves = ['move 2 1',
        #          'move 1 0',
        #          'lift 1',
        #          'move 2 1',
        #          'down 2 2',
        #          'move 1 2',
        #          'lift 2',
        #          'down 2 2']

        # moves = ['lift 1', 'move 1 1', 'down 1 2', 'move 2 1', 'lift 2', 'down 1 2']
        # moves = ['move 0 1', 'lift 1', 'down 1 2', 'move 2 1', 'lift 2', 'down 1 2']
        return moves


class DeliveryPlanner_PartB:

    def __init__(self, warehouse, todo, max_distance, max_steering):

        # TODO: You may use this function for any initialization required for your planner
        self.warehouse = np.array(warehouse)
        self.todo = todo
        self.max_distance = max_distance
        self.max_steering = max_steering
        self.minigrid = OrderedDict()
        self.xRange = 10
        self.yRange = 10
        self.resolution = .1
        self.distanceToTarg = .45
        self.oldBearing = 0.0
        
        pass

    def findHeuristic(self, x, y, goalx, goaly):
      dx = abs(x - goalx)
      dy = abs(y - goaly)
      return dx + dy

    def xytoij(self, x, y):
      # print int(round(-2 * y)), int(round(2 * x))
      return int(round(-self.yRange * y)), int(round(self.xRange * x))
      # pass
    

    def ijtoxy(self, i, j):
      # print int(round(self.xRange * j)), int(round(- self.yRange * i))
      # return (j / self.xRange, - i / self.yRange)
      return float(j) / self.xRange, float(- i )/ self.yRange
      return 
      pass

    def angle_trunc(self, a, max_steering):
      """Helper function to map all angles onto [-pi, pi]

      Arguments:
          a(float): angle to truncate.

      Returns:
          angle between -pi and pi.
      """
      return ((a + max_steering) % (max_steering * 2)) - max_steering

    def compute_distance(self, p, q):
      x1, y1 = p
      x2, y2 = q

      dx = x2 - x1
      dy = y2 - y1

      return math.sqrt(dx**2 + dy**2)


    def compute_bearing(self, p, q):
      x1, y1 = p
      x2, y2 = q

      dx = x2 - x1
      dy = y2 - y1

      return math.atan2(dy, dx)

    def truncate_angle(self, t):
      return ((t+PI) % (2*PI)) - PI


      # bearing1 = self.truncate_angle(self.compute_bearing(previousPos, currentPos))
      # print "bearing1", bearing1 
      # print "goto", goto
      # bearing2 = self.truncate_angle(self.compute_bearing(currentPos, goto))
      # print "bearing2", bearing2
      # # bearing2 = atan2(previous_xy[1] - 0, previous_xy[0] - 0)
      # steering_angle = (bearing1 - bearing2)

      # if steering_angle > self.max_steering:
      #   steering_angle = self.max_steering

      # if steering_angle < -self.max_steering:
      #   steering_angle = -self.max_steering

      # print "new steering angle", steering_angle


    def measure_distance_and_bearing_to(self, previousPos, currentPos, goto=(0,0), noise=False):

      # current_position = (self.x, self.y)

      distance_to_point = self.compute_distance(previousPos, currentPos)
      bearing_to_point = self.compute_bearing(previousPos, currentPos)

      measured_distance = distance_to_point
      
      # print "bearing to point", bearing_to_point
      measured_bearing = self.truncate_angle(
          bearing_to_point - self.oldBearing)
      if measured_bearing != 0:
        self.oldBearing = bearing_to_point

      # print "currentPos", currentPos
      # print "previousPos", previousPos
      # print "oldbearing", self.oldBearing
      # print "measured bearing ", measured_bearing

      # print "steering is", steering
      # self.bearing = steering
      # print "measured bearing and self bearing", measured_bearing, steering
      return measured_distance, measured_bearing


    def plan_delivery(self):

        # Sample of what a moves list should look like - replace with your planner results
        # print "warehouse", self.warehouse
        # print "todo", self.todo
        # print "max distance", self.max_distance
        # print "max steering", self.max_steering

        final_moves = []

        cost = 1
        delta = [[-1, 0], # go up
                 [ 0,-1], # go left
                 [ 1, 0], # go down
                 [ 0, 1], # go right
                 [ -1, -1], # diag up left
                 [ 1, 1], # diag down right
                 [ -1, 1], # diag up right
                 [ 1, -1]] # diag down left

        delta_name = np.array(['up', 'lf', 'dn', 'rt', 'dul', 
        'ddr', 'dur', 'ddl'])

        

        # xRange = 2
        # yRange = 2
        itemOrder = 0
        itemOrderList = []
        wallPadding = False
        count = 0

        testGrid = {}

        # for i in range(len(self.warehouse)):
        #     for j in range(len(self.warehouse[0])):
        #       print i,j
        #       testGrid[[i][j]] = 1

        for i in range(len(self.warehouse)):
            for j in range(len(self.warehouse[0])):
                # print i, j
                # print count
                newx = j
                newy = - i
                var = self.warehouse[i][j]
                for m in range(self.xRange):
                  for n in range(self.yRange):
                    # print "x and y", (newx, newy)
                    if (self.todo.count((newx, newy)) > 0):
                      # print "found ", newx, newy
                      self.minigrid[(newx, newy)] = itemOrder
                      itemOrderList.append(itemOrder)
                      itemOrder += 1
                    elif var == '#':
                      self.minigrid[(newx, newy)] = '#'
                    
                    elif var == '@':
                      if ('@' in self.minigrid.values()) == False:
                        # print newx, newy
                        self.minigrid[newx + .5, newy - .5] = '@'
                        self.minigrid[newx, newy] = '.'
                        initVal = (newx + .5, newy - .5)
                        # print '@ at ', newx + .5, newy - .5
                      else:
                        if (initVal != (newx, newy)):
                          self.minigrid[(newx, newy)] = '.'
                      # if len(dz) == 3:
                        
                      # else:
                      #   dz.append((newx, newy))
                      #   self.minigrid[(newx, newy)] = '.'

                    
                    else:
                        self.minigrid[(newx, newy)] = '.'
                        # print (newx, newy)
                    if newy == 0:
                      newy = - round(newy + self.resolution, 1)
                      # print "newy was zero", newy
                    else:
                      newy = round(newy - self.resolution, 1)
                    count += 1
                  newx = round(newx + self.resolution, 1)
                  newy = -i
                  
        # print self.minigrid
        # print count 
        newMiniGrid = {}
        paddingList = {}
        goals = []
        for key, value in self.minigrid.items():
          # print "key ", key
          # if value >= 0 and value < 20:
            # goals.append(value)
            # itr = .1
            # for i in range(10):
            #   if (round(key[0] + itr, 1), round(key[1] + itr, 1)) in self.minigrid:
            #     if self.minigrid[(round(key[0] + itr, 1), round(key[1] + itr, 1))] != '#':
            #       self.minigrid[(round(key[0] + itr, 1), round(key[1] + itr, 1))] = '$'
            #   itr += .1
            # itr = .1
            # for i in range(10):
            #   if (round(key[0] - itr, 1), round(key[1] - itr, 1)) in self.minigrid:
            #     if self.minigrid[(round(key[0] - itr, 1), round(key[1] - itr, 1))] != '#':
            #       self.minigrid[(round(key[0] - itr, 1), round(key[1] - itr, 1))] = '$'
              # itr += .1
            # print (key[0] - .2, key[1] - .2)
            # print key[1] + .2
            # print self.minigrid[(key[0] + .1, key[1] + .1)]

          if value == '#' or (value >= 0 and value < 20):
            itr = .1
            # print "#######################key is ", key
            r = 3
            # for i in range(5):
            
            itr = .1
            for i in range(r):
              if (round(key[0] + itr, 1), round(key[1] + itr, 1)) in self.minigrid:
                # print "plus plus", key[0] + itr, key[1] + itr
                if self.minigrid[(round(key[0] + itr, 1), round(key[1] + itr, 1))] != '#':
                  self.minigrid[(round(key[0] + itr, 1), round(key[1] + itr, 1))] = '$'
                  # print "value ", self.minigrid[(round(key[0] + itr, 1), round(key[1] - itr, 1))]
              itr += .1
         
            itr = .1
            for i in range(r):
              if (round(key[0] + itr, 1), round(key[1] - itr, 1)) in self.minigrid:
                # print "plus minus", key[0] + itr, key[1] - itr
                if self.minigrid[(round(key[0] + itr, 1), round(key[1] - itr, 1))] != '#':
                  self.minigrid[(round(key[0] + itr, 1), round(key[1] - itr, 1))] = '$'
                  # print "value ", self.minigrid[(round(key[0] + itr, 1), round(key[1] - itr, 1))]
              itr += .1

            itr = .1
            for i in range(r):
              if (round(key[0] - itr, 1), round(key[1] + itr, 1)) in self.minigrid:
                # print "minus plus", key[0] - itr, key[1] + itr
                if self.minigrid[(round(key[0] - itr, 1), round(key[1] + itr, 1))] != '#':
                  self.minigrid[(round(key[0] - itr, 1), round(key[1] + itr, 1))] = '$'
                  # print "value ", self.minigrid[(round(key[0] + itr, 1), round(key[1] - itr, 1))]
              itr += .1

            itr = .1
            for i in range(r):
              if (round(key[0] - itr, 1), round(key[1] - itr, 1)) in self.minigrid:
                # print "minus minus", key[0] - itr, key[1] - itr
                if self.minigrid[(round(key[0] - itr, 1), round(key[1] - itr, 1))] != '#':
                  self.minigrid[(round(key[0] - itr, 1), round(key[1] - itr, 1))] = '$'
                  # print "value ", self.minigrid[(round(key[0] + itr, 1), round(key[1] - itr, 1))]
              itr += .1
   
        heuristic = np.array([[0 for col in range(len(self.warehouse[0]) * self.xRange)] for row in range(len(self.warehouse) * self.yRange)])
        previousTarget = []
        goal = (0,0)
        init = 0
        targ = 0
        for target in self.todo:
          self.oldBearing = 0
          for key, value in self.minigrid.items():
            # print "xy", key, value
            # print "ij ", ij
            ij = self.xytoij(key[0], key[1])
            if value == '@':
              # print "found @ at ", key
              if init == 0:
                fixedinit = self.xytoij(key[0], key[1])
                init = fixedinit
                # print "init", init
            elif key == target:
              goal = self.xytoij(key[0], key[1])
              targ = value
              # print "target", target
              # print "goal", goal
              # print "targ", targ

            heuristic[ij[0]][ij[1]] = self.findHeuristic(key[0], key[1], target[0], target[1])
            
          closed = np.array([[0 for col in range(len(self.warehouse[0]) * self.xRange)] for row in range(len(self.warehouse) * self.yRange)])
          closed[[init[0]],[init[1]]] = 1
          action = np.array([[-1 for col in range(len(self.warehouse[0]) * self.xRange)] for row in range(len(self.warehouse) * self.yRange)])
          # print action
          expand = np.array([[-1 for col in range(len(self.warehouse[0]) * self.xRange)] for row in range(len(self.warehouse) * self.yRange)])
          

          x = init[0]
          y = init[1]
          g = 0
          h = heuristic[x][y]
          f = g + h

          open = [[f, g, h, x, y]]

          found = False  # flag that is set when search is complete
          resign = False # flag set if we can't find expand
          count = 0
 

          # # print "goal", goal
          # # print "heuristic", heuristic
        
          while found is False and resign is False:
            if len(open) == 0:
                print "closed", closed
                resign = True
                print ("fail")
                
            else:
                open.sort()
                open.reverse()
                next = open.pop()
                # print "next ", next
                
                x = next[3]
                y = next[4]
                g = next[1]

                expand[x][y] = count
                count += 1

                if x == goal[0] and y == goal[1]:
                    found = True
                    # print "found", closed
                    # print next
                else:
                    # expand winning element and add to new open list
                    for i in range(len(delta)):
                        x2 = x + delta[i][0]
                        y2 = y + delta[i][1]
                        if x2 >= 0 and x2 < len(self.warehouse) * self.xRange and y2 >= 0 and y2 < len(self.warehouse[0]) * self.yRange:
                            gxy = self.ijtoxy(x2, y2)
                            # print "x2, y2", x2, y2
                            # print "gxy", (gxy[0], gxy[1])
                            # print "minigrid", self.minigrid[(gxy[0], gxy[1])]
                            # print closed[x2][y2]
                            # print self.minigrid[(gxy[0], gxy[1])]                    
                            if closed[x2][y2] == 0 and (self.minigrid[(gxy[0], gxy[1])] == '.'): # or previousTarget.count(self.minigrid[(gxy[0], gxy[1])]) > 0) :
                                g2 = g + cost
                                h2 = heuristic[x2][y2]
                                f2 = g2 + h2
                                open.append([f2, g2, h2, x2, y2])
                                closed[x2][y2] = 1
                                # print "target ", target
                                # print "closed ", closed
                                action[x2][y2] = i
                            elif closed[x2][y2] == 0 and (gxy[0], gxy[1]) == target:  # and self.warehouse[x][y] != '@':
                                g2 = g + cost
                                h2 = heuristic[x2][y2]
                                f2 = g2 + h2
                                open.append([f2, g2, h2, x2, y2])
                                # print "target ", target 
                                # closed[x2][y2] = target
                                action[x2][y2] = i
                
          # print action
          # [[-1 for col in range(len(self.warehouse[0]) * self.xRange)] for row in range(len(self.warehouse) * self.yRange)]
          policy = np.array([["   " for col in range(len(self.warehouse[0]) * self.xRange)] for row in range(len(self.warehouse) * self.yRange)])
          reversePolicy = np.array([["   " for col in range(len(self.warehouse[0]))] for row in range(len(self.warehouse))])
          x = goal[0]
          y = goal[1]
          policy[x][y] = targ

          # print "action len", len(action)
          while x != init[0] or y != init[1]:
            x2 = abs(x - delta[action[x][y]][0])
            y2 = abs(y - delta[action[x][y]][1])
            # print self.ijtoxy(x,y)
            # print "x, y", x, y
            # print "x2, y2", x2, y2
            policy[x2][y2] = delta_name[action[x][y]]
            x = x2
            y = y2

          # print policy


          x = init[0]
          y = init[1]
          xyinit = self.ijtoxy(x,y)

          reverse = []
          # bool nextToDz = False
          lastX = 1000
          lastY = 1000
          moves = []
          previousBearing = 0
        
          while x != goal[0] or y != goal[1]:
            previousxy = self.ijtoxy(x,y)
            # print "xy and grid value ", previousxy, self.minigrid[previousxy]
            if policy[x][y] == 'up':
              x = x - 1
              y = y 

              currentxy = self.ijtoxy(x,y)
              distance = self.compute_distance(previousxy, currentxy)
              targetDistance = self.compute_distance(currentxy, target)
              distance, bearing = self.measure_distance_and_bearing_to(previousxy, currentxy, target)
              
              if bearing > self.max_steering:
                moves.append('move ' + str(self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(-self.max_steering) + ' 0 ')
                # print "up distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = abs(bearing) - self.max_steering
              elif bearing < -self.max_steering:
                moves.append('move ' + str(-self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(self.max_steering) + ' 0 ')
                # print "ddr-min distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = bearing + self.max_steering

              # print "up distance and bearing and target", distance, bearing, targetDistance

              if targetDistance <= self.distanceToTarg:
                lastX = x + 1
                lastY = y
                moves.append('lift ' + str(targ))
                reverse.append('down ' + str(xyinit[0]) + ' ' + str(xyinit[1]))
                break
              else:
                moves.append('move ' + str(bearing) + ' ' + str(distance))
                reverse.append('move ' + str(-bearing) + ' ' + str(distance))

            elif policy[x][y] == 'lf':
              x = x
              y = y - 1

              currentxy = self.ijtoxy(x,y)
              distance = self.compute_distance(previousxy, currentxy)
              targetDistance = self.compute_distance(currentxy, target)
              distance, bearing = self.measure_distance_and_bearing_to(previousxy, currentxy)

              if bearing > self.max_steering:
                moves.append('move ' + str(self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(-self.max_steering) + ' 0 ')
                # print "up distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = abs(bearing) - self.max_steering
              elif bearing < -self.max_steering:
                moves.append('move ' + str(-self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(self.max_steering) + ' 0 ')
                # print "ddr-min distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = bearing + self.max_steering

              # print "lf distance and bearing and target", distance, bearing, targetDistance

              if targetDistance <= self.distanceToTarg:
                lastX = x
                lastY = y + 1
                moves.append('lift ' + str(targ))
                reverse.append('down ' + str(xyinit[0]) + ' ' + str(xyinit[1]))
                break
              else:
                moves.append('move ' + str(bearing) + ' ' + str(distance))
                reverse.append('move ' + str(-bearing) + ' ' + str(distance))

            elif policy[x][y] == 'dn':
              x = x + 1
              y = y

              currentxy = self.ijtoxy(x,y)
              targetDistance = self.compute_distance(currentxy, target)
              distance, bearing = self.measure_distance_and_bearing_to(previousxy, currentxy)

              if bearing > self.max_steering:
                moves.append('move ' + str(self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(-self.max_steering) + ' 0 ')
                # print "up distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = abs(bearing) - self.max_steering
              elif bearing < -self.max_steering:
                moves.append('move ' + str(-self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(self.max_steering) + ' 0 ')
                # print "ddr-min distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = bearing + self.max_steering

              # print "dn distance and bearing and target", distance, bearing, targetDistance

              if targetDistance <= self.distanceToTarg:
                lastX = x - 1
                lastY = y
                moves.append('lift ' + str(targ))
                reverse.append('down ' + str(xyinit[0]) + ' ' + str(xyinit[1]))
                break
              else:
                moves.append('move ' + str(bearing) + ' ' + str(distance))
                reverse.append('move ' + str(-bearing) + ' ' + str(distance))

            elif policy[x][y] == 'rt':
              x = x
              y = y + 1

              currentxy = self.ijtoxy(x,y)
              distance = self.compute_distance(previousxy, currentxy)
              targetDistance = self.compute_distance(currentxy, target)
              distance, bearing = self.measure_distance_and_bearing_to(previousxy, currentxy)

              if bearing > self.max_steering:
                moves.append('move ' + str(self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(-self.max_steering) + ' 0 ')
                # print "up distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = abs(bearing) - self.max_steering
              elif bearing < -self.max_steering:
                moves.append('move ' + str(-self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(self.max_steering) + ' 0 ')
                # print "ddr-min distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = bearing + self.max_steering

              # print "rt distance and bearing and target", distance, bearing, targetDistance

              if targetDistance <= self.distanceToTarg:
                lastX = x
                lastY = y - 1
                moves.append('lift ' + str(targ))
                reverse.append('down ' + str(xyinit[0]) + ' ' + str(xyinit[1]))
                break
              else:
                moves.append('move ' + str(bearing) + ' ' + str(distance))
                reverse.append('move ' + str(-bearing) + ' ' + str(distance))

            elif policy[x][y] == 'dul':
              x = x - 1
              y = y - 1
              currentxy = self.ijtoxy(x,y)
              # distance = self.compute_distance(previousxy, currentxy)
              targetDistance = self.compute_distance(currentxy, target)
              distance, bearing = self.measure_distance_and_bearing_to(previousxy, currentxy, target)

              if bearing > self.max_steering:
                moves.append('move ' + str(self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(-self.max_steering) + ' 0 ')
                # print "up distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = abs(bearing) - self.max_steering
              elif bearing < -self.max_steering:
                moves.append('move ' + str(-self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(self.max_steering) + ' 0 ')
                # print "ddr-min distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = bearing + self.max_steering

              
              # print "dul distance and bearing and target", distance, bearing, targetDistance
              
              
              if targetDistance <= self.distanceToTarg:
                lastX = x + 1
                lastY = y + 1
                moves.append('lift ' + str(targ))
                reverse.append('down ' + str(xyinit[0]) + ' ' + str(xyinit[1]))
                break
              else:
                moves.append('move ' + str(bearing) + ' ' + str(distance))
                reverse.append('move ' + str(-bearing) + ' ' + str(distance))

            elif policy[x][y] == 'ddr':
              previousxy = self.ijtoxy(x,y)
              x = x + 1
              y = y + 1

              currentxy = self.ijtoxy(x,y)
              targetDistance = self.compute_distance(currentxy, target)
              
              distance, bearing = self.measure_distance_and_bearing_to(previousxy, currentxy)

              if bearing > self.max_steering:
                moves.append('move ' + str(self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(-self.max_steering) + ' 0 ')
                # print "up distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = abs(bearing) - self.max_steering
              elif bearing < -self.max_steering:
                moves.append('move ' + str(-self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(self.max_steering) + ' 0 ')
                # print "ddr-min distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = bearing + self.max_steering

              # print "ddr distance and bearing and target", distance, bearing, targetDistance

              
              if targetDistance <= self.distanceToTarg:
                lastX = x - 1
                lastY = y - 1
                moves.append('lift ' + str(targ))
                reverse.append('down ' + str(xyinit[0]) + ' ' + str(xyinit[1]))
                break
              else:
                moves.append('move ' + str(bearing) + ' ' + str(distance))
                reverse.append('move ' + str(-bearing) + ' ' + str(distance))

            elif policy[x][y] == 'dur':
              x = x - 1
              y = y + 1
              currentxy = self.ijtoxy(x,y)
              targetDistance = self.compute_distance(currentxy, target)

              distance, bearing = self.measure_distance_and_bearing_to(previousxy, currentxy)

              if bearing > self.max_steering:
                moves.append('move ' + str(self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(-self.max_steering) + ' 0 ')
                # print "up distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = abs(bearing) - self.max_steering
              elif bearing < -self.max_steering:
                moves.append('move ' + str(-self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(self.max_steering) + ' 0 ')
                # print "ddr-min distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = bearing + self.max_steering

              # print "dur distance and bearing and target", distance, bearing, targetDistance
              
              if targetDistance <= self.distanceToTarg:
                lastX = x + 1
                lastY = y - 1
                moves.append('lift ' + str(targ))
                reverse.append('down ' + str(xyinit[0]) + ' ' + str(xyinit[1]))
                break
              else:
                moves.append('move ' + str(bearing) + ' ' + str(distance))
                reverse.append('move ' + str(-bearing) + ' ' + str(distance))

            elif policy[x][y] == 'ddl':
              x = x + 1
              y = y - 1
              currentxy = self.ijtoxy(x,y)

              targetDistance = self.compute_distance(currentxy, target)
              distance, bearing = self.measure_distance_and_bearing_to(previousxy, currentxy)

              if bearing > self.max_steering:
                moves.append('move ' + str(self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(-self.max_steering) + ' 0 ')
                # print "up distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = abs(bearing) - self.max_steering
              elif bearing < -self.max_steering:
                moves.append('move ' + str(-self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(self.max_steering) + ' 0 ')
                # print "ddr-min distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = bearing + self.max_steering

              # print "ddl distance and bearing and target", distance, bearing, targetDistance
              
              if targetDistance <= self.distanceToTarg:
                lastX = x - 1
                lastY = y + 1
                moves.append('lift ' + str(targ))
                reverse.append('down ' + str(xyinit[0]) + ' ' + str(xyinit[1]))
                break
              else:
                moves.append('move ' + str(bearing) + ' ' + str(distance))
                reverse.append('move ' + str(-bearing) + ' ' + str(distance))

            # print "current xy ", x, y
          # print moves
          # final_moves.extend(moves)
          # print final_moves
          # print reverse
          # temp = reverse[1:len(reverse) - 1]
          # temp.reverse()
          # # print "last ", reverse.pop()
          # print "temp ", temp
          
          # # if (moves[-1] == temp[0]):
          # #   moves += temp[1:]
          # # else:
          # moves += temp
          # moves.append(reverse.pop())
          # print moves

          # init = self.xytoij(target[0], target[1])
          init2 = lastX, lastY
          target2 = self.ijtoxy(init[0], init[1])

          # print "init2", init2
          # print "target2", target2

          for key, value in self.minigrid.items():
            # print "xy", key, value
            # print "ij ", ij
            ij = self.xytoij(key[0], key[1])
            # if value == '@':
            #   # print "found @ at ", key
            #   if init == 0:
            #     fixedinit = self.xytoij(key[0], key[1])
            #     init = fixedinit
            #     print "init", init
            if key == target2:
              goal = self.xytoij(key[0], key[1])
              targ = value
              # print "goal", goal
              # print "targ", targ

            heuristic[ij[0]][ij[1]] = self.findHeuristic(key[0], key[1], target[0], target[1])
            
          closed = np.array([[0 for col in range(len(self.warehouse[0]) * self.xRange)] for row in range(len(self.warehouse) * self.yRange)])
          closed[[init2[0]],[init2[1]]] = 1
          action = np.array([[-1 for col in range(len(self.warehouse[0]) * self.xRange)] for row in range(len(self.warehouse) * self.yRange)])
          # print action
          expand = np.array([[-1 for col in range(len(self.warehouse[0]) * self.xRange)] for row in range(len(self.warehouse) * self.yRange)])
          

          x = init2[0]
          y = init2[1]
          g = 0
          h = heuristic[x][y]
          f = g + h

          open = [[f, g, h, x, y]]

          found = False  # flag that is set when search is complete
          resign = False # flag set if we can't find expand
          count = 0
 

          # # print "goal", goal
          # # print "heuristic", heuristic
        
          while found is False and resign is False:
            if len(open) == 0:
                print "closed", closed
                resign = True
                print ("fail")
                
            else:
                open.sort()
                open.reverse()
                next = open.pop()
                # print "next ", next
                
                x = next[3]
                y = next[4]
                g = next[1]

                expand[x][y] = count
                count += 1

                if x == goal[0] and y == goal[1]:
                    found = True
                    # print "found", closed
                    # print next
                else:
                    # expand winning element and add to new open list
                    for i in range(len(delta)):
                        x2 = x + delta[i][0]
                        y2 = y + delta[i][1]
                        if x2 >= 0 and x2 < len(self.warehouse) * self.xRange and y2 >= 0 and y2 < len(self.warehouse[0]) * self.yRange:
                            gxy = self.ijtoxy(x2, y2)
                            # print "x2, y2", x2, y2
                            # print "gxy", (gxy[0], gxy[1])
                            # print "minigrid", self.minigrid[(gxy[0], gxy[1])]
                            # print closed[x2][y2]
                            # print self.minigrid[(gxy[0], gxy[1])]                    
                            if closed[x2][y2] == 0 and (self.minigrid[(gxy[0], gxy[1])] == '.'): # or previousTarget.count(self.minigrid[(gxy[0], gxy[1])]) > 0) :
                                g2 = g + cost
                                h2 = heuristic[x2][y2]
                                f2 = g2 + h2
                                open.append([f2, g2, h2, x2, y2])
                                closed[x2][y2] = 1
                                # print "target ", target
                                # print "closed ", closed
                                action[x2][y2] = i
                            elif closed[x2][y2] == 0 and (gxy[0], gxy[1]) == target2:  # and self.warehouse[x][y] != '@':
                                g2 = g + cost
                                h2 = heuristic[x2][y2]
                                f2 = g2 + h2
                                open.append([f2, g2, h2, x2, y2])
                                # print "target ", target 
                                # closed[x2][y2] = target
                                action[x2][y2] = i
                
          # print action
          # [[-1 for col in range(len(self.warehouse[0]) * self.xRange)] for row in range(len(self.warehouse) * self.yRange)]
          policy = np.array([["   " for col in range(len(self.warehouse[0]) * self.xRange)] for row in range(len(self.warehouse) * self.yRange)])
          reversePolicy = np.array([["   " for col in range(len(self.warehouse[0]))] for row in range(len(self.warehouse))])
          x = goal[0]
          y = goal[1]
          policy[x][y] = targ

          # print "action len", len(action)
          while x != init2[0] or y != init2[1]:
            x2 = abs(x - delta[action[x][y]][0])
            y2 = abs(y - delta[action[x][y]][1])
            # print self.ijtoxy(x,y)
            # print "x, y", x, y
            # print "x2, y2", x2, y2
            policy[x2][y2] = delta_name[action[x][y]]
            x = x2
            y = y2

          # print "reverse policy", policy

          while x != goal[0] or y != goal[1]:
            previousxy = self.ijtoxy(x,y)
            # print "xy and grid value ", previousxy, self.minigrid[previousxy]
            if policy[x][y] == 'up':
              x = x - 1
              y = y 

              currentxy = self.ijtoxy(x,y)
              distance = self.compute_distance(previousxy, currentxy)
              targetDistance = self.compute_distance(currentxy, target)
              distance, bearing = self.measure_distance_and_bearing_to(previousxy, currentxy, target)
              
              if bearing > self.max_steering:
                moves.append('move ' + str(self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(-self.max_steering) + ' 0 ')
                # print "up distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = abs(bearing) - self.max_steering
              elif bearing < -self.max_steering:
                moves.append('move ' + str(-self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(self.max_steering) + ' 0 ')
                # print "ddr-min distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = bearing + self.max_steering

              # print "up distance and bearing and target", distance, bearing, targetDistance

              if targetDistance <= self.distanceToTarg:
                lastX = x + 1
                lastY = y
                moves.append('lift ' + str(targ))
                reverse.append('down ' + str(xyinit[0]) + ' ' + str(xyinit[1]))
                break
              else:
                moves.append('move ' + str(bearing) + ' ' + str(distance))
                reverse.append('move ' + str(-bearing) + ' ' + str(distance))

            elif policy[x][y] == 'lf':
              x = x
              y = y - 1

              currentxy = self.ijtoxy(x,y)
              distance = self.compute_distance(previousxy, currentxy)
              targetDistance = self.compute_distance(currentxy, target)
              distance, bearing = self.measure_distance_and_bearing_to(previousxy, currentxy)

              if bearing > self.max_steering:
                moves.append('move ' + str(self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(-self.max_steering) + ' 0 ')
                # print "up distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = abs(bearing) - self.max_steering
              elif bearing < -self.max_steering:
                moves.append('move ' + str(-self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(self.max_steering) + ' 0 ')
                # print "ddr-min distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = bearing + self.max_steering

              # print "lf distance and bearing and target", distance, bearing, targetDistance

              if targetDistance <= self.distanceToTarg:
                lastX = x
                lastY = y + 1
                moves.append('lift ' + str(targ))
                reverse.append('down ' + str(xyinit[0]) + ' ' + str(xyinit[1]))
                break
              else:
                moves.append('move ' + str(bearing) + ' ' + str(distance))
                reverse.append('move ' + str(-bearing) + ' ' + str(distance))

            elif policy[x][y] == 'dn':
              x = x + 1
              y = y

              currentxy = self.ijtoxy(x,y)
              targetDistance = self.compute_distance(currentxy, target)
              distance, bearing = self.measure_distance_and_bearing_to(previousxy, currentxy)

              if bearing > self.max_steering:
                moves.append('move ' + str(self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(-self.max_steering) + ' 0 ')
                # print "up distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = abs(bearing) - self.max_steering
              elif bearing < -self.max_steering:
                moves.append('move ' + str(-self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(self.max_steering) + ' 0 ')
                # print "ddr-min distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = bearing + self.max_steering

              # print "dn distance and bearing and target", distance, bearing, targetDistance

              if targetDistance <= self.distanceToTarg:
                lastX = x - 1
                lastY = y
                moves.append('lift ' + str(targ))
                reverse.append('down ' + str(xyinit[0]) + ' ' + str(xyinit[1]))
                break
              else:
                moves.append('move ' + str(bearing) + ' ' + str(distance))
                reverse.append('move ' + str(-bearing) + ' ' + str(distance))

            elif policy[x][y] == 'rt':
              x = x
              y = y + 1

              currentxy = self.ijtoxy(x,y)
              distance = self.compute_distance(previousxy, currentxy)
              targetDistance = self.compute_distance(currentxy, target)
              distance, bearing = self.measure_distance_and_bearing_to(previousxy, currentxy)

              if bearing > self.max_steering:
                moves.append('move ' + str(self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(-self.max_steering) + ' 0 ')
                # print "up distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = abs(bearing) - self.max_steering
              elif bearing < -self.max_steering:
                moves.append('move ' + str(-self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(self.max_steering) + ' 0 ')
                # print "ddr-min distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = bearing + self.max_steering

              # print "rt distance and bearing and target", distance, bearing, targetDistance

              if targetDistance <= self.distanceToTarg:
                lastX = x
                lastY = y - 1
                moves.append('lift ' + str(targ))
                reverse.append('down ' + str(xyinit[0]) + ' ' + str(xyinit[1]))
                break
              else:
                moves.append('move ' + str(bearing) + ' ' + str(distance))
                reverse.append('move ' + str(-bearing) + ' ' + str(distance))

            elif policy[x][y] == 'dul':
              x = x - 1
              y = y - 1
              currentxy = self.ijtoxy(x,y)
              # distance = self.compute_distance(previousxy, currentxy)
              targetDistance = self.compute_distance(currentxy, target)
              distance, bearing = self.measure_distance_and_bearing_to(previousxy, currentxy, target)

              if bearing > self.max_steering:
                moves.append('move ' + str(self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(-self.max_steering) + ' 0 ')
                # print "up distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = abs(bearing) - self.max_steering
              elif bearing < -self.max_steering:
                moves.append('move ' + str(-self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(self.max_steering) + ' 0 ')
                # print "ddr-min distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = bearing + self.max_steering
              
              # print "dul distance and bearing and target", distance, bearing, targetDistance
              
              
              if targetDistance <= self.distanceToTarg:
                lastX = x + 1
                lastY = y + 1
                moves.append('lift ' + str(targ))
                reverse.append('down ' + str(xyinit[0]) + ' ' + str(xyinit[1]))
                break
              else:
                moves.append('move ' + str(bearing) + ' ' + str(distance))
                reverse.append('move ' + str(-bearing) + ' ' + str(distance))

            elif policy[x][y] == 'ddr':
              previousxy = self.ijtoxy(x,y)
              x = x + 1
              y = y + 1

              currentxy = self.ijtoxy(x,y)
              targetDistance = self.compute_distance(currentxy, target)
              
              distance, bearing = self.measure_distance_and_bearing_to(previousxy, currentxy)
              # print "ddr bearing", bearing
              if bearing > self.max_steering:
                moves.append('move ' + str(self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(-self.max_steering) + ' 0 ')
                # print "ddr-max distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = abs(bearing) - self.max_steering
              elif bearing < -self.max_steering:
                moves.append('move ' + str(-self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(self.max_steering) + ' 0 ')
                # print "ddr-min distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = bearing + self.max_steering

              # print "ddr distance and bearing and target", distance, bearing, targetDistance

              
              if targetDistance <= self.distanceToTarg:
                lastX = x - 1
                lastY = y - 1
                moves.append('lift ' + str(targ))
                reverse.append('down ' + str(xyinit[0]) + ' ' + str(xyinit[1]))
                break
              else:
                moves.append('move ' + str(bearing) + ' ' + str(distance))
                reverse.append('move ' + str(-bearing) + ' ' + str(distance))

            elif policy[x][y] == 'dur':
              x = x - 1
              y = y + 1
              currentxy = self.ijtoxy(x,y)
              targetDistance = self.compute_distance(currentxy, target)

              distance, bearing = self.measure_distance_and_bearing_to(previousxy, currentxy)

              if bearing > self.max_steering:
                moves.append('move ' + str(self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(-self.max_steering) + ' 0 ')
                # print "up distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = abs(bearing) - self.max_steering
              elif bearing < -self.max_steering:
                moves.append('move ' + str(-self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(self.max_steering) + ' 0 ')
                # print "ddr-min distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = bearing + self.max_steering

              # print "dur distance and bearing and target", distance, bearing, targetDistance
              
              if targetDistance <= self.distanceToTarg:
                lastX = x + 1
                lastY = y - 1
                moves.append('lift ' + str(targ))
                reverse.append('down ' + str(xyinit[0]) + ' ' + str(xyinit[1]))
                break
              else:
                moves.append('move ' + str(bearing) + ' ' + str(distance))
                reverse.append('move ' + str(-bearing) + ' ' + str(distance))

            elif policy[x][y] == 'ddl':
              x = x + 1
              y = y - 1
              currentxy = self.ijtoxy(x,y)

              targetDistance = self.compute_distance(currentxy, target)
              distance, bearing = self.measure_distance_and_bearing_to(previousxy, currentxy)

              if bearing > self.max_steering:
                moves.append('move ' + str(self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(-self.max_steering) + ' 0 ')
                # print "up distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = abs(bearing) - self.max_steering
              elif bearing < -self.max_steering:
                moves.append('move ' + str(-self.max_steering) + ' 0 ') # adjust angle
                reverse.append('move ' + str(self.max_steering) + ' 0 ')
                # print "ddr-min distance and bearing and target", 0, self.max_steering, targetDistance
                bearing = bearing + self.max_steering

              # print "ddl distance and bearing and target", distance, bearing, targetDistance
              
              if targetDistance <= self.distanceToTarg:
                lastX = x - 1
                lastY = y + 1
                moves.append('lift ' + str(targ))
                reverse.append('down ' + str(xyinit[0]) + ' ' + str(xyinit[1]))
                break
              else:
                moves.append('move ' + str(bearing) + ' ' + str(distance))
                reverse.append('move ' + str(bearing) + ' ' + str(distance))

            # print "current xy ", x, y

          s = 'down ' + str(target2[0]) + ' ' + str(target2[1])
          moves.append(s)
          print "moves for target", targ, moves
          final_moves.extend(moves)
          # print final_moves
        # print "printing"
        print "print final moves", final_moves
        # for key, value in self.minigrid.items():
        #   if value == '$':
        #     print key
        #     # print "keys with not allowed", key, value

        # for key, value in self.minigrid.items():
        #   if value == '#':
        #     print "keys with wall", key, value



        # print "padding at ", self.minigrid[(3.0, 1.0)]




          
        # print self.minigrid
        # print self.minigrid[(4.0, -2.5)]





        # moves = ['move 1.570963 2.0',  # rotate and move north 2 spaces
        #           'move 1.570963 0.1',  # rotate west and move closer to second box
        #           'lift 1',             # lift the second box
        #           'move 0.785398 1.5',  # rotate to sw and move down 1.5 squares
        #           'down 3.5 -4.0',      # set the box out of the way
        #           'move -0.785398 2.0',  # rotate to west and move 2.5 squares
        #           'move -1.570963 2.7',  # rotate to north and move to pick up box 0
        #           'lift 0',             # lift the first box
        #           'move -1.570963 0.0',  # rotate to the south east
        #           'move -0.785398 1.0',  # finish rotation
        #           'move 0.785398 2.5',  # rotate to east and move
        #           'move -1.570963 2.5',  # rotate and move south
        #           'down 4.5 -4.5',      # set down the box in the dropzone
        #           'move -1.570963 0.6',  # rotate to west and move towards box 1
        #           'lift 1',             # lift the second box
        #           'move 1.570963 0.0',  # rotate north
        #           'move 1.570963 0.6',  # rotate east and move back towards dropzone
        #           'down 4.5 -4.5']      # deliver second box
        # moves = []
        return final_moves
        # return moves