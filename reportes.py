# ==========================================================
# REPORTES.PY
# Funciones para visualizar y consultar reclamos
# ==========================================================

# Se importa la función que conecta con la base de datos
from base_datos import conectar_bd

# Se importa el diccionario de estados
from datos import Estados


# ==========================================================
# Función para visualizar todos los reclamos registrados
# ==========================================================

def visualizar_reclamos():

    print("\nLISTA DE RECLAMOS REGISTRADOS\n")

    conexion, cursor = conectar_bd()

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


# ==========================================================
# Función para generar un reporte de reclamos por estado
# ==========================================================

def reporte_por_estado():

    print("\nREPORTE DE RECLAMOS POR ESTADO\n")

    # Se muestran los estados disponibles
    print("Estados disponibles:\n")

    for clave in Estados:
        print(clave + ".", Estados[clave])

    opcion = input("\nSeleccione el estado que desea consultar: ").strip()

    if opcion not in Estados:

        print("\nERROR: Debe seleccionar un estado válido.")
        return

    estado = Estados[opcion]

    conexion, cursor = conectar_bd()

    cursor.execute(
        "SELECT * FROM reclamos WHERE estado = ?",
        (estado,)
    )

    reclamos = cursor.fetchall()

    print("\nRECLAMOS CON ESTADO:", estado.upper(), "\n")

    if len(reclamos) == 0:

        print("No existen reclamos con ese estado.")

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