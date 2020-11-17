from scipy.fft import fft, ifft
import pandas as pd
import matplotlib.pyplot as plt

df_stable = pd.read_csv('STABLE.CSV', sep=',', decimal='.')
df_wave = pd.read_csv('WAVE.CSV', sep=',', decimal='.')
df_noisy = pd.read_csv('NOISY.CSV', sep=',', decimal='.')

df_stable.columns = list(range(0,128)) # * Si los nombres de columna vienen bien, no hace falta
df_noisy.columns = list(range(0,128))  # *
df_wave.columns = list(range(0,128))  # *

isTrue = [1] * 49
isFalse = [0] * 49


df_stable['noisy'] = isFalse
df_stable['stable'] = isTrue
df_stable['wave'] = isFalse


df_noisy['noisy'] = isTrue
df_noisy['stable'] = isFalse
df_noisy['wave'] = isFalse

# print(df_noisy)

df_wave['noisy'] = isFalse
df_wave['stable'] = isFalse
df_wave['wave'] = isTrue


result = pd.concat([df_noisy,df_stable,df_wave], ignore_index = True) #, keys=['x', 'y', 'z', 'type']
print(result)

result.to_csv('COMPLETE_DATASET.csv') # ! Crear archivo [.CSV]
