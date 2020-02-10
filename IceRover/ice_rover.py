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

"""
 === Introduction ===
 
   A few months ago a new rover was sent to McMurdo Station in the Antarctic. The rover is a technical marvel
   as it is equipped with the latest scientific sensors and analyzers capable of surviving the harsh climate of the
   South Pole.  The goal is for the rover to reach a series of test sites and perform scientific sampling and analysis.
   Due to the extreme conditions, the rover will be air dropped via parachute into the test area.  The good news is
   the surface is smooth and free from any type of obstacles, the bad news is the surface is entirely ice which may 
   introduce noise into your rovers movements.  The station scientists are ready to deploy the new rover, but first 
   we need to create and test the planning software that will be used on board to ensure it can complete it's goals.

   The assignment is broken up into two parts.

   Part A:
        Create a SLAM implementation to process a series of landmark (beacon) measurements and movement updates.

        Hint: A planner with an unknown number of motions works well with an online version of SLAM.

    Part B:
        Here you will create the planner for the rover.  The rover does unfortunately has a series of limitations:

        - Start position
          - The rover will land somewhere within range of at least 3 or more landmarks (beacons or sites) for measurements.

        - Measurements
          - Measurements will come from beacons and test sites within range of the rover's antenna horizon (the horizon distance).
            * The format is {'landmark id':{'distance':0.0, 'bearing':0.0, 'type':'beacon'}, ...}
          - Beacons and test sites will always return a measurement if in range.

        - Movements
          - Action: 'move 1.570963 1.0'
            * The rover will turn counterclockwise 90 degrees and then move 1.0
          - stochastic due to the icy surface.
          - if max distance or steering is exceeded, the rover will not move.

        - Samples
          - Provided as list of x and y coordinates, [[0., 0.], [1., -3.5], ...]
          - Action: 'sample'
            * The rover will attempt to take a sample at the current location.
          - A rover can only take a sample once per requested site.
          - The rover must be within 0.25 distance to successfully take a sample.
            * Hint: Be sure to account for floating point limitations
          - The is a 100ms penalty if the robot is requested to sample a site not on the list or if the site has
            previously been sampled.
          - You may temporarily use sys.stdout = open('stdout.txt', 'w') to directly print data if necessary, HOWEVER, you MUST REMOVE these lines before submitting your code or it will keep our testing framework from giving you a grade (larger than a zero). 

        The rover will always execute a measurement first, followed by an action.

        The rover will have a time limit of 5 seconds to find and sample all required sites.
"""
from matrix import matrix
from robot import Robot
from math import *
import math
PI = math.pi

def truncate_angle(t):
    return ((t+PI) % (2*PI)) - PI

