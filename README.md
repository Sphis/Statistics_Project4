### Universidad de Costa Rica
#### IE0405 - Modelos Probabilísticos de Señales y Sistemas
##### Proyecto 4: Procesos aleatorios (segundo ciclo del 2022)

- Kevin Delgado Rojas, B82566
- Kevin Campos Castro, B91519
- Christabel Alvarado Anchía, B80286

# Paquete `proceso`

> Este paquete analiza la secuencia aleatoria $P(t)$ de consumo de potencia diaria, en cuatro secciones distintas. Las funciones de estas secciones se explican en detalle a continuación. Está diseñado para utilizar los datos guardados en datos.json (Guardado en la misma dirección que el archivo siendo ejecutado).

## Funciones

### densidad(df_consumo)
Esta función es capaz de encontrar la función de densidad de probabilidad de la secuencia aleatoria $P(t)$. La función se encarga de encontrar los parámetros $c$ , $loc$, $scale$, que conforman la función de densidad utilizada, la cual es *genlogistic*. Recibe como parámetro un DataFrame, y la función internamente tiene varios métodos de análisis para retornar los valores esperados de $c$ , $loc$, $scale$.

### grafica(df_consumo)
Esta función es capaz de graficar la función de densidad de probabilidad de la secuencia aleatoria $P(t)$. La función se encarga de mostrar el comportamiento o evolución en el tiempo desde las 00:00 horas hasta las 23:00 horas. Recibe como parámetro un DataFrame, y la función calcula los valores de $c$ , $loc$, $scale$ para cada una de las 24 horas del día, y por último se muestra la gráfica del comportamiento de la potencia respecto al tiempo. 

### probabilidad(df_consumo, t1, t2, p1, p2)
Esta función es capaz de encontrar la probabilidad de ocurrencia de un valor $p_1$ < $P$ < $p_2$ en el tiempo $t_1$ < $t$ < $t_2$ de la secuencia aleatoria $P(t)$. Recibe como parámetros un DataFrame, un intervalo de las horas y potencias de consumo que se desea analizar. Y por último, muestra la probabilidad de ocurrencia deseada.

### autocorrelacion(df_consumo, hora1, hora2)
Para esta asignación se ingresan los datos que se quieren estudiar, en este caso serían 2 horas de interés.
Se utiliza la matriz ‘’datos_hora’’ para tomar las horas particulares del usuario (hora1, hora2) y encontrar la potencia asociada a ese tiempo específico y se guardan en dataframes, luego, se utiliza el método de .corr de pandas para encontrar la correlación entre las dos variables, esto último sería la salida de interés.

### autocovarianza(df_consumo, hora1, hora2)
La función de autocovarianza funciona similar a la anterior. Se toman las dos horas de interés ya ingresadas y por medio de la librería de pandas y se calcula la covarianza entre estos tiempos. La autocovarianza (o el momento conjunto central de orden dos) de un proceso estocástico está definida por la siguiente ecuación:
$$C_{xx}(t,t+\tau) = E[(X(t)-E[X(t)])(X(t+\tau)-E[X(t+\tau)])]$$
Esto es lo mismo que realiza la función .cov de pandas.

### datos_demanda()
Esta función se encarga de leer el archivo .json y crear un dataframe con las características necesarias para ejecutar otras funciones en estacionaridad. No recibe ningún argumento, ya que siempre utiliza datos.json.
Tiene una única salida, el data frame generado.

### datos_hora(df, time)
Obtiene los datos de consumo de potencia de una hora particular a lo largo de todos los datos disponibles en df. Recibe df un data frame que tiene las características del data frame generado por datos_demanda y time la hora que se desea obtener.
Su salida es un data frame formado por los datos de consumo durante time.

### correlacion_horas(df, hora_1, hora_2)
Determinar el coeficiente de correlación entre dos horas particulares a lo largo de todos los datos disponibles en el data frame. Recibe el data frame generado por datos_demanda y las dos horas a comparar. Su salida es el índice de correlación calculado

### wss(P_t)
Determina si P_t es estacionaria en sentido amplio. Imprime un mensaje indicando los resultados. Recibe el data frame generado por datos_demanda. Su salida es una variable booleana, indica verdadero cuando P es estacionaria y falso en caso contrario.

### prom_temporal(P, dia)
Calcula el promedio temporal de P para un día en específico. Imprime un mensaje indicando el promedio temporal calculado. Recibe el data frame generado por datos_demanda (P) y el día que se desea analizar. Su salida es el promedio calculado.

### ergodicidad(P, dia)
Determina si P es ergódico en un día. Imprime un mensaje indicando los resultados. Recibe el data frame generado por datos_demanda (P) y el día que se desea analizar. Su salida es una variable booleana, indica verdadero cuando P es ergódico y falso en caso contrario.

### psd(df_consumo, hora9)
Esta función se encarga de analizar el espectro de densidad de potencia de una hora particular ingresada por el usuario. Esta gráfica va a mostrar el comportamiento de potencia de una señal aleatoria y como se distribuye en todas las frecuencias, en otras palabras es el comportamiento de $P(t)$ en el dominio de la frecuencia. ‘’hora9’’ (tiempo ingresado por el usuario) es la hora de la que se va a extraer los valores de potencia asociado, el segundo parámetro de esta función, ‘’dt’’ indica el valor de la frecuencia de muestreo y ‘’np.arrange()’’ crea un vector de valores del 0 al 365 (se toma 365 por la hora escogida de cada día del año) cada uno espaciado por un parámetro dt.

