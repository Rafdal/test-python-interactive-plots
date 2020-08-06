import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

noisy = pd.read_csv('NOISY_DATASET.CSV', sep=',', decimal='.') # index= [0,1,2]
stable = pd.read_csv('STABLE_DATASET.CSV', sep=',', decimal='.') # index= [3,4,5]
mov = pd.read_csv('MOV_DATASET.CSV', sep=',', decimal='.') # index= [6,7,8]

isTrue = [1] * 250
isFalse = [0] * 250


noisy['noisy'] = isTrue
noisy['stable'] = isFalse
noisy['mov'] = isFalse

stable['noisy'] = isFalse
stable['stable'] = isTrue
stable['mov'] = isFalse

mov['noisy'] = isFalse
mov['stable'] = isFalse
mov['mov'] = isTrue


result = pd.concat([noisy,stable,mov], ignore_index = True) #, keys=['x', 'y', 'z', 'type']
# result.to_csv('COMPLETE_DATASET.csv') # ! Crear archivo [.CSV]

print(result)