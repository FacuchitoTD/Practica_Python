herramientas = []
existencias = []

cantidad = input('Ingrese la cantidad de herramientas a cargar por favor: ')
while not cantidad.isdigit():
    print('Debe escribir un número')
    cantidad = input('Ingrese nuevamente la cantidad de herramientas a cargar: ')
cantidad = int(cantidad)

var_apoyo = 0

while var_apoyo < cantidad:
    nombre_herramienta = input(f'Ingrese el nombre de la herramienta {var_apoyo + 1} por favor: ')
    if nombre_herramienta == '':
        print('Debe ingresar algún nombre de una herramienta')
    elif nombre_herramienta in herramientas:
        print('El nombre de esa herramienta está duplicado')
    else:
        herramientas.append (nombre_herramienta)
        var_apoyo +=1

print('\n----Ingrese la cantidad de stock de cada herramienta----')
for i in range(cantidad):
    print(f'Herramientas: {herramientas[i]}')
    cantidad_unidades = input(f'Ingrese la cantidad de unidades: ')
    while not cantidad_unidades.isdigit():
        print('Debe ingresar un número válido.')
        cantidad_unidades = input (f'Ingrese nuevamente la cantidad de unidades: ')
    
    existencias.append(int(cantidad_unidades))

print('\n---- Resumen de herramientas cargadas ----')
for i in range(cantidad):
    print(f'{herramientas[i]}: {existencias[i]} unidades')
