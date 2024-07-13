import mysql.connector
from mysql.connector import errorcode

# Datos de conexión a MySQL
config = {
    'user': 'audrey45',
    'password': 'Agusandy136',
    'host': 'localhost',
    'raise_on_warnings': True
}
# Intentar conectar a MySQL
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # Crear la base de datos
    try:
        cursor.execute("CREATE DATABASE el_nomade")
        print("Base de datos 'el_nomade' creada con éxito.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print("La base de datos 'el_nomade' ya existe.")
        else:
            print(err.msg)

    # Seleccionar la base de datos
    cursor.execute("USE el_nomade")

    # Crear tablas
    tablas = {
        'usuarios': (
            "CREATE TABLE usuarios ("
            "  id INT AUTO_INCREMENT PRIMARY KEY,"
            "  usuario VARCHAR(50) NOT NULL,"
            "  contrasena VARCHAR(255) NOT NULL"
            ")"
        ),
        'puntos_turisticos': (
            "CREATE TABLE puntos_turisticos ("
            "  id INT AUTO_INCREMENT PRIMARY KEY,"
            "  nombre VARCHAR(100) NOT NULL,"
            "  descripcion TEXT,"
            "  ubicacion VARCHAR(255)"
            ")"
        ),
        'guias_turisticos': (
            "CREATE TABLE guias_turisticos ("
            "  id INT AUTO_INCREMENT PRIMARY KEY,"
            "  nombre VARCHAR(100) NOT NULL,"
            "  contacto VARCHAR(100),"
            "  especialidad VARCHAR(100)"
            ")"
        ),
        'restaurantes': (
            "CREATE TABLE restaurantes ("
            "  id INT AUTO_INCREMENT PRIMARY KEY,"
            "  nombre VARCHAR(100) NOT NULL,"
            "  direccion VARCHAR(255),"
            "  tipo_cocina VARCHAR(100)"
            ")"
        )
    }

    for nombre_tabla, ddl in tablas.items():
        try:
            cursor.execute(ddl)
            print(f"Tabla '{nombre_tabla}' creada con éxito.")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print(f"La tabla '{nombre_tabla}' ya existe.")
            else:
                print(err.msg)

    # Cerrar cursor y conexión
    cursor.close()
    cnx.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")