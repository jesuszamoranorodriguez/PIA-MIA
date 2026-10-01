# E1.1 · Conversor de unidades: pide grados Celsius y muestra
# Fahrenheit y Kelvin con 2 decimales.

gradosC = int(input("Introduzca el valor de grados a transformar:"))

gradosF = (gradosC * 1.8) + 32

gradosK = gradosC + 273.15

print(f"Usted ha introducido {gradosC} la conversión es la siguiente:")
print(f"Fahrenteit = {gradosF}")
print(f"Kelvin = {gradosK}")