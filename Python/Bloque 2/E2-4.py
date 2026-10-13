# Frecuencia de caracteres de un texto: normaliza, separa y cuenta; muestra el top 5.


SIGNOS = ".,:;!?¡¿()\"'"

def contar_palabras(texto: str) -> dict[str, int]:

    limpio = texto.lower()
    for s in SIGNOS:        
        limpio = limpio.replace(s, "")

    frecuencia = {}
    for c in limpio:
        frecuencia[c] = frecuencia.get(c, 0) + 1

    return frecuencia

print(contar_palabras("HOLA ALBERTO!!"))