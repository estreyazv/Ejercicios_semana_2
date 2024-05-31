# Ver si dos palabras son anagramas o no

def es_anagrama(palabra_1, palabra_2):
    '''Esta función reordena las palabras y devuelve True o False
    dependiendo de si las dos palabras dadas son anagramas o no'''
    return sorted(palabra_1) == sorted(palabra_2)

palabra_1 = input('Escribe una palabra: ')

palabra_2 = input('Escribe otra palabra: ')

print('Las dos palabras escogidas son anagramas?', es_anagrama(palabra_1,palabra_2))