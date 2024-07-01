import cx_Oracle

class DatosTipo:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def listaDeTipos(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT ID, NOMBRE FROM PRO_TIPO")
        except self.connection.error as error:
            print("Error: ", error)
        return cursor
