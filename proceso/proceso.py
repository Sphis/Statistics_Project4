"""Módulo de proceso."""
from fitter import Fitter
import numpy as np
from scipy import stats
from scipy.stats import genlogistic
import matplotlib.pyplot as plt
import requests
import pandas as pd
import statistics
import json


def demanda():
    """Función de datos de demananda.

    Esta función lee y carga los datos de consumo del archivo .json.

    Parameters
    ----------
    Sin parámetros de entrada

    Returns
    -------
    df : dataframe
            Dataframe con los datos de consumo.
    """
    # Se cargan los datos de consumo del archivo .json
    with open('datos.json') as file:
        datos = json.load(file)
    df = pd.DataFrame(datos['data'])
    return df


def densidad(df_consumo):
    """Función de densidad.

    Esta función es capaz de encontrar la función de densidad de
    probabilidad de la secuencia aleatoria.
    En esta se encuentran los parámetros que conforman el polinomio de grado 7.

    Parameters
    ----------
    df_consumo : dataframe
        Dataframe con los datos de consumo

    Returns
    -------
    Devuelve los parámetros como funciones del tiempo
    """
    # Vectores de los parámetros de la función de distribución
    c = []
    loc = []
    scale = []

    # Método para almacenar datos
    datos_hora = []
    for hora in range(0, 24):
        cada_hora = []
        while hora < len(df_consumo.axes[0]):
            cada_hora.append((df_consumo['MW'][hora]))
            hora = hora + 24
        datos_hora.append(cada_hora)

    # Método para encontrar los parámetros
    for i in range(0, 24):
        # Seleccion del modelo.
        modelo = 'genlogistic'

        # Parametros para la hora especifica.
        mejorAjuste_Horas = Fitter(datos_hora[i], distributions=[modelo])
        mejorAjuste_Horas.fit()

        # Parametros de la distribucion.
        params = mejorAjuste_Horas.fitted_param

        # Guardar los datosen los arreglos, su posicion indica su hora.
        c.append(params[modelo][0])
        loc.append(params[modelo][1])
        scale.append(params[modelo][2])

    # horas
    x = list(range(0, 24))

    # Se hayan los coeficientes de las funciones del polinomio de grado 7
    c_t = np.polyfit(x, c, 7)
    loc_t = np.polyfit(x, loc, 7)
    scale_t = np.polyfit(x, scale, 7)

    print("Los coeficientes de la función del tiempo c(t) son: ", c_t)
    print("Los coeficientes de la función del tiempo loc(t) son: ", loc_t)
    print("Los coeficientes de la función del tiempo scale(t) son: ", scale_t)
    return 'Retorna los coeficientes'


