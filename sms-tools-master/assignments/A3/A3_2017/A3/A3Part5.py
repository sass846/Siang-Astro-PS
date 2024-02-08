from scipy.signal import get_window
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft,ifft
import math
import sys
sys.path.append('C:/Users/k2vas/OneDrive/Documents/firstYear/EE220/sms-tools-master/software/models')
import utilFunctions as UF

tol = 1e-14  # threshold used to compute phase

def dftAnal(x, w, N):
    """
	Analysis of a signal using the discrete Fourier transform
	x: input signal, w: analysis window, N: FFT size 
	returns mX, pX: magnitude and phase spectrum
	"""

    if not (UF.isPower2(N)):  # raise error if N not a power of two
        raise ValueError("FFT size (N) is not a power of 2")

    if w.size > N:  # raise error if window size bigger than fft size
        raise ValueError("Window size (M) is bigger than FFT size")

    hN = (N // 2) + 1  # size of positive spectrum, it includes sample 0
    hM1 = (w.size + 1) // 2  # half analysis window size by rounding
    hM2 = w.size // 2  # half analysis window size by floor
    fftbuffer = np.zeros(N)  # initialize buffer for FFT
    w = w / sum(w)  # normalize analysis window
    xw = x * w  # window the input sound
    fftbuffer[:hM1] = xw[hM2:]  # zero-phase window in fftbuffer
    fftbuffer[-hM2:] = xw[:hM2]
    X = fft(fftbuffer)  # compute FFT
    absX = abs(X[:hN])  # compute ansolute value of positive side
    absX[absX < np.finfo(float).eps] = np.finfo(float).eps  # if zeros add epsilon to handle log
    mX = 20 * np.log10(absX)  # magnitude spectrum of positive frequencies in dB
    X[:hN].real[np.abs(X[:hN].real) < tol] = 0.0  # for phase calculation set to 0 the small values
    X[:hN].imag[np.abs(X[:hN].imag) < tol] = 0.0  # for phase calculation set to 0 the small values
    pX = np.unwrap(np.angle(X[:hN]))  # unwrapped phase spectrum of positive frequencies
    return mX, pX

def zpFFTsizeExpt(x,fs):
    w1 = get_window('hamming',256)
    w2 = get_window('hamming',512)
    xseg = x[0:256]
    mX1,pX1 = dftAnal(xseg,w1,256)
    mX2,pX2 = dftAnal(x,w2,512)
    mX3,pX3 = dftAnal(xseg,w1,512)
    return (mX1,mX2,mX3);