##Exponential decrease for Cu2+ and pure(?) water

import matplotlib.pyplot as plt
import numpy as np
import math

Cu_data = "H2O.csv" #H2O.csv, cu_tail.csv
C = 0.05
t_factor = 50E-3
t = []
y = []
with open(Cu_data) as fo:
    lines = fo.readlines()
    lines.remove(lines[0])
    lines.remove(lines[0])
    for line in lines:
        temp = line.split(',')
        t.append(float(temp[0])*t_factor)
        y.append(float(temp[1]))
peak_point = [592,727,797]

plt.plot(t,y,color = 'red',linewidth = 1.0)
plt.xlabel('Time(ms)')
plt.ylabel('Amplitude')
plt.xlim(25,50)
plt.ylim(0.075,0.175)
plt.title('Exponential decrease of pure water',fontsize = 'large', fontweight = 'bold')

peak_value = []
for i in peak_point:
    peak_value.append(np.log(y[i]-C))
for i in range(0,len(peak_point)):
    peak_point[i] = t_factor*peak_point[i]
    
k = np.polyfit(peak_point,peak_value,1)#k[0] is the slope, k[1] is C

print(len(peak_point))
i=0
# Plot the fitting line
k[1] = np.exp(peak_value[i])/np.exp(peak_point[i]*k[0])
t2 = np.linspace(20,60)
y2 = k[1]*np.exp(t2*k[0])
plt.plot(t2,y2,color = 'blue',linewidth = 1.0)
print("Hesitate time = "+str(-1/k[0]))
plt.savefig("Cu_tail.png")
plt.close()


