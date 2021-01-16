import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

movdir = Path('mov')
flojdir = Path('floj')
pesodir = Path('peso')
pre = Path('PRE')

timestamps = list(range(0,512))

filename = ''


for i in range(0,256):
    filename = 'PESO' + str(i) + '.CSV'

    df = pd.read_csv(pesodir / filename, sep=',', decimal='.')


    df.insert(0, 'timestamp', timestamps)

    df.rename(columns = {'x':'accX'}, inplace = True)
    df.rename(columns = {'\ty':'accY'}, inplace = True)
    df.rename(columns = {'\tz':'accZ'}, inplace = True)

    # print(df['\ty'])
    # print(df)


    df.to_csv(pre / pesodir / filename, index=False) # ! Crear archivo [.CSV]
    pass