class SLAM:
    """Create a basic SLAM module.
    """

    def __init__(self):
        """Initialize SLAM components here.
        """
        self.Robot = Robot()
        self.Omega = matrix()
        # self.Omega.value[0][0] = 1.0
        # self.Omega.value[1][1] = 1.0
        self.Xi = matrix()
        # Xi.value[0][0] = 0.0
        # Xi.value[1][0] = 0.0
        self.measure = {}
        self.landMarkCount  = 0
        self.init = False
        self.bearing = 0
        self.x = 0
        self.y = 0
        
        # TODO

    def process_measurements(self, measurements):
        """Process a new series of measurements.

        Args:
            measurements(dict): Collection of measurements
                in the format {'landmark id':{'distance':0.0, 'bearing':0.0, 'type':'beacon'}, ...}

        Returns:
            x, y: current belief in location of the rover relative to initial location before movement
        """
        # TODO
        if self.init == False:
          dim = 2 * (1 + len(measurements))
          # print "dimension is ", dim
          # print "size of measurements ", len(measurements)
          self.Omega.zero(dim, dim)
          self.Omega.value[0][0] = 1.0
          self.Omega.value[1][1] = 1.0

          self.Xi.zero(dim, 1)
          self.Xi.value[0][0] = 0.0
          self.Xi.value[1][0] = 0.0
          self.init = True
        
        
        # print measurements
        for m in measurements.keys():
          # print "distance and steering ", measurements[m]['distance'], measurements[m]['bearing']

          dx = cos(measurements[m]['bearing']) * measurements[m]['distance']
          dy = sin(measurements[m]['bearing']) * measurements[m]['distance']
          # print "landmark x and y ", dx, dy

          # if m in self.measure:
          #   print "Already exists", m
          # else:
          #   self.landMarkCount += 1
          #   self.measure[m] = self.landMarkCount

        # for i in range(len(self.measure)):
        #   m  = 2 * (1 + (i + 1))
        #   print m 
        #   # get x, y coordinates for landmark
        #   print measurement[i][1+0]
          
          # for b in range(2):
          #   self.Omega.value[b][b]     +=  1.0 / measurement_noise
          #   self.Omega.value[m+b][m+b] +=  1.0 / measurement_noise
          #   self.Omega.value[b][m+b]   += -1.0 / measurement_noise
          #   self.Omega.value[m+b][b]   += -1.0 / measurement_noise
          #   self.Xi.value[b][0]        += -dx
          #   self.Xi.value[m+b][0]      +=  dy
          



        # print measurements
        # raise NotImplementedError

        x = 0.0
        y = 0.0

        return self.x, self.y

    def process_movement(self, steering, distance, motion_noise):
        """Process a new movement.

        Args:
            steering(float): amount to turn
            distance(float): distance to move
            motion_noise(float): movement noise

        Returns:
            x, y: current belief in location of the rover relative to initial location after movement
        """
        
        self.bearing = truncate_angle(self.bearing + float(steering))
        # print self.Robot.find_next_point(steering, distance)

        print "motion noise ", motion_noise

        self.x = self.x + (distance * math.cos(self.bearing))
        self.y = self.y + (distance * math.sin(self.bearing))
        # print "x and y", self.x, self.y, self.bearing
        # TODO
        # raise NotImplementedError

        x = 0.0
        y = 0.0

        return self.x, self.y


