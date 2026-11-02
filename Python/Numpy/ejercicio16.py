import numpy as np
from sklearn.datasets import load_iris

# En ejercicios anteriores obtuviste para el problema de las flores, una matriz x y un vector y.

datos = load_iris().data
resultado = load_iris().target

x = datos[:99, [0, 2]]
y = resultado[:99]

nueva = np.column_stack((x, y))
print(nueva)
