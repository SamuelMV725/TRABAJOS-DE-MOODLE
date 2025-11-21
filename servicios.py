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
