from persona import persona
misContactos = [persona(123,'Luis', 'casa 1'), persona(321, 'Julio', 'Casa 2')]

def crearContacto(numero, nombre, direccion):
    misContactos.append(persona(numero, nombre, direccion))
    print("Contacto almacenado...")

def buscarContacto(nombre):
    if len(misContactos) == 0:
        print("La lista esta vacía, no hay contactos que buscar...")
    else:
        encontrado = False
        for i in range(len(misContactos)):
            if misContactos[i].verNombre() == nombre:
                print("EL teléfono es ", misContactos[i].verNumero())
                print("La dirección es ", misContactos[i].verDireccion())
                encontrado = True
                break
            else:
                encontrado = False
        if encontrado == False:
            print("Dato no existente...")

def mostrarContactos():
    if len(misContactos) == 0:
        print("La lista esta vacía, no hay contactos que buscar...")
    else:
        for i in range(len(misContactos)):
            print('Nombre: ', misContactos[i].verNombre(), ' Dirección', misContactos[i].verDireccion(), ' Teléfono', misContactos[i].verNumero())

def modificarContacto(nombre):
    if len(misContactos) == 0:
        print("La lista esta vacía, no hay contactos que buscar...")
    else:
        encontrado = False
        posicion = None
        for i in range(len(misContactos)):
            if misContactos[i].verNombre() == nombre:
                posicion = i
                encontrado = True
                break
            else:
                encontrado = False
        if encontrado:
            nuevoNumero = int(input("Ingrese el nuevo número: "))
            nuevoNombre = input("Ingrese nuevo nombre: ")
            nuevaDireccion = input("Ingrese la nueva dirección: ")
            misContactos[posicion].modificarNumero(nuevoNumero)
            misContactos[posicion].modificarNombre(nuevoNombre)
            misContactos[posicion].modificarDireccion(nuevaDireccion)
            print("Datos actualizados con éxito...")
        else:
            print("Dato no encontrado...")

def main():
    op = 0
    while op != 7:
        print("--------------------AGENDA 2022-----------------------")
        print("1. Crear contacto")
        print("2. Buscar contacto")
        print("3. Ver contactos")
        print("4. Modificar contacto")
        print("5. Eliminar contacto")
        print("6. Crear reporte en HTML")
        print("7. Salir del programa\n\n")
        op = int(input("Ingrese el número de opción: "))
        if op == 1:
            numero = int(input("Ingrese el número de teléfono: "))
            nombre = input("Ingrese el nombre: ")
            direccion = input("Ingrese la dirección: ")
            crearContacto(numero, nombre, direccion)
        elif op == 2:
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            buscarContacto(nombre)
        elif op == 3:
            mostrarContactos()
        elif op == 4:
            nombre = input("Ingrese el nombre del contacto: ")
            modificarContacto(nombre)

#iniciar programa
main()