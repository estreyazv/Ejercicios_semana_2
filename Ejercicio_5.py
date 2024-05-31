def tareas_pendientes():
    '''Permite introducir una lista de tareas y marcarlas como completadas dejarlas como pendientes'''

    while True:
        print('Elegir una entre las siguientes opciones: ')
        print('a) Agregar tarea')
        print('b) Marcar tarea como completada')
        print('c) Ver tareas Pendientes')
        print('d) Salir')
        opcion = input(': ')

        if opcion == 'a':
            pregunta = 'si'
            tareas_no_completadas = {}
            suma = 0
            while pregunta == 'si':
                suma += 1
                contador = 'tarea_' + str(suma)
                tarea = input('Cuál es la tarea que quieres añadir? ')
                tareas_no_completadas[contador] = tarea
                pregunta = input('Quieres agregar más tareas (si/no)? ')


        elif opcion == 'b':
            pregunta = input('Quieres marcar una tarea como completada (si/no)? ')
            if pregunta == 'si':
                print(tareas_no_completadas)
                clave = input('Escribe qué tarea quieres marcar como completada (ejemplo: tarea_1): ')
                clave.lower()
                tareas_completadas = {}
                if clave in tareas_no_completadas:
                    tareas_completadas[clave] = tareas_no_completadas.pop(clave)
                    print(f'La {clave} ha sido movida a las tareas completadas')
                    print('Tareas completadas', tareas_completadas)

        elif opcion == 'c':
            print('Tareas pendientes: ', tareas_no_completadas)

        elif opcion == 'd':
            print('Proceso finalizado')

        else:
            print('La respuesta introducida no es válida. Elegir una de las opciones: ')



print(tareas_pendientes())