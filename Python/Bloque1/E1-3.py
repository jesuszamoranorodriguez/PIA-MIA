# Tabla de multiplicar con formato alineado usando f-strings.

for i in range(1, 11):
    print(f"Tabla del {i}:")
    for n in range(11):
        print(f"{i} x {n} = {i*n}")
    i +=1

     