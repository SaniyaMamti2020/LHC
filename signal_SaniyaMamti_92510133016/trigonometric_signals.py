import numpy as np
import matplotlib.pyplot as plt

def sine_wave(A, f, phi, t):
    """Generate sine wave"""
    signal = A * np.sin(2 * np.pi * f * t + phi)
    plt.plot(t, signal)
    plt.title("Sine Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

def cosine_wave(A, f, phi, t):
    """Generate cosine wave"""
    signal = A * np.cos(2 * np.pi * f * t + phi)
    plt.plot(t, signal)
    plt.title("Cosine Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

def exponential_signal(A, a, t):
    """Generate exponential signal"""
    signal = A * np.exp(a * t)
    plt.plot(t, signal)
    plt.title("Exponential Signal")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal