# 马培祯

import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(-np.pi,np.pi,1000)
wc = 0.5*np.pi
M = 50

def h(n):
    if(n==0):
        h=0.5+0j
    else:
        h=np.sin(wc*n) / (np.pi*n)
    return h

def H(M):
    H=0+0j
    for n in range(-M,M+1):
        print('h(',n,')=',h(n))
        H+=h(n)*np.exp(-1j*w*n)
    return H

Habs = np.abs(H(M))
print(Habs)
plt.figure(figsize=(6, 6))
plt.plot(w/np.pi, Habs)
plt.title("|H(w)|")
plt.xlabel("Frequency(pi)")
plt.ylabel("Amplitude")
plt.show()