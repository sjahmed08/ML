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

#These import statements give you access to library functions which you may
# (or may not?) want to use.

import random
import copy

from math import *
from glider import *
from copy import deepcopy
from numpy import mean



#This is the function you will have to write for part A. 
#-The argument 'height' is a floating point number representing 
# the number of meters your glider is above the average surface based upon 
# atmospheric pressure. (You can think of this as hight above 'sea level'
# except that Mars does not have seas.) Note that this sensor may be off
# a static  amount that will not change over the course of your flight.
# This number will go down over time as your glider slowly descends.
#
#-The argument 'radar' is a floating point number representing the
# number of meters your glider is above the specific point directly below
# your glider based off of a downward facing radar distance sensor. Note that
# this sensor has random Gaussian noise which is different for each read.

#-The argument 'mapFunc' is a function that takes two parameters (x,y)
# and returns the elevation above "sea level" for that location on the map
# of the area your glider is flying above.  Note that although this function
# accepts floating point numbers, the resolution of your map is 1 meter, so
# that passing in integer locations is reasonable.
#
#
#-The argument OTHER is initially None, but if you return an OTHER from
# this function call, it will be passed back to you the next time it is
# called, so that you can use it to keep track of important information
# over time.
#


# CITE: measurement_prob() from ps3_solutions
# https://classroom.udacity.com/courses/cs373/lessons/48532754/concepts/487174160923  
def measurement_prob(height, radar, particle_measurement, sigma):
        # calculates how likely a measurement should be
        measurement = height - radar
        error = 1
        error_distance = measurement - particle_measurement
        error *= (exp(- ((error_distance) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2)))
        return error
# END CITE    

def estimate_next_pos(height, radar, mapFunc, OTHER):
   #example of how to find the actual elevation of a point of ground from the map:
   # actualElevation = mapFunc(5,4)
   #print "height", height
   # print "radar", radar - height
   # in this order for grading purposes.
   #
   # xy_estimate = (0,0)  #Sample answer, (X,Y) as a tuple.

   #TODO - remove this canned answer which makes this template code
   #pass one test case once you start to write your solution.... 

   # optionalPointsToPlot = [ (1,1), (2,2), (3,3) ]  #Sample (x,y) to plot 
   # optionalPointsToPlot = [ (1,1,0.5),   (2,2, 1.8), (3,3, 3.2) ] #(x,y,heading)


   # return xy_estimate, OTHER, optionalPointsToPlot
   
   if OTHER == None:
      #print OTHER
      N = 30000
      T = 1
      p = []

      for i in range(N):
         x = random.uniform(-250, 250)
         y = random.uniform(-250, 250)
         h = random.gauss(0,pi/4.0)

         
         particle = (glider(x, y, z = height, heading = h))
         p.append(deepcopy(particle))


      N = len(p)
      w = []

      for i in range(N):
         w.append(measurement_prob(height, radar, mapFunc(p[i].x, p[i].y), 25))
      
      p3 = []
      index = int(random.random() * N)
      
      beta = 0.0
      mw = max(w)
      ret = []
      optionalPointsToPlot = []
      
      for i in range(1000):
         beta += random.random() * 2.0 * mw
         while beta > w[index]:
            beta -= w[index]
            index = (index + 1) % N
         # if w[index] < mw * 0.10:
         if index < 251:
            p[index].x += random.uniform(-2, 2)
            p[index].y += random.uniform(-2, 2)
            p[index].heading += random.uniform(-pi / 16, pi / 16)
            
         p3.append(deepcopy(p[index]))
      p = deepcopy(p3)

      p4 = []
      for i in range(len(p)):
         p[i].glide()
         p4.append(deepcopy(p[i]))
         optionalPointsToPlot.append((p4[i].x,p4[i].y,p4[i].heading))
         if w[i] >= mw * .90:
            ret.append((p4[i].x, p4[i].y))

      p = deepcopy(p4)
      return tuple(mean(ret, axis=0)), p, optionalPointsToPlot

   else:
      p = deepcopy(OTHER)
      N = len(p)
      w = []

      for i in range(N):
         w.append(measurement_prob(height, radar, mapFunc(p[i].x, p[i].y), 25))   

      N = len(w)    
      p3 = []
      index = int(random.random() * N)
      
      beta = 0.0
      mw = max(w)
      ret = []
      optionalPointsToPlot = []

      for i in range(N):
         beta += random.random() * 2.0 * mw
         while beta > w[index]:
            beta -= w[index]
            index = (index + 1) % N
         # if w[index] < mw * 0.10:
         if index < 251:
            p[index].x += random.uniform(-2, 2)
            p[index].y += random.uniform(-2, 2)
            p[index].heading += random.uniform(-pi / 16, pi / 16)
         p3.append(deepcopy(p[index]))
      p = deepcopy(p3)

      p4 = []
      for i in range(len(p)):
         p[i].glide()
         p4.append(deepcopy(p[i]))
         optionalPointsToPlot.append((p4[i].x,p4[i].y,p4[i].heading))
         if w[i] >= mw * .90:
            ret.append((p4[i].x, p4[i].y))

      p = deepcopy(p4)
      return tuple(mean(ret, axis=0)), p, optionalPointsToPlot

