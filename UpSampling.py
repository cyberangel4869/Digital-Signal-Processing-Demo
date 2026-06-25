import numpy as np
import matplotlib.pyplot as plt
# L倍线性插值后，等效采样频率fs'=fs*L，真实信号的f不变
# x'(m)=x(m/L),when m=0,L,-L,2L,-2L ...
# else x'(m)=0
# 因此，X'(z)=X(z^L)
# 频谱图像横向缩短，导致(-pi,pi)以外的镜像图像进入(-pi,pi）区间
# 实际使用时，需要加上|w|<pi/L的低通滤波器来去除镜像频谱图像

# 定义参数
N = 1000  # 原始信号长度
L = 3     # 插零因子
fs = 1000  # 采样频率

# 生成原始信号
t = np.arange(N) / fs
original_signal = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 100 * t)

# 进行L倍插零
interpolated_signal = np.zeros(N * L)
interpolated_signal[::L] = original_signal

# 计算并绘制频谱
def plot_fft(signal, title):
    N = len(signal)
    f = np.fft.fftfreq(N,1.0/(2*np.pi))
    spectrum = np.abs(np.fft.fft(signal))
    
    plt.figure()
    plt.plot(f, spectrum)
    plt.title(title)
    plt.xlabel('Frequency [rad]')
    plt.ylabel('Magnitude')
    plt.grid(True)

# 绘制原始信号的频谱
plot_fft(original_signal, 'Original Signal Frequency Spectrum')

# 绘制插零后的信号的频谱
plot_fft(interpolated_signal, f'Interpolation by {L} - Frequency Spectrum')

plt.show()