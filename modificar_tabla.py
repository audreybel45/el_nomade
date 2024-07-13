import mysql.connector
from mysql.connector import errorcode

# Datos de conexión a MySQL
config = {
    'user': 'audrey45',
    'password': 'Agusandy136',
    'host': 'localhost',
    'database': 'el_nomade',
    'raise_on_warnings': True
}

# Intentar conectar a MySQL
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # Lista de alteraciones a realizar en la tabla
    alteraciones = [
        "ALTER TABLE puntos_turisticos ADD COLUMN provincia VARCHAR(100) NOT NULL",
        "ALTER TABLE puntos_turisticos ADD COLUMN pais VARCHAR(100) NOT NULL",
        "ALTER TABLE puntos_turisticos ADD COLUMN hospedajes TEXT",
        "ALTER TABLE puntos_turisticos ADD COLUMN transporte TEXT",
        "ALTER TABLE puntos_turisticos ADD COLUMN formas_llegar TEXT",
        "ALTER TABLE puntos_turisticos ADD COLUMN foto LONGBLOB"
    ]

    # Ejecutar cada alteración
    for alteracion in alteraciones:
        try:
            cursor.execute(alteracion)
            print(f"Alteración realizada: {alteracion}")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DUP_FIELDNAME:
                print(f"El campo ya existe en la tabla.")
            else:
                print(f"Error al realizar alteración '{alteracion}': {err.msg}")

    # Cerrar cursor y conexión
    cursor.close()
    cnx.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
