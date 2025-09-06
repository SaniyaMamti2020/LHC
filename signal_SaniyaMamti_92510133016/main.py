import numpy as np
import matplotlib.pyplot as plt
from unitary_signals import unit_step, unit_impulse, ramp_signal
from trigonometric_signals import sine_wave, cosine_wave
from operations import time_shift, signal_addition, signal_multiplication

# 1. Generate and plot unit step & unit impulse
n = np.arange(-10, 10, 1)
step = unit_step(n)
impulse = unit_impulse(n)

# 2. Generate sine wave (A=2, f=5Hz, phi=0, t=0..1 sec)
t = np.linspace(0, 1, 500)
sine = sine_wave(2, 5, 0, t)

# 3. Perform time shifting on sine wave by +5 units
shifted_sine = time_shift(sine, 5)
plt.plot(sine, label="Original Sine")
plt.plot(shifted_sine, label="Shifted Sine (+5)")
plt.legend()
plt.title("Time Shifting")
plt.show()

# 4. Add unit step and ramp signal
ramp = ramp_signal(n)
added = signal_addition(step, ramp)
plt.stem(n, added, use_line_collection=True)
plt.title("Addition: Unit Step + Ramp")
plt.show()

# 5. Multiply sine and cosine of same frequency
cosine = cosine_wave(2, 5, 0, t)
multiplied = signal_multiplication(sine, cosine)
plt.plot(t, multiplied)
plt.title("Multiplication: Sine * Cosine")
plt.show()