# 1. Se importa SQLite3 para trabajar con la base de datos
import sqlite3

# Se importan los diccionarios desde el archivo datos.py
from datos import Categorias, Estados


# Función para registrar un nuevo reclamo en la base de datos
def registrar_reclamo():

    print("\nREGISTRO DE NUEVO RECLAMO\n")

    descripcion = input("Ingrese una breve descripción del reclamo: ").strip()

    if descripcion == "":
        print("\nERROR: La descripción no puede quedar vacía.")
        return

    print("\nCategorías disponibles:\n")

    for clave in Categorias:
        print(clave + ".", Categorias[clave]["Nombre"])

    opcion_categoria = input("\nSeleccione el número de la categoría: ").strip()

    if opcion_categoria in Categorias:
        categoria = Categorias[opcion_categoria]["Nombre"]
        subcategorias_disponibles = Categorias[opcion_categoria]["Subcategorias"]
        print("\nCategoría seleccionada:", categoria)

    else:
        print("\nERROR: Debe seleccionar una categoría válida.")
        return

    print("\nSubcategorías disponibles para la categoría " + categoria + ":\n")

    for i in range(len(subcategorias_disponibles)):
        print(str(i + 1) + ".", subcategorias_disponibles[i])

    opcion_subcategoria = input("\nSeleccione el número de la subcategoría: ").strip()

    if opcion_subcategoria.isdigit():

        opcion_subcategoria = int(opcion_subcategoria)

        if opcion_subcategoria >= 1 and opcion_subcategoria <= len(subcategorias_disponibles):
            subcategoria = subcategorias_disponibles[opcion_subcategoria - 1]
            print("\nSubcategoría seleccionada:", subcategoria)

        else:
            print("\nERROR: Debe seleccionar una subcategoría válida.")
            return

    else:
        print("\nERROR: Debe ingresar un número.")
        return

    provincia = input("\nIngrese la provincia: ").strip().title()
    municipio = input("Ingrese el municipio o partido: ").strip().title()
    barrio = input("Ingrese el barrio: ").strip().title()
    calle = input("Ingrese la calle: ").strip().title()
    altura = input("Ingrese la altura: ").strip()

    print("\nEstados disponibles:\n")

    for clave in Estados:
        print(clave + ".", Estados[clave])

    opcion_estado = input("\nSeleccione el número del estado del reclamo: ").strip()

    if opcion_estado in Estados:
        estado = Estados[opcion_estado]
        print("\nEstado seleccionado:", estado)

    else:
        print("\nERROR: Debe seleccionar un estado válido.")
        return

    if provincia == "" or municipio == "" or barrio == "" or calle == "" or altura == "":
        print("\nERROR: No se pueden dejar campos vacíos.")
        return

    if not altura.isdigit():
        print("\nERROR: La altura debe ser un número.")
        return

    conexion = sqlite3.connect("observatorio_barrial.db")
    cursor = conexion.cursor()

    cursor.execute("""INSERT INTO reclamos 
                   (descripcion,
                   categoria,
                   subcategoria,
                   provincia,
                   municipio,
                   barrio,
                   calle,
                   altura,
                   estado)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (descripcion,
                                                           categoria,
                                                           subcategoria,
                                                           provincia,
                                                           municipio,
                                                           barrio,
                                                           calle,
                                                           int(altura),
                                                           estado))

    conexion.commit()
    conexion.close()

    print("\nReclamo registrado correctamente.")


# Función para visualizar todos los reclamos registrados
def visualizar_reclamos():

    print("\nLISTA DE RECLAMOS REGISTRADOS\n")

    conexion = sqlite3.connect("observatorio_barrial.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM reclamos")

    reclamos = cursor.fetchall()

    if len(reclamos) == 0:
        print("No existen reclamos registrados.")

    else:
        for reclamo in reclamos:
            print("ID:", reclamo[0])
            print("Descripción:", reclamo[1])
            print("Categoría:", reclamo[2])
            print("Subcategoría:", reclamo[3])
            print("Provincia:", reclamo[4])
            print("Municipio o partido:", reclamo[5])
            print("Barrio:", reclamo[6])
            print("Calle:", reclamo[7])
            print("Altura:", reclamo[8])
            print("Estado:", reclamo[9])
            print("-" * 60)

    conexion.close()