# This is the function you will have to write for part B. The goal in part B
# is to navigate your glider towards (0,0) on the map steering # the glider 
# using its rudder. Note that the Z height is unimportant.

#
# The input parameters are exactly the same as for part A.

def angle_trunc(a):
    """Helper function to map all angles onto [-pi, pi]

    Arguments:
        a(float): angle to truncate.

    Returns:
        angle between -pi and pi.
    """
    return ((a + pi) % (pi * 2)) - pi

def next_angle(height, radar, mapFunc, OTHER=None):

   #How far to turn this timestep, limited to +/-  pi/8, zero means no turn.
   steering_angle = .01
   time_step = 1

   if OTHER == None:
      #print OTHER
      N = 30000
      T = 1
      p = []

      for i in range(N):
         x = random.uniform(-250, 250)
         y = random.uniform(-250, 250)
         h = random.gauss(0,pi/4.0)

         
         particle = (glider(x, y, z = height, heading = h))
         p.append(deepcopy(particle))


      N = len(p)
      w = []

      for i in range(N):
         w.append(measurement_prob(height, radar, mapFunc(p[i].x, p[i].y), 30))
      
      p3 = []
      index = int(random.random() * N)
      
      beta = 0.0
      mw = max(w)
      ret = []
      optionalPointsToPlot = []
      
      for i in range(1000):
         beta += random.random() * 2.0 * mw
         while beta > w[index]:
            beta -= w[index]
            index = (index + 1) % N
         # if w[index] < mw * 0.10:
         if index < 251:
            p[index].x += random.uniform(-1, 1)
            p[index].y += random.uniform(-1, 1)
            p[index].heading += random.uniform(-pi / 16, pi / 16)
            
         p3.append(deepcopy(p[index]))
      p = deepcopy(p3)

      p4 = []
      for i in range(len(p)):
         p[i].glide()
         p4.append(deepcopy(p[i]))
         optionalPointsToPlot.append((p4[i].x,p4[i].y,p4[i].heading))
         if w[i] >= mw * .90:
            ret.append((p4[i].x, p4[i].y))

      p = deepcopy(p4)
      p.append(tuple(mean(ret, axis=0)))
      p.append(time_step)

      return steering_angle, p, optionalPointsToPlot

   else:
      p = deepcopy(OTHER)
      N = len(p)
      w = []

      time_step = p[len(p) - 1]
      # print "timestep", time_step
      previous_xy = p[len(p) - 2]
      # print "previous xy", previous_xy

      for i in range(N - 2):
         w.append(measurement_prob(height, radar, mapFunc(p[i].x, p[i].y), 30))   

      N = len(w)    
      p3 = []
      index = int(random.random() * N)
      
      beta = 0.0
      mw = max(w)
      ret = []
      optionalPointsToPlot = []
      heading = []

      for i in range(N):
         beta += random.random() * 2.0 * mw
         while beta > w[index]:
            beta -= w[index]
            index = (index + 1) % N
         # if w[index] < mw * 0.10:
         if index < 251:
            p[index].x += random.uniform(-1, 1)
            p[index].y += random.uniform(-1, 1)
            p[index].heading += random.uniform(-pi / 16, pi / 16)
         p3.append(deepcopy(p[index]))
         if w[i] >= mw * .90:
            ret.append((p3[i].x, p3[i].y))
            optionalPointsToPlot.append((p3[i].x,p3[i].y,p3[i].heading))
      p = deepcopy(p3)

      p4 = []

      # heading_avg = sum(heading) / len(heading)
      current_xy = tuple(mean(ret, axis=0))

      if time_step > 35:
         
         # print "current_xy", current_xy
         bearing1 = angle_trunc(atan2(previous_xy[1] - current_xy[1], previous_xy[0] - current_xy[0]))
         # print "bearing1", bearing1 
         bearing2 = angle_trunc(atan2(current_xy[1] - 0, current_xy[0] - 0))
         # print "bearing2", bearing2 - bearing1
         # bearing2 = atan2(previous_xy[1] - 0, previous_xy[0] - 0)
         steering_angle = (bearing2 - bearing1)

         if steering_angle > pi / 8:
            steering_angle = pi / 8

         if steering_angle < -pi /8:
            steering_angle = -pi / 8

         # print "steering angle", steering_angle
         for i in range(len(p)):
            p[i].glide(rudder=steering_angle)
            # p[i].glide()
            heading.append(p[i].heading)
            
            p4.append(deepcopy(p[i]))
                 
         p4.append(deepcopy(p[i]))
         heading_avg = sum(heading) / len(heading)
         # steering_angle = heading_avg

      else:
         for i in range(len(p)):
            p[i].glide()
            p4.append(deepcopy(p[i]))

      p = deepcopy(p4)


         
      p.append(current_xy)
      p.append(time_step + 1)
      
      return steering_angle, p, optionalPointsToPlot