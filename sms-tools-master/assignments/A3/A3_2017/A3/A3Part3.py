import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft,ifft
import math

thresh = 1e-14

def testRealEven(x):
    M = len(x)
    hN = (M // 2) + 1  # size of positive spectrum, it includes sample 0
    hM1 = (M + 1) // 2  # half analysis window size by rounding
    hM2 = int(math.floor(M / 2))  # half analysis window size by floor
    fftbuffer = np.zeros(M)  # initialize buffer for FFT
    y = np.zeros(x.size)  # initialize output array
    fftbuffer[:hM1] = x[hM2:]  # zero-phase window in fftbuffer
    fftbuffer[-hM2:] = x[:hM2]
    X = fft(fftbuffer,M)
    X_dash = X.copy()
    for i in range(0,len(X_dash)):
        if(X_dash[i].imag < thresh):
            X_dash[i] = X_dash[i].real
    isrealeven = True
    for k in X.imag:
        if(k!=0):
            isrealeven = False
            break
    return (isrealeven,fftbuffer,X);