from scipy.fft import fft, ifft
import pandas as pd
import matplotlib.pyplot as plt

df_estatica = pd.read_csv('estatica.CSV', sep=',', decimal='.')
df_moviendo = pd.read_csv('moviendo.CSV', sep=',', decimal='.')
df_stand_by = pd.read_csv('stand-by.CSV', sep=',', decimal='.')

x0 = df_estatica.values[:,0]
x1 = df_moviendo.values[:,0]
x2 = df_stand_by.values[:,0]

# print(x0)

y0 = fft(x0) # Estatica
y1 = fft(x1) # Moviendo
y2 = fft(x2) # Stand-By

# print(y0)

plt.style.use('dark_background')

plt.xlabel("Mediciones")
width = 1.0
alpha = 1.0
plt.plot(y0, linewidth = width, alpha = alpha, color= 'red')
plt.plot(y1, linewidth = width, alpha = alpha, color= 'blue')
plt.plot(y2, linewidth = width, alpha = alpha, color= 'yellow')
plt.show()