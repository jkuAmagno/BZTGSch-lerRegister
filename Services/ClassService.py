from hashlib import new
from msilib.schema import Class
import sqlite3
from unicodedata import name

class ClassService:
    def AddClass(self, name, teacherId, schoolId):
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO Classes 
            VALUES(?,?,?)
        """,
        (name, teacherId, schoolId))
        connection.commit()
        connection.close()

    def AddClassWithoutSchoolId(self, name, teacherId):
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO Classes 
            VALUES(?,?,?)
        """,
        (name, teacherId, -1))
        connection.commit()
        connection.close()

    def GetClass(self, classId):
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        sqlQuery = "SELECT class.ROWID, class.* FROM CLASSES AS class WHERE class.ROWID = " + str(classId) 
        cursor.execute(sqlQuery)
        content = cursor.fetchall()
        return content

    def GetAllClasses(self):
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        sqlQuery = "SELECT class.ROWID, class.* FROM CLASSES AS class"
        cursor.execute(sqlQuery)
        content = cursor.fetchall()
        return content
     
    def GetClassByName(self, className):
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        sqlQuery = "SELECT class.ROWID, class.* FROM CLASSES AS class WHERE class.Name = '" + str(className) +  "'"
        cursor.execute(sqlQuery)
        content = cursor.fetchall()
        return content

    def GetStudentsOfClass(self, classId):
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        sqlquery = "SELECT student.* FROM Students AS student WHERE student.classId =" + str(classId)
        cursor.execute(sqlquery)
        content = cursor.fetchall()
        return content