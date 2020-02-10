""" 
  Alejandro Guizar

Here is a measurement and motion generator for project 3, part A. Based on problem set 6 and the ice rover test suite, it produces a series of measurements and motions that can be used to verify your SLAM implementation. Hope it helps.
"""


import random as rnd
import hashlib
from robot import Robot
from ice_rover import SLAM


def make_landmarks(world_size, num):
    return [(rnd.uniform(-world_size, world_size), rnd.uniform(-world_size, world_size)) for _ in range(num)]


def add_measurement(measurement, landmark, distance, bearing):
    measurement[int(hashlib.md5(str(landmark) + 'hash seed').hexdigest(), 16)] = {
        'distance': distance,
        'bearing': bearing,
        'type': 'beacon'
    }


def make_data(time_steps=20, num_landmarks=5, world_size=100, measurement_range=50, max_distance=20,
              motion_noise=.01):
    world_size /= 2.  # the world spans from -world_size/2 to world_size/2

    while True:
        measure_motions = []

        # make robot and landmarks
        r = Robot(max_distance=max_distance)
        landmarks = make_landmarks(world_size, num_landmarks)
        seen = [False] * num_landmarks

        for k in range(time_steps):
            # sense
            measurement = {}
            for i, landmark in enumerate(landmarks):
                distance, bearing = r.measure_distance_and_bearing_to(landmark, noise=True)
                if distance < measurement_range:
                    add_measurement(measurement, landmark, distance, bearing)
                    seen[i] = True

            # move
            x = r.x
            y = r.y
            bearing = r.bearing
            while True:
                steering = rnd.uniform(-r.max_steering, r.max_steering)
                distance = rnd.uniform(0, max_distance)
                r.move(steering, distance)
                if -world_size <= r.x <= world_size and -world_size <= r.y <= world_size:
                    steering += rnd.uniform(-motion_noise, motion_noise)
                    distance *= rnd.uniform(1. - motion_noise, 1. + motion_noise)
                    measure_motions.append((measurement, (steering, distance)))
                    break
                # if we'd be leaving the robot world, pick instead a new direction
                r.x = x
                r.y = y
                r.bearing = bearing

        # we are done when all landmarks were observed; otherwise re-run
        if sum(seen) == num_landmarks:
            return measure_motions, r.x, r.y


def is_close(a, b, tol):
    return abs(a - b) < tol


if __name__ == '__main__':
    for _ in range(10):
        measure_motions, rx, ry = make_data()
        slam = SLAM()
        for measurement, (steering, distance) in measure_motions:
            slam.process_measurements(measurement)
            ex, ey = slam.process_movement(steering, distance)

        print 'robot\t\t', rx, ry
        print 'estimation\t', ex, ey
        print

        assert is_close(rx, ex, tol=2), abs(rx - ex)
        assert is_close(ry, ey, tol=2), abs(ry - ey)
