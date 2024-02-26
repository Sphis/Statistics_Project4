"""Estacionaridad.

En este modulo se comprueba la estacionaridad de P.
"""
import pandas as pd
import requests
import statistics
import math
import json
from scipy.integrate import simps


def datos_demanda():
    """Lectura de datos.

    Lee los datos de demanda (MW) desde el archivo datos.json,
    y convierte los datos en un DataFrame, además elimina columnas
    inecesarias y separa la fecha y hora en dos columnas para facilitar
    el análisis
    """
    with open('datos.json') as file:
        datos = json.load(file)
    df = pd.json_normalize(datos['data'], max_level=1)
    temp = df["fechaHora"].str.split(" ", n=1, expand=True)
    df.insert(0, 'Hora', temp[1])
    df.insert(0, 'Fecha', temp[0])
    df = df.drop(['fechaHora', 'MW_P'], axis=1)
    return df


def datos_hora(df, time):
    """Obtiene consumo de potencia.

    Obtiene los datos de consumo de potencia de una hora particular
    a lo largo de todos los datos disponibles en el data frame.
    """
    return df[df['Hora'].str.contains(time)]


def correlacion_horas(df, hora_1, hora_2):
    """Calcula autocorrelación.

    Determinar el coeficiente de correlación entre dos horas
    particulares a lo largo de todos los datos disponibles en
    el data frame.
    """
    new_df = pd.DataFrame()
    new_df_a = datos_hora(df, hora_1).reset_index()
    new_df_b = datos_hora(df, hora_2).reset_index()
    new_df['A'] = new_df_a['MW']
    new_df['B'] = new_df_b['MW']
    corr = new_df['A'].corr(new_df['B'])
    return corr


def wss(P_t):
    """Determina si es estacionario.

    Determinar la media y la autocorrelación. Para cada una se calcula
    que los resultados sean constantes entre sí con una tolerancia del
    5%. Si lo anterior es verdadero para ambos dretorna True, en caso
    contrario retorna False. Además imprime un mensaje indicando los
    resultados
    """
    media = []
    auto_corr = []
    for hora in range(24):
        temp = datos_hora(P_t, str(hora))
        media.append(statistics.mean(list(temp['MW'])))
    med = statistics.median(media)
    flag = True
    for i in range(24):
        temp = math.isclose(med, media[i], rel_tol=0.05)
        if not (temp):
            flag = False
    if (flag):
        for hora in range(24):
            auto_corr.append(correlacion_horas(P_t, hora, hora+1))
            med = statistics.median(auto_corr)
        for i in range(24):
            temp = math.isclose(med, auto_corr[i], rel_tol=0.05)
            if (temp):
                flag = False
    if (flag):
        print("P(t) es estacionaria en sentido amplio")
    else:
        print("P(t) no es estacionaria en sentido amplio")
    return flag


def prom_temporal(P, dia):
    """Calcula el promedio temporal.

    Calcula el promedio temporal de P para un día en especifico.
    Para esto calcula el area bajo la curva y la divide entre el periodo.
    """
    valores_dia = []
    ind = P.Fecha.ne(dia).idxmin()
    for i in range(24):
        valores_dia.append(P.loc[ind]['MW'])
        ind += 1
    area_bajo_curva = simps(valores_dia, dx=5)
    prom_temp = area_bajo_curva/24
    print(f"El promedio temporal es {prom_temp}")
    return prom_temp


def ergodicidad(P, dia):
    """Determina si P es ergódico.

    Calcula el promedio temporal y el promedio
    estadístico. Luego confirma si son iguales, con una tolerancia del 5%
    """
    valores_dia = []
    promedios = []
    ind = P.Fecha.ne(dia).idxmin()
    for i in range(24):
        valores_dia.append(P.loc[ind]['MW'])
        ind += 1
    promedios.append(statistics.mean(valores_dia))
    print(f"El promedio estadistico es {promedios[0]}")
    promedios.append(prom_temporal(P, dia))
    flag = math.isclose(promedios[0], promedios[1], rel_tol=0.05)
    if (flag):
        print("P(t) es ergódico")
    else:
        print("P(t) no es ergódico")
    return flag