def grafica(df_consumo):
    """Función gráfica.

    Esta función es capaz de graficar la función de
    densidad de probabilidad de la secuencia aleatoria P(t)

    Parameters
    ----------
    df_consumo : dataframe
        Dataframe con los datos de consumo

    Returns
    -------
    Gráfica de densidad de probabilidad.F
    """
    # Vectores de los parámetros de la función de distribución
    c = []
    loc = []
    scale = []

    # Método para almacenar datos
    datos_hora = []
    for hora in range(0, 24):
        cada_hora = []
        while hora < len(df_consumo.axes[0]):
            cada_hora.append((df_consumo['MW'][hora]))
            hora = hora + 24
        datos_hora.append(cada_hora)

    # Método para obtener los parámetros
    for i in range(0, 24):
        # Seleccion del modelo.
        modelo = 'genlogistic'

        # Parametros para la hora especifica.
        mejorAjuste_Horas = Fitter(datos_hora[i], distributions=[modelo])
        mejorAjuste_Horas.fit()

        # Parametros de la distribucion.
        params = mejorAjuste_Horas.fitted_param

        # Guardar los datosen los arreglos, su posicion indica su hora.
        c.append(params[modelo][0])
        loc.append(params[modelo][1])
        scale.append(params[modelo][2])
    x = np.arange(700, 1800)

    # Aqui se muestra la figura
    fig, (ax0, ax1, ax2, ax3, ax4, ax5, ax6, ax7,
          ax8, ax9, ax10, ax11, ax12, ax13, ax14,
          ax15, ax16, ax17, ax18, ax19, ax20, ax21,
          ax22, ax23) = plt.subplots(24, 1, sharex=True)

    fig.suptitle(
        'Gráfica de la función de densidad de probabilidad'
        'de la secuencia aleatoria', fontsize=10)

    ax0.plot(x, genlogistic.pdf(x, c[0], loc[0], scale[0]))
    ax0.tick_params(labelsize=8)
    ax0.set_ylabel("00:00", fontsize=8)

    ax1.plot(x, genlogistic.pdf(x, c[1], loc[1], scale[1]))
    ax1.tick_params(labelsize=8)

    ax2.plot(x, genlogistic.pdf(x, c[2], loc[2], scale[2]))
    ax2.tick_params(labelsize=8)

    ax3.plot(x, genlogistic.pdf(x, c[3], loc[3], scale[3]))
    ax3.tick_params(labelsize=8)

    ax4.plot(x, genlogistic.pdf(x, c[4], loc[4], scale[4]))
    ax4.tick_params(labelsize=8)

    ax5.plot(x, genlogistic.pdf(x, c[5], loc[5], scale[5]))
    ax5.tick_params(labelsize=8)

    ax6.plot(x, genlogistic.pdf(x, c[6], loc[6], scale[6]))
    ax6.tick_params(labelsize=8)

    ax7.plot(x, genlogistic.pdf(x, c[7], loc[7], scale[7]))
    ax7.tick_params(labelsize=8)

    ax8.plot(x, genlogistic.pdf(x, c[8], loc[8], scale[8]))
    ax8.tick_params(labelsize=8)

    ax9.plot(x, genlogistic.pdf(x, c[9], loc[9], scale[9]))
    ax9.tick_params(labelsize=8)

    ax10.plot(x, genlogistic.pdf(x, c[10], loc[10], scale[10]))
    ax10.tick_params(labelsize=8)

    ax11.plot(x, genlogistic.pdf(x, c[11], loc[11], scale[11]))
    ax11.tick_params(labelsize=8)

    ax12.plot(x, genlogistic.pdf(x, c[12], loc[12], scale[12]))
    ax12.set_ylabel("12:00", fontsize=8)
    ax12.tick_params(labelsize=8)

    ax13.plot(x, genlogistic.pdf(x, c[13], loc[13], scale[13]))
    ax13.tick_params(labelsize=8)

    ax14.plot(x, genlogistic.pdf(x, c[14], loc[14], scale[14]))
    ax14.tick_params(labelsize=8)

    ax15.plot(x, genlogistic.pdf(x, c[15], loc[15], scale[15]))
    ax15.tick_params(labelsize=8)

    ax16.plot(x, genlogistic.pdf(x, c[16], loc[16], scale[16]))
    ax16.tick_params(labelsize=8)

    ax17.plot(x, genlogistic.pdf(x, c[17], loc[17], scale[17]))
    ax17.tick_params(labelsize=8)

    ax18.plot(x, genlogistic.pdf(x, c[18], loc[18], scale[18]))
    ax18.tick_params(labelsize=8)

    ax19.plot(x, genlogistic.pdf(x, c[19], loc[19], scale[19]))
    ax19.tick_params(labelsize=8)

    ax20.plot(x, genlogistic.pdf(x, c[20], loc[20], scale[20]))
    ax20.tick_params(labelsize=8)

    ax21.plot(x, genlogistic.pdf(x, c[21], loc[21], scale[21]))
    ax21.tick_params(labelsize=8)

    ax22.plot(x, genlogistic.pdf(x, c[22], loc[22], scale[22]))
    ax22.tick_params(labelsize=8)

    ax23.plot(x, genlogistic.pdf(x, c[23], loc[23], scale[23]))
    ax23.set_ylabel("23:00", fontsize=8)
    ax23.tick_params(labelsize=8)
    ax23.set_xlabel("Potencia(MW)")

    plt.show()
    return 'Grafica de densidad de probabilidad'


def probabilidad(df_consumo, t1, t2, p1, p2):
    """Función de probabilidad.

    Esta función es capaz de encontrar la probabilidad de ocurrencia de un
    valor p1 < P < p2 en el tiempo t1 < t < t2 de la
    secuencia aleatoria P(t)

    Parameters
    ----------
    df_consumo : dataframe
        Dataframe con los datos de consumo
    t1 : int
        Primer hora
    t2 : int
        Segunda hora
    p1 : int
        Primer potencia
    p2 : int
        Segunda potencia

    Returns
    -------
    prob_Total : float
        Probabilidad de las 2 horas y 2 potencias.
    """
    # Vectores de los parámetros de la función de distribución
    c = []
    loc = []
    scale = []

    # Método para almacenar datos
    datos_hora = []
    for hora in range(0, 24):
        cada_hora = []
        while hora < len(df_consumo.axes[0]):
            cada_hora.append((df_consumo['MW'][hora]))
            hora = hora + 24
        datos_hora.append(cada_hora)

    # Método para obtener los parámetros
    for i in range(0, 24):
        # Selección del modelo.
        modelo = 'genlogistic'

        # Parametros para la hora especifica.
        mejorAjuste_Horas = Fitter(datos_hora[i], distributions=[modelo])
        mejorAjuste_Horas.fit()

        # Parametros de la distribucion.
        params = mejorAjuste_Horas.fitted_param

        # Guardar los datosen los arreglos, su posicion indica su hora.
        c.append(params[modelo][0])
        loc.append(params[modelo][1])
        scale.append(params[modelo][2])

    # Método para encontrar probabilidad
    prob_t = []
    for i in range(t1, t2+1):
        prob_t.append(genlogistic.cdf(
            p2, c[i], loc[i], scale[i]) - genlogistic.cdf(
                p1, c[i], loc[i], scale[i]))
    # Operación de la suma entre la cantidad de horas del intervalo
    prob_Total = sum(prob_t)/len(prob_t)

    return prob_Total
