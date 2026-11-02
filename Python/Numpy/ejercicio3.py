import numpy as np

m = np.array([[1, 4, 6, 5],
              [4, 1, 7, 3],
              [2, 9, 1, 2],
              [6, 3, 1, 1]])

# Muestra el elemento de la fila 2º y la columna 3º. Es el valor del 7.
print(m[1, 2])
# Muestra la 3º Fila
print(m[2])
# Muestra la 2º Columna
print(m[:, 1])
# Muestra la 2º y 3º Columna
print(m[:, 1:3])
# Muestra la 2º y 3º Fila
print(m[1:3])
# Muestra la última columna. Debe funcionar independientemente del número de columnas.
print(m[:, -1])
# Muestra la 2º y 4º Columna y la 1º y 3º fila
print(m[[0, 2]][:, [1, 3]])
# Muestra de la 2º a la 3º Columna y de la 1º a la 3º fila
print(m[0:3, 1:3])
# Muestra todas las columnas excepto la primera y la última. Debe funcionar independientemente del número de columnas.
print(m[:, 1:-1])
# Muestra todas las filas excepto la primera y la última. Debe funcionar independientemente del número de filas.
print(m[1:-1])
# Muestra todas las columnas excepto la primera y la última y todas las filas excepto la primera y la última. Debe funcionar independientemente del número de filas y columnas
print(m[1:-1, 1:-1])

# Imprime la matriz y haz que las cabeceras de cada columna sean A, B , C y D
print("A B C D")
for fila in m:
    print(fila[0], fila[1], fila[2], fila[3])
