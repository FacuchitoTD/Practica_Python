# case 7:
#             print('-----Actualización de Stock-----')
#             if not herramientas:
#                 print('No hay herramientas cargadas en el inventario.')
#                 continue
#             elif len(existencias) < len(herramientas):
#                 print('El stock de algunas herramientas no ha sido cargado. Por favor, cargue el stock de todas las herramientas para actualizar.')
#                 continue
#             else:
#                 herramienta_actualizar = input('Ingrese el nombre de la herramienta a actualizar: ')
#                 while herramienta_actualizar == '':
#                     print('Debe ingresar algún nombre de una herramienta')
#                     herramienta_actualizar = input('Ingrese nuevamente el nombre de la herramienta a actualizar: ')
#                 if herramienta_actualizar in herramientas:
#                     cantidad_unidades = input(f'Ingrese la nueva cantidad de unidades para {herramienta_actualizar}: ')
#                     while not cantidad_unidades.isdigit():
#                         print('Debe ingresar un número válido.')
#                         cantidad_unidades = input(f'Ingrese nuevamente la nueva cantidad de unidades para {herramienta_actualizar}: ')
#                     cantidad_unidades = int(cantidad_unidades)
#                     index_herramienta = herramientas.index(herramienta_actualizar)
#                     existencias[index_herramienta] += cantidad_unidades
#                     print(f'El stock de {herramienta_actualizar} ha sido actualizado a {existencias[index_herramienta]} unidades.')
#                 else:
#                     print('La herramienta no se encuentra en el inventario')
#         case 8:
#             print('-----Venta de Herramienta-----')
#             if not herramientas:
#                 print('No hay herramientas cargadas en el inventario.')
#                 continue
#             elif len(existencias) < len(herramientas):
#                 print('El stock de algunas herramientas no ha sido cargado. Por favor, cargue el stock de todas las herramientas para realizar ventas.')
#                 continue
#             else:
#                 herramienta_vender = input('Ingrese el nombre de la herramienta a vender: ')
#                 while herramienta_vender == '':
#                     print('Debe ingresar algún nombre de una herramienta')
#                     herramienta_vender = input('Ingrese nuevamente el nombre de la herramienta a vender: ')
#                 if herramienta_vender in herramientas:
#                     cantidad_vender = input(f'Ingrese la cantidad de unidades a vender para {herramienta_vender}: ')
#                     while not cantidad_vender.isdigit():
#                         print('Debe ingresar un número válido.')
#                         cantidad_vender = input (f'Ingrese nuevamente la cantidad de unidades a vender para {herramienta_vender}: ')
#                     cantidad_vender = int(cantidad_vender)
#                     index_herramienta = herramientas.index(herramienta_vender)
#                     if existencias[index_herramienta] >= cantidad_vender:
#                         existencias[index_herramienta] -= cantidad_vender
#                         print(f'Se han vendido {cantidad_vender} unidades de {herramienta_vender}. Stock restante: {existencias[index_herramienta]} unidades.')
#                     else:
#                         print(f'No hay suficiente stock de {herramienta_vender} para realizar la venta. Stock disponible: {existencias[index_herramienta]} unidades.')
#                         continue
#                 else:
#                     print('La herramienta no se encuentra en el inventario')