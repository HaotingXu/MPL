import matplotlib.pyplot as plt
import numpy as np

CH1 = []
CH2 = []
t_factor = 50E-3
input_file = "time.csv"

with open(input_file) as file_obj:
    lines = file_obj.readlines()
    lines.remove(lines[0])
    lines.remove(lines[0])
    for line in lines:
        temp = line.split(',')
        CH1.append(float(temp[1].strip()))
        CH2.append(float(temp[2].strip()))
plt.figure(num=3,figsize=(8,5))
# Plotting initial figure
plt.plot(CH1,CH2,color='blue',linewidth=1.0)
# setting size of image
plt.xlabel('CH1')
plt.ylabel('CH2')
plt.title('Figure in X-Y mode',fontsize='large',fontweight='bold')
# save fig and close
plt.savefig("time.png")
plt.close()


#data analysis
CH_1_new = []
CH_2_new = []
average_rate = 2.0 #average nearly 2 points
j = 0
for j in range(0,len(CH1),int(average_rate)):
    CH_1_new.append((CH1[j] + CH1[j+1])/average_rate)
    CH_2_new.append((CH2[j] + CH2[j+1])/average_rate)

    
# Plotting initial figure
plt.plot(CH_1_new,CH_2_new,color='blue',linewidth=1.0)
# setting size of image
plt.xlabel('CH1')
plt.ylabel('CH2')
plt.title('Figure in X-Y mode',fontsize='large',fontweight='bold')
# save fig and close
plt.savefig("time2.png")
plt.close()
#finding minimum and maximum and compute their difference
min = CH_1_new[0]
max = CH_1_new[0]
for j in range(0,len(CH_1_new)):
    if CH_1_new[j] <= min:
        min = CH_1_new[j]
    elif CH_1_new[j] >= max:
        max = CH_1_new[j]
difference = max - min
#fiding peak and compute the width
peak_value = []
peak_value_1 = []
peak_value_2 = []
for j in range(0,len(CH_1_new)-1):
    if abs(CH_2_new[j+1] - CH_2_new[j]) >= 0.02:
        peak_value.append(CH_1_new[j])

## Sort two peak
peak_ref = peak_value[0]
for j in range(0,len(peak_value)):
    if abs(peak_value[j] - peak_ref)<=0.5:
        peak_value_1.append(peak_value[j])
    else:
        peak_value_2.append(peak_value[j])

## Compute width
min = peak_value_1[0]
max = peak_value_1[0]
for j in range(0,len(peak_value_1)):
    if peak_value_1[j] <= min:
        min = peak_value_1[j]
    elif peak_value_1[j]>= max:
        max = peak_value_1[j]
width_1 = max - min

min = peak_value_2[0]
max = peak_value_2[0]
for j in range(0,len(peak_value_2)):
    if peak_value_2[j] <= min:
        min = peak_value_2[j]
    elif peak_value_2[j]>= max:
        max = peak_value_2[j]
width_2 = max - min

width_average = (width_1+width_2)/2.0
proportion = width_average/difference
print("width_average=  "+str(width_average))
print("proportion = "+str(proportion))



        
