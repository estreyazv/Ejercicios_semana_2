import random,string

def crear_contraseña(longitud_contraseña):
    caracteres = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
    contraseña = []

    for i in range(longitud_contraseña):
        aleatorio = random.choice(caracteres)
        contraseña.append(aleatorio)
        final = ''.join(contraseña)
    return final


longitud_contraseña = int(input('Escribe la longitud de contraseña deseada: '))
prueba = crear_contraseña(longitud_contraseña)
print(prueba)