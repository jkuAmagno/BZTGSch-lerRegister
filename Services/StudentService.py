import sqlite3
class StudentService:
    def AddStudent(self, firstname, lastname, age, classId):
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO Students 
            VALUES(?,?,?,?)
        """,
        (firstname, lastname, age, classId))
        connection.commit()
        connection.close()

    def GetAllStudents(self):
        connection = sqlite3.connect("Database/Register.db")
        cursor = connection.cursor()
        sqlQuery = "SELECT student.ROWID, student.* FROM Students AS student"
        cursor.execute(sqlQuery)
        content = cursor.fetchall()
        return content