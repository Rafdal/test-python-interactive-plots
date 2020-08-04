import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('moviendo.CSV', sep=',', decimal='.')

plt.style.use('dark_background')

plt.xlabel("Mediciones")

plt.plot(df, linewidth=0.6)
plt.show()