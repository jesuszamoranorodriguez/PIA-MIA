import numpy as np

# Crea una array de numpy con los siguiente números primos: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 pero que el array sea de tipo "float" de 32 bits.
primos = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], dtype=np.float32)

# Usando la función arange de numpy crea un array con los números del 100 al 200 pero sin incluir el 200. Muestra el resultado.
a = np.arange(100, 200)
print(a)

# Usando la función range estándar de Python crea un array con los números del 100 al 200 pero sin incluir el 200. Muestra el resultado.
b = list(range(100, 200))
print(b)

print(type(a))
print(type(range(100, 200)))

# ¿Qué diferencia hay con arange?
# El arange devuelve un array de numpy y range un objeto range de python que hay que pasar a lista
