import sqlite3

# Función para agregar un producto
def agregar_producto():
    try:
        nombre = input("Nombre del producto: ")
        descripcion = input("Descripción del producto: ")
        cantidad = int(input("Cantidad disponible: "))
        precio = float(input("Precio del producto: "))
        categoria = input("Categoría del producto: ")

        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()

        cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
        (nombre, descripcion, cantidad, precio, categoria))
        
        conexion.commit()
        conexion.close()
        print("Producto agregado exitosamente.")
    except Exception as e:
        print("Error al agregar el producto:", e)

# Función para consultar los productos
def consultar_productos():
    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()

        print("\n--- Listado de Productos ---")
        for producto in productos:
            print(f"ID: {producto[0]} | Nombre: {producto[1]} | Cantidad: {producto[3]} | Precio: ${producto[4]:.2f} | Categoría: {producto[5]}")
        
        conexion.close()
    except Exception as e:
        print("Error al consultar los productos:", e)

# Función para actualizar la cantidad de un producto
def actualizar_producto():
    try:
        id_producto = int(input("ID del producto a actualizar: "))
        nueva_cantidad = int(input("Nueva cantidad disponible: "))

        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        
        cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, id_producto))
        conexion.commit()
        
        if cursor.rowcount > 0:
            print("Cantidad actualizada exitosamente.")
        else:
            print("No se encontró un producto con el ID especificado.")
        
        conexion.close()
    except Exception as e:
        print("Error al actualizar el producto:", e)

# Función para eliminar un producto
def eliminar_producto():
    try:
        id_producto = int(input("ID del producto a eliminar: "))

        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conexion.commit()
        
        if cursor.rowcount > 0:
            print("Producto eliminado exitosamente.")
        else:
            print("No se encontró un producto con el ID especificado.")
        
        conexion.close()
    except Exception as e:
        print("Error al eliminar el producto:", e)

# Función para generar un reporte de bajo stock
def reporte_bajo_stock():
    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()

        umbral = 5  # Umbral de stock bajo
        cursor.execute("SELECT id, nombre, cantidad FROM productos WHERE cantidad < ?", (umbral,))
        productos = cursor.fetchall()
        
        print("\n--- Reporte de Bajo Stock ---")
        if productos:
            for producto in productos:
                print(f"ID: {producto[0]} - Nombre: {producto[1]} - Cantidad: {producto[2]} unidades")
        else:
            print("No hay productos con bajo stock.")
        
        conexion.close()
    except Exception as e:
        print("Error al generar el reporte de bajo stock:", e)
