# 马培祯

import numpy as np
import matplotlib.pyplot as plt

N = 64

#时域sinc函数，频域上为标准门限函数X(e^jw)
freq = np.linspace(-np.pi,np.pi,N)
def X(w):
    if(np.abs(w)<=0.4*np.pi):
        return np.exp(-1j*w*15)
    else:
        return 0 
X = [X(w) for w in freq]
plt.figure(figsize=(5, 4))
plt.stem(freq/np.pi, np.abs(X))
plt.title("X(w)")
plt.xlabel("Frequency(pi)")
plt.ylabel("Amplitude")

def x(n):
    if(n==0):
        x=0.4
    else:
        x=np.sin(0.4*np.pi*n)/(np.pi*n)
    return x

#时域上的矩形窗函数d(n),频域上为类sinc的周期函数
def d(n):
    if(abs(n)<=15):
        return 1 
    else:
        return 0
d_list = [d(n) for n in range(-N//2,N//2)]
Dg = np.fft.fft(d_list)
plt.figure(figsize=(8, 4))
plt.stem(freq/np.pi,np.abs(Dg))
plt.title("|Dg|")
plt.xlabel("Frequency(pi)")
plt.ylabel("Amplitude")

#X和D频域卷积，相当于时域相乘后FFT变换
x_d = [x(n-15)*d(n) for n in range(-N//2,N//2)]
X_D = np.fft.fft(x_d)
plt.figure(figsize=(8, 4))
plt.stem(freq/np.pi,np.abs(X_D))
plt.title("|X(e^jw)*D(e^jw)/2pi|")
plt.xlabel("Frequency(pi)")
plt.ylabel("Amplitude")

#X0和D频域卷积，相当于时域相乘后FFT变换
x0_d = [x(n)*d(n) for n in range(-N//2,N//2)]
X0_D = np.fft.fft(x0_d)
plt.figure(figsize=(8, 4))
plt.stem(freq/np.pi,np.abs(X0_D))
plt.title("|X0(e^jw)*Dg(e^jw)/2")
plt.xlabel("Frequency(pi)")
plt.ylabel("Amplitude")

plt.show()


