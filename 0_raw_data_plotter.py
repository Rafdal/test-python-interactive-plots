from scipy.fft import fft, ifft
import pandas as pd
import matplotlib.pyplot as plt

# df_stable = pd.read_csv('STABLE.CSV', sep=',', decimal='.')
df_fan1 = pd.read_csv('FAN_1.CSV', sep=',', decimal='.')
df_fan2 = pd.read_csv('FAN_2.CSV', sep=',', decimal='.')
df_fan3 = pd.read_csv('FAN_3.CSV', sep=',', decimal='.')
df_noisy = pd.read_csv('NOISY.CSV', sep=',', decimal='.')

# print(df_stable)
# print(df_wave)
# print(df_noisy)

# x0 = df_stable.T.values[:,:]
x1 = df_fan1.T.values[:,:]
x2 = df_fan2.T.values[:,:]
x3 = df_fan3.T.values[:,:]
x4 = df_noisy.T.values[:,:]

# print(x0)
# print(x1)
# print(x2)

# y0 = fft(x0) # Estatica
# y1 = fft(x1) # Moviendo
# y2 = fft(x1) # Stand-By

# print(y0)

plt.style.use('dark_background')

plt.xlabel("Mediciones")
width = 0.8
alpha = 0.05
plt.plot(x1, linewidth = width, alpha = alpha, color= 'red')
plt.plot(x2, linewidth = width, alpha = alpha, color= 'yellow')
plt.plot(x3, linewidth = width, alpha = alpha, color= 'red')
plt.show()