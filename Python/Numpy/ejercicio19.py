import numpy as np

# Tienes los datos de las ventas diarias de una tienda durante un año. Los datos incluyen ventas anormalmente altas debido a días festivos o promociones. 
# El objetivo es limpiar los datos eliminando estos valores atípicos y analizar la tendencia general de ventas.

np.random.seed(0)
sales_data = np.random.normal(500, 50, 365)
sales_data[[50, 120, 180, 250, 300]] = [1500, 1400, 1600, 1700, 1800]

media = np.mean(sales_data)
desviacion = np.std(sales_data)

normales = (sales_data > media - 3 * desviacion) & (sales_data < media + 3 * desviacion)
limpio = sales_data[normales]
print("Atipicos:", sales_data[~normales])
print("Dias que quedan:", len(limpio))

print("Media:", np.mean(limpio))
print("Mediana:", np.median(limpio))
print("Desviacion:", np.std(limpio))

trimestre1 = limpio[0:90]
trimestre2 = limpio[90:180]
trimestre3 = limpio[180:270]
trimestre4 = limpio[270:]
print("Trimestre 1:", trimestre1.sum())
print("Trimestre 2:", trimestre2.sum())
print("Trimestre 3:", trimestre3.sum())
print("Trimestre 4:", trimestre4.sum())

dias = np.arange(365)[normales]
orden = np.argsort(limpio)
print("Dias con menos ventas:", dias[orden[:5]])
print("Ventas:", limpio[orden[:5]])
