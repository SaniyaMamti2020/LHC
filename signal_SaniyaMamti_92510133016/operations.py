import numpy as np
import matplotlib.pyplot as plt

def time_shift(signal, k):
    """Shift signal by k units"""
    shifted = np.roll(signal, k)
    return shifted

def time_scale(signal, k):
    """Scale time axis by factor k"""
    indices = np.arange(0, len(signal))
    scaled_indices = indices * k
    return scaled_indices, signal

def signal_addition(signal1, signal2):
    """Add two signals"""
    return np.add(signal1, signal2)

def signal_multiplication(signal1, signal2):
    """Multiply two signals"""
    return np.multiply(signal1,signal2)