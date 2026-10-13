import csv
from pathlib import Path

def cargarDato():
    RUTA = Path(__file__).parent / "ventas_sucio.csv"
    return RUTA