class WayPointPlanner:
    """Create a planner to navigate the rover to reach all the intended way points from an unknown start position.
    """

    def __init__(self,  max_distance, max_steering):
        """Initialize your planner here.
        

        Args:
            max_distance(float): the max distance the robot can travel in a single move.
            max_steering(float): the max steering angle the robot can turn in a single move.
        """
        # TODO
        self.max_dist = max_distance
        self.max_steer = max_steering
        self.bearing = 0
        self.movements = 0
        self.distance = 0
        self.todo = []
        self.last_todo = []
        self.sample = False
        self.distance_remain = 0
        self.steer_remain = 0
        self.explore = True
        self.site = {}
        self.site_id = 0
        self.distance_list = []
        self.x = 0
        self.y = 0
        self.robot_found = False
        self.to_go = []
        


    def next_move(self, sample_todo, measurements):
        """Next move based on the current set of measurements.

        Args:
            sample_todo(list): Set of locations remaining still needing a sample to be taken.
            measurements(dict): Collection of measurements from beacons and test sites in range.
                in the format {'landmark id':{'distance':0.0, 'bearing':0.0, 'type':'beacon'}, ...}

        Return:
            Next command to execute on the rover.
                allowed:
                    'move 1.570963 1.0' - turn left 90 degrees and move 1.0 distance
                    'sample' - take sample (will succeed if within tolerance of intended sample site)
        """
        dist = .4
        dist_inc = .3

        if self.sample == True:
          action = 'sample '
          self.sample = False
          return action

        # raise NotImplementedError
        if len(self.todo) == 0:
          self.todo = sample_todo
          # print self.todo

        if self.todo != sample_todo:
          # print "sample found", self.todo, sample_todo
          # print "found" 
          if self.last_todo != sample_todo:
            # print "found new site"
            self.robot_found = False

          if self.movements == 3:
            self.distance += dist_inc
            steering = .71
            self.movements = 1
            # action = 'move ' + str(steering) + ' ' + str(self.distance)
            self.sample = True
          elif self.movements == 0: # first movement
            self.distance = dist
            steering = .71
            self.movements += 1
            # action = 'move ' + str(steering) + ' ' + str(self.distance)
            self.sample = True
          else:
            steering = 0
            self.movements += 1
            # action = 'move ' + str(steering) + ' ' + str(self.distance)
            self.sample = True

          if self.robot_found == True:
            steering = measurements[self.site_id]['bearing']
            distance = measurements[self.site_id]['distance']
            
            # print distance 
            # exit()
            if (distance > self.max_dist):
              distance = self.max_dist

            if (steering > self.max_steer):
              steering = self.max_steer

            if (steering < (-self.max_steer)):
              steering = -self.max_steer
            # print "going to found site", steering, distance
            self.distance = distance
          else:
            for m in measurements:
              # print m
              if measurements[m]['type'] == 'site':
                self.robot_found = True
                self.site_id = m
                steering = measurements[m]['bearing']
                distance = measurements[m]['distance']

                if (distance > self.max_dist):
                  distance = self.max_dist

                if (steering > self.max_steer):
                  steering = self.max_steer

                if (steering < (-self.max_steer)):
                    steering = -self.max_steer

                self.distance = distance
                break

          if (self.distance > self.max_dist):
              self.distance = self.max_dist

          if (steering > self.max_steer):
            steering = self.max_steer

          if (steering < (-self.max_steer)):
            steering = -self.max_steer

          self.last_todo = sample_todo
          self.bearing = truncate_angle(self.bearing + float (steering))
          self.x = self.x + (self.distance * math.cos(self.bearing))
          self.y = self.y + (self.distance * math.sin(self.bearing))
        
          action = 'move ' + str(steering) + ' ' + str(self.distance)
          
          self.sample = True
          return action
          

        if self.explore == True:
          if self.movements == 7:
            self.distance += dist_inc
            steering = 1.570963
            self.movements = 1
            # action = 'move ' + str(steering) + ' ' + str(self.distance)
            self.sample = True
          elif self.movements == 0: # first movement
            self.distance = dist
            steering = 1.570963
            self.movements += 1
            # action = 'move ' + str(steering) + ' ' + str(self.distance)
            self.sample = True
          else:
            steering = 0
            self.movements += 1
            # action = 'move ' + str(steering) + ' ' + str(self.distance)
            self.sample = True
          # print measurements
          
          if self.site_id == 0:
            for m in measurements:
              if measurements[m]['type'] == 'site':
                self.site_id = m
                # print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@site",m
                steering = measurements[m]['bearing']
                distance = measurements[m]['distance']
                # print steering
                # print distance 
                # exit()
                if (distance > self.max_dist):
                  distance = self.max_dist

                if (steering > self.max_steer):
                  steering = self.max_steer

                if (steering < (-self.max_steer)):
                   steering = -self.max_steer

                self.distance = distance
                break
          else:
            steering = measurements[self.site_id]['bearing']
            distance = measurements[self.site_id]['distance']
            # print steering
            # print distance 
            # exit()
            if (distance > self.max_dist):
              distance = self.max_dist

            if (steering > self.max_steer):
              steering = self.max_steer

            if (steering < (-self.max_steer)):
              steering = -self.max_steer

            self.distance = distance

          self.bearing = truncate_angle(self.bearing + float(steering))
          self.x = self.x + (self.distance * math.cos(self.bearing))
          self.y = self.y + (self.distance * math.sin(self.bearing))

          # print "ice rover x,y", self.x, self.y
          action = 'move ' + str(steering) + ' ' + str(self.distance)
          # print "movements ", self.movements
          # print "bearing is ", self.bearing
          # print "action is", action
          return action
