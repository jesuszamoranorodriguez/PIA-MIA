# E3.2
import csv
from pathlib import Path
 
RUTA = Path(__file__).parent.parent / "datos" / "iris.csv"
MEDIDA = {'largo_sep','ancho_sep','largo_pet','ancho_pet'}

def obtener_media_columna(filas, columna):

    valores =  {}

    for fila in filas: 
        clase = fila["clase"]

        if clase not in valores:
            valores[clase]=[]
        valores[clase].append(fila[columna])

    resultados= {}
    for clase, v in valores.items():
        resultados[clase]=(sum(v)/len(v),2)

with open(RUTA, newline="") as f:
    filas = list(csv.DictReader(f))

# CONVERSION
for fila in filas:
    for medida in MEDIDA:
        fila[medida]=float(fila[medida])

for medida in MEDIDA:
    obtener_media_columna(filas, medida)
    print(obtener_media_columna(filas, medida))

