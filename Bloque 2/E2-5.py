# Normaliza una lista de valores al rango 0-1 con una sola comprensión.
valores = [12, 7, 30, 18]
 
lo, hi = min(valores), max(valores)
 
norm = [... for v in valores]
