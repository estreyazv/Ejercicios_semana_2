# Programa que sirve para calcular el índice de masa corporal

peso = float(input('Escribe tu peso en kg: '))
altura = float(input('Escribe tu altura en metros: '))

imc = round(peso / (altura * altura),2)
print(f'Su índice de masa corporal es de {imc}')

# Los valores estándar han sido cogidos de internet
if imc <= 18.8:
    print('Peso Insuficiente:'
        'peso por debajo del rango recomendado')
elif 18.5 < imc < 24.9:
    print('Peso Normal o Saludable')
elif 25.0 < imc < 29.9:
    print('Sobrepeso')
else:
    print('Obesidad')