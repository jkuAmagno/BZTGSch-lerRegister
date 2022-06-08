import sqlite3

class ClassService:

    def AddClass(name, teacherId, schoolId):
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO Classes 
            VALUES(?,?,?)
        """,
        (name, teacherId, schoolId))
        connection.commit()
        connection.close()
        
    def GetClass(classId):
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        sqlQuery = "SELECT class.ROWID, class.* FROM CLASSES AS class WHERE class.ROWID = " + str(classId) 
        cursor.execute(sqlQuery)
        content = cursor.fetchall()
        return content

    def GetAllClasses():
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        sqlQuery = "SELECT class.ROWID, class.* FROM CLASSES AS class"
        cursor.execute(sqlQuery)
        content = cursor.fetchall()
        return content

    def GetStudentsOfClass(connection, classId):
        pass

    
    