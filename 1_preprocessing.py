from scipy.fft import fft, ifft
import pandas as pd
import matplotlib.pyplot as plt

# df_stable = pd.read_csv('STABLE.CSV', sep=',', decimal='.')
# df_wave = pd.read_csv('WAVE.CSV', sep=',', decimal='.')
# df_noisy = pd.read_csv('NOISY.CSV', sep=',', decimal='.')
df_fan1 = pd.read_csv('FAN_1.CSV', sep=',', decimal='.')
df_fan2 = pd.read_csv('FAN_2.CSV', sep=',', decimal='.')
df_fan3 = pd.read_csv('FAN_3.CSV', sep=',', decimal='.')
df_stable = pd.read_csv('STABLE.CSV', sep=',', decimal='.')

# df_stable.columns = list(range(0,128)) # * Si los nombres de columna vienen bien, no hace falta
# df_noisy.columns = list(range(0,128))  # *
# df_wave.columns = list(range(0,128))  # *

three = [3] * 50
two = [2] * 50
one = [1] * 50
zero = [0] * 50
level1 = ['fan1'] * 50
level2 = ['fan2'] * 50
level3 = ['fan3'] * 50


df_fan1['speed'] = one

df_fan2['speed'] = two

df_fan3['speed'] = three

df_stable['speed'] = zero

result = pd.concat([df_fan1,df_fan2,df_fan3,df_stable], ignore_index = True) #, keys=['x', 'y', 'z', 'type']
print(result)

result.to_csv('COMPLETE_DATASET.csv') # ! Crear archivo [.CSV]