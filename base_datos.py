import sqlite3

# Función para inicializar la base de datos
def inicializar_base_datos():
    try:
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        
        # Crear la tabla productos si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                categoria TEXT
            )
        """)
        
        conexion.commit()
        conexion.close()
    except Exception as e:
        print("Error al inicializar la base de datos:", e)
