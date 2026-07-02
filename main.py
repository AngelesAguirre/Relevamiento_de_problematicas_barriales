# 1. SE IMPORTAN LAS FUNCIONES

# a. Función que crea la base de datos
from base_datos import crear_base_datos

# b. Funciones CRUD
from crud import registrar_reclamo, buscar_reclamo, actualizar_reclamo, eliminar_reclamo

# c. Funciones de reportes
from reportes import visualizar_reclamos, reporte_por_estado


# d. Función principal del sistema
def menu_principal():

    while True:
        print("\n==============================")
        print(" OBSERVATORIO BARRIAL")
        print("==============================")
        print("1. Registrar reclamo")
        print("2. Visualizar reclamos")
        print("3. Buscar reclamo por ID")
        print("4. Actualizar reclamo por ID")
        print("5. Eliminar reclamo por ID")
        print("6. Reporte de reclamos por estado")
        print("7. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            registrar_reclamo()

        elif opcion == "2":
            visualizar_reclamos()

        elif opcion == "3":
            buscar_reclamo()

        elif opcion == "4":
            actualizar_reclamo()

        elif opcion == "5":
            eliminar_reclamo()

        elif opcion == "6":
            reporte_por_estado()

        elif opcion == "7":
            print("\nSistema finalizado correctamente.")
            break

        else:
            print("\nERROR: Debe seleccionar una opción válida.")


# Este bloque permite ejecutar el programa desde main.py
if __name__ == "__main__":

    # Se crea la base de datos antes de iniciar el sistema
    crear_base_datos()

    # Se ejecuta el menú principal
    menu_principal()