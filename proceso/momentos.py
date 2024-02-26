"""Momentos.

Módulo encargado de calcular autocovarianza y autocorrelación.
"""
from fitter import Fitter
import numpy as np
from scipy import stats
from scipy.stats import genlogistic
import matplotlib.pyplot as plt
import requests
import pandas as pd
import statistics
import json


def autocorrelacion(df_consumo, hora1, hora2):
    """Cálculo de autocorrelación.

    Toma los datos de potencia asociadas a las horas que ingresó el usario
    (hora1 y hora2) y se guardan ambos de estos datos en un dataframe "x",
    por último se la autocorrelación por medio del función .corr(),
    esta función devuelve una matriz por lo que se guarda el valor buscado
    en correlación usando ".iat".
    """
    # Método para almacenar datos
    datos_hora = []
    for hora in range(0, 24):
        cada_hora = []
        while hora < len(df_consumo.axes[0]):
            cada_hora.append((df_consumo['MW'][hora]))
            hora = hora + 24
        datos_hora.append(cada_hora)

    # Tomando los datos de la primera hora asignada
    periodo1 = pd.DataFrame(datos_hora[hora1])
    # Tomando los datos de la segunda hora asignada
    periodo2 = pd.DataFrame(datos_hora[hora2])
    x = pd.concat([periodo1, periodo2], axis=1)
    # Método de pandas para encontrar la
    # correlación entre periodo 1 y periodo 2
    correlacion1 = x.corr(method='pearson')
    correlacion = correlacion1.iat[0, 1]
    return print('El coeficiente de autocorrelación '
                 'entre las horas ' + str(hora1) + ':00 '
                 'y ' + str(hora2) + ':00 es de: \n', correlacion)


def autocovarianza(df_consumo, hora1, hora2):
    """Cálculo de autocovarianza.

    Similar al caso anterior se busca la potencia asociada a
    las horas ingresadas por el usuario y se calcula la autocovarianza
    con la función de .cov(), puesto la misma solo acepta series de
    pandas se usa la función squeeze().
    """
    # Método para almacenar datos
    datos_hora = []
    for hora in range(0, 24):
        cada_hora = []
        while hora < len(df_consumo.axes[0]):
            cada_hora.append((df_consumo['MW'][hora]))
            hora = hora + 24
        datos_hora.append(cada_hora)
    # Tomando los datos de la primera hora asignada
    periodo1 = pd.DataFrame(datos_hora[hora1])
    # Tomando los datos de la segunda hora asignada
    periodo2 = pd.DataFrame(datos_hora[hora2])
    # Se guardan ambos periodos en una serie:
    consumoP1 = periodo1.squeeze()
    consumoP2 = periodo2.squeeze()
    # Calculando covarianza con pandas
    covar = consumoP1.cov(consumoP2)
    return print('El autocovarianza entre '
                 'las horas ' + str(hora1) + ':00 '
                 'y ' + str(hora2) + ":00 es de: \n", covar)
