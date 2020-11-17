from scipy.fft import fft, ifft
import pandas as pd
import matplotlib.pyplot as plt

df_stable = pd.read_csv('STABLE.CSV', sep=',', decimal='.')
df_wave = pd.read_csv('WAVE.CSV', sep=',', decimal='.')
df_noisy = pd.read_csv('NOISY.CSV', sep=',', decimal='.')

# print(df_stable)
# print(df_wave)
# print(df_noisy)

x0 = df_stable.T.values[:,:]
x1 = df_wave.T.values[:,:]
x2 = df_noisy.T.values[:,:]

# print(x0)
# print(x1)
# print(x2)

# y0 = fft(x0) # Estatica
# y1 = fft(x1) # Moviendo
# y2 = fft(x1) # Stand-By

# print(y0)

plt.style.use('dark_background')

plt.xlabel("Mediciones")
width = 1
alpha = 0.1
plt.plot(x0, linewidth = width, alpha = alpha, color= 'red')
# plt.plot(x1, linewidth = width, alpha = alpha, color= 'green')
plt.plot(x2, linewidth = width, alpha = alpha, color= 'yellow')
plt.show()