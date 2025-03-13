## Overview
This repository contains an implementation of a simple 2D vehicle simulator that models the motion and control of a car based on its physical parameters.

### Simulation Object (Car)
The simulation tracks the following states for the vehicle:
- **x**: Position along the x-axis in meters.
- **y**: Position along the y-axis in meters.
- **v**: Speed in m/s.
- **theta**: Orientation angle from the positive x-axis, measured in radians.

### Main Function: simulatorStep
The `simulatorStep` method updates the vehicle state based on:
1. Commanded acceleration (`a`) to adjust speed and position over time step (`dt`).
2. Steering angle applied at the wheels.
3. Time increment (`dt`) for simulation advancement.

### Simulation Phase Implementation

#### Phase 1: Acceleration
- The car accelerates from rest (0 m/s) with a constant acceleration of `a=0.4 m/s²`.
- This continues until the vehicle reaches `v=10 m/s`.

#### Phase 2: Constant Speed
- Once at 10 m/s, the car maintains this speed for an extended period.

#### Phase 3: Circular Motion (Clockwise)
- After reaching constant velocity, the car transitions to a circular path with approximately a radius of ~100 meters.
- The turning is achieved by adjusting the steering angle in positive increments over a set time interval (`dt_turn`).

### Visualization Methods
After running the simulation:
1. Plot vehicle trajectory (x vs y).
2. Overlay longitudinal and lateral acceleration on separate plots.

## Dependencies
This implementation requires NumPy for numerical computations and matplot