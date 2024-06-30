import cx_Oracle

class Autor:
    def __init__(self):
        """Con la función connect nos conectamos a ORACLE, indicando el servidor, puerto, usuario, contraseña y
               base de datos."""
        self.__connect = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
        """Creamos un cursor (tupla) para almacenar los datos devueltos por la consulta. El Método cursor() devuelve un 
        objeto que permite ejecutar cualquier instrucción SQL"""
        self.__cursor = self.__connect.cursor()

    def ultimoId(self):
        res= None
        consulta = "SELECT MAX(ID) from PRO_AUTOR"
        try:
            self.__cursor.execute(consulta)
            res = 0
            for dat in self.__cursor:
                print(dat)
                if dat is None or dat < 1:
                    res = 1
                else:
                    res = int(dat) + 1
            print(res)
            return res
        except self.__connect.Error as error:
            print("Error: ", error)

    def insautor(self,nom,ape,res,foto):
        id = int(self.ultimoId())
        r = 0
        consultaAlta = ('INSERT INTO PRO_AUTOR(ID,NOMBRE,APELLIDOS,RESUMEN,FOTO) '
                        'VALUES(:P1,UPPER(:P2),UPPER(:P3),:P4,:P5)')
        try:
            id=self.ultimoId()
            print(id)
            self.__cursor.execute(consultaAlta, (id, nom, ape,res,foto))
            r = self.__cursor.rowcount
            if r > 0:
                self.__connect.commit()
            return r
        except self.__connect.Error as error:
            print("Error: ", error)
    def modautor(self,id,nom,ape,res,foto) :
       r = 0
       consultaMod = 'UPDATE PRO_AUTOR SET NOMBRE=UPPER(:P1),APELLIDOS=UPPER(:P2),RESUMEN=:P3,FOTO=:P4 WHERE ID=:P5'
       try:
           self.__cursor.execute(consultaMod, (nom, ape, res, foto,id))
           r = self.__cursor.rowcount
           if r > 0:
               self.__connect.commit()
           return r
       except self.__connect.Error as error:
           print("Error: ", error)

    def delautor(self,id):
        r = 0
        consultaDel = 'DELETE FROM PRO_AUTOR WHERE ID=:P5'
        try:
            self.__cursor.execute(consultaDel, (id))
            r = self.__cursor.rowcount
            if r > 0:
                self.__connect.commit()
            return r
        except self.__connect.Error as error:
            print("Error: ", error)

    def autores(self):
        consulta="SELECT ID,NOMBRE,APELLIDOS,RESUMEN,FOTO FROM PRO_AUTOR "
        try:
            return self.__cursor.execute(consulta)
        except self.__connect.Error as error:
            print("Error: ", error)

    def autorById(self,id):
        consulta = "SELECT ID,NOMBRE,APELLIDOS,RESUMEN,FOTO FROM PRO_AUTOR WHERE ID=:P1"
        try:
            return self.__cursor.execute(consulta,(id,))
        except self.__connect.Error as error:
            print("Error: ", error)
