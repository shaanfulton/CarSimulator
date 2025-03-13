# The class CarSimulator is a simple 2D vehicle simulator.
# The vehicle states are:
# - x: is the position on the x axis on a xy plane
# - y: is the position on the y axis on a xy plane
# - v is the vehicle speed in the direction of travel of the vehicle
# - theta: is the angle wrt the x axis (0 rad means the vehicle
#   is parallel to the x axis, in the positive direction;
#   pi/2 rad means the vehicle is parallel
#   to the y axis, in the positive direction)
# - NOTE: all units are SI: meters (m) for distances, seconds (s) for
#   time, radians (rad) for angles...
#
# (1)
# Write the method "simulatorStep", which should update
# the vehicle states, given 3 inputs:
#  - a: commanded vehicle acceleration
#  - wheel_angle: steering angle, measured at the wheels;
#    0 rad means that the wheels are "straight" wrt the vehicle.
#    A positive value means that the vehicle is turning counterclockwise
#  - dt: duration of time after which we want to provide
#    a state update (time step)
#
# (2)
# Complete the function "main". This function should run the following simulation:
# - The vehicle starts at 0 m/s
# - The vehicle drives on a straight line and accelerates from 0 m/s to 10 m/s
#   at a constant rate of 0.4 m/s^2, then it proceeds at constant speed.
# - Once reached the speed of 10 m/s, the vehicle drives in a clockwise circle of
#   roughly 100 m radius
# - the simulation ends at 100 s
#
# (3)
# - plot the vehicle's trajectory on the xy plane
# - plot the longitudinal and lateral accelerations over time

import numpy as np
import matplotlib.pyplot as plt

class CarSimulator():
    def __init__(self, wheelbase, v0, theta0):
        # INPUTS:
        # the wheel base is the distance between the front and the rear wheels
        self.wheelbase = wheelbase
        self.x = 0
        self.y = 0
        self.v = v0
        self.theta = theta0

    def simulatorStep(self, a, wheel_angle, dt):
        self.x += self.v * np.cos(self.theta) * dt
        self.y += self.v * np.sin(self.theta) * dt
        self.v += a * dt
        self.theta += (self.v / self.wheelbase) * np.tan(wheel_angle) * dt

def main():
    wheelbase = 4
    v0 = 0
    theta0 = 0
    simulator = CarSimulator(wheelbase, v0, theta0)
    dt = 0.1
    total_time = 100
    time_steps = int(total_time / dt)

    x_vals, y_vals, long_acc, lat_acc, times = [], [], [], [], []

    for step in range(time_steps):
        current_time = step * dt
        if simulator.v < 10:
            a = 0.4
            wheel_angle = 0
        else:
            a = 0
            wheel_angle = -np.arctan(simulator.wheelbase / 100)

        simulator.simulatorStep(a, wheel_angle, dt)

        x_vals.append(simulator.x)
        y_vals.append(simulator.y)
        times.append(current_time)
        long_acc.append(a)
        lat_acc.append(simulator.v**2 / 100 if simulator.v >= 10 else 0)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(x_vals, y_vals)
    plt.xlabel('X Position (m)')
    plt.ylabel('Y Position (m)')
    plt.title('Vehicle Trajectory')
    plt.axis('equal')

    plt.subplot(1, 2, 2)
    plt.plot(times, long_acc, label='Longitudinal Acceleration (m/s²)')
    plt.plot(times, lat_acc, label='Lateral Acceleration (m/s²)')
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s²)')
    plt.title('Accelerations over Time')
    plt.legend()

    plt.tight_layout()
    plt.show()

main()
