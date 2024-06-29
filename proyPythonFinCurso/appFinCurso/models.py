import cx_Oracle

class DatosTipo:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def insertaNuevoTipo(self, nombre):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT MAX(ID) FROM PRO_TIPO")
            maxID = cursor.fetchone()[0]
            if maxID is None:
                newID = 1
            else:
                newID = maxID + 1
            cursor.execute("INSERT INTO PRO_TIPO (ID, NOMBRE) VALUES(:P1, UPPER(:P2))",(newID, nombre))
        except self.connection.error as error:
            print("Error: ", error)
        return cursor


    def listaDeTipos(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT ID, NOMBRE FROM PRO_TIPO")
        except self.connection.error as error:
            print("Error: ", error)
        return cursor

    # def encuentraLibroPorId(self):
    #     cursor = self.connection.cursor()
    #     try:
    #     except self.connection.error as error:
    #         print("Error: ", error)
    #
    #
    #
    #
    # def modificaTipo(self):
    #     print()
    #
    # def borraTipoPorId(self):
    #     print()
