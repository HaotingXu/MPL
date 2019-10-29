import matplotlib.pyplot as plt
import numpy as np
import seaborn
t=[]
y=[]
t_factor = 50E-3
delta_function_fre = []
output_file = open('frequency.txt','w')

print("-----------------------------------------------------------------")
print("Fourier Transformation Delta Function Result, increasing current.")
print("-----------------------------------------------------------------")
for j in [18,20,22,24,27]:
    filename = str(j)+'_1.csv'
    with open(filename) as file_object:
        lines = file_object.readlines()
        lines.remove(lines[0])
        lines.remove(lines[0])
        for line in lines:
            temp = line.split(',')
            t.append(float(temp[0]))
            y.append(float(temp[1]))
        
        factor = 2.0E4
        n = len(y) # length of the signal
        k = np.arange(n)
        frq = k*factor #
        YY = np.fft.fft(y) # 未归一化
        i=0
        sum_1 = 0
        delta_function_fre = []
        for i in range(600,800):
            if abs(YY[i]-YY[i-1]) >= 0.2:
                delta_function_fre.append(frq[i])
                sum_1 = sum_1 + frq[i]
        sum_1 = sum_1/len(delta_function_fre)

        
        filename = str(j)+'_2.csv'
    with open(filename) as file_object:
        lines = file_object.readlines()
        lines.remove(lines[0])
        lines.remove(lines[0])
        for line in lines:
            temp = line.split(',')
            t.append(float(temp[0]))
            y.append(float(temp[1]))
        
        factor = 2.0E4
        n = len(y) # length of the signal
        k = np.arange(n)
        frq = k*factor #
        YY = np.fft.fft(y) # 未归一化
        i=0
        sum_2 = 0
        delta_function_fre = []
        for i in range(600,800):
            if abs(YY[i]-YY[i-1]) >= 0.2:
                delta_function_fre.append(frq[i])
                sum_2 = sum_2 + frq[i]
        sum_2 = sum_2/len(delta_function_fre)
        print(str(j)+"_1     ,"+str(sum_1/1.0E6)+" ,MHz",file = output_file)        
        print(str(j)+"_2     ,"+str(sum_2/1.0E6)+" ,MHz",file = output_file)
t=[]
y=[]
t_factor = 50E-3
delta_function_fre = []
print("-----------------------------------------------------------------")
print("Fourier Transformation Delta Function Result, decreasing current.")
print("-----------------------------------------------------------------")
for j in [24,22,20,18]:
    filename = str(j)+'_1b.csv'
    with open(filename) as file_object:
        lines = file_object.readlines()
        lines.remove(lines[0])
        lines.remove(lines[0])
        for line in lines:
            temp = line.split(',')
            t.append(float(temp[0]))
            y.append(float(temp[1]))
        
        factor = 2.0E4
        n = len(y) # length of the signal
        k = np.arange(n)
        frq = k*factor #
        YY = np.fft.fft(y) # 未归一化
        i=0
        sum_1 = 0
        delta_function_fre = []
        for i in range(600,800):
            if abs(YY[i]-YY[i-1]) >= 0.2:
                delta_function_fre.append(frq[i])
                sum_1 = sum_1 + frq[i]
        sum_1 = sum_1/len(delta_function_fre)

        
        filename = str(j)+'_2b.csv'
    with open(filename) as file_object:
        lines = file_object.readlines()
        lines.remove(lines[0])
        lines.remove(lines[0])
        for line in lines:
            temp = line.split(',')
            t.append(float(temp[0]))
            y.append(float(temp[1]))
        
        factor = 2.0E4
        n = len(y) # length of the signal
        k = np.arange(n)
        frq = k*factor #
        YY = np.fft.fft(y) # 未归一化
        i=0
        sum_2 = 0
        delta_function_fre = []
        for i in range(600,800):
            if abs(YY[i]-YY[i-1]) >= 0.2:
                delta_function_fre.append(frq[i])
                sum_2 = sum_2 + frq[i]
        sum_2 = sum_2/len(delta_function_fre)
        print(str(j)+"_1b     ,"+str(sum_1/1.0E6)+" ,MHz",file = output_file)        
        print(str(j)+"_2b     ,"+str(sum_2/1.0E6)+" ,MHz",file = output_file)

print("-----------------------------------------------------------------")
output_file.close()
