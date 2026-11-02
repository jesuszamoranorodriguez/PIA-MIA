import numpy as np

# 
def imprimir_datos(matriz):
    x = matriz[:, :-1]
    y = matriz[:, -1]

    print("Caracteristicas de cada vino:", x.shape[1])
    print("Muestras de vino:", matriz.shape[0])

    tipos = np.unique(y)
    print("Tipos de vino:", len(tipos), tipos)

    print("Maximos:", x.max(axis=0))
    print("Minimos:", x.min(axis=0))

    return x, y


datos = np.loadtxt("wine.csv", delimiter=",")
x, y = imprimir_datos(datos)
print(x)
print(y)
