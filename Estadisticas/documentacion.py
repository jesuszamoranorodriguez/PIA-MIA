import statistics
from fractions import Fraction
from decimal import Decimal

# ---------------------------------------------------------
# PROMEDIOS Y MEDIDAS DE TENDENCIA CENTRAL
# ---------------------------------------------------------

# mean(data)
# Devuelve la media aritmética de los datos (promedio).
# Es la suma de los valores dividida entre el número de observaciones.
print("mean:", statistics.mean([1, 2, 3, 4, 4]))

# fmean(data, weights=None)
# Convierte los valores a flotantes y calcula la media aritmética rápidamente.
# Opcionalmente soporta pesos para calcular una media ponderada.
print("fmean:", statistics.fmean([3.5, 4.0, 5.25]))

# geometric_mean(data)
# Calcula la media geométrica de los datos.
# Utiliza el producto de los valores para indicar la tendencia central.
print("geometric_mean:", statistics.geometric_mean([54, 24, 36]))

# harmonic_mean(data, weights=None)
# Devuelve la media armónica de los datos, útil para promediar tasas o velocidades.
# Es el recíproco de la media aritmética de los recíprocos de los datos.
print("harmonic_mean:", statistics.harmonic_mean([40, 60]))

# kde(data, h, kernel='normal', *, cumulative=False)
# Estima la función de densidad de probabilidad continua a partir de una muestra discreta.
# (Disponible a partir de Python 3.13)
if hasattr(statistics, 'kde'):
    f_hat = statistics.kde([-2.1, -1.3, -0.4, 1.9, 5.1, 6.2], h=1.5)
    print("kde (evaluado en 0):", f_hat(0))

# kde_random(data, h, kernel='normal', *, seed=None)
# Retorna una función para seleccionar un valor aleatorio basado en la densidad de probabilidad de kde().
# (Disponible a partir de Python 3.13)
if hasattr(statistics, 'kde_random'):
    rand_func = statistics.kde_random([-2.1, -1.3, -0.4, 1.9, 5.1, 6.2], h=1.5, seed=42)
    print("kde_random:", rand_func())

# median(data)
# Devuelve la mediana o valor central de los datos.
# Si hay un número par de elementos, promedia los dos valores centrales.
print("median:", statistics.median([1, 3, 5, 7]))

# median_low(data)
# Devuelve la mediana baja de los datos numéricos.
# En un número par de elementos, devuelve el menor de los dos centrales.
print("median_low:", statistics.median_low([1, 3, 5, 7]))

# median_high(data)
# Devuelve la mediana alta de los datos numéricos.
# En un número par de elementos, devuelve el mayor de los dos centrales.
print("median_high:", statistics.median_high([1, 3, 5, 7]))

# median_grouped(data, interval=1.0)
# Calcula la mediana de datos agrupados o continuos, estimando el percentil 50.
# Útil cuando los datos están agrupados en rangos.
print("median_grouped:", statistics.median_grouped([52, 52, 53, 54]))

# mode(data)
# Devuelve la moda, que es el valor más común de datos discretos o nominales.
# Si hay varios valores igual de comunes, devuelve el primero encontrado.
print("mode:", statistics.mode([1, 1, 2, 3, 3, 3, 3, 4]))

# multimode(data)
# Retorna una lista con las modas (valores más comunes) de los datos.
# Retornará varios elementos si hay empate en la frecuencia máxima.
print("multimode:", statistics.multimode('aabbbc'))

# quantiles(data, *, n=4, method='exclusive')
# Divide los datos en 'n' intervalos continuos equiprobables.
# Retorna 'n - 1' puntos de corte (por defecto, cuartiles).
print("quantiles:", statistics.quantiles([105, 129, 87, 86, 111, 111, 89, 81, 108, 92, 110, 100, 75, 105, 103, 109, 76, 119, 99, 91, 103, 129, 106, 101, 84, 111, 74, 87, 86, 103, 103, 106, 86, 111, 75, 87, 102, 121, 111, 88, 89, 101, 106, 95, 103, 107, 101, 81, 109, 104]))

# ---------------------------------------------------------
# MEDIDAS DE DISPERSIÓN
# ---------------------------------------------------------

# pstdev(data, mu=None)
# Calcula la desviación típica poblacional de los datos.
# Es la raíz cuadrada de la varianza poblacional.
print("pstdev:", statistics.pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))

# pvariance(data, mu=None)
# Calcula la varianza poblacional de los datos.
# Mide la variabilidad exacta considerando los datos como la población total.
print("pvariance:", statistics.pvariance([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))

# stdev(data, xbar=None)
# Calcula la desviación típica muestral de los datos.
# Usado cuando los datos representan una muestra y no la población entera.
print("stdev:", statistics.stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))

# variance(data, xbar=None)
# Calcula la varianza muestral de los datos.
# Ayuda a estimar la varianza de la población a partir de una muestra.
print("variance:", statistics.variance([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))

# ---------------------------------------------------------
# ESTADÍSTICAS PARA RELACIONES ENTRE DOS ENTRADAS
# ---------------------------------------------------------

# covariance(x, y)
# Calcula la covarianza muestral de dos variables (x e y).
# Mide la tendencia de dos variables a variar juntas.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 2, 3, 1, 2, 3, 1, 2, 3]
print("covariance:", statistics.covariance(x, y))

# correlation(x, y, method='linear')
# Calcula el coeficiente de correlación de Pearson o Spearman para dos entradas.
# Indica el grado de asociación lineal o de rango entre x e y.
print("correlation:", statistics.correlation([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))

# linear_regression(x, y, proportional=False)
# Devuelve la pendiente (slope) e intersección (intercept) para regresión lineal simple.
# Útil para estimar la mejor línea recta que se ajusta a los puntos (x, y).
slope, intercept = statistics.linear_regression([1, 2, 3, 4, 5], [2, 4, 5, 4, 5])
print(f"linear_regression: slope={slope:.2f}, intercept={intercept:.2f}")

# ---------------------------------------------------------
# OBJETOS ADICIONALES
# ---------------------------------------------------------

# NormalDist(mu=0.0, sigma=1.0)
# Objeto para crear y manipular distribuciones normales de una variable aleatoria.
# Permite operaciones como calcular probabilidades y generar muestras.
dist = statistics.NormalDist(mu=100, sigma=15)
print("NormalDist (probabilidad X < 115):", dist.cdf(115))