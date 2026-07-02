# 1. Se importa sqlite3 para trabajar con la base de datos
import sqlite3


# 2. Nombre de la base de datos del proyecto
NOMBRE_BASE_DATOS = "observatorio_barrial.db"


# 3. Función para conectar con la base de datos
def conectar_bd():

    # Se crea o se conecta a la base de datos del proyecto
    conexion = sqlite3.connect(NOMBRE_BASE_DATOS)

    # El cursor permite ejecutar instrucciones SQL
    cursor = conexion.cursor()

    # Se devuelve la conexión y el cursor para usarlos en otras funciones
    return conexion, cursor


# Función para crear la base de datos y la tabla principal
def crear_base_datos():

    # Se obtiene la conexión y el cursor usando la función conectar_bd()
    conexion, cursor = conectar_bd()

    # Se crea la tabla de reclamos si todavía no existe
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reclamos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion TEXT,
        categoria TEXT NOT NULL,
        subcategoria TEXT NOT NULL,
        provincia TEXT NOT NULL,
        municipio TEXT NOT NULL,
        barrio TEXT NOT NULL,
        calle TEXT NOT NULL,
        altura INTEGER NOT NULL,
        estado TEXT NOT NULL)
    """)

    # Se guardan los cambios realizados en la base de datos
    conexion.commit()

    # Se cierra la conexión
    conexion.close()

    print("Base de datos creada correctamente.")