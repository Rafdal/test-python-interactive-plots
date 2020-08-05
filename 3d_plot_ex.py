# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

noisy = pd.read_csv('NOISY_DATASET.CSV', sep=',', decimal='.') # index= [0,1,2]
stable = pd.read_csv('STABLE_DATASET.CSV', sep=',', decimal='.') # index= [3,4,5]
mov = pd.read_csv('MOV_DATASET.CSV', sep=',', decimal='.') # index= [6,7,8]

noisy2 = pd.read_csv('NOISE_FFT_DATA.CSV', sep=',', decimal='.',) #  names=['noisy']
stable2 = pd.read_csv('STABLE_FFT_DATA.CSV', sep=',', decimal='.')
moving2 = pd.read_csv('MOV_FFT_DATA.CSV', sep=',', decimal='.')

# plt.style.use('dark_background')

fig = plt.figure()
fig.tight_layout()

ax = fig.add_subplot(1,2,1, projection='3d')
ax2 = fig.add_subplot(1,2,2) # , aspect=0.005, adjustable='box'

xn = noisy.values[:,0]
yn = noisy.values[:,1]
zn = noisy.values[:,2]

xs = stable.values[:,0]
ys = stable.values[:,1]
zs = stable.values[:,2]

xm = mov.values[:,0]
ym = mov.values[:,1]
zm = mov.values[:,2]

ax.scatter(xn, yn, zn, color = 'red', s=12)
ax.scatter(xs, ys, zs, color = 'blue', s=50)
ax.scatter(xm, ym, zm, color = 'green', s=12)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax2.plot(noisy2, linewidth=1.2, color='red')
ax2.plot(stable2, linewidth=1.2, color='yellow')
ax2.plot(moving2, linewidth=1.2, color='blue')

plt.show()
