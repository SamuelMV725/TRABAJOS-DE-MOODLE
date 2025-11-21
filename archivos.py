import csv

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