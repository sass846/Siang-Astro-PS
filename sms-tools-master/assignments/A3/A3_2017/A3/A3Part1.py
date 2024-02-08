import math
import numpy as np

def minimizeEnergySpreadDFT(x,fs,f1,f2):
    P1 = int(fs/f1)
    P2 = int(fs/f2)
    M = (int)(P1*P2/(int)(math.gcd(P1,P2)))
    X = DFT(x,M)
    return 20*np.log10(np.sqrt(np.square(X[0:int(M/2+1)].real)+np.square(X[0:int(M/2+1)].imag)));

def DFT(input_signal,numberofpoints):
    X = np.empty(numberofpoints,dtype = 'complex')
    temp = 0
    for k in range(numberofpoints):
        temp = 0
        for n in range(numberofpoints):
            temp = temp + (input_signal[n])*complex(np.cos((2*np.pi/numberofpoints)*n*k),-(np.sin((2*np.pi/numberofpoints)*n*k)))
        X[k] = temp;
    return X;