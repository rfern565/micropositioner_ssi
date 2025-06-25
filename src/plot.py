import matplotlib.pyplot as plt
import time
import math
import random

plt.ion()
fig, ax = plt.subplots()

times = []
positions = []
targets = []
outputs = []

# Simulation parameters
target = 1000  # target position in µm
pos = 0
vel = 0
kp = 0.8
ki = 0.01
kd = 0.2
integral = 0
last_error = 0

start_time = time.time()

while True:
    t = time.time() - start_time
    error = target - pos
    integral += error
    derivative = error - last_error
    output = kp * error + ki * integral + kd * derivative
    last_error = error

    # Simulate actuator response (simple inertia + random jitter)
    vel = 0.1 * output
    pos += vel + random.uniform(-1, 1)  # small noise

    times.append(t)
    positions.append(pos)
    targets.append(target)
    outputs.append(output)

    # Plot live
    ax.clear()
    ax.plot(times, positions, label='Position (um)')
    ax.plot(times, targets, label='Target (um)', linestyle='--')
    ax.plot(times, outputs, label='PID Output', linestyle=':')
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Microns / Output")
    ax.legend()
    plt.pause(0.01)

    time.sleep(0.01)
