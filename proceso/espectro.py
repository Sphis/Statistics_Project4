"""Espectro.

En este modulo grafica el espectro de densidad de potencia.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json


def psd(df_consumo, hora9):
    """Obtiene gráfica de densidad espectral.

    Toma datos de potencia de datos.json de una hora específicada por
    el usuario (guardado en hora9) y los gráfica con una frecuencia de muestreo
    dt, el eje x es el tiempo en días, razón por la que se crea un intervalo
    de 0 a 365.
    """
    # Método para almacenar datos
    datos_hora = []
    for hora in range(0, 24):
        cada_hora = []
        while hora < len(df_consumo.axes[0]):
            cada_hora.append((df_consumo['MW'][hora]))
            hora = hora + 24
        datos_hora.append(cada_hora)

    # Tomando los datos de potencia de una
    # hora especificada por el usuario
    dt = 0.01
    t = np.arange(0, 365, dt)
    periodo9 = datos_hora[hora9]
    nse1 = np.random.randn(len(t))

    plt.psd(periodo9, 512, 1./dt, color="green")
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('PSD(db) de las ' + str(hora9) + ':00')

    plt.show()
    return
