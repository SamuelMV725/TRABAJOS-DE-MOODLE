from servicios import agregar_producto, actualizar_producto, mostrar_inventario, buscar_producto, eliminar_producto, calcular_estadisticas
from archivos import guardar_csv, cargar_csv


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