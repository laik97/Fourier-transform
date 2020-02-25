import numpy as np
import math
import matplotlib.pyplot as plt
import Sinusoid
from Square import Square


def fourier_series_square(amp, P, coeffs_number, wave, time, fs, length):
    L = P / 2
    first_half = wave[np.where((time > 0) & (time < L))]
    first_half = first_half[1]
    a0 = (1/(2*L))*(first_half + (-first_half))
    bn = np.array([])
    for n in range(1,coeffs_number + 1):
        bn = np.append(bn, (2*amp/(n*math.pi))*(1-math.cos(n*math.pi)))
    result = np.array([])
    for n in range(0, coeffs_number):
        temp = Sinusoid.Sin(bn[n], ((n+1)/2*L), fs=fs, length=length)
        result = np.append(result, temp.sin)
    result = result.reshape(coeffs_number, fs)
    return sum(result)


def fourier_series_triangle(amp, P, coeffs_number, fs, length):
    L = P/2
    a0 = 1 - L / 2
    bn = np.array([])
    result = np.array([])
    for n in range(1, coeffs_number + 1):
        bn = np.append(bn, (8 * amp * (math.sin((math.pi*n / 2)))**2) / ((math.pi ** 2) * (n ** 2)))
    for n in range(0, coeffs_number):
        temp = Sinusoid.Sin(bn[n], (n) / L*2, fs=fs, length=length, phi=0.5)
        result = np.append(result, temp.sin)
    result = result.reshape(coeffs_number, fs)
    return sum(result), result


def plot_series(series, number):
    for n in range(number):
        plt.plot(series[n*2])


