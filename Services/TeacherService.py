import sqlite3
class TeacherService:
    def AddTeacher(self, firstname, lastname, age):
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO Teachers 
            VALUES(?,?,?)
        """,
        (firstname, lastname, age))
        connection.commit()
        connection.close()

    def GetAllTeachers(self):
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        sqlQuery = "SELECT teacher.ROWID, teacher.* FROM Teachers AS teacher"
        cursor.execute(sqlQuery)
        content = cursor.fetchall()
        return content

    def GetTeacher(self, teacherId):
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        sqlQuery = "SELECT teacher.ROWID, teacher.* FROM Teachers AS teacher WHERE teacher.ROWID = '" + str(teacherId) + "'"
        cursor.execute(sqlQuery)
        content = cursor.fetchall()
        return content

    def GetTeacherByName(self, Teachername):
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        sqlQuery = "SELECT teacher.ROWID, teacher.* FROM Teachers AS teacher WHERE teacher.Lastname = '" + str(Teachername) + "'"
        cursor.execute(sqlQuery)
        content = cursor.fetchall()
        return content
