
import numpy as np

# 设置打印选项以显示复数为 a + bj 格式


def fft(x):
    N = len(x)
    if N <= 1:
        return x
    elif N % 2 > 0:
        raise ValueError("Size of x must be a power of 2")
    
    # Compute the even and odd indexed elements and factor out the twiddle factors.
    X_even = fft(x[::2])#按索引的奇偶分开计算
    X_odd = fft(x[1::2])
    T = [np.exp(-2j * np.pi * k / N) for k in range(N // 2)]#旋转因子
    arr1 = X_even+T*X_odd
    arr2 = X_even-T*X_odd
    print("eve:",X_even)
    print("odd:",X_odd)
    print("Wxx:",T)
    print("rs1:",arr1)
    print("rs2:",arr2)
    print("\n")
    result = np.concatenate((arr1,arr2))#拼接结果的前后部分
    return result

x = np.array([0, np.sqrt(2)/2, 1, np.sqrt(2)/2, 0, -np.sqrt(2)/2, -1, -np.sqrt(2)/2])
y = fft(x)
input("FFT递归调用以完成，按回车键退出")
