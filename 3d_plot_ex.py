# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

noisy = pd.read_csv('NOISY_DATASET.CSV', sep=',', decimal='.') # index= [0,1,2]
stable = pd.read_csv('STABLE_DATASET.CSV', sep=',', decimal='.') # index= [3,4,5]
mov = pd.read_csv('MOV_DATASET.CSV', sep=',', decimal='.') # index= [6,7,8]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

isNoisy = [-1] * 250
isStable = [0] * 250
isMov = [1] * 250

noisy['type'] = isNoisy
stable['type'] = isStable
mov['type'] = isMov

# xn = noisy.values[:,0]
# yn = noisy.values[:,1]
# zn = noisy.values[:,2]

# xs = stable.values[:,0]
# ys = stable.values[:,1]
# zs = stable.values[:,2]

# xm = mov.values[:,0]
# ym = mov.values[:,1]
# zm = mov.values[:,2]

result = pd.concat([noisy,stable,mov], ignore_index = True) #, keys=['x', 'y', 'z', 'type']
result.to_csv('COMPLETE_DATASET.csv')

print(result)

# ax.scatter(xn, yn, zn, color = 'red', s=12)
# ax.scatter(xs, ys, zs, color = 'blue', s=50)
# ax.scatter(xm, ym, zm, color = 'green', s=12)

# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# plt.show()
