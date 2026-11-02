import numpy as np

# Crea una función llamada mostrar_tamanyo que le pasemos un array de numpy y nos imprima el tamaño de cada una de las dimensiones. 
def mostrar_tamanyo(array):
    for i in range(array.ndim):
        print("El nº de elementos de la dimension", i, "es", array.shape[i])


a = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
b = np.array([[2, 3], [5, 7], [11, 13], [17, 19], [23, 29], [31, 37]])
c = np.array([[[2, 3], [5, 7]], [[11, 13], [17, 19]], [[23, 29], [31, 37]]])

mostrar_tamanyo(a)
print()
mostrar_tamanyo(b)
print()
mostrar_tamanyo(c)
