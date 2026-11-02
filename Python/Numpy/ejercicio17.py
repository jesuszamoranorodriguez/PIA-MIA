import matplotlib.pyplot as plt
import numpy as np

# Modifica el código que genera la variable x para que sea un array de numpy y de tipo float. Muestra la imagen
# Modifica el código que genera la variable x para que sean 10 valores entre el [-3,3]. Muestra la imagen
# Modifica el código que genera la variable x para que sean 20 valores entre el [-3,3]. Muestra la imagen
# Modifica el código que genera la variable x para que sean 40 valores entre el [-3,3]. Muestra la imagen
# Modifica el código que genera la variable x para que sean 60 valores entre el [-3,3]. Muestra la imagen
# Modifica el código que genera la variable x para que sean 100 valores entre el [-3,3]. Muestra la imagen


figure = plt.figure(figsize=(8, 8))
axes = figure.add_subplot()
x = np.array([-3, -2, -1, 0, 1, 2, 3], dtype=float)
y = 3*(1 - x)**2 * np.exp(-x**2) - 10*(x/5 - x**3)*np.exp(-x**2) - 1./3*np.exp(-(x + 1)**2)
axes.plot(x, y)
plt.show()

figure = plt.figure(figsize=(8, 8))
axes = figure.add_subplot()
x = np.linspace(-3, 3, 10)
y = 3*(1 - x)**2 * np.exp(-x**2) - 10*(x/5 - x**3)*np.exp(-x**2) - 1./3*np.exp(-(x + 1)**2)
axes.plot(x, y)
plt.show()

figure = plt.figure(figsize=(8, 8))
axes = figure.add_subplot()
x = np.linspace(-3, 3, 20)
y = 3*(1 - x)**2 * np.exp(-x**2) - 10*(x/5 - x**3)*np.exp(-x**2) - 1./3*np.exp(-(x + 1)**2)
axes.plot(x, y)
plt.show()

figure = plt.figure(figsize=(8, 8))
axes = figure.add_subplot()
x = np.linspace(-3, 3, 40)
y = 3*(1 - x)**2 * np.exp(-x**2) - 10*(x/5 - x**3)*np.exp(-x**2) - 1./3*np.exp(-(x + 1)**2)
axes.plot(x, y)
plt.show()

figure = plt.figure(figsize=(8, 8))
axes = figure.add_subplot()
x = np.linspace(-3, 3, 60)
y = 3*(1 - x)**2 * np.exp(-x**2) - 10*(x/5 - x**3)*np.exp(-x**2) - 1./3*np.exp(-(x + 1)**2)
axes.plot(x, y)
plt.show()

figure = plt.figure(figsize=(8, 8))
axes = figure.add_subplot()
x = np.linspace(-3, 3, 100)
y = 3*(1 - x)**2 * np.exp(-x**2) - 10*(x/5 - x**3)*np.exp(-x**2) - 1./3*np.exp(-(x + 1)**2)
axes.plot(x, y)
plt.show()
