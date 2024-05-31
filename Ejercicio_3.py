lista_contactos = []

def crear_contacto():
    usuario = {}
    usuario['nombre'] = input('Escribe el nombre del contacto: ')
    usuario['telefono'] = int(input('Escribe el número de teléfono del contacto: '))
    usuario['email'] = input('Escribe el email del contacto: ')
    return usuario

def consultar_contacto():
    print('Escoge una opción ')
    print('1. Consultar un teléfono')
    print('2. Consultar un email')

    consulta = int(input(': '))

    nombre = input('Escribe el nombre del usuario cuyos datos quieres consultar: ')
    nombre = nombre.lower()

    if consulta == 1:
        for elemento in lista_contactos:
            if nombre in elemento.values():
                print('El teléfono del usuario consultado es: ', elemento['telefono'])
    elif consulta == 2:
        for elemento in lista_contactos:
            if nombre in elemento.values():
                print('El email del usuario consultado es: ', elemento['email'])
    else:
        print('El usuario escrito no se encuentra en la agenda')


# Comienzo del programa principal
while True:
    print('Elige una opción: ')
    print('1. Crear un contacto nuevo')
    print('2. Mostrar la agenda entera')
    print('3. Consultar un contacto en la agenda')
    print('4. Terminar proceso')

    opcion = int(input(': '))

    if opcion == 1:
        usuario = crear_contacto()
        lista_contactos.append(usuario)

    elif opcion == 2:
        print(lista_contactos)

    elif opcion == 3:
        print(consultar_contacto())

    elif opcion == 4:
        print('Proceso finalizado')
        break
    else:
        print('Escriba una respuesta válida')
