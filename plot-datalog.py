import pandas as pd
import matplotlib.pyplot as plt

noisy = pd.read_csv('NOISY_DATASET.CSV', sep=',', decimal='.',) #  names=['noisy']
# stable = pd.read_csv('STABLE_FFT_DATA.CSV', sep=',', decimal='.', names=['stable'])
# moving = pd.read_csv('MOV_FFT_DATA.CSV', sep=',', decimal='.', names=['moving'])

plt.style.use('dark_background')

# .drop(index=0)
# .drop(index=0)
# .drop(index=0)

""" pd.concat([
    noisy, 
    stable, 
    moving
    ], 
    axis=1
).plot.line() """

x = noisy.values[:,0]
x = noisy.values[:,0]

# plt.scatter()

# plt.show();


# x = range(0, 63, 1)
# plt.plot(x,noisy, linewidth=1.2, color='red')
# plt.plot(x,stable, linewidth=1.2, color='yellow')
# plt.plot(x,moving, linewidth=1.2, color='blue')
