#importamos librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from micromlgen import port

#cargamos los datos de entrada
df = pd.read_csv("COMPLETE_DATASET.csv")

# Separo el dataframe en los datos (X) y los target (Y)
X = df.iloc[:,0:384]
Y = df.iloc[:,385]
print(Y)

# Normalización
X_std = StandardScaler().fit_transform(X, y=Y)

pca = PCA(n_components=3, whiten=True)
principalComponents = pca.fit_transform(X, y=Y)

print('components:', pca.n_components)
print('Variance Ratio:', pca.explained_variance_ratio_)

principalDf = pd.DataFrame(data = principalComponents, columns = ['PC1', 'PC2', 'PC3'])

finalDf = pd.concat([principalDf, Y], axis = 1, ignore_index=True)
finalDf.columns = ['PC1', 'PC2', 'PC3', 'speed']
# print(finalDf)


""" plt.scatter(finalDf.loc[finalDf['speed']==0, 'PC1']
    , finalDf.loc[finalDf['speed'] == 0, 'PC2']
    , c = 'grey'
    , s = 50
    , linewidths= 0
    , alpha = 0.5)

plt.scatter(finalDf.loc[finalDf['speed'] == 1, 'PC1']
    , finalDf.loc[finalDf['speed'] == 1, 'PC2']
    , c = 'blue'
    , s = 50
    , linewidths= 0
    , alpha = 0.5)
plt.scatter(finalDf.loc[finalDf['speed'] == 2, 'PC1']
    , finalDf.loc[finalDf['speed'] == 2, 'PC2']
    , c = 'yellow'
    , s = 50
    , linewidths= 0
    , alpha = 0.5)
plt.scatter(finalDf.loc[finalDf['speed'] == 3, 'PC1']
    , finalDf.loc[finalDf['speed'] == 3, 'PC2']
    , c = 'red'
    , s = 50
    , linewidths= 0
    , alpha = 0.5)

plt.grid()
plt.show() """


fig = plt.figure()
fig.tight_layout()

ax = fig.add_subplot(1,1,1, projection='3d')
# ax2 = fig.add_subplot(1,2,2) # , aspect=0.005, adjustable='box'

x0 = finalDf.loc[finalDf['speed']==0, 'PC1']
y0 = finalDf.loc[finalDf['speed']==0, 'PC2']
z0 = finalDf.loc[finalDf['speed']==0, 'PC3']

x1 = finalDf.loc[finalDf['speed']==1, 'PC1']
y1 = finalDf.loc[finalDf['speed']==1, 'PC2']
z1 = finalDf.loc[finalDf['speed']==1, 'PC3']

# x2 = finalDf.loc[finalDf['speed']==2, 'PC1']
# y2 = finalDf.loc[finalDf['speed']==2, 'PC2']
# z2 = finalDf.loc[finalDf['speed']==2, 'PC3']

# x3 = finalDf.loc[finalDf['speed']==3, 'PC1']
# y3 = finalDf.loc[finalDf['speed']==3, 'PC2']
# z3 = finalDf.loc[finalDf['speed']==3, 'PC3']

alpha = 0.3
size = 20

ax.scatter(x0, y0, z0, color = 'grey', s=size, alpha = alpha)
ax.scatter(x1, y1, z1, color = 'blue', s=size, alpha = alpha)
# ax.scatter(x2, y2, z2, color = 'yellow', s=size, alpha = alpha)
# ax.scatter(x3, y3, z3, color = 'red', s=size, alpha = alpha)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()