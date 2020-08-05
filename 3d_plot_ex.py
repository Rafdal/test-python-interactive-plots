# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

noisy = pd.read_csv('NOISY_DATASET.CSV', sep=',', decimal='.')
stable = pd.read_csv('STABLE_DATASET.CSV', sep=',', decimal='.')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xn = noisy.values[:,0]
yn = noisy.values[:,1]
zn = noisy.values[:,2]

xs = stable.values[:,0]
ys = stable.values[:,1]
zs = stable.values[:,2]

ax.scatter(xn, yn, zn, color = 'red')
ax.scatter(xs, ys, zs, color = 'blue')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
