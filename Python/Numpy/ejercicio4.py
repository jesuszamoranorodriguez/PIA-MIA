import numpy as np

# El siguiente array contiene las temperaturas medias que ha hecho en Valencia en cada mes [10.2, 10.7, 13.3, 15.8, 19.3, 23.6, 26, 25.9, 22.8, 19.1, 13.9, 10.8 ]
temperaturas = np.array([10.2, 10.7, 13.3, 15.8, 19.3, 23.6, 26, 25.9, 22.8, 19.1, 13.9, 10.8])

# Muestra las temperaturas cuyo valor sea mayor que 20
print(temperaturas[temperaturas > 20])
# Muestra las temperaturas cuyo valor sea menor que 11
print(temperaturas[temperaturas < 11])
# Muestra las temperaturas cuyo valor sea mayor que 20 o menor que 11
print(temperaturas[(temperaturas > 20) | (temperaturas < 11)])
