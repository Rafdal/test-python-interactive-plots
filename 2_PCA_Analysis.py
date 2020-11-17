#importamos librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from micromlgen import port

#cargamos los datos de entrada
df = pd.read_csv("COMPLETE_DATASET.csv")

# Separo el dataframe en los datos (X) y los target (Y)
X = df.iloc[:,0:256]
Y = df.iloc[:,257:260]
print(Y)

# Normalización
X_std = StandardScaler().fit_transform(X, y=Y)

pca = PCA(n_components=2, whiten=False)
principalComponents = pca.fit_transform(X, y=Y)

print(pca.n_components)

principalDf = pd.DataFrame(data = principalComponents, columns = ['PC1', 'PC2'])

# principalDf['noisy'] = Y
finalDf = pd.concat([principalDf, Y], axis = 1, ignore_index=True)
finalDf.columns = ['PC1', 'PC2', 'noisy','stable','wave']
print(finalDf)


# print()

plt.scatter(finalDf.loc[finalDf['noisy']==1, 'PC1']
    , finalDf.loc[finalDf['noisy'] == 1, 'PC2']
    , c = 'r'
    , s = 50
    , linewidths= 0
    , alpha = 0.5)

plt.scatter(finalDf.loc[finalDf['stable'] == 1, 'PC1']
    , finalDf.loc[finalDf['stable'] == 1, 'PC2']
    , c = 'g'
    , s = 50
    , linewidths= 0
    , alpha = 0.5)
plt.scatter(finalDf.loc[finalDf['wave'] == 1, 'PC1']
    , finalDf.loc[finalDf['wave'] == 1, 'PC2']
    , c = 'b'
    , s = 50
    , linewidths= 0
    , alpha = 0.5)

plt.grid()
plt.show()



