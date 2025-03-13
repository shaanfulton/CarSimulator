import numpy as np
import matplotlib.pyplot as plt

class CarSimulator():
    def __init__(self, wheelbase, v0, theta0):
        # INPUTS:
        # The wheel base is the distance between the front and the rear wheels
        self.wheelbase = wheelbase
        # Initial position, velocity, and orientation
        self.x = 0
        self.y = 0
        self.v = v0 
        self.theta = theta0

    def simulatorStep(self, a, wheel_angle, dt):
        # Update position, velocity, and orientation
        self.x += self.v * np.cos(self.theta) * dt
        self.y += self.v * np.sin(self.theta) * dt
        self.v += a * dt
        self.theta += (self.v / self.wheelbase) * np.tan(wheel_angle) * dt
        self.theta += (self.v / self.wheelbase) * np.tan(wheel_angle) * dt

def main():
    wheelbase = 4 # Distance between front and rear wheels (m)
    v0 = 0 # Initial velocity (m/s)
    theta0 = 0 # Initial orientation (radians)
    simulator = CarSimulator(wheelbase, v0, theta0)
    dt = 0.1 # Time step (s)
    total_time = 100 # Total simulation time (s)
    time_steps = int(total_time / dt)

    # Arrays to store simulation data for plotting
    x_vals, y_vals, long_acc, lat_acc, times = [], [], [], [], []

    for step in range(time_steps):
        current_time = step * dt
        
        # Phase 1: Acceleration to target speed
        if simulator.v < 10:
            a = 0.4 # Constant acceleration (m/s²)
            wheel_angle = 0 # Drive straight
        # Phase 2 & 3: Constant speed and circular motion
        else:
            a = 0 # Maintain constant speed
            wheel_angle = -np.arctan(simulator.wheelbase / 100) # Turn in circle with ~100m radius

        # Update vehicle state
        simulator.simulatorStep(a, wheel_angle, dt)

        # Record data for plotting
        x_vals.append(simulator.x)
        y_vals.append(simulator.y)
        times.append(current_time)
        long_acc.append(a)
        # Calculate lateral acceleration (centripetal) when in circular motion
        lat_acc.append(simulator.v**2 / 100 if simulator.v >= 10 else 0)

    # Create visualization plots
    plt.figure(figsize=(12, 6))

    # Plot vehicle trajectory
    plt.subplot(1, 2, 1)
    plt.plot(x_vals, y_vals)
    plt.xlabel('X Position (m)')
    plt.ylabel('Y Position (m)')
    plt.title('Vehicle Trajectory')
    plt.axis('equal')

    # Plot acceleration components
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
