from limpieza import limpiarDatos
import csv

def validarDatos():

    datos = limpiarDatos()
    rechazos = []
    validas = []
    for n, fila in enumerate(datos):
        try:
            limpia = limpiarDatos(fila)
        except (ValueError, KeyError) as e:
            rechazos.append({"linea": n,
                            "motivo": str(e)})
            continue
        validas.append(limpia)

    return {"rechazos": rechazos, "validas": validas}

def crearLimpio(validas):
    with open("limpio.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=validas[0].keys())
        writer.writeheader()
        writer.writerows(validas)

def crearErrores(rechazos):
    with open("errores.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rechazos[0].keys())
        writer.writeheader()
        writer.writerows(rechazos)