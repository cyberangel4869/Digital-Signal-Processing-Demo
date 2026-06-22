import matplotlib.pyplot as plt
import numpy as np

error = np.array([0,0,0,1,0,0,0,0,0])#模拟0时刻的单位脉冲响应
u = np.array([0,0,0,0,0,0,0,0])

k0=2.01
k1=-3
k2=1

for n in range(2,8):
    u[n]=u[n-1]+k0*error[n]+k1*error[n-1]+k2*error[n-2]

x=np.array([0,1,2,3,4,5])
y=u[2:8]
    
plt.plot(x,y,label=f'PID')
plt.xlabel('k')
plt.ylabel('u(k)')
plt.title("PID")
plt.legend()
plt.grid(True)
plt.show()
