import numpy as np

# Transforma el siguiente array en 8 bits sin signo y muestra cuánto ocupa en memoria
a = np.array([1, -2, 3])
a = a.astype(np.uint8)
print(a, a.nbytes)

# Transforma el siguiente array en 8 bits sin signo y muestra cuánto ocupa en memoria
b = np.array([1, 254, 255])
b = b.astype(np.uint8)
print(b, b.nbytes)

# Transforma el siguiente array en 8 bits con signo y muestra cuánto ocupa en memoria
b = np.array([1, 127, 128])
b = b.astype(np.int8)
print(b, b.nbytes)

# Transforma el siguiente array en 8 bits con signo y muestra cuánto ocupa en memoria
b = np.array([1, -128, -129])
b = b.astype(np.int8)
print(b, b.nbytes)

# Transforma el siguiente array en float32 y muestra cuánto ocupa en memoria

b = np.array([1, 2, 3])
b = b.astype(np.float32)
print(b, b.nbytes)

# Transforma el siguiente array en int32 y muestra cuánto ocupa en memoria
b = np.array([1.9, 2.01, 3.51])
b = b.astype(np.int32)
print(b, b.nbytes)
