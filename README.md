# PID & SSI Control System

### Overview

The micropositioner uses a piezo actuator for each axis, and we’ve implemented a closed-loop PID controller to precisely move the stage to a user-defined position. Position feedback comes from a magnetic encoder that outputs 4096 discrete values over a 2mm range via SSI. The system can be driven by a signal generator or DAC (e.g., MCP4728), depending on the hardware setup.

This repo includes both the firmware running on the Arduino and a Python script for simulating and plotting PID behavior across all three axes.

---

Features

- Real-time PID control loop (adjustable `kp`, `ki`, `kd`)
- Position feedback from a 12-bit SSI encoder
- Simulated control of X, Y, and Z axes for development/testing
- Live plotting of position, output, and target over time
- Optional DAC support via I2C
- Easily swappable between simulation and real hardware

---
Example Output from X, Y, Z Axis PID Simulation

<img width="628" alt="Screenshot 2025-06-25 at 1 21 17 PM" src="https://github.com/user-attachments/assets/a0e63676-9949-4ae6-bea6-57353fb44f82" />
