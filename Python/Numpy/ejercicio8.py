import numpy as np

m = np.array([[1, 4, 6, 5],
              [4, 1, 7, 3],
              [2, 9, 1, 2],
              [6, 3, 1, 1]])

# A todos los elementos de la matriz sumale un 10. Usando las funciones de numpy
print(np.add(m, 10))

# A todos los elementos de la matriz sumale un 10 y divídelos entre 2. Usando las funciones de numpy
print(np.divide(np.add(m, 10), 2))

# A todos los elementos de la matriz sumale un 10. Usando operadores

print(m + 10)
# A todos los elementos de la matriz sumale un 10 y divídelos entre 2. Usando operadores

print((m + 10) / 2)
