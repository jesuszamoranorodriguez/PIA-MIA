import numpy as np

m = np.arange(168).reshape(3, 7, 8)
print(m)

print(m[0, 2:5, 2:6])

print(m[:, 2:5, 2:6])
