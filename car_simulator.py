import numpy as np
import matplotlib.pyplot as plt

class CarSimulator():
    def __init__(self, wheelbase, v0, theta0):
        # INPUTS:
        # The wheel base is the distance between the front and the rear wheels
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
