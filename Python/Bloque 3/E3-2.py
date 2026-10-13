# E3.2 · Carga iris.csv con DictReader, convierte las medidas a float y calcula la media por clase.

import csv
from pathlib import Path
 
RUTA = Path(__file__).parent.parent / "datos" / "iris.csv"
 
with open(RUTA, newline="") as f:
    filas = list(csv.DictReader(f))


for fila in filas:
    print(fila)
    fila["largo_pet"] = float(fila["largo_pet"])
    fila["ancho_pet"] = float(fila["ancho_pet"])
    fila["largo_sep"] = float(fila["largo_sep"])
    fila["ancho_sep"] = float(fila["ancho_sep"])


clase = set(f["clase"] for f in filas)
for clas in clase:
    largo_sep_setosa = (f["largo_sep"] for f in filas if f["clase"] == clas)

    print(clas)
    print(largo_sep_setosa)

    








    #if "clase" in fila:
        #print(fila["clase"])
        #media_largo_sep_setosa = sum(f["largo_sep"] for f in filas if f["clase"] == "setosa") / len([f for f in filas if f["clase"] == "setosa"])
        
        #print(f"Media largo_sep (setosa): {media_largo_sep_setosa}")

    
