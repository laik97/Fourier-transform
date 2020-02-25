import numpy as np
import scipy.fftpack as fft
import math
import matplotlib.pyplot as plt


class Sin:
    """Sinusoidal wave creator"""

    def __init__(self, amp=1, f=1, fs=256, length=1, phi=0):
        """Holds wave values and its time domain.
        amp -- amplitude
        f -- wave frequency [Hz[
        fs -- sampling frequency (best powers of 2)
        length -- wave length for time t domain (best in radians)
        Calculated by: amp * sin(2 * PI * f * t + PI * phi)
        """
        self.amp = amp
        self.f = f
        self.fs = fs
        self.length = length
        self.phi = phi*math.pi
        self.sin, self.time = self._create_sin()

    def _create_sin(self):
        """Given constructor values calculaters sin vales and time domain samples."""
        time = np.arange(0, self.length, self.length/self.fs)
        sin = [self.amp*math.sin(2*math.pi*self.f*t + self.phi) for t in time]
        return sin, time

    def __sum_sin(*args):
        """Provided waves, returns their sum"""
        print(len(args))
        result = np.array([])
        for sin in args:
            result = np.append(result,sin)
        result = result.reshape(len(args),len(args[0]))
        return sum(result)

    def quick_sum(*args):
        """Provided different wave(s), returns their sum."""
        result = np.array([])
        for i in range(len(args)):
            result = np.append(result, args[i].sin)
        result = result.reshape(len(args),len(args[0].sin))
        return sum(result)


    def spectral_analysis(wave, fs, length, show_stem=False):
        """Given complex (or simple) wave, returns it's (most important) spectral frequencies.
        Graphs them additionally for show_stem == True
        """
        print(len(wave))
        magn = fft.fft(wave) # complex values
        freq = fft.fftfreq(len(wave))

        freq = freq[np.where(freq > 0)]*fs/length
        magn = abs(magn[np.where(freq > 0)])*2/fs

        magn_mean = magn/len(magn)
        imp_f = freq[np.where(magn > magn_mean)]
        imp_magn = magn[np.where(magn > magn_mean)]

        fig, ax = plt.subplots(figsize = (11,6))
        ax.stem(freq, magn, use_line_collection = True)
        ax.set_xlim(0,fs/2)
        if show_stem:
            plt.show()
        return imp_f, imp_magn