import csv
from informe import crearLimpio, crearErrores, validarDatos
from limpieza import limpiarDatos

if __name__ == "__main__":
    resultado = validarDatos()
    crearLimpio(resultado["validas"])
    crearErrores(resultado["rechazos"])