# Clasificador de notas: pide una nota, valida el rango 0-10 y
# muestra la calificación.

notaUsuario = int(input("Introduce la nota del usuario:"))

if notaUsuario in range(0, 11):
    print(f"El usuario ha tenido una calificación de: {notaUsuario}")
else:
    print("Se ha introducido un valor fuera de rango")
