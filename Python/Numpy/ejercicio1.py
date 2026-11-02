import numpy as np

# Crea una array de numpy con los siguiente números primos: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
primos = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

# Muestra el último elemento. Y debes hacerlo sin saber su longitud.
print(primos[-1])
# Muestra el 3º elemento
print(primos[2])
# Muestra el último y 3º elemento.
print(primos[[-1, 2]])
# Muestra del 2º al 5º elemento.
print(primos[1:5])
# Muestra el 2° y el 5° elemento
print(primos[[1, 4]])
# Muestra el último y el penúltimo elemento. Y debes hacerlo sin saber su longitud.
print(primos[[-1, -2]])
