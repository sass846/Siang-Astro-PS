import os
import sys
import numpy as np
import math
from scipy.signal import get_window
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft,fftshift
from scipy.signal import get_window

sys.path.append( 'C:/Users/k2vas/OneDrive/Documents/firstYear/EE220/sms-tools-master/software/models/')
import stft
import utilFunctions as UF
eps = np.finfo(float).eps

def computeEngEnv(inputFile,window,M,N,H):
    inputFile = "C:\\Users\\k2vas\\OneDrive\\Documents\\firstYear\\EE220\\sms-tools-master\\"+inputFile[6:]
    fs,x = UF.wavread(inputFile)
    w = get_window(window,M,False)
    X_dash,P_dash = stft.stftAnal(x,w,N,H)
    engEnv = np.zeros((X_dash.shape[0],2))
    lowFreqLimit = int(3000*N/fs)
    highFreqLimit = int(10000*N/fs)
    i =0
    for mX in X_dash:
        mX = mX/20
        #for k in mX:
        #    print(k)
        #print('overbdlfjg psodifh paoif hapsofig asdgi jasoitjasporigmaofi jgsiodfmgosdir thoadrivm oadi gjhpadiofg hasiugh baidufg haeirugh apeil')
        engEnv[i][0] = 10*(energy(mX,0,lowFreqLimit))
        engEnv[i][1] = 10*(energy(mX,lowFreqLimit-1,highFreqLimit))
        i = i + 1
    return engEnv

def energy(X,low,high):
    sum = 0
    for k in range(low+1,high):
        X[k] = 10**X[k]
    for k in range(low+1,high):
        sum = sum + X[k]*X[k]
    return np.log10(sum)