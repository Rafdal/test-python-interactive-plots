from scipy.fft import fft, ifft
import pandas as pd
import matplotlib.pyplot as plt

# df_stable = pd.read_csv('STABLE.CSV', sep=',', decimal='.')
# df_wave = pd.read_csv('WAVE.CSV', sep=',', decimal='.')
# df_noisy = pd.read_csv('NOISY.CSV', sep=',', decimal='.')
df_fan1 = pd.read_csv('FAN_1.CSV', sep=',', decimal='.')
df_fan2 = pd.read_csv('FAN_2.CSV', sep=',', decimal='.')
df_fan3 = pd.read_csv('FAN_3.CSV', sep=',', decimal='.')


# df_stable.columns = list(range(0,128)) # * Si los nombres de columna vienen bien, no hace falta
# df_noisy.columns = list(range(0,128))  # *
# df_wave.columns = list(range(0,128))  # *

isTrue = [1] * 50
isFalse = [0] * 50


df_fan1['noisy'] = isFalse
df_fan1['stable'] = isTrue
df_fan1['wave'] = isFalse


df_fan2['noisy'] = isTrue
df_fan2['stable'] = isFalse
df_fan2['wave'] = isFalse

# print(df_noisy)

df_fan3['noisy'] = isFalse
df_fan3['stable'] = isFalse
df_fan3['wave'] = isTrue


result = pd.concat([df_fan1,df_fan2,df_fan3], ignore_index = True) #, keys=['x', 'y', 'z', 'type']
print(result)

result.to_csv('COMPLETE_DATASET.csv') # ! Crear archivo [.CSV]
