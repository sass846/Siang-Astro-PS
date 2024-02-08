import os
import sys
import numpy as np
import math
from scipy.signal import get_window
import matplotlib.pyplot as plt
from scipy.io.wavfile import write, read

sys.path.append( 'C:/Users/k2vas/OneDrive/Documents/firstYear/EE220/sms-tools-master/software/models/')
sys.path.append( 'C:/Users/k2vas/OneDrive/Documents/firstYear/EE220/sms-tools-master/')
import stft
import utilFunctions as UF
eps = np.finfo(float).eps

def computeSNR(inputFile="C:\\Users\\k2vas\\OneDrive\\Documents\\firstYear\\EE220\\sms-tools-master\\sounds\\bendir.wav", window='hamming',M=2048,N=1024,H=256):
    w = get_window(window,M,False)
    
    inputFile = "C:\\Users\\k2vas\\OneDrive\\Documents\\firstYear\\EE220\\sms-tools-master\\"+inputFile[6:]
    print(inputFile)
    fs,x = read(inputFile)
    x_reconstructed = stft.stft(x,w,N,H)
    noise = x - x_reconstructed
    E_signal1 = energy(x_reconstructed)
    E_noise1 = energy(noise)
    SNR1 = 10*np.log10(E_signal1/E_noise1)
    E_signal2 = energy(x_reconstructed[M:len(x)-M])
    E_noise2 = energy(noise[M:len(noise)-M])
    SNR2 = 10*np.log10(E_signal2/E_noise2)
    return (SNR1,SNR2);

def energy(X):
    X = X 
    energy = np.sum(np.square(X.real)+np.square(X.imag))
    return energy
	