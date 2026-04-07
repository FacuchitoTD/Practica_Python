import random

def actividad1():
    print("\n----- ACTIVIDAD 1 -----")
    estudiantes = ["Juan", "María", "Pedro", "Ana", "Luis", "Sofía", "Carlos", "Lucía", "Diego", "Valentina"]
    notas = [8.5, 9.0, 7.5, 6.0, 8.0, 9.5, 7.0, 8.5, 6.5, 9.0]

    for i in range(len(estudiantes)):
        print(f"{estudiantes[i]}: {notas[i]}")
    
    promedio = sum(notas) / len(notas)
    print(f"Promedio de notas: {promedio:.2f}")

    nota_mayor = max(notas)
    estudiante_mayor = estudiantes[notas.index(nota_mayor)]
    print(f"Nota más alta: {estudiante_mayor} ({nota_mayor})")
    
    nota_menor = min(notas)
    estudiante_menor = estudiantes[notas.index(nota_menor)]
    print(f"Nota más baja: {estudiante_menor} ({nota_menor})")

def actividad2():
    print('\n----- ACTIVIDAD 2 -----')
    lista = []
    for i in range(5):
        producto = input(f"Ingrese el producto {i+1}: ")
        while not producto:
            producto = input(f"Ingrese el producto {i+1}: ")
        lista.append(producto)
    
    lista_ordenada = sorted(lista)
    print("Lista ordenada alfabéticamente:")
    for producto in lista_ordenada:
        print(f"- {producto}")

    eliminar = input("Ingrese el producto que desea eliminar: ")
    if eliminar in lista:
        lista.remove(eliminar)
        print(f"Lista actualizada: {lista}")
    else:
        print(f"Producto '{eliminar}' no encontrado.")

def actividad3():
    print('\n----- ACTIVIDAD 3 -----')
    numeros = [random.randint(1, 100) for _ in range(15)]
    
    numeros_pares = [n for n in numeros if n % 2 == 0]
    numeros_impares = [n for n in numeros if n % 2 != 0]

    print(f"Lista original: ")
    for numero in numeros:
        print(numero)

    print(f"Pares ({len(numeros_pares)} números):")
    for par in numeros_pares:
        print(f"- {par}")

    print(f"Impares ({len(numeros_impares)} números):")
    for impar in numeros_impares:
        print(f"- {impar}")

def actividad4():
    print('\n----- ACTIVIDAD 4 -----')
    datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
    print(f"Lista original: {datos}")
    
    datos_sin_duplicados = []
    for d in datos:
        if d not in datos_sin_duplicados:
            datos_sin_duplicados.append(d)
    print("Lista sin duplicados:")
    for dato in datos_sin_duplicados:
        print(f"- {dato}")

def actividad5():
    print('\n----- ACTIVIDAD 5 -----')
    alumnos = ["Juan", "María", "Pedro", "Ana", "Luis", "Sofía", "Carlos", "Lucía"]
    
    print("Alumnos actuales:")
    for alumno in alumnos: print(f"- {alumno}")

    eleccion = input("\n¿Quiere eliminar a algún alumno? (s/n): ")
    if eleccion.lower() == 's':
        eliminar = input("Nombre del alumno a eliminar: ")
        if eliminar in alumnos:
            alumnos.remove(eliminar)
        else:
            print("No se encontró al alumno.")

    eleccion_add = input("\n¿Desea añadir un alumno? (s/n): ")
    if eleccion_add.lower() == 's':
        nuevo = input("Nombre del nuevo alumno: ")
        if nuevo: alumnos.append(nuevo)

    print("\nLista final de alumnos:")
    for alumno in alumnos:
        print(f"- {alumno}")

def actividad6():
    print('\n----- ACTIVIDAD 6 -----')
    numeros = [1, 2, 3, 4, 5, 6, 7]
    print(f"Original: {numeros}")

    numeros = [numeros[-1]] + numeros[:-1]

    print("Rotada (con slicing):")
    for n in numeros:
        print(f"- {n}")

def actividad7():
    print('\n----- ACTIVIDAD 7 -----')

    temperaturas = [
        [12,25],
        [14,27],
        [10,23],
        [16,29],
        [12,16],
        [20,29],
        [22,30]
    ]
    minimas = [dia[0] for dia in temperaturas]
    maximas = [dia[1] for dia in temperaturas]  

    promedio_min = sum(minimas) / len(minimas)
    promedio_max = sum(maximas) / len(maximas)
    print(f"Promedio de temperaturas mínimas: {promedio_min:.1f}°C") 
    print(f"Promedio de temperaturas máximas: {promedio_max:.1f}°C") 

    amplitudes = [dia[1] - dia[0] for dia in temperaturas]
    mayor_amplitud = max(amplitudes)
    dia_mayor_amplitud = amplitudes.index(mayor_amplitud) + 1
    print(f"La mayor amplitud térmica fue de {mayor_amplitud}°C el día {dia_mayor_amplitud}")

def actividad8():
    print('\n----- ACTIVIDAD 8 -----')
    notas_alumnos = [
        [8, 9, 7],  
        [10, 6, 8], 
        [7, 7, 9],  
        [9, 10, 9], 
        [6, 8, 7]   
    ]

    print("Promedio por Estudiante:")
    for i in range(len(notas_alumnos)):
        fila = notas_alumnos[i]
        promedio_est = sum(fila) / len(fila)
        print(f"- Estudiante {i+1}: {promedio_est:.2f}")

    print("\nPromedio por Materia:")
    nombres_materias = ["Matemática", "Programación", "Inglés"]
    for j in range(3):
        notas_materia = [fila[j] for fila in notas_alumnos]
        promedio_materia = sum(notas_materia) / len(notas_materia)
        print(f"- {nombres_materias[j]}: {promedio_materia:.2f}")

