import sqlite3
class SchoolService:
    def AddSchool(self, name, city, zip):
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO Schools 
            VALUES(?,?,?)
        """,
        (name, city, zip))
        connection.commit()
        connection.close()

    def GetAllSchools(self):
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        sqlQuery = "SELECT school.ROWID, school.* FROM Schools AS school"
        cursor.execute(sqlQuery)
        content = cursor.fetchall()
        return content