## Resultados


### Módulo de proceso
Este módulo determina la función densidad de probabilidad de la secuencia aleatoria $P(t)$ , en este caso la función utilizada fue $genlogistic$, la cual tiene como parámetros $c$ , $loc$, $scale$. La función de densidad asociada a esta es:
```math   
f(x, c) =c\cdot \frac{e{(-x)}}{(1+e{-x})^{e+1}}   
```
Al ejecutar la función `demanda(df_consumo)`se obtivieron las funciones del tiempo de los párametros, los cuales son:
 ```math
c(t) = 4.57199340 \cdot 10^{-8} \cdot t^7 -5.00399491 \cdot 10^{-6} \cdot t^6 + 2.09913189 \cdot 10^{-4} \cdot t^5 - 4.32940873 \cdot 10^{-3} \cdot t^4 + 4.60710835 \cdot 10^{-2} \cdot t^3 - 2.33562409 \cdot 10^{-1} \cdot t^2 + 3.68052322 \cdot 10^{-1} \cdot t + 6.52281140 \cdot 10^{-1}  
```  

 ```math
loc(t) = 2.85391745 \cdot 10^{-5} \cdot t^7 -2.39480688 \cdot 10^{-3} \cdot t^6 + 7.39492808 \cdot 10^{-2} \cdot t^5 - 9.84120610 \cdot 10^{-1} \cdot t^4 + 3.91618298 \cdot t^3 - 2.19374917 \cdot 10^{1} \cdot t^2 - 1.03908708 \cdot 10^{2} \cdot t + 1.03447704 \cdot 10^{3}
``` 

 ```math
scale(t) = -1.32009676 \cdot 10^{-6} \cdot t^7 + 7.54402041 \cdot 10^{-5} \cdot t^6 - 1.40668876 \cdot 10^{-3} \cdot t^5 + 6.56674366 \cdot 10^{-3} \cdot t^4 + 7.82871767 \cdot 10^{-2} \cdot t^3 - 8.31609677 \cdot 10^{-1} \cdot t^2 + 1.26876083 \cdot t + 2.33549419 \cdot 10^{1}
``` 

Posteriormente, la función  `grafica(df_consumo)` se encargó de mostrar la evolución con el tiempo de la secuencia aleatoria $P(t)$, la gráfica se muestra a continuación:

![Gráfica de la densidad de probabilidad aleatoria de la secuencia aleatoria](https://github.com/mpss-eie/P4G8/blob/main/Im%C3%A1genes/densidad.png)

Por último, la función `probabilidad(df_consumo, t1, t2, p1, p2)` determina la probabilidad de ocurrencia de un valor 1000 MW < P < 1200MW en el tiempo 0 < t < 4, donde el tiempo está dado en horas, de la secuencia aleatoria $P(t)$. Para encontrar esta probabilidad se hizo uso de la propiedad de probabilidad:

```math
P(x_1 < X < x_2) = CDF(x_2) - CDF(x_1)
```
Entonces se calculó la probabilidad en el intervalo de las horas para ese intervalo de consumo de potencia, dando como resultado que la probalidad de ocurrencia sea de **0.21589043025328863%**

### Módulo de momentos
Este módulo es encargado de determinar la autocorrelación y la autocovarianza, las mismas cuantifican el grado de relación lineal entre un mismo proceso aleatorio en distintos de tiempo (en este caso el valor de t1 y t2 corresponden al valor de hora ingresada por el usuario) y entre dos procesos distintos, es decir, nos permiten conocer que tan relacionadas están los procesos aleatorios estudiados. 

Se obtiene que para la función de autocorrelación con las horas 1:00 y 14:00 una autocorrelación de **0.27159(...)**. Se verificó que el código estuviera correcto ingresando la misma hora $(t_1 = t_2)$, para la cual se espera una autocorrelación de 1 por teoría.
Para la autocovarianza, si se ingresan las horas 1:00 y 4:00, se obtiene una autocovarianza de **1896.106(...)**.

### Módulo espectro
Basado en el método de Welch, la misma es un método para determinar la densidad espectral de potencia, que es una gráfica que muestra como se comporta la potencia de una señal ante diferentes frecuencias. Para esta práctica se estudia la densidad espectral de potencia de las 2:00pm, pero es posible cambiar este valor. El resultado obtenido es el siguiente:
![Gráfica de densidad espectral](https://github.com/mpss-eie/P4G8/blob/main/Im%C3%A1genes/GraficaEspectro.png)

### Módulo estacionaridad
Este módulo se encarga de determinar si $P(t)$ es estacionario en sentido amplio, con una tolerancia del 5%. Para esta función se obtuvo que los datos analizados **no son estacionarios en sentido amplio**, ajustándose a los resultados esperados según las discusiones en clase. 

Luego, también se calcula el promedio temporal durante un día. Para las pruebas en revision.py se calculó el promedio temporal el primero de enero de 2019 y se obtuvo que es **4894.04**. 

Finalmente, se utiliza el promedio temporal y el promedio estadístico para determinar si P es ergódico. Para los datos analizados se obtuvo que P **no es ergódico**.
