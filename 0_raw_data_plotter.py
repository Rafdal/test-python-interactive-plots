from scipy.fft import fft, ifft
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

root = Path('mov')

# df_stable = pd.read_csv('STABLE.CSV', sep=',', decimal='.')
# df_fan1 = pd.read_csv('FAN_1.CSV', sep=',', decimal='.')
# df_fan2 = pd.read_csv('FAN_2.CSV', sep=',', decimal='.')
# df_fan3 = pd.read_csv('FAN_3.CSV', sep=',', decimal='.')
# df_noisy = pd.read_csv('NOISY.CSV', sep=',', decimal='.')
# raw_stable = pd.read_csv('raw_STABLE.CSV', sep=',', decimal='.')
# raw_fan3 = pd.read_csv('raw_FAN3.CSV', sep=',', decimal='.')
# filtered_fan3 = pd.read_csv('filtered_FAN3.CSV', sep=',', decimal='.')
# filtered_stable = pd.read_csv('filtered_STABLE.CSV', sep=',', decimal='.')

# xyz_stable = pd.read_csv('XYZ_STABLE.CSV', sep=',', decimal='.') # * FFT + Filtro
# xyz_ST = xyz_stable.T.values[:,:]
# xyz_fan3 = pd.read_csv('XYZ_FAN3.CSV', sep=',', decimal='.') # * FFT + Filtro
# xyz_f3 = xyz_fan3.T.values[:,:]

mpu_stable = pd.read_csv(root / 'MOV4.CSV', sep=',', decimal='.')
x = mpu_stable.values[:,0]
y = mpu_stable.values[:,1]
z = mpu_stable.values[:,2]


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
plt.plot(x, linewidth = width, alpha = alpha, color= 'red')
plt.plot(y, linewidth = width, alpha = alpha, color= 'green')
plt.plot(z, linewidth = width, alpha = alpha, color= 'blue')
plt.show()