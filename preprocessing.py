import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

noisy = pd.read_csv('NOISY_DATASET.CSV', sep=',', decimal='.') # index= [0,1,2]
stable = pd.read_csv('STABLE_DATASET.CSV', sep=',', decimal='.') # index= [3,4,5]
mov = pd.read_csv('MOV_DATASET.CSV', sep=',', decimal='.') # index= [6,7,8]

isNoisy = [-1] * 250
isStable = [0] * 250
isMov = [1] * 250

noisy['type'] = isNoisy
stable['type'] = isStable
mov['type'] = isMov



result = pd.concat([noisy,stable,mov], ignore_index = True) #, keys=['x', 'y', 'z', 'type']
result.to_csv('COMPLETE_DATASET.csv')

print(result)