import sqlite3


class ConexionDB():
    # En el metodo constructor creamos una atributo llamado conexion y hacemos la conexion ala base de datos
    def __init__(self):
        try:
            self.conexion = sqlite3.connect("db/db.db")
            #("Conexion exitosa")
        except Exception as e:
            print(e)

    #Creamos un metodo para cerrar la conexion de la BD
    def close(self):
        self.conexion.close()

    # Creamos un metodo para abrir la conexion de la BD
    def open(self):
        self.conexion = sqlite3.connect('db/db.db')
        self.cursor = self.conexion.cursor()

    # Creamos un metodo para crear la tabla donde vamos a guardar la informacion
    def createTable(self):
        try:
            self.open()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS tabla (id INTEGER PRIMARY KEY AUTOINCREMENT, region TEXT, country TEXT, language TEXT, time REAL)")
            self.conexion.commit()
        except Exception as error:
            print ("Error creando tabla", error)
        finally:
            self.close()

    # Creamos un metodo para retornar las filas de la tabla
    def showRow(self):
        try:
            self.open()
            self.cursor.execute(f"SELECT * FROM tabla")
            rows = self.cursor.fetchall()
            self.close()
            return rows
        except Exception as error:
            self.close()
            print("Error ShowRow", error)

    # Creamos un metodo para agregar registros ala tabla
    def addRow(self, fila):
        try:
            self.open()
            self.cursor.execute(f"INSERT INTO tabla (region, country, language, time) VALUES (?, ?, ? ,?)", fila)
            self.conexion.commit()
            self.close()
        except Exception as error:
            self.close()
            print ("Error addRow", error)