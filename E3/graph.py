import matplotlib.pyplot as plt
import numpy as np
A = 0.15
B = 20
# 定义 x 变量的范围 (-3，3) 数量 50 
x=np.linspace(1,100)
y=B*x/(np.log(A*x))

# Figure 并指定大小
plt.figure(num=3,figsize=(8,5))
# 绘制 y=x^2 的图像，设置 color 为 red，线宽度是 1，线的样式是 --
plt.plot(x,y,color='blue',linewidth=1.0,linestyle='--')

# 设置 x，y 轴的范围以及 label 标注
plt.xlim(1,110)
plt.ylim(300,1000)
plt.xlabel('x')
plt.ylabel('y')
plt.text(40,850,r'$y=\frac{Bx}{\ln (Ax)} \ \ A = 0.15,B = 20$',fontsize = 20,color = 'blue')

# 显示图像
plt.show()
