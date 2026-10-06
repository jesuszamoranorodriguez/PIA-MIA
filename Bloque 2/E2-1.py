# E2.1 · Estadísticas de una lista de notas: media, máximo, mínimo y cuántas aprobadas, sin usar statistics.

notasAlumnado = [7, 8, 3, 9, 1, 5, 4]


def sacarNotaMedia():
    notaMedia = 0
    for i in range(0, len(notasAlumnado)):
        notaMedia += notasAlumnado[i]
    notaMedia = notaMedia / len(notasAlumnado)
    return notaMedia

def notaMayor():
    notasAlumnado.sort()
    return notasAlumnado[-1]

def notaMenor(): 
    notasAlumnado.sort()
    return notasAlumnado[0]

def calcularAprobados():
    aprobado = 0
    for i in notasAlumnado:
        if(i >= 5):
            aprobado +=1
    return aprobado

print(f"El numero de aprobados es: {calcularAprobados()}")

print(f"La nota mayor es: {notaMayor()}")

print(f"La nota menor es: {notaMenor()}")

print(f"La nota media es: {sacarNotaMedia():.2f}")

