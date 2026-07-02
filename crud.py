# ==========================================================
# CRUD.PY
# Funciones para crear, buscar, modificar y eliminar reclamos
# ==========================================================

# Se importa la función que conecta con la base de datos
from base_datos import conectar_bd

# Se importan los diccionarios desde datos.py
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

    print("\nSubcategorías disponibles:\n")

    for i in range(len(subcategorias_disponibles)):
        print(str(i + 1) + ".", subcategorias_disponibles[i])

    opcion_subcategoria = input("\nSeleccione el número de la subcategoría: ").strip()

    if opcion_subcategoria.isdigit():
        opcion_subcategoria = int(opcion_subcategoria)

        if 1 <= opcion_subcategoria <= len(subcategorias_disponibles):
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

    conexion, cursor = conectar_bd()

    cursor.execute("""
        INSERT INTO reclamos
        (descripcion, categoria, subcategoria, provincia, municipio, barrio, calle, altura, estado)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        descripcion,
        categoria,
        subcategoria,
        provincia,
        municipio,
        barrio,
        calle,
        int(altura),
        estado
    ))

    conexion.commit()
    conexion.close()

    print("\nReclamo registrado correctamente.")


# Función para buscar un reclamo por ID
def buscar_reclamo():

    print("\nBÚSQUEDA DE RECLAMO POR ID\n")

    id_reclamo = input("Ingrese el ID del reclamo que desea buscar: ").strip()

    if not id_reclamo.isdigit():
        print("\nERROR: El ID debe ser un número.")
        return

    conexion, cursor = conectar_bd()

    cursor.execute("SELECT * FROM reclamos WHERE id = ?", (int(id_reclamo),))

    reclamo = cursor.fetchone()

    if reclamo is None:
        print("\nNo se encontró ningún reclamo con ese ID.")

    else:
        print("\nRECLAMO ENCONTRADO\n")
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

    conexion.close()


# Función para actualizar el estado de un reclamo mediante su ID
def actualizar_reclamo():

    print("\nACTUALIZACIÓN DE RECLAMO\n")

    id_reclamo = input("Ingrese el ID del reclamo que desea actualizar: ").strip()

    if not id_reclamo.isdigit():
        print("\nERROR: El ID debe ser un número.")
        return

    conexion, cursor = conectar_bd()

    cursor.execute("SELECT * FROM reclamos WHERE id = ?", (int(id_reclamo),))

    reclamo = cursor.fetchone()

    if reclamo is None:
        print("\nNo se encontró ningún reclamo con ese ID.")
        conexion.close()
        return

    print("\nReclamo seleccionado:")
    print("ID:", reclamo[0])
    print("Descripción:", reclamo[1])
    print("Estado actual:", reclamo[9])

    print("\nEstados disponibles:\n")

    for clave in Estados:
        print(clave + ".", Estados[clave])

    opcion_estado = input("\nSeleccione el nuevo estado del reclamo: ").strip()

    if opcion_estado in Estados:
        nuevo_estado = Estados[opcion_estado]

    else:
        print("\nERROR: Debe seleccionar un estado válido.")
        conexion.close()
        return

    cursor.execute("""
        UPDATE reclamos
        SET estado = ?
        WHERE id = ?
    """, (nuevo_estado, int(id_reclamo)))

    conexion.commit()
    conexion.close()

    print("\nReclamo actualizado correctamente.")


# Función para eliminar un reclamo mediante su ID
def eliminar_reclamo():

    print("\nELIMINACIÓN DE RECLAMO\n")

    id_reclamo = input("Ingrese el ID del reclamo que desea eliminar: ").strip()

    if not id_reclamo.isdigit():
        print("\nERROR: El ID debe ser un número.")
        return

    conexion, cursor = conectar_bd()

    cursor.execute("SELECT * FROM reclamos WHERE id = ?", (int(id_reclamo),))

    reclamo = cursor.fetchone()

    if reclamo is None:
        print("\nNo se encontró ningún reclamo con ese ID.")
        conexion.close()
        return

    print("\nReclamo seleccionado:")
    print("ID:", reclamo[0])
    print("Descripción:", reclamo[1])
    print("Categoría:", reclamo[2])
    print("Subcategoría:", reclamo[3])

    confirmacion = input("\n¿Está seguro/a de eliminar este reclamo? (s/n): ").strip().lower()

    if confirmacion == "s":

        cursor.execute("DELETE FROM reclamos WHERE id = ?", (int(id_reclamo),))

        conexion.commit()

        print("\nReclamo eliminado correctamente.")

    else:
        print("\nEliminación cancelada.")

    conexion.close()