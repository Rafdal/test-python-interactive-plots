# Python Plotting & Preprocessing data

## Descripcion
En este repositorio utilizo dos scripts para el procesamiento y analisis de los datos generados por la arduino para posteriormente meterlos en la red neuronal que se va a encargar de hallar el patron entre las tres variables seleccionadas como **features** del modelo de Machine Learning.

El primer script es *3d_plot_ex.py* el cual lo uso para visualizar los graficos tanto de las nubes de puntos de las tres variables de frecuencias seleccionadas del output de la **Transformada Rapida de Fourier (FFT)** que implemento la Arduino.

Asi como tambien analizar el espectro completo de frecuencias que genero la **FFT** de cada caso especifico para poder identificar las features del sistema.


## TO-DO
En el otro repositorio (El que usa Keras para el machine learning). Queda probar algun dataset para resolver un problema de clasificacion, familiarizarme un poco con la libreria y los casos de uso. Y por ultimo meterle el dataset que genere "COMPLETE_DATASET.CSV" para entrenar la red que voy a hardcodear en la arduino.