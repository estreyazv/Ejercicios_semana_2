def descuento_compra():
    '''Aplica un descuento X sobre el artículo comprado'''
    descuento = float(input('Escribe el porcentaje de descuento que quieres aplicar (sólo el número): '))
    
    descuento = 1-(descuento/100)
    
    print(f'El {articulo} que compraste tendría un nuevo precio que se quedaría en {precio_original*descuento} euros aplicando el descuento')

# Comienzo del programa principal
# Pedir datos al usuario

compra = {}

articulo = input('Qué artículo compraste? ')

precio_original = float(input('Cuánto te costó? '))
print(descuento_compra())