import pandas as pd
import matplotlib.pyplot as plt

noisy = pd.read_csv('NOISE_FFT_DATA.CSV', sep=',', decimal='.',) #  names=['noisy']
stable = pd.read_csv('STABLE_FFT_DATA.CSV', sep=',', decimal='.')
moving = pd.read_csv('MOV_FFT_DATA.CSV', sep=',', decimal='.')

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

# x = noisy.values[:,0]
# x = noisy.values[:,0]

# plt.scatter()



# x = range(1, 63, 1)
plt.plot(noisy, linewidth=1.2, color='red')
plt.plot(stable, linewidth=1.2, color='yellow')
plt.plot(moving, linewidth=1.2, color='blue')

plt.show();