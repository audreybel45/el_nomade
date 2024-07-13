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

# Crear una conexión
def create_connection():
    try:
        cnx = mysql.connector.connect(**config)
        return cnx
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Create
def create_punto_turistico(nombre, provincia, pais, descripcion, hospedajes, transporte, formas_llegar, foto, ubicacion):
    cnx = create_connection()
    if cnx:
        cursor = cnx.cursor()
        add_punto = ("INSERT INTO puntos_turisticos "
                     "(nombre, provincia, pais, descripcion, hospedajes, transporte, formas_llegar, foto, ubicacion) "
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data_punto = (nombre, provincia, pais, descripcion, hospedajes, transporte, formas_llegar, foto, ubicacion)
        cursor.execute(add_punto, data_punto)
        cnx.commit()
        cursor.close()
        cnx.close()
        print("Punto turístico creado con éxito.")

# Read
def read_puntos_turisticos():
    cnx = create_connection()
    if cnx:
        cursor = cnx.cursor()
        query = "SELECT * FROM puntos_turisticos"
        cursor.execute(query)
        for (id, nombre, provincia, pais, descripcion, hospedajes, transporte, formas_llegar, foto, ubicacion) in cursor:
            print(f"ID: {id}, Nombre: {nombre}, Provincia: {provincia}, País: {pais}, Descripción: {descripcion}, "
                  f"Hospedajes: {hospedajes}, Transporte: {transporte}, Formas de Llegar: {formas_llegar}, "
                  f"Ubicación: {ubicacion}")
        cursor.close()
        cnx.close()

# Update
def update_punto_turistico(id, nombre, provincia, pais, descripcion, hospedajes, transporte, formas_llegar, foto, ubicacion):
    cnx = create_connection()
    if cnx:
        cursor = cnx.cursor()
        update_punto = ("UPDATE puntos_turisticos SET nombre=%s, provincia=%s, pais=%s, descripcion=%s, hospedajes=%s, "
                        "transporte=%s, formas_llegar=%s, foto=%s, ubicacion=%s WHERE id=%s")
        data_punto = (nombre, provincia, pais, descripcion, hospedajes, transporte, formas_llegar, foto, ubicacion, id)
        cursor.execute(update_punto, data_punto)
        cnx.commit()
        cursor.close()
        cnx.close()
        print("Punto turístico actualizado con éxito.")

# Delete
def delete_punto_turistico(id):
    cnx = create_connection()
    if cnx:
        cursor = cnx.cursor()
        delete_punto = "DELETE FROM puntos_turisticos WHERE id=%s"
        cursor.execute(delete_punto, (id,))
        cnx.commit()
        cursor.close()
        cnx.close()
        print("Punto turístico eliminado con éxito.")

# Ejemplos de uso
if __name__ == "__main__":
    # Crear un nuevo punto turístico
    create_punto_turistico("Playa Bonita", "Buenos Aires", "Argentina", "Una playa hermosa.", "Hotel XYZ", "Bus", "Auto", None, "Ubicación exacta")

    # Leer todos los puntos turísticos
    read_puntos_turisticos()

    # Actualizar un punto turístico existente
    update_punto_turistico(1, "Playa Hermosa", "Buenos Aires", "Argentina", "Una playa aún más hermosa.", "Hotel ABC", "Bus", "Auto", None, "Nueva ubicación")

    # Eliminar un punto turístico
    delete_punto_turistico(1)
