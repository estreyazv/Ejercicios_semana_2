alumnos_notas = []

def introducir_notas():
    '''Función que permite introducir las notas de cada alumno'''
    datos_alumno = []
    nombre_alumno = input('Escribe el nombre del alumno: ')
    datos_alumno.append(nombre_alumno.upper())
    notas = []
    pregunta = input('Quieres introducir alguna nota? (si/no) ')
    while pregunta != 'no':
        nota = float(input('Escribe una nota: '))
        notas.append(nota)
        pregunta = input('Quieres introducir alguna otra nota? (si/no) ')
    datos_alumno.append(notas)
    alumnos_notas.append(datos_alumno)

def mostrar_notas():
    '''Función que muestra las notas de un alumno'''
    nombre_alumno = input('Escribe el nombre del alumno: ')
    nombre_alumno = nombre_alumno.upper()

    for elemento in alumnos_notas:
        if elemento[0] == nombre_alumno:
            print(f'Las notas de {nombre_alumno} son las siguientes {elemento[1][0:]}')

def calcular_nota_media ():
    '''Función que calcula la nota media de un alumno'''
    nombre_alumno = input('Escribe el nombre del alumno para calcular la media: ')
    nombre_alumno = nombre_alumno.upper()

    for elemento in alumnos_notas:
        if elemento[0] == nombre_alumno:
            num_elementos = len(elemento)
            suma_notas = sum(elemento[1][0:])
            print(f'Las nota media de {nombre_alumno} es de {suma_notas/num_elementos}')

# Comienzo del programa principal
while True:
    print('Elige una opción: ')
    print('1. Introducir notas de un alumno')
    print('2. Mostrar todos los datos')
    print('3. Mostrar las notas de un alumno')
    print('4. Calcular nota media de un alumno')
    print('5. Terminar proceso')

    opcion = int(input(': '))

    if opcion == 1:
        print(introducir_notas())

    elif opcion == 2:
        print(alumnos_notas)

    elif opcion == 3:
        print(mostrar_notas())

    elif opcion == 4:
        print(calcular_nota_media())

    elif opcion == 5:
        print('Proceso finalizado')
        break

    else:
        print('Escriba una respuesta válida')