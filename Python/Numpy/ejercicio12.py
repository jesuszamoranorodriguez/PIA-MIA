import numpy as np
# Muestra con numpy el número de dimensiones de los siguientes arrays:

a = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
b = np.array([[2, 3], [5, 7], [11, 13], [17, 19], [23, 29], [31, 37]])
c = np.array([[[2, 3], [5, 7]], [[11, 13], [17, 19]], [[23, 29], [31, 37]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
