# Listas paralelas
herramientas = []
existencias = []

# Cantidad de herramientas
cantidad = int(input("Ingrese la cantidad de herramientas: "))

# Carga de nombres
i = 0
while i < cantidad:
    nombre = input("Nombre de herramienta " + str(i+1) + ": ")

    if nombre == "":
        print("Error: nombre vacío.")
        continue

    duplicado = False
    for j in range(i):
        if herramientas[j].lower() == nombre.lower():
            duplicado = True

    if duplicado:
        print("Error: nombre duplicado.")
        continue

    herramientas.append(nombre)
    i = i + 1

# Carga de existencias
i = 0
while i < cantidad:
    print("Herramienta:", herramientas[i])
    stock = int(input("Cantidad: "))

    if stock < 0:
        print("Error: no puede ser negativo.")
        continue

    existencias.append(stock)
    i = i + 1

# Menú principal
opcion = ""
while opcion != "8":
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Ver inventario")
    print("2. Consultar stock")
    print("3. Reporte de agotados")
    print("4. Alta de nuevo producto")
    print("5. Actualizar stock")
    print("6. Salir")
    opcion = input("Elegí una opción: ")

    # Opción 3: ver inventario completo
    if opcion == "1":
        print("\n--- INVENTARIO ---")
        for i in range(len(herramientas)):
            print(str(i) + " | " + herramientas[i] + " | Stock: " + str(existencias[i]))

    # Opción 4: consultar stock por nombre
    elif opcion == "2":
        nombre = input("Nombre de la herramienta a buscar: ")
        encontrado = False
        for k in range(len(herramientas)):
            if herramientas[k].lower() == nombre.lower():
                print(herramientas[k] + " → stock disponible: " + str(existencias[k]))
                encontrado = True
        if not encontrado:
            print("Error: no se encontró esa herramienta.")

    # Opción 5: reporte de agotados
    elif opcion == "3":
        print("\n--- PRODUCTOS AGOTADOS ---")
        hay_agotados = False
        for k in range(len(herramientas)):
            if existencias[k] == 0:
                print(herramientas[k] + " → SIN STOCK")
                hay_agotados = True
        if not hay_agotados:
            print("No hay productos agotados.")

    # Opción 6: alta de nuevo producto
    elif opcion == "4":
        nombre = input("Nombre de la nueva herramienta: ")

        if nombre == "":
            print("Error: el nombre no puede estar vacío. Volviendo al menú.")
            continue

        duplicado = False
        for k in range(len(herramientas)):
            if herramientas[k].lower() == nombre.lower():
                duplicado = True

        if duplicado:
            print("Error: ese nombre ya existe. Volviendo al menú.")
            continue

        stock = int(input("Stock inicial: "))

        if stock < 0:
            print("Error: el stock no puede ser negativo. Volviendo al menú.")
            continue

        herramientas.append(nombre)
        existencias.append(stock)
        cantidad = cantidad + 1
        print("Herramienta agregada correctamente.")

    # Opción 7: actualizar stock
    elif opcion == "5":
        nombre = input("Nombre de la herramienta: ")
        idx = -1
        for k in range(len(herramientas)):
            if herramientas[k].lower() == nombre.lower():
                idx = k

        if idx == -1:
            print("Error: no se encontró esa herramienta.")
        else:
            print("Stock actual de " + herramientas[idx] + ": " + str(existencias[idx]))
            tipo = input("¿Venta o ingreso? (v/i): ")

            if tipo == "v":
                cantidad_mov = int(input("Cantidad a vender: "))
                if cantidad_mov > existencias[idx]:
                    print("Error: stock insuficiente. Disponible: " + str(existencias[idx]))
                else:
                    existencias[idx] = existencias[idx] - cantidad_mov
                    print("Venta registrada. Nuevo stock: " + str(existencias[idx]))

            elif tipo == "i":
                cantidad_mov = int(input("Cantidad a ingresar: "))
                existencias[idx] = existencias[idx] + cantidad_mov
                print("Ingreso registrado. Nuevo stock: " + str(existencias[idx]))

            else:
                print("Opción inválida.")

    # Opción 8: salir
    elif opcion == "6":
        print("Saliendo del sistema.")

    else:
        print("Opción inválida. Elegí entre 1 y 6.")