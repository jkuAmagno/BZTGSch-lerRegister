import sqlite3
class TeacherService:
    def AddTeacher(firstname, lastname, age):
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO Teachers 
            VALUES(?,?,?)
        """,
        (firstname, lastname, age))
        connection.commit()
        connection.close()

    def GetAllTeachers():
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        sqlQuery = "SELECT teacher.ROWID, teacher.* FROM Teachers AS teacher"
        cursor.execute(sqlQuery)
        content = cursor.fetchall()
        return content