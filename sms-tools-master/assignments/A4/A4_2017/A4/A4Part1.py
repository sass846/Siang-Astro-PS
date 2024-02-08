import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft,ifft,fftshift
from scipy.signal import get_window

def windowAnal(window,M):
    e = 1e-12
    N = 8*M
    w = get_window(window,M)
    X = fft(w,8*M)
    X = X + e
    mX = np.zeros(len(X))
    mX = 20*np.log10(np.sqrt(np.square(X.real)+np.square(X.imag)))
    mXbuffer = np.zeros(len(mX))
    mXbuffer[:int(N/2)] = mX[int(N/2):]
    mXbuffer[-int(N/2):] = mX[:int(N/2)]
    mXdash = np.append(mXbuffer[-1],mXbuffer[0:-1])
    return mXbuffer,mXbuffer-mXdash

def extractMainLobe(window,M):
    mX,slopes = windowAnal(window,M)
    
    
    
    maximumIndices = np.zeros(len(mX)-1)
    minimumIndices = np.zeros(len(mX)-1)
    
    for i in range(0,len(slopes)-1):
        if(slopes[i]>0 and slopes[i+1]<0):
            maximumIndices[i]=1
        if(slopes[i]<0 and slopes[i+1]>0):
            minimumIndices[i]=-1
    
    midIndex = int(len(maximumIndices)/2)+1
    
    y = maximumIndices[midIndex]
    
    
    combined = maximumIndices+minimumIndices
    
    count = 0
    mainLobeRight = 0
    sideLobePeak = 0
    sideLobeRight = 0
    for i in range(midIndex,len(maximumIndices)):
        if(count==2):
            break;
        if(minimumIndices[i]==-1):
            count = count + 1
            if(count==1):
                mainLobeRight = i
        if(maximumIndices[i]==1):
            sideLobePeak = mX[i]
    
    halflength = mainLobeRight - midIndex
    
    output = mX[midIndex-halflength:midIndex+halflength+1]
    return output
