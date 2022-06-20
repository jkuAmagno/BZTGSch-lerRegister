import sqlite3
import os

from ClassService   import ClassService
from TeacherService import TeacherService
from SchoolService  import SchoolService
from StudentService import StudentService

def CreateDatabase():
    if os.path.exists("Database/Register.db"):
        os.remove("Database/Register.db")
        
    connection = sqlite3.connect("Database/Register.db")
    connection.close()

def CreateTable(query):
    connection = sqlite3.connect("Database/Register.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def FillDatabase():
    classService = ClassService()
    studentService = StudentService()
    teacherService  = TeacherService()
    schoolService = SchoolService()
  
    schoolService.AddSchool("BBS Haarentor", "Oldenburg", 12345 )
    teacherService.AddTeacher("Max", "Lehrermann", 45)
    classService.AddClass("FA2C", 1, 1)

    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)
    studentService.AddStudent("Max", "Mustermann", 420, 1)

    print(schoolService.GetAllSchools())
    print(teacherService.GetAllTeachers())
    print(classService.GetAllClasses())
    print(studentService.GetAllStudents())

StudentTable = """
    CREATE TABLE IF NOT EXISTS Students(
        Firstname VARCHAR(50)
        ,Lastname VARCHAR(50)
        ,Age INTEGER
        ,ClassId Integer
    )"""
ClassTable = """ 
    CREATE TABLE IF NOT EXISTS Classes(
        Name VARCHAR(50)
        ,TeacherId INTEGER
        ,SchoolId INTEGER
    )"""
TeacherTable = """
    CREATE TABLE IF NOT EXISTS Teachers(
        Firstname VARCHAR(50)
        ,Lastname VARCHAR(50)
        ,Age INTEGER
    )"""
SchoolTable = """
    CREATE TABLE IF NOT EXISTS Schools(
        Name VARCHAR(50)
        ,City VARCHAR(50)
        ,Zip VARCHAR(50)
    )"""


# Create Script
CreateDatabase()
CreateTable(StudentTable)
CreateTable(ClassTable)
CreateTable(TeacherTable)
CreateTable(SchoolTable)
FillDatabase()










    
