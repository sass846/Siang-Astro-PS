from scipy.fftpack import fft
import numpy as np
import math

def optimalZeropad(x,fs,f):
    numberofsamplesperperiod = int(fs/f)
    numberofperiods = len(x)/numberofsamplesperperiod
    totalnumberofperiods = int(numberofperiods)+1
    N = totalnumberofperiods*numberofsamplesperperiod
    zeroslength = N-len(x)
    zeros = np.zeros(zeroslength)
    x = np.append(x,zeros)
    X = fft(x,N)
    return 20*np.log10(np.sqrt(np.square(X[0:int(N/2+1)].real)+np.square(X[0:int(N/2+1)].imag)));
    