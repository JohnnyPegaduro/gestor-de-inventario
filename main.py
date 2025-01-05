from base_datos import inicializar_base_datos
from funcionalidades import agregar_producto, consultar_productos, actualizar_producto, eliminar_producto, reporte_bajo_stock

# Menú principal
def main():
    inicializar_base_datos()  # Inicializar la base de datos
    
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Consultar productos")
        print("3. Actualizar cantidad de producto")
        print("4. Eliminar producto")
        print("5. Generar reporte de bajo stock")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            consultar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            reporte_bajo_stock()
        elif opcion == "6":
            print("¡Gracias por usar el sistema de inventario!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar la aplicación
if __name__ == "__main__":
    main()
