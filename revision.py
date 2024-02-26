from proceso import proceso, momentos, estacionaridad, espectro

# SECCIÓN A: Función de densidad de probabilidad

# 0. Datos de demanda de potencia
A0 = proceso.demanda()
print(A0)

# 1. Función de densidad del proceso aleatorio
A1 = proceso.densidad(A0)
print(A1)

# 2. Gráfica de la secuencia aleatoria
A2 = proceso.grafica(A0)
print(A2)

# 3. Probabilidad de tener un consumo p1 < P < p2 en t1 < T < t2
A3 = proceso.probabilidad(A0, 0, 4, 1000, 1200)
print("La probabilidad de consumo de entre 1000 y 1200 MW entre las 00:00 y las 04:00 horas es de:", A3)

# SECCIÓN B: Momentos
# 4. Autocorrelación
B4 = momentos.autocorrelacion(A0, 1, 14)

# 5. Autocovarianza
B5 = momentos.autocovarianza(A0, 1, 4)

# SECCIÓN C: Estacionaridad

# Lectura de datos
df_full = estacionaridad.datos_demanda()

# 6. Estacionaridad en sentido amplio
C6 = estacionaridad.wss(df_full)
print(C6)

# 7. Promedio temporal
C7 = estacionaridad.prom_temporal(df_full, '2019-01-01')
print(C7)

# 8. Ergodicidad
C8 = estacionaridad.ergodicidad(df_full, '2019-01-01')
print(C8)

# SECCIÓN D: Características espectrales

# 9. Función de densidad espectral de potencia
D9 = espectro.psd(A0, 2)
