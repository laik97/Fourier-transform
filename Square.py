import numpy as np
from Sinusoid import Sin

class Square(Sin):
    """Square wave created on the base of sinusoid wave."""
    def __init__(self, amp=1, f=1, fs=256, length=1, phi=0):
        Sin.__init__(self,amp,f,fs,length,phi)
        self.square = self._square_from_sin()

    def _square_from_sin(self):
        """Creates square wave from sinusoid"""
        max_val = max(self.sin)
        min_val = min(self.sin)
        square = np.array([max_val if val > 0 else min_val for val in self.sin])
        return square