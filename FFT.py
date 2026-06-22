
import numpy as np
import matplotlib.pyplot as plt

# 定义输入信号
x = np.array([0, np.sqrt(2)/2, 1, np.sqrt(2)/2, 0, -np.sqrt(2)/2, -1, -np.sqrt(2)/2])

# 进行FFT运算
result = np.fft.fft(x)

# 计算实部和虚部
RELresult = np.real(result)
IMGresult = np.imag(result)

freq = range(8)
t=range(8)

plt.figure()

plt.subplot(3,1,1)
plt.plot(t,x,label='Signal')
plt.xlabel('time')
plt.ylabel('value')
plt.legend()
plt.grid(True)

# 绘制FFT结果的虚部
plt.subplot(3, 1, 2)
plt.plot(freq, IMGresult, label='Imaginary')
plt.xlabel('Frequency')
plt.ylabel('Imaginary Part')
plt.legend()
plt.grid(True)

# 绘制FFT结果的实部
plt.subplot(3, 1, 3)
plt.plot(freq, RELresult, label='Real')
plt.xlabel('Frequency')
plt.ylabel('Real Part')
plt.legend()
plt.grid(True)

# 调整子图之间的间距
plt.tight_layout()

# 显示图表
plt.show()
