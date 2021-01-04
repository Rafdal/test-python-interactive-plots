from scipy import signal
from scipy.fft import fft, fftshift, fftfreq
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np


def plotFourier(data, color = 'red', alpha = 1, linewidth = 1, freq=1/1000, samples=512):
    hann = signal.windows.hann(samples)

    windowed = hann*data

    yf = fft(windowed)
    xf = fftfreq(samples, freq)[:samples//2]

    plt.plot(xf, 2.0/samples * np.abs(yf[0:samples//2]), linewidth = width, alpha = alpha, color = color)
    pass


movdir = Path('mov')
flojdir = Path('floj')
pesodir = Path('peso')


# for i in range(450):
# 	filename = "MOV" + str(i) + ".CSV"
# 	mpu_mov = pd.read_csv(movdir / filename, sep=',', decimal='.')
# 	print(mpu_mov)
# 	break
# 	pass

mpu_peso = pd.read_csv(pesodir / 'PESO0.CSV', sep=',', decimal='.')
mpu_mov = pd.read_csv(movdir / 'MOV0.CSV', sep=',', decimal='.')


xm = mpu_mov.values[:,0]
ym = mpu_mov.values[:,1]
zm = mpu_mov.values[:,2]

xp = mpu_peso.values[:,0]
yp = mpu_peso.values[:,1]
zp = mpu_peso.values[:,2]

# print(df_wave)
# print(df_noisy)

# x1 = df_fan1.T.values[:,:]
# x2 = df_fan2.T.values[:,:]
# x3 = df_fan3.T.values[:,:]
# x4 = df_noisy.T.values[:,:]
# xStable = filtered_stable.values[:,:]
# xFan3 = filtered_fan3.values[:,:]

plt.style.use('dark_background')
plt.xlabel("Mediciones")
width = 1
alpha = 1

# plotFourier(xm, 'red', 0.5)
# plotFourier(xp, 'orange',0.5)
plotFourier(yp, 'blue',0.5)
plotFourier(ym, 'lightblue',0.5)

# plt.plot(xp, linewidth = width, alpha = alpha, color= 'red')
# plt.plot(yp, linewidth = width, alpha = alpha, color= 'green')
# plt.plot(zp, linewidth = width, alpha = alpha, color= 'blue')

# plt.plot(xm, linewidth = width, alpha = alpha, color= 'orange')
# plt.plot(ym, linewidth = width, alpha = alpha, color= 'yellow')
# plt.plot(zm, linewidth = width, alpha = alpha, color= 'lightblue')


plt.show()

