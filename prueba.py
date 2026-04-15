herramienta = []
existencia = []

while True:   # REPETIR SIEMPRE
    print("Bienvenido a la herramienta de inventario")
    print('''
    1. Cargar herramientas
    2. Cargar stock de herramientas
    3. Mostrar resumen de herramientas cargadas
    4. Buscar herramienta por nombre
    5. Mostrar herramientas con stock agotado
    6. Agregar nueva herramienta al inventario
    7. Actualizar stock (Venta/Ingreso)
    8. salir del programa''')
    opción = input("Ingresa una opción: ")
    while not opción.isdigit() or int(opción) < 1 or int(opción) > 8:
        print("opcion incorrecta")
        opción = input("Ingresa una opción: ")
        opción = int(opción)

    match opción:
        case 1:
                cantidad = input("Ingresa la cantidad de herramientas: ")
                while not cantidad.isdigit() or int(cantidad) <= 0:
                    print("Cantidad incorrecta")
                    cantidad = input("Ingresa la cantidad de herramientas: ")
                    cantidad = int(cantidad)
                    contador = 0
                    while contador < cantidad:
                        nom_herramienta = input(f"Ingresa el nombre de la herramienta: {contador + 1}")
                        if nom_herramienta == "":
                            print("ERROR: Nombre incorrecto vuelve a ingresar un nombre de herramienta")
                        elif nom_herramienta in herramienta:
                            print("ERROR: El nombre ya existe!")
                        else:
                            herramienta.append(nom_herramienta)
                            contador += 1
        case 2:
            print("Ingrese la cantidad de stock de cada herramienta")
            if not herramienta:
                print("No hay herramientas cargadas en el inventario. Por favor, cargue herramientas primero.")
            elif len(existencia) == len(herramienta):
                print("El inventario de herramientas se ha procesado correctamente. Para realizar modificaciones en las existencias, por favor acceda a la opción 7 del menú principal.")
            else:
                for i in range(len(existencia), len(herramienta)):
                    print(f"Herramienta: {herramienta[i]}")
                    cantidad_unidades = input(f"Ingrese la cantidad de unidades: ")
                    while not cantidad_unidades.isdigit():
                        print("La cantidad debe ser un valor numérico positivo.")
                        cantidad_unidades = input(f"Ingrese nuevamente la cantidad de unidades: ")
                    existencia.append(int(cantidad_unidades))
        case 3:
            print("Resumen de herramientas cargadas")
            if not herramienta:
                print("No hay herramientas cargadas en el inventario.")
            elif len(existencia) < len(herramienta):
                print("El stock de algunas herramientas no ha sido cargado. Por favor, cargue el stock de todas las herramientas para mostrar el resumen completo.")
            else:
                for i in range(len(herramienta)):
                    print(f"{herramienta[i]}: {existencia[i]} unidades")
        case 4:
            if not herramienta:
                print("Inventario vacío. Debe registrar herramientas para acceder a esta opción")
            elif len(existencia) < len(herramienta):
                print("Error: Índice de búsqueda no disponible. Complete el registro de existencias de todo el catálogo para continuar.")
            else:
                herramienta_busqueda = input("Ingrese el nombre de la herramienta a buscar: ")
                while herramienta_busqueda == "":
                    print("Debe ingresar algún nombre de una herramienta")
                    herramienta_busqueda = input("Ingrese nuevamente el nombre de la herramienta a buscar: ")
                if herramienta_busqueda in herramienta:
                    index_herramienta = herramienta.index(herramienta_busqueda)
                    print(f"{herramienta_busqueda}: {existencia[index_herramienta]} unidades")
                else:
                    print("La herramienta no se encuentra en el inventario")
        case 5:
            print("Informe de Inventario: Existencias Agotadas")
            if len(herramienta) == 0:
                print("No hay herramientas cargadas en el inventario.")
            elif len(existencia) < len(herramienta):
                print("El stock de algunas herramientas no ha sido cargado.")
            else:
                hay_agotados = False
                for i in range(len(existencia)):
                    if existencia[i] == 0:
                        hay_agotados = True
                        break
                if not hay_agotados:
                    print("No hay herramientas con stock agotado.")
                else:
                    print("Las siguientes herramientas no tienen stock:")
                    for i in range(len(herramienta)):
                        if existencia[i] == 0:
                            print(f"- {herramienta[i]}")
        case 6:
            print("Ingreso de nueva herramienta")
            nombre_nueva_herramienta = input("Ingrese el nombre de la herramienta a agregar: ")
            if nombre_nueva_herramienta == "":
                print("Debe ingresar algún nombre de una herramienta")
                continue
            elif nombre_nueva_herramienta in herramienta:
                print("El nombre de esa herramienta ya existe en el inventario")
                continue
            elif len(existencia) < len(herramienta):
                print("Stock incompleto. Cargar existencias actuales para habilitar el alta de nuevas herramientas.")
                continue
            else:
                herramienta.append(nombre_nueva_herramienta)
                cantidad_unidades = input(f"Ingrese la cantidad de unidades para {nombre_nueva_herramienta}: ")
                if not cantidad_unidades.lstrip('-').isdigit() or int(cantidad_unidades) < 0:
                    print("Debe ingresar un número válido (entero positivo).")
                    herramienta.pop()
                    continue
                cantidad_unidades = int(cantidad_unidades)
                existencia.append(cantidad_unidades)
                print(f"{nombre_nueva_herramienta} ha sido agregada al inventario con {cantidad_unidades} unidades.")
        case 7:
            print("Actualización de Stock (Venta / Ingreso)")
            if not herramienta:
                print("No hay herramientas cargadas en el inventario.")
                continue
            elif len(existencia) < len(herramienta):
                print("Error de validación: La actualización de stock requiere la carga previa de las existencias faltantes.")
                continue
            herramienta_actualizar = input("Ingrese el nombre de la herramienta: ")
            while herramienta_actualizar == "":
                print("Debe ingresar algún nombre de una herramienta.")
                herramienta_actualizar = input("Ingrese nuevamente el nombre de la herramienta: ")
            if herramienta_actualizar not in herramienta:
                print("La herramienta no se encuentra en el inventario.")
                continue
            index_herramienta = herramienta.index(herramienta_actualizar)
            print("¿Qué operación desea realizar?")
            print("  1. Venta (disminuir stock)")
            print("  2. Ingreso (reponer stock)")
            tipo_operacion = input("Seleccione una opción (1 o 2): ")
            while tipo_operacion != '1' and tipo_operacion != '2':
                print("Opción no válida. Ingrese 1 para Venta o 2 para Ingreso.")
                tipo_operacion = input("Seleccione una opción (1 o 2): ")
                cantidad_unidades = input("Ingrese la cantidad de unidades: ")
                while not cantidad_unidades.isdigit() or int(cantidad_unidades) <= 0:
                print("Debe ingresar un número entero positivo.")
                cantidad_unidades = input("Ingrese nuevamente la cantidad de unidades: ")
                cantidad_unidades = int(cantidad_unidades)
                if tipo_operacion == '1':
                    if existencia[index_herramienta] >= cantidad_unidades:
                        existencia[index_herramienta] -= cantidad_unidades
                        print(f"Venta registrada. Stock restante de {herramienta_actualizar}: {existencia[index_herramienta]} unidades.")
                    else:
                        print(f"Stock insuficiente. Disponible: {existencia[index_herramienta]} unidades.")
                else:
                    existencia[index_herramienta] += cantidad_unidades
                    print(f"Ingreso registrado. stock. actualizado de {herramienta_actualizar}: {existencia[index_herramienta]} unidades.")
        case 8:
            print("Saliendo del programa...")
            break
