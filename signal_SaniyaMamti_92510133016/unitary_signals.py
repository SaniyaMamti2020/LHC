import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    """Generate unit step signal"""
    signal = np.array([1 if i >= 0 else 0 for i in n])
    plt.stem(n, signal)
    plt.title("Unit Step Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

def unit_impulse(n):
    """Generate unit impulse signal"""
    signal = np.array([1 if i == 0 else 0 for i in n])
    plt.stem(n, signal)
    plt.title("Unit Impulse Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

def ramp_signal(n):
    """Generate ramp signal"""
    signal = np.array([i if i >= 0 else 0 for i in n])
    plt.stem(n, signal)
    plt.title("Ramp Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal