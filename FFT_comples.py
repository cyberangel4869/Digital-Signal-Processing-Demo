
import numpy as np

# 采用递归调用的方式实现FFT运算，便于展示FFT内部的计算过程
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
    # FFT核心运算单元：蝶形结
    arr1 = X_even+T*X_odd
    arr2 = X_even-T*X_odd
    # 每层蝶形结的输入输出
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
