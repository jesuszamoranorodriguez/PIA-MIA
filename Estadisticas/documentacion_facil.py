import statistics
from fractions import Fraction
from decimal import Decimal

# ---------------------------------------------------------
# PROMEDIOS Y MEDIDAS DE TENDENCIA CENTRAL
# ---------------------------------------------------------

# mean(data)
# El promedio de toda la vida. 
# Sumas todas las notas o números y lo divides entre cuántos hay.
print("mean:", statistics.mean([1, 2, 3, 4, 4]))

# fmean(data, weights=None)
# Hace lo mismo que el promedio normal, pero es una versión súper rápida.
# Ideal si tienes muchísimos números y tienes prisa.
print("fmean:", statistics.fmean([3.5, 4.0, 5.25]))

# geometric_mean(data)
# Un promedio raro que se usa cuando las cosas crecen multiplicándose.
# Por ejemplo, para calcular cómo crece tu dinero en el banco cada año.
print("geometric_mean:", statistics.geometric_mean([54, 24, 36]))

# harmonic_mean(data, weights=None)
# Otro promedio especial. Su uso más famoso es para calcular velocidades.
# Si vas a 40km/h y vuelves a 60km/h, esto te dice la velocidad media real.
print("harmonic_mean:", statistics.harmonic_mean([40, 60]))

# kde(data, h, kernel='normal', *, cumulative=False)
# Dibuja una línea suave (curva) que adivina la forma de tus datos.
# (Solo en Python 3.13 en adelante).
if hasattr(statistics, 'kde'):
    f_hat = statistics.kde([-2.1, -1.3, -0.4, 1.9, 5.1, 6.2], h=1.5)
    print("kde (evaluado en 0):", f_hat(0))

# kde_random(data, h, kernel='normal', *, seed=None)
# Saca un número al azar guiándose por la forma de esa curva suave que mencionamos arriba.
# (Solo en Python 3.13 en adelante).
if hasattr(statistics, 'kde_random'):
    rand_func = statistics.kde_random([-2.1, -1.3, -0.4, 1.9, 5.1, 6.2], h=1.5, seed=42)
    print("kde_random:", rand_func())

# median(data)
# Si pones todos tus números en fila del más pequeño al más grande...
# La mediana es el que se queda justo en el centro. ¡No se deja engañar por extremos!
print("median:", statistics.median([1, 3, 5, 7]))

# median_low(data)
# Si hay un número par de datos (y por tanto dos en el centro), 
# esta función elige siempre al más pequeño de los dos.
print("median_low:", statistics.median_low([1, 3, 5, 7]))

# median_high(data)
# Lo contrario de la anterior: si hay un número par de datos en el centro,
# se queda con el número más grande de los dos.
print("median_high:", statistics.median_high([1, 3, 5, 7]))

# median_grouped(data, interval=1.0)
# Calcula el centro cuando los números vienen agrupados por bloques o rangos 
# (por ejemplo: edades de 10-20, 20-30).
print("median_grouped:", statistics.median_grouped([52, 52, 53, 54]))

# mode(data)
# El "Rey de la popularidad". Simplemente te dice qué número o cosa se repite más veces.
print("mode:", statistics.mode([1, 1, 2, 3, 3, 3, 3, 4]))

# multimode(data)
# Igual que la moda, pero por si hay un empate en el primer puesto.
# Te devuelve una lista con todos los ganadores.
print("multimode:", statistics.multimode('aabbbc'))

# quantiles(data, *, n=4, method='exclusive')
# Funciona como un cuchillo: corta tus datos ordenados en partes iguales.
# Si n=4, corta los datos en 4 pedazos iguales (los famosos cuartiles).
print("quantiles:", statistics.quantiles([10, 20, 30, 40, 50, 60, 70, 80, 90]))


# ---------------------------------------------------------
# MEDIDAS DE DISPERSIÓN (¿Qué tan esparcidos están los números?)
# ---------------------------------------------------------

# pstdev(data, mu=None)
# Desviación típica. Te dice en promedio qué tan "alejados" están los datos del centro.
# Si el número es pequeño, todos los datos son muy parecidos.
print("pstdev:", statistics.pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))

# pvariance(data, mu=None)
# Varianza. Es pariente cercana de la anterior (literalmente es la de arriba al cuadrado).
# Otra forma de medir si los datos están todos juntos o muy dispersos.
print("pvariance:", statistics.pvariance([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))

# stdev(data, xbar=None)
# Igual que la desviación típica, pero ajustada por si NO tienes todos los datos del mundo,
# sino solo un grupo pequeño (una muestra) para investigar.
print("stdev:", statistics.stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))

# variance(data, xbar=None)
# Lo mismo que la varianza de arriba, pero de nuevo, 
# ajustada para cuando solo tienes una pequeña muestra y no todos los datos.
print("variance:", statistics.variance([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))


# ---------------------------------------------------------
# ESTADÍSTICAS PARA COMPARAR DOS COSAS
# ---------------------------------------------------------

# covariance(x, y)
# Te dice si dos cosas se mueven juntas. 
# Por ejemplo: ¿si sube la temperatura, sube la venta de helados? 
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 2, 3, 1, 2, 3, 1, 2, 3]
print("covariance:", statistics.covariance(x, y))

# correlation(x, y, method='linear')
# Como la covarianza, pero más fácil de leer. Va de -1 a 1.
# 1 = van exactamente de la mano; 0 = no tienen absolutamente nada que ver.
print("correlation:", statistics.correlation([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))

# linear_regression(x, y, proportional=False)
# Si dibujas puntos en un mapa, esto te da la "línea recta perfecta" que los atraviesa.
# Sirve para predecir: "si X vale esto, ¿cuánto valdrá Y?".
slope, intercept = statistics.linear_regression([1, 2, 3, 4, 5], [2, 4, 5, 4, 5])
print(f"linear_regression: inclinación={slope:.2f}, punto de corte={intercept:.2f}")


# ---------------------------------------------------------
# HERRAMIENTAS EXTRAS
# ---------------------------------------------------------

# NormalDist(mu=0.0, sigma=1.0)
# La famosa "Campana de Gauss".
# Útil para calcular probabilidades de cosas muy comunes, como la altura de la gente o notas de exámenes.
dist = statistics.NormalDist(mu=100, sigma=15)
print("NormalDist (probabilidad de que algo sea menor a 115):", dist.cdf(115))