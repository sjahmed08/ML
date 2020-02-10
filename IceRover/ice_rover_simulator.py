from turtle import *
import time
import re

def get_beacons(area_map):
    beacons=[]
    for i in range(len(area_map)):
        for j in range(len(area_map[i])):
            if area_map[i][j]=='L':
                center=j+.5,(i+.5)*-1
                #print center
                beacons.append(center)
            if area_map[i][j]=='@':
                start_loc=j+.5,(i+.5)*-1
                start=start_loc
    return beacons,start
    
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
    if length==.5:
        color("red")
    if length==.4:
        color("black")
    if length==.6:
        color("blue")
    fill(True)
    for i in range(4):
        #move forwards and turn at right angle
        #write(position())
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
            write('SAMPLE')
            hold=1
        if move_parts[0]=='move':
            left(float(move_parts[1]))
            forward(float(move_parts[2]))
            if hold==0:
                write(position())

        
############## MAIN ########################
area_map=['......',
                               '..LL..',
                               '..L@..']
todo=[(2.0, -3.0),
                           (16.5, -2.5),
                           (18.0, -12.5),
                           (32.5, -1.5),
                           (38.5, -3.75),
                           (43.0, -3.75),
                           (35.5, -14.0),
                           (52.0, -14.0)]
                           
#  python /Users/ken/Documents/OMSCS/AI4R_fall_2019/IceRover_working/ice_rover_simulator.py

moves=['move 0.55920551592 2.85', 'move 0.78098456261 2.85', 'move 0.809538603863 2.85', 'move 0.952205849619 2.85', 'move -1.58079632679 2.85', 'move -1.58079632679 0.639700434967', 'sample', 'move 0.460039055732 2.85', 'move 1.00517495796 2.85', 'move 1.07660559129 2.85', 'move 1.31314753183 2.85', 'move 1.17399125098 2.85', 'move 0.715210012903 2.85', 'move 1.37552533744 2.85', 'move 1.39285650377 2.85', 'move 1.09865068477 2.85', 'move 1.10925061511 2.85', 'move 1.53076854539 2.85', 'move 0.614768708369 2.85', 'move 1.23140871718 2.85', 'move 1.25600904921 2.85', 'move 1.35427933484 2.85', 'move 1.49390330248 2.85', 'move 1.07255783741 2.85', 'move 1.23398766762 2.85', 'move 1.31387119301 2.85', 'move 0.595109090917 2.85', 'move 0.784792096151 2.85', 'move 1.36248679385 2.85', 'move 1.1201812797 2.85', 'move 0.825612594424 2.85', 'move 0.656532666522 2.85', 'move 0.9189283321 2.85', 'move 1.35408492283 2.85', 'move 1.35242873947 2.85', 'move 0.777129334368 2.85', 'move 0.701706521651 2.85', 'move 1.36126863839 2.85', 'move 1.24627932411 2.85', 'move 1.09499505784 2.85', 'move 1.34018792226 2.85', 'move 1.34005345979 2.85', 'move 1.2683999548 2.85', 'move 1.06260346127 2.85', 'move 1.11676019842 2.85', 'move 0.857433357976 2.85', 'move 1.19539750349 2.85', 'move 1.22414144622 2.85', 'move 1.25956338811 2.85', 'move 1.46929708164 2.85', 'move 1.41133288549 2.85', 'move 1.44221050475 2.85', 'move 0.57758464836 2.85', 'move 1.54676228973 2.85', 'move 0.592408944313 2.85', 'move 0.883205525365 2.85', 'move 1.2169651514 2.85', 'move 0.551801711102 2.85', 'move 0.675402902775 2.85', 'move 0.965098850759 2.85', 'move 1.16800625214 2.85', 'move 1.11388443472 2.85', 'move 1.48840555922 2.85', 'move 0.55643776333 2.85', 'move 0.826929666253 2.85', 'move 0.623716041525 2.85', 'move 0.578820136223 2.85', 'move 1.16751003426 2.85', 'move 0.682682804695 2.85', 'move 1.4778984403 2.85', 'move 0.819620404635 2.85', 'move 0.552930688474 2.85', 'move 1.51211900231 2.85', 'move 1.44300686188 2.85', 'move 1.0154040317 2.85', 'move 0.885927688635 2.85', 'move 0.69339665245 2.85', 'move 0.78270206532 2.85', 'move 0.601966608421 2.85', 'move -1.11327365157 1.90648118646', 'move 0.544811760026 0.294724300039', 'sample', 'move 0.452599408837 2.85', 'move 0.791494138072 2.85', 'move 0.437140403078 2.85', 'move 1.47966439471 2.85', 'move 0.864024354598 2.85', 'move 1.47260697777 2.85', 'move 1.42819165069 2.85', 'move 0.614728618001 2.85', 'move 0.621204389691 2.85', 'move 1.53999324292 2.85', 'move 0.444859776069 2.85', 'move 1.31718059738 2.85', 'move 1.3739864965 2.85', 'move 0.917192104624 2.85', 'move 1.21260835089 2.85', 'move 1.4917920786 2.85', 'move 0.782562172775 2.85', 'move 0.997500228967 2.85', 'move 1.45368878235 2.85', 'move 0.712461936062 2.85', 'move 0.799446185927 2.85', 'move 0.602630847615 2.85', 'move 1.09191576576 2.85', 'move 1.44781544534 2.85', 'move 1.25908786895 2.85']


##### set coordinates for area map
setworldcoordinates(0, -len(area_map), len(area_map[0]), 0)
turtlesize(stretch_wid=2, stretch_len=2)

# get beacons and start form area map
beacons, start = get_beacons(area_map)

#draw start location blue 
obstacles(.6,start[0],start[1])

#draw beacons black
#for i in range(len(beacons)):
    #obstacles(.4,beacons[i][0],beacons[i][1])

## draw sites to sample from todo green
for i in range(len(todo)):
    obstacles(.5,todo[i][0],todo[i][1])
    


###### draw path - from start and moves list
draw_path_moves(start, moves)



print window_width()
print window_height()
exitonclick()