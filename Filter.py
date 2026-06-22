

import numpy as np
import matplotlib.pyplot as plt
# 单位冲击信号
input = np.zeros(32)
input[16] = 1
# 输入信号的频域波形
zin = np.fft.fft(input)

freq = np.linspace(-np.pi, np.pi, 32)
# 低通滤波器，与输入信号的频域波形相乘得到输出信号的频域波形
def filter(zin,freq,wc):
    zout = np.zeros(len(zin))
    if(len(zin)==len(freq)):
        for i in range(len(zin)):
            if(np.abs(freq[i])<=wc):
                zout[i] = zin[i]
            else:
                zout[i] = 0
    return zout
#输出信号的频域波形
zout = filter(zin,freq,np.pi/2)
print("zout arry:",zout)
# 输出信号的时域波形
output = np.fft.ifft(zout)
print("output arry:",np.abs(output))


plt.figure(figsize=(18, 6))

# 输入信号波形
plt.subplot(1, 3, 1)
plt.stem(range(-16,16),np.abs(input))
plt.title('Input model')
plt.xlabel('Time')
plt.ylabel('Amplitude')

# 输出信号波形
plt.subplot(1, 3, 2)
plt.stem(range(-16,16),np.abs(output))
plt.title('Output model')
plt.xlabel('Time')
plt.ylabel('Amplitude')

#标准sinc函数波形
x = np.linspace(-16,16,1000)
plt.subplot(1,3,3)
plt.plot(x,np.abs(np.sin(0.5*np.pi*x)/(x*np.pi)))
plt.title("|sinc(x*pi/2)|")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
