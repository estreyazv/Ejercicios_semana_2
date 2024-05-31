# Conversión de grados celsius a fahrenheit y viceversa

while True:
    print('Elige una de las siguientes opciones: ')
    print('1. Realizar la conversión de farhenheit a grados celsius')
    print('2. Realizar la conversión de grados celsius a farhenheit')
    print('3. Finalizar')

    opcion = int(input(': '))
    if opcion == 1:
        grados_far = float(input('Escribe los grados farhenheit: '))
        celsius = (grados_far - 32)/1.8
        print(grados_far, 'grados farhenheit equivalen a', celsius, 'grados celsius')
    elif opcion == 2:
        grados_cels = float(input('Escribe los grados celsius: '))
        far = 9 / 5 * grados_cels + 32
        print(grados_cels, 'grados celsius equivalen a', far, 'grados farhenheit' )
    elif opcion == 3:
        print('Proceso finalizado')
    else:
        print('El valor introducido no es correcto')