def actividad9():
    print('\n----- ACTIVIDAD 9 -----')

    turno = 'X'
    matriz = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]
    
    print("Tablero original:")
    for fila in matriz:
        print(fila)

    while True:
        print("Turno de:", turno)

        fila = input("Ingrese la fila (0-2) para colocar su ficha: ")
        columna = input("Ingrese la columna (0-2) para colocar su ficha: ")

        if not fila.isdigit() or not columna.isdigit():
            print("Debe ingresar números válidos.")
            continue
        fila, columna = int(fila), int(columna)

        if not (0 <= fila < 3 and 0 <= columna < 3):
            print("Posición inválida")
            continue
        if matriz[fila][columna] == "-":
            matriz[fila][columna] = turno
            print("Tablero actualizado:")
            for f in matriz:
                print(f)
            if turno == "X":
                turno = "O"
            else:
                turno = "X"
        else:
            print("Posición ocupada, intente nuevamente.")
            continue

def actividad10():
    print('\n----- ACTIVIDAD 10 -----')

    productos = ["Pan", "Leche", "Huevos", "Queso"]
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    ventas = [
    [10, 20, 30, 40, 50, 60, 70],
    [5, 10, 15, 20, 25, 30, 35],
    [8, 16, 24, 32, 40, 48, 56],
    [12, 24, 36, 48, 60, 72, 84]
]
    mayor_venta = 0
    dia_mayor_venta = 0
    mayor_producto = 0
    producto_mas_vendido = 0

    print('Ventas por día: ')
    for i in range(7):
        total_dia = 0
        for j in range(4):
            total_dia += ventas[j][i]
        print(f"Día {i+1}: {total_dia} unidades")
        if total_dia > mayor_venta:
            mayor_venta = total_dia
            dia_mayor_venta = dias[i]
    print(f"El día con mayor ventas fue el día {dia_mayor_venta} con {mayor_venta} unidades vendidas.")

    print('\nVentas por producto: ')
    for i in range(4):
        total_producto = 0
        for j in range(7):
            total_producto += ventas[i][j]
        print(f"Producto {productos[i]}: {total_producto} unidades")
        if total_producto > mayor_producto:
            mayor_producto = total_producto
            producto_mas_vendido = productos[i]
    print(f"El producto más vendido es {producto_mas_vendido} con {mayor_producto} unidades")

def actividad11():
    print('\n----- ACTIVIDAD 11 -----')
    lista_alumnos =['Leonel Messi','Agustina','Franco','Facundo Exequiel','Mauricio','Lucia','Martin','Clara','Lara','Daiana']
    busqueda = input('Ingrese el nombre del alumno a buscar: ').title()
    if busqueda in lista_alumnos:
        print(f'''
            El alumno {busqueda} está en la lista !!!
            Se encuentra en la posición {lista_alumnos.index(busqueda) + 1} de la lista
            ''')
    else:
        print(f'el alumno/a {busqueda} no está en la lista ')

def actividad12():
    print('\n----- ACTIVIDAD 12 -----')
    lista_numeros = []
    for i in range(8):
        while True:
            numero = input('Ingrese un número entero por favor: ')
            if numero.lstrip('-').isdigit():
                lista_numeros.append(int(numero))
                break
            else:
                print('Error, debe ingresar un número entero.')
    print('\nLista Original: ')
    for numero in lista_numeros:
        print(numero)
    
    print('\nLista ordenada menor a mayor: ')
    for numero in sorted(lista_numeros):
        print(numero)

    print('\nLista ordenada de mayor a menor: ')
    for numero in sorted(lista_numeros, reverse=True):
        print(numero)

def actividad13():
    print('\n----- ACTIVIDAD 13 -----')
    puntajes = [450,1200,875,990,300,1500,640]
    mayor_puntaje = max(puntajes)
    menor_puntaje = min(puntajes)
    print(f'Puntaje máximo: {mayor_puntaje}')
    print(f'Puntaje mínimo: {menor_puntaje}')

    print(f'\nLista de ranking de mayor a menor: ')
    ranking=sorted(puntajes, reverse=True)
    for rank in ranking:
        print(rank)
    
    print(f'El puntaje 990 está en la posición {ranking.index(990)+1} de la lista')
    

while True:
    print("""
╔══════════════════════════════════╗
║      MENÚ DE ACTIVIDADES         ║
╠══════════════════════════════════╣
║  1. Actividad 1                  ║
║  2. Actividad 2                  ║
║  3. Actividad 3                  ║
║  4. Actividad 4                  ║
║  5. Actividad 5                  ║
║  6. Actividad 6                  ║
║  7. Actividad 7                  ║
║  8. Actividad 8                  ║
║  9. Actividad 9                  ║
║ 10. Actividad 10                 ║
║ 11. Actividad 11                 ║
║ 12. Actividad 12                 ║
║ 13. Actividad 13                 ║
║  0. Salir                        ║
╚══════════════════════════════════╝
""")

    opcion = input("Seleccione una actividad: ")

    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
        continue

    match opcion:
        case '1':
            actividad1()
        case '2':
            actividad2()
        case '3':
            actividad3()
        case '4':
            actividad4()
        case '5':
            actividad5()
        case '6':
            actividad6()
        case '7':
            actividad7()
        case '8':
            actividad8()
        case '9':
            actividad9()
        case '10':
            actividad10()
        case '11':
            actividad11()
        case '12':
            actividad12()
        case '13':
            actividad13()
        case '0':
            print("Saliendo del programa...")
            break
        case _:
            print("Error: opción no válida. Elija entre 0 y 13.")