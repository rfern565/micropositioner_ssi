import matplotlib.pyplot as plt
import time
import random

plt.ion()
fig, ax = plt.subplots()

# Time + data series
times = []

# Position, target, and output for each axis
positions = {'x': 0, 'y': 0, 'z': 0}
targets = {'x': 1000, 'y': 500, 'z': 1500}
outputs = {'x': 0, 'y': 0, 'z': 0}
velocities = {'x': 0, 'y': 0, 'z': 0}

# PID tuning
kp = {'x': 0.8, 'y': 0.6, 'z': 0.9}
ki = {'x': 0.01, 'y': 0.01, 'z': 0.01}
kd = {'x': 0.2, 'y': 0.25, 'z': 0.15}

integrals = {'x': 0, 'y': 0, 'z': 0}
last_errors = {'x': 0, 'y': 0, 'z': 0}

# For plotting
pos_data = {'x': [], 'y': [], 'z': []}
out_data = {'x': [], 'y': [], 'z': []}
target_data = {'x': [], 'y': [], 'z': []}

start_time = time.time()

while True:
    t = time.time() - start_time
    times.append(t)

    for axis in ['x', 'y', 'z']:
        # PID computation
        error = targets[axis] - positions[axis]
        integrals[axis] += error
        derivative = error - last_errors[axis]
        last_errors[axis] = error

        output = (
            kp[axis] * error +
            ki[axis] * integrals[axis] +
            kd[axis] * derivative
        )
        outputs[axis] = output

        # Simulate motion
        velocities[axis] = 0.1 * output
        positions[axis] += velocities[axis] + random.uniform(-1, 1)

        # Store data
        pos_data[axis].append(positions[axis])
        out_data[axis].append(outputs[axis])
        target_data[axis].append(targets[axis])

    # Plot
    ax.clear()
    for axis in ['x', 'y', 'z']:
        ax.plot(times, pos_data[axis], label=f'{axis.upper()} Position')
        ax.plot(times, target_data[axis], linestyle='--', label=f'{axis.upper()} Target')
        ax.plot(times, out_data[axis], linestyle=':', label=f'{axis.upper()} Output')
    
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("µm / Output")
    ax.legend(loc='upper right')
    plt.pause(0.01)
    time.sleep(0.01)
