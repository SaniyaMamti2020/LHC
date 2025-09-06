from signal_SaniyaMamti_92510133016 import unitary_signals, trigonometric_signals, operations
import numpy as np
import matplotlib.pyplot as plt

# --- Unitary signals ---
n1 = np.arange(-10, 10)   # Discrete index values
step = unitary_signals.unit_step(n1)
impulse = unitary_signals.unit_impulse(n1)
ramp = unitary_signals.ramp_signal(n1)

# --- Trigonometric signals ---
t = np.linspace(0, 1, 500)  # time vector from 0 to 1 sec
sine = trigonometric_signals.sine_wave(2, 5, 0, t)       # A=2, f=5Hz, phi=0
cosine = trigonometric_signals.cosine_wave(2, 5, 0, t)
expo = trigonometric_signals.exponential_signal(1, -2, t)  # example exponential

# --- Operations ---

# Time shifting sine wave by +5
shifted_sine = operations.time_shift(sine, 5)
plt.plot(t, sine, label="Original Sine")
plt.plot(t, shifted_sine, label="Shifted Sine (+5)")
plt.legend()
plt.title("Time Shift Example")
plt.show()

# Time scaling sine wave by factor 2
n2 = np.arange(0, 20, 0.1)
sine_n2 = np.sin(n2)

scaled_time, scaled_sine = operations.time_scale(sine_n2, 2)

plt.figure(figsize=(8, 5))
plt.plot(n2, sine_n2, label="Original Sine")
plt.plot(scaled_time, scaled_sine, label="Time Scaled (k=2)")
plt.legend()
plt.title("Time Scaling Example")
plt.show()

# Addition: step + ramp
added = operations.signal_addition(step, ramp)
plt.stem(n1, added)
plt.title("Addition: Unit Step + Ramp")
plt.show()

# Multiplication: sine * cosine
multiplied = operations.signal_multiplication(sine, cosine)
plt.plot(t, multiplied)
plt.title("Multiplication: Sine * Cosine")
plt.show()