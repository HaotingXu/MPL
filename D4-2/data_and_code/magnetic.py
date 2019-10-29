##Experiment: MNR

import matplotlib.pyplot as plt
import numpy as np
# initializing varibles, 'b' standing for back
current = []
frequency_1 = []
frequency_2 = []
frequency_1b = []
frequency_2b = []
input_file = "frequency.txt"
current_value = [18,20,22,24,27] ## Set current values, the actual value is current_value/10 Ampere
pi = 3.1415926535
gamma = 42.576375 ##it is gamma/2*pi  unit  MHz/T
mu_0 = 4*pi*1E-7
## Load data from input_file  frequency unit MHz
with open(input_file) as file_object:
    lines = file_object.readlines()
    for line in lines:
        temp = line.split(',')
        for j in current_value:
            if temp[0].strip() == str(j)+"_1":
                current.append(float(j)/10)
                frequency_1.append(float(temp[1].strip()))
            elif temp[0].strip() == str(j)+"_2":
                frequency_2.append(float(temp[1].strip()))
            elif temp[0].strip() == str(j)+"_1b":
                frequency_1b.append(float(temp[1].strip()))
            elif temp[0].strip() == str(j)+"_2b":
                frequency_2b.append(float(temp[1].strip()))
frequency_1b.append(frequency_1[4])
frequency_2b.append(frequency_2[4])
print(current)

##Computing B
for i in range(0,5):
    frequency_1[i] = frequency_1[i]/gamma
    frequency_2[i]= frequency_2[i]/gamma
    frequency_1b[i] = frequency_1b[i]/gamma
    frequency_2b[i] = frequency_2b[i]/gamma

print(frequency_2[1] - frequency_1[1])
for i in range(0,len(current)):
    current[i] = mu_0*np.sqrt((current[i] - 0.21)/3.11E-5)## relationship between magnetic field intensity and current
plt.figure(num=3,figsize=(8,5))

plt.plot(current,frequency_1,color='blue',linewidth=1.0)
plt.plot(current,frequency_1b,color = 'red',linewidth = 1.0)
# setting size of image
plt.xlabel(' Magnetic field intensity(A/m)')
plt.ylabel('Magnetic Induction(T)')
plt.title('Magnetic Hystersis Loop (one peak)',fontsize='large',fontweight='bold')
# save fig and close
plt.savefig("MAG/MHL_1.png")
plt.close()

##Computing B_2


plt.figure(num=3,figsize=(8,5))

plt.plot(current,frequency_2,color='blue',linewidth=1.0)
plt.plot(current,frequency_2b,color = 'red',linewidth = 1.0)
# setting size of image
plt.xlabel('Magnetic field intensity (A/m)')
plt.ylabel('Magnetic Field(T)')
plt.title('Magnetic Hystersis Loop (two peaks)',fontsize='large',fontweight = 'bold')
# save fig and close
plt.savefig("MAG/MHL_2.png")
plt.close()

