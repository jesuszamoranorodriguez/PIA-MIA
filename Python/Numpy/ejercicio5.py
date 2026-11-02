import numpy as np
from sklearn.datasets import load_iris

datos = load_iris().data
resultado = load_iris().target

# Crea un array llamado sepal_length con las 99 primeras filas y la 1º columna de la matriz datos
sepal_length = datos[:99, 0]
# Crea un array llamado petal_length con las 99 primeras filas y la 3º columna de la matriz datos
petal_length = datos[:99, 2]

# Crea un array llamado x juntando las 2 columnas sepal_length y petal_length

x = np.column_stack((sepal_length, petal_length))
print(x)

# Crea un array llamado y con las 99 primeras filas del vector resultado
y = resultado[:99]
print(y)

# Crea un array llamado x con las 99 primeras filas , la 1º columna y la 3º columna de la matriz datos.

x = datos[:99, [0, 2]]
print(x)
