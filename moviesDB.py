import mysql.connector
import config as cfg

class MovieDB:

    host = ""
    user = ""
    password = ""
    database = ""
    connection = ""
    cursor = ""

    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'kino'
        )
    
    def createEntry(self,values):
        cursor = self.db.cursor()
        sql="insert into movies (title,director,year,rating) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        newId = cursor.lastrowid
        return newId
    
    def getAllMovies(self):
        cursor = self.db.cursor()
        sql="select * from movies"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        return returnArray
    
    def findById(self, id):
        cursor = self.db.cursor()
        sql = "select * from movies where id=%s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)
    
    def updateEntry(self, values):
        cursor = self.db.cursor()
        sql = "update movie set title=%s,director=%s,year=%s,rating=%f where id=%s"
        cursor.execute(sql, values)
        self.db.commit()
    
    def deleteEntry(self, id):
        cursor = self.db.cursor()
        sql = "delete from movies where id=%s"
        values = (id,)

        cursor.execute(sql,values)
        self.db.commit()
        print("delete done")
    
    def convertToDictionary(self,result):
        colnames=['id','Title','Director','Year','Rating']
        item = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return item
    
    def closeAll(self):
        db.close()
        cursor.close()

movieDB = MovieDB()

