import matplotlib.pyplot as plt
import numpy as np
import seaborn

t=[]
y=[]
t_factor = 50E-3
i = -1
fig = []
for j in [18,20,22,24,27]:
    fig.append(0)
    i = i+1
    filename = str(j)+'_1.csv'
    with open(filename) as file_object:
        lines = file_object.readlines()
        lines.remove(lines[0])
        lines.remove(lines[0])
        for line in lines:
            temp = line.split(',')
            t.append(float(temp[0])*t_factor)
            y.append(float(temp[1]))
        
    factor = 2.0E4
    n = len(y) # length of the signal
    k = np.arange(n)
    frq = k*factor #
    YY = np.fft.fft(y) # 未归一化
    plt.figure(dpi = 150)
    fig[i], ax = plt.subplots(2, 1)
    ax[0].plot(t,y)
    ax[0].set_xlabel('Time(ms)')
    ax[0].set_ylabel('Signal Amplitude')
    
    ax[1].plot(frq,abs(YY),'r') # plotting the spectrum
    ax[1].set_xlabel('Freq (10MHz)')
    ax[1].set_ylabel('|Y(freq)|')
    ax[1].set_xlim(600*factor,800*factor)
    ax[1].set_ylim(0,1)
    plt.tight_layout()
    plt.savefig("plot/"+str(j)+"_1.png")
    plt.close(fig[i])
    y = []
    t = []

##################################################
#################################################
for j in [18,20,22,24,27]:
    fig.append(0)
    i = i+1
    filename = str(j)+'_2.csv'
    with open(filename) as file_object:
        lines = file_object.readlines()
        lines.remove(lines[0])
        lines.remove(lines[0])
        for line in lines:
            temp = line.split(',')
            t.append(float(temp[0])*t_factor)
            y.append(float(temp[1]))
        
    factor = 2.0E4
    n = len(y) # length of the signal
    k = np.arange(n)
    frq = k*factor #
    YY = np.fft.fft(y) # 未归一化
    plt.figure(dpi = 150)
    fig[i], ax = plt.subplots(2, 1)
    ax[0].plot(t,y)
    ax[0].set_xlabel('Time(ms)')
    ax[0].set_ylabel('Signal Amplitude')
    
    ax[1].plot(frq,abs(YY),'r') # plotting the spectrum
    ax[1].set_xlabel('Freq (10MHz)')
    ax[1].set_ylabel('|Y(freq)|')
    ax[1].set_xlim(600*factor,800*factor)
    ax[1].set_ylim(0,1)
    plt.tight_layout()
    plt.savefig("plot/"+str(j)+"_2.png")
    plt.close(fig[i])
    y = []
    t = []

for j in [18,20,22,24]:
    fig.append(0)
    i = i+1
    filename = str(j)+'_1b.csv'
    with open(filename) as file_object:
        lines = file_object.readlines()
        lines.remove(lines[0])
        lines.remove(lines[0])
        for line in lines:
            temp = line.split(',')
            t.append(float(temp[0])*t_factor)
            y.append(float(temp[1]))
        
    factor = 2.0E4
    n = len(y) # length of the signal
    k = np.arange(n)
    frq = k*factor #
    YY = np.fft.fft(y) # 未归一化
    plt.figure(dpi = 150)
    fig[i], ax = plt.subplots(2, 1)
    ax[0].plot(t,y)
    ax[0].set_xlabel('Time(ms)')
    ax[0].set_ylabel('Signal Amplitude')
    
    ax[1].plot(frq,abs(YY),'r') # plotting the spectrum
    ax[1].set_xlabel('Freq (10MHz)')
    ax[1].set_ylabel('|Y(freq)|')
    ax[1].set_xlim(600*factor,800*factor)
    ax[1].set_ylim(0,1)
    plt.tight_layout()
    plt.savefig("plot/"+str(j)+"_1b.png")
    plt.close(fig[i])
    y = []
    t = []

for j in [18,20,22,24]:
    fig.append(0)
    i = i+1
    filename = str(j)+'_2b.csv'
    with open(filename) as file_object:
        lines = file_object.readlines()
        lines.remove(lines[0])
        lines.remove(lines[0])
        for line in lines:
            temp = line.split(',')
            t.append(float(temp[0])*t_factor)
            y.append(float(temp[1]))
        
    factor = 2.0E4
    n = len(y) # length of the signal
    k = np.arange(n)
    frq = k*factor #
    YY = np.fft.fft(y) # 未归一化
    plt.figure(dpi = 150)
    fig[i], ax = plt.subplots(2, 1)
    ax[0].plot(t,y)
    ax[0].set_xlabel('Time(ms)')
    ax[0].set_ylabel('Signal Amplitude')
    
    ax[1].plot(frq,abs(YY),'r') # plotting the spectrum
    ax[1].set_xlabel('Freq (10MHz)')
    ax[1].set_ylabel('|Y(freq)|')
    ax[1].set_xlim(600*factor,800*factor)
    ax[1].set_ylim(0,1)
    plt.tight_layout()
    plt.savefig("plot/"+str(j)+"_2b.png")
    plt.close(fig[i])
    y = []
    t = []
