# Frecuencia de palabras de un texto: normaliza, separa y cuenta; muestra el top 5.

SIGNOS = ".,:;!?¡¿()\"'"

def contar_palabras(texto: str) -> dict[str, int]:

    limpio = texto.lower()
    for s in SIGNOS:        
        limpio = limpio.replace(s, " ")

    return limpio


print(contar_palabras("HOLA ALBERTO!!"))