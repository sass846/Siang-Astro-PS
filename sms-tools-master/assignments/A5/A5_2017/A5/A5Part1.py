import os
import sys
import numpy as np
import math
from scipy.signal import get_window
import matplotlib.pyplot as plt

sys.path.append( 'C:/Users/k2vas/OneDrive/Documents/firstYear/EE220/sms-tools-master/software/models/')
import utilFunctions as UF
import dftModel as DFT
eps = np.finfo(float).eps

def minFreqEstErr(inputFile,f):
    inputFile = 'C://Users//k2vas//OneDrive//Documents//firstYear//EE220//sms-tools-master//sounds'+inputFile
    fs,x = UF.wavread(inputFile)
    prevN = 0
    mindiff = 1000
    minLoc = 0
    minN = 1
    minM = 0
    for i in range(0,int(np.log10(len(x))/np.log10(2))):
        for j in range(101,int(np.power(2,i)),100):
            if(fs/2-j//2<0):
                x_dash = x[0:int(fs/2+j//2+1)]
            if(fs/2+j//2>len(x)):
                x_dash = x[int(fs/2-j//2):len(x)]
            if(fs/2+j//2>len(x) and fs/2-j//2<0):
                x_dash = x[0:len(x)]
            else:
                x_dash = x[int(fs/2-j//2):int(fs/2+j//2+1)]
            w = get_window('blackman',j)
            mX,pX = DFT.dftAnal(x_dash,w,int(np.power(2,i)))
            ploc = UF.peakDetection(mX,-40)
            iploc,_,_ = UF.peakInterp(mX,pX,ploc)
            if(np.abs(f-fs*iploc/np.power(2,i))<mindiff):
                mindiff = np.abs(f-fs*iploc/np.power(2,i))
                minN = np.power(2,i)
                minM = j
                minLoc = fs*iploc/minN
        if(mindiff<0.05):
                break
            
    return (minLoc[0],minN,minM)
