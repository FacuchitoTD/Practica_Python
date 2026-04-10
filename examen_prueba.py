herramientas = []
existencias = []

while True:
    print('-----Bienvenido al sistema de inventario de herramientas-----')
    print('''
    Seleccione una opción del siguiente menú:
    1. Cargar herramientas
    2. Cargar stock de herramientas
    3. Mostrar resumen de herramientas cargadas
    4. Buscar herramienta por nombre
    5. Mostrar herramientas con stock agotado
    6. Agregar nueva herramienta al inventario
    7. Actualizar stock (Venta/Ingreso)
    8. salir del programa
    ''')
    opcion = input('Ingrese una opcion: ')
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 8:
        print('Opción no válida. Por favor, ingrese una opción del 1 al 8.')
        opcion = input('Ingrese nuevamente una opción: ')
    opcion = int(opcion)

    match opcion:
        case 1:
            cantidad = input('Ingrese la cantidad de herramientas a cargar por favor: ')
            while not cantidad.isdigit() or int(cantidad) <= 0:
                print('Debe escribir un número válido y positivo')
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
        case 2:
            print('\n----Ingrese la cantidad de stock de cada herramienta----')
            if not herramientas:
                print('No hay herramientas cargadas en el inventario. Por favor, cargue herramientas primero.')
            elif len(existencias) == len(herramientas):
                print('El stock de las herramientas ya ha sido cargado. Si desea actualizar el stock, por favor seleccione la opción 7 del menú.')
            else:
                for i in range(len(existencias), len(herramientas)):
                    print(f'Herramientas: {herramientas[i]}')
                    cantidad_unidades = input(f'Ingrese la cantidad de unidades: ')
                    while not cantidad_unidades.isdigit():
                        print('Debe ingresar un número válido (entero positivo).')
                        cantidad_unidades = input (f'Ingrese nuevamente la cantidad de unidades: ')    
                    existencias.append(int(cantidad_unidades))
        case 3:
            print('\n---- Resumen de herramientas cargadas ----')
            if not herramientas:
                print('No hay herramientas cargadas en el inventario.')
            elif len(existencias) < len(herramientas):
                print('El stock de algunas herramientas no ha sido cargado. Por favor, cargue el stock de todas las herramientas para mostrar el resumen completo.')
            else:
                for i in range(len(herramientas)):
                    print(f'{herramientas[i]}: {existencias[i]} unidades')
        case 4:
            if not herramientas:
                print('No hay herramientas cargadas en el inventario. Por favor, cargue herramientas primero.')
            elif len(existencias) < len(herramientas):
                print('El stock de algunas herramientas no ha sido cargado. Por favor, cargue el stock de todas las herramientas para realizar búsquedas.')
            else:
                herramienta_busqueda = input ('Ingrese el nombre de la herramienta a buscar: ')
                while herramienta_busqueda == '':
                    print('Debe ingresar algún nombre de una herramienta')
                    herramienta_busqueda = input ('Ingrese nuevamente el nombre de la herramienta a buscar: ')
                if herramienta_busqueda in herramientas:
                    index_herramienta = herramientas.index(herramienta_busqueda)
                    print(f'{herramienta_busqueda}: {existencias[index_herramienta]} unidades')
                else:
                    print('La herramienta no se encuentra en el inventario')
            
        case 5:
            print('----- Reporte de Herramientas con Stock Agotado -----')
            if len(herramientas) == 0:
                print('No hay herramientas cargadas en el inventario.')
            elif len(existencias) < len(herramientas):
                print('El stock de algunas herramientas no ha sido cargado.')
            else:
                hay_agotados = False
                for i in range(len(existencias)):
                    if existencias[i] == 0:
                        hay_agotados = True
                        break
                if not hay_agotados:
                    print('No hay herramientas con stock agotado.')
                else:
                    print('Las siguientes herramientas no tienen stock:')
                    for i in range(len(herramientas)):
                        if existencias[i] == 0:
                            print(f'- {herramientas[i]}')
        case 6:
            print('-----Ingreso de nueva herramienta-----')
            nombre_nueva_herramienta = input('Ingrese el nombre de la herramienta a agregar: ')
            if nombre_nueva_herramienta == '':
                print('Debe ingresar algún nombre de una herramienta')
                continue
            elif nombre_nueva_herramienta in herramientas:
                print('El nombre de esa herramienta ya existe en el inventario')
                continue
            elif len(existencias) < len(herramientas):
                print('El stock de algunas herramientas no ha sido cargado. Por favor, cargue el stock de todas las herramientas para agregar una nueva herramienta al inventario.')
                continue
            else:
                herramientas.append(nombre_nueva_herramienta)
                cantidad_unidades = input(f'Ingrese la cantidad de unidades para {nombre_nueva_herramienta}: ')
                if not cantidad_unidades.lstrip('-').isdigit() or int(cantidad_unidades) < 0:
                    print('Debe ingresar un número válido (entero positivo).')
                    herramientas.pop()
                    continue
                cantidad_unidades = int(cantidad_unidades)
                existencias.append(cantidad_unidades)
                print(f'{nombre_nueva_herramienta} ha sido agregada al inventario con {cantidad_unidades} unidades.')
        case 7:
            print('-----Actualización de Stock (Venta / Ingreso)-----')
            if not herramientas:
                print('No hay herramientas cargadas en el inventario.')
                continue
            elif len(existencias) < len(herramientas):
                print('El stock de algunas herramientas no ha sido cargado. Por favor, cargue el stock de todas las herramientas primero.')
                continue
            herramienta_actualizar = input('Ingrese el nombre de la herramienta: ')
            while herramienta_actualizar == '':
                print('Debe ingresar algún nombre de una herramienta.')
                herramienta_actualizar = input('Ingrese nuevamente el nombre de la herramienta: ')
            if herramienta_actualizar not in herramientas:
                print('La herramienta no se encuentra en el inventario.')
                continue
            index_herramienta = herramientas.index(herramienta_actualizar)
            print('¿Qué operación desea realizar?')
            print('  1. Venta (disminuir stock)')
            print('  2. Ingreso (reponer stock)')
            tipo_operacion = input('Seleccione una opción (1 o 2): ')
            while tipo_operacion != '1' and tipo_operacion != '2':
                print('Opción no válida. Ingrese 1 para Venta o 2 para Ingreso.')
                tipo_operacion = input('Seleccione una opción (1 o 2): ')
            cantidad_unidades = input('Ingrese la cantidad de unidades: ')
            while not cantidad_unidades.isdigit() or int(cantidad_unidades) <= 0:
                print('Debe ingresar un número entero positivo.')
                cantidad_unidades = input('Ingrese nuevamente la cantidad de unidades: ')
            cantidad_unidades = int(cantidad_unidades)
            if tipo_operacion == '1':
                if existencias[index_herramienta] >= cantidad_unidades:
                    existencias[index_herramienta] -= cantidad_unidades
                    print(f'Venta registrada. Stock restante de {herramienta_actualizar}: {existencias[index_herramienta]} unidades.')
                else:
                    print(f'Stock insuficiente. Disponible: {existencias[index_herramienta]} unidades.')
            else:
                existencias[index_herramienta] += cantidad_unidades
                print(f'Ingreso registrado. Stock actualizado de {herramienta_actualizar}: {existencias[index_herramienta]} unidades.')
        case 8:
            print('Saliendo del programa...')
            break