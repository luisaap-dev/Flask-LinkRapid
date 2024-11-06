import sqlite3
import string
import secrets

class AcortadorURL:
    def __init__(self, ruta_bd='database/acortador_urls.db'):
        self.ruta_bd = ruta_bd

    def _conectar(self):
        # Crea una conexión a la base de datos SQLite
        return sqlite3.connect(self.ruta_bd)

    def _generar_url_corta(self):
        # Genera dos URL cortas aleatorias con caracteres alfanuméricos
        caracteres = string.ascii_letters + string.digits
        return [ ''.join(secrets.choice(caracteres) for _ in range(8)) for _ in range(2)]

    def crear_tabla(self):
        conexion = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            # Crea una tabla si no existe para almacenar URLs
            cursor.execute("CREATE TABLE IF NOT EXISTS urls (url_corta TEXT PRIMARY KEY, url_larga TEXT)")
            conexion.commit()
        except sqlite3.Error as e:
            print("Error al crear la tabla:", e)
        finally:
            if conexion:
                conexion.close()

    def acortar_url(self, url_larga):
        url_cortas = self._generar_url_corta()
        conexion = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            for url_corta in url_cortas:
                # Inserta una nueva URL larga y su correspondiente URL corta en la base de datos
                cursor.execute("INSERT INTO urls (url_corta, url_larga) VALUES (?, ?)", (url_corta, url_larga))
            conexion.commit()
        except sqlite3.Error as e:
            print("Error al acortar la URL:", e)
        finally:
            if conexion:
                conexion.close()
        return url_cortas

    def obtener_url_larga(self, url_corta):
        conexion = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            # Recupera la URL larga asociada a una URL corta específica
            cursor.execute("SELECT url_larga FROM urls WHERE url_corta = ?", (url_corta,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        except sqlite3.Error as e:
            print("Error al obtener la URL larga:", e)
        finally:
            if conexion:
                conexion.close()

    def borrar_url(self, url_corta):
        conexion = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            # Elimina una entrada de la base de datos utilizando la URL corta como identificador
            cursor.execute("DELETE FROM urls WHERE url_corta = ?", (url_corta,))
            conexion.commit()
        except sqlite3.Error as e:
            print("Error al borrar la URL:", e)
        finally:
            if conexion:
                conexion.close()
