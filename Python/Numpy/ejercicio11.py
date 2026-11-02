import numpy as np

# Crea una función llamada f que acepte como parámetro el número y que retorne lo siguiente:

def f(numero):
    if numero <= 3:
        return 0
    elif numero <= 5:
        return 4
    elif numero <= 6:
        return 5
    elif numero <= 7:
        return 6
    elif numero <= 9:
        return 8
    else:
        return 10

# Crea ahora el vector de numpy [1,5,4,7,3,9,8,6] y aplícale la función f

v = np.array([1, 5, 4, 7, 3, 9, 8, 6])
f_vector = np.vectorize(f)
print(f_vector(v))
