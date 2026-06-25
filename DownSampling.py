import numpy as np
import matplotlib.pyplot as plt

# 模拟M倍抽取对信号频谱的影响
# 抽取使得等效的采样频率下降，导致w变成w/M
# 频谱中pi代表采样频率fs，fs的变化导致横轴的“分度”变大，而真实信号的f不会改变
# 抽取导致原先在w0处，f=w0*fs/pi的信号，由于fs'=fs/M，而移动到w0*M处，使频谱被拉长
# 因此，只有最高频率低于pi/M的信号在经过抽取后，频谱图像在(-pi,pi)上依然完整
# 若信号最高频率不满足上一条，则需要加上|w|<pi/M的低通滤波器来避免频率混叠

# 定义参数
N = 1000  # 原始信号长度
M = 3     # 抽取因子
fs = 1000  # 采样频率

# 生成原始信号
t = np.arange(N) / fs
original_signal = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 100 * t)

# 进行M倍抽取
downsampled_signal = original_signal[::M]

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

# 绘制抽取后的信号的频谱
plot_fft(downsampled_signal, f'Downsampling by {M} - Frequency Spectrum')

plt.show()