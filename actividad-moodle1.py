# inventario.py

# -------------------------------------------
# Solicitar datos al usuario
# -------------------------------------------

# Solicitar el nombre del producto
nombre = input("Ingrese el nombre del producto: ")

# -------------------------------------------
# Solicitar y validar el precio
# Se repite la solicitud hasta que el usuario ingrese un valor numérico válido
# -------------------------------------------
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("❌ El precio no puede ser negativo. Intente de nuevo.")
            continue
        break
    except ValueError:
        print("❌ Valor inválido. Por favor ingrese un número válido para el precio.")

# -------------------------------------------
# Solicitar y validar la cantidad
# Se repite la solicitud hasta que el usuario ingrese un número entero válido
# -------------------------------------------
while True:
    try:
        cantidad = int(input("Ingrese la cantidad en inventario: "))
        if cantidad < 0:
            print("❌ La cantidad no puede ser negativa. Intente de nuevo.")
            continue
        break
    except ValueError:
        print("❌ Valor inválido. Por favor ingrese un número entero para la cantidad.")

# -------------------------------------------
# Calcular el costo total del inventario
# -------------------------------------------
costo_total = precio * cantidad

# -------------------------------------------
# Mostrar los resultados en consola con formato claro
# -------------------------------------------
print(f"\nProducto: {nombre} | Precio: {precio:.2f} | Cantidad: {cantidad} | Total: {costo_total:.2f}")

# -------------------------------------------
# Descripción general del programa:
# Este programa solicita al usuario los datos de un producto (nombre, precio y cantidad),
# valida que el precio y la cantidad sean numéricos y positivos,
# calcula el costo total del inventario (precio * cantidad)
# y muestra los resultados en consola con un formato legible.
# -------------------------------------------