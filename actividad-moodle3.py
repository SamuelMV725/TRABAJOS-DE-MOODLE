import csv

# ------------------------
# FUNCIONES DE INVENTARIO
# ------------------------

def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un producto al inventario"""
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

def mostrar_inventario(inventario):
    """Muestra el inventario completo"""
    if not inventario:
        print("Inventario vacío.")
        return
    print(f"{'Nombre':20} {'Precio':10} {'Cantidad':10} {'Subtotal':10}")
    print("-" * 55)
    subtotal = lambda p: p["precio"] * p["cantidad"]
    for p in inventario:
        print(f"{p['nombre']:20} {p['precio']:10.2f} {p['cantidad']:10} {subtotal(p):10.2f}")

def buscar_producto(inventario, nombre):
    """Busca un producto por nombre"""
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza precio y/o cantidad de un producto"""
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        return True
    return False

def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario"""
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False

def calcular_estadisticas(inventario):
    """Calcula estadísticas del inventario"""
    if not inventario:
        return {
            "unidades_totales": 0,
            "valor_total": 0.0,
            "producto_mas_caro": None,
            "producto_mayor_stock": None
        }
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"])
    }

# ------------------------
# FUNCIONES DE ARCHIVOS CSV
# ------------------------

def guardar_csv(inventario, ruta, incluir_header=True):
    """Guarda inventario en archivo CSV"""
    if not inventario:
        print("No se puede guardar: inventario vacío.")
        return
    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])
            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])
        print(f"Inventario guardado en: {ruta}")
    except PermissionError:
        print("Error: No tiene permisos para escribir en esta ubicación.")
    except Exception as e:
        print(f"Error al guardar archivo: {e}")

def cargar_csv(ruta):
    """Carga inventario desde CSV, retornando lista de productos y filas inválidas"""
    inventario_cargado = []
    errores = 0
    try:
        with open(ruta, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            if header != ["nombre", "precio", "cantidad"]:
                print("Encabezado inválido.")
                return [], 0
            for i, row in enumerate(reader, start=2):
                if len(row) != 3:
                    errores += 1
                    continue
                nombre, precio, cantidad = row
                try:
                    precio = float(precio)
                    cantidad = int(cantidad)
                    if precio < 0 or cantidad < 0:
                        raise ValueError
                    inventario_cargado.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
                except ValueError:
                    errores += 1
                    continue
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except UnicodeDecodeError:
        print("Error de codificación al leer el archivo.")
    except Exception as e:
        print(f"Error al cargar archivo: {e}")
    
    return inventario_cargado, errores

# ------------------------
# MENÚ PRINCIPAL
# ------------------------

def menu():
    print("\n--- MENÚ DE INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Mostrar estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")
    try:
        opcion = int(input("Elija una opción (1-9): "))
        if opcion not in range(1, 10):
            raise ValueError
        return opcion
    except ValueError:
        print("Opción inválida.")
        return None

# ------------------------
# MAIN
# ------------------------

def main():
    inventario = []
    while True:
        opcion = menu()
        if opcion is None:
            continue
        
        if opcion == 1:
            nombre = input("Nombre: ").strip()
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                if precio < 0 or cantidad < 0:
                    raise ValueError
                agregar_producto(inventario, nombre, precio, cantidad)
                print("Producto agregado.")
            except ValueError:
                print("Precio o cantidad inválidos.")
        
        elif opcion == 2:
            mostrar_inventario(inventario)
        
        elif opcion == 3:
            nombre = input("Nombre a buscar: ").strip()
            p = buscar_producto(inventario, nombre)
            if p:
                print(f"Producto encontrado: {p}")
            else:
                print("Producto no encontrado.")
        
        elif opcion == 4:
            nombre = input("Nombre a actualizar: ").strip()
            try:
                precio = input("Nuevo precio (Enter para mantener): ")
                cantidad = input("Nueva cantidad (Enter para mantener): ")
                nuevo_precio = float(precio) if precio else None
                nueva_cantidad = int(cantidad) if cantidad else None
                if (nuevo_precio is not None and nuevo_precio < 0) or (nueva_cantidad is not None and nueva_cantidad < 0):
                    raise ValueError
                if actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
                    print("Producto actualizado.")
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("Valores inválidos.")
        
        elif opcion == 5:
            nombre = input("Nombre a eliminar: ").strip()
            if eliminar_producto(inventario, nombre):
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")
        
        elif opcion == 6:
            stats = calcular_estadisticas(inventario)
            print(f"Unidades totales: {stats['unidades_totales']}")
            print(f"Valor total: {stats['valor_total']:.2f}")
            print(f"Producto más caro: {stats['producto_mas_caro']}")
            print(f"Producto con mayor stock: {stats['producto_mayor_stock']}")
        
        elif opcion == 7:
            ruta = input("Ruta archivo CSV: ").strip()
            guardar_csv(inventario, ruta)
        
        elif opcion == 8:
            ruta = input("Ruta archivo CSV: ").strip()
            cargado, errores = cargar_csv(ruta)
            if cargado:
                decision = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
                if decision == "S":
                    inventario = cargado
                    accion = "Reemplazado"
                else:
                    # Política: sumar cantidades, actualizar precio al nuevo
                    for p in cargado:
                        existente = buscar_producto(inventario, p["nombre"])
                        if existente:
                            existente["cantidad"] += p["cantidad"]
                            existente["precio"] = p["precio"]
                        else:
                            inventario.append(p)
                    accion = "Fusionado"
                print(f"Productos cargados: {len(cargado)}, filas inválidas: {errores}, acción: {accion}")
            else:
                print("No se cargaron productos.")
        
        elif opcion == 9:
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()