# Sistema de inventario
# El programa permite agregar productos, mostrar inventario, calcular estadísticas y salir del sistema.

# Lista para almacenar los productos
inventario = []

# Función para agregar un producto al inventario
def agregar_producto():
    """
    Función para agregar un producto al inventario. 
    Solicita el nombre, precio y cantidad del producto, 
    luego lo guarda en el inventario como un diccionario.
    """
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    
    # Creamos un diccionario para el producto y lo añadimos a la lista de inventario
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print(f"Producto {nombre} agregado al inventario.\n")

# Función para mostrar el inventario
def mostrar_inventario():
    """
    Función para mostrar todos los productos en el inventario.
    Si el inventario está vacío, se muestra un mensaje indicándolo.
    """
    if not inventario:
        print("El inventario está vacío.\n")
    else:
        print("Inventario:")
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        print()  # Salto de línea para mayor claridad

# Función para calcular estadísticas del inventario
def calcular_estadisticas():
    """
    Función para calcular y mostrar las estadísticas del inventario:
    - Valor total del inventario (precio * cantidad de cada producto).
    - Cantidad total de productos en el inventario.
    """
    if not inventario:
        print("El inventario está vacío, no se pueden calcular estadísticas.\n")
    else:
        valor_total = 0
        cantidad_total = 0
        for producto in inventario:
            valor_total += producto['precio'] * producto['cantidad']
            cantidad_total += producto['cantidad']
        
        print(f"Valor total del inventario: {valor_total}")
        print(f"Cantidad total de productos registrados: {cantidad_total}\n")

# Función principal que muestra el menú y ejecuta las opciones seleccionadas
def menu():
    """
    Función que muestra un menú de opciones y ejecuta las acciones correspondientes.
    El programa continuará mostrando el menú hasta que el usuario seleccione salir.
    """
    while True:
        # Mostrar el menú de opciones
        print("Menú de opciones:")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")
        
        # Solicitar opción al usuario
        opcion = input("Seleccione una opción (1-4): ")
        
        # Procesar la opción seleccionada usando condicionales
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("Gracias por usar el sistema de inventario. ¡Hasta pronto!")
            break  # Salir del bucle y terminar el programa
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.\n")

# Llamar a la función menu para iniciar el programa
menu()
