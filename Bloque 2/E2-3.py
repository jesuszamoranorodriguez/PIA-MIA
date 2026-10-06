# Agenda: diccionario de contactos con alta, baja, búsqueda y listado ordenado, en un bucle de menú.
contactos = {
    "Celia": 697,
    "Jesus": 123,
    "Pepe": 888,
    "Pablo": 909
}

while(True):
    eleccion = int(input("\nSelecciona la opción deseada:\n1.Agregar un contacto\n2.Eliminar un contacto\n3.Buscar un contacto\n4.Listar todos los contactos"))
    
    match eleccion:
        case 1:
            nombreIntroducir = input("Introduzca el nombre del usuario")
            numeroIntroducir = input("Intrudzca el numero del usuario")

            contactos[nombreIntroducir] = numeroIntroducir
        case 2:
            contactoElimninar = input("Introduzca el nombre del contacto a eliminar")

            if contactoElimninar in contactos:
                del contactos[contactoElimninar]
                print("Contacto eliminado correctamente")
            else:
                print("Ha ocurrido un error eliminando el usuario")
        case 3:
            buscarcontacto = input("Introduzca el nombre del contacto a buscar")
            if buscarcontacto in contactos: 
                print(f"El contacto existe! Su nombre es:\n{buscarcontacto}\ny su telefono:\n{contactos.get(buscarcontacto)}")
            else:
                print("No existe dicho contacto")
        case 4: 
            contatosOrdenado = dict(sorted(contactos.items()))
            print(contatosOrdenado)
        case _: 
            print("Muchas gracias por usar el programa")
            break;


