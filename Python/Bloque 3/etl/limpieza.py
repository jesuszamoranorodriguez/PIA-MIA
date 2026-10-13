from carga import cargarDato
import csv

def limpiarDatos():
    with open(cargarDato(), newline="") as f:
        datos = list(csv.DictReader(f))
    return datos