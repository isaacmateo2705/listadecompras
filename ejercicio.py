# Ingrese una lista de compras: manzanas, plátanos, leche, pan
# Los productos en la lista de compras son: ['manzanas', 'plátanos', 'leche', 'pan']

compras = input("Ingrese una lista de compras: ")
productos = compras.split(", ")
print(f"Los productos en la lista de compras son: {productos}")

# Convertir la lista de compras en una tupla
def convertir_lista_a_tupla(lista):
    return tuple(productos)
delista_tupla=convertir_lista_a_tupla(productos)
print(f'Los productos en la lista d ecompras son:{delista_tupla}')
print(type(productos))
print(type(delista_tupla))