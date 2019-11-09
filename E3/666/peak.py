import matplotlib.pyplot as plt
import numpy as np
import seaborn

freq=[]
intensity=[]
back=[]
fig=[]
#READ BACKGROUND
background_file = 'background.txt'
data_file = '20Pa_air'
with open(background_file) as file_obj:
    data = file_obj.readlines()
    for line in data:
        temp = line.split()
        freq.append(float(temp[0]))
        back.append(float(temp[1]))

with open(data_file) as file_obj:
    data = file_obj.readlines()
    for line in data:
        temp = line.split()
        intensity.append(float(temp[1]))
for i in range(0,len(freq)-1):
    intensity[i] = intensity[i] - back[i]
for i in range(0,len(intensity)-1):
    if abs(intensity[i+1]-intensity[i])> 14:
        print(freq[i])
plt.plot(freq,intensity,color = 'blue',linewidth=1.0)
plt.xlabel('$f$(Hz)')
plt.show()
        
