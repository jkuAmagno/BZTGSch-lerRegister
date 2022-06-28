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

    studentService.AddStudent("Max", "Mustermann", 36, 1)
    studentService.AddStudent("Max", "Mustermann", 24, 1)
    studentService.AddStudent("Max", "Mustermann", 35, 1)
    studentService.AddStudent("Max", "Mustermann", 37, 1)
    studentService.AddStudent("Max", "Mustermann", 75, 1)
    studentService.AddStudent("Max", "Mustermann", 35, 1)
    studentService.AddStudent("Max", "Mustermann", 56, 1)
    studentService.AddStudent("Max", "Mustermann", 32, 1)
    studentService.AddStudent("Max", "Mustermann", 25, 1)
    studentService.AddStudent("Max", "Mustermann", 42, 1)
    studentService.AddStudent("Max", "Mustermann", 24, 1)
    studentService.AddStudent("Max", "Mustermann", 16, 1)
    studentService.AddStudent("Max", "Mustermann", 1, 1)
    studentService.AddStudent("Max", "Mustermann", 24, 1)
    studentService.AddStudent("Max", "Mustermann", 67, 1)
    studentService.AddStudent("Max", "Mustermann", 78, 1)
    studentService.AddStudent("Max", "Mustermann", 56, 1)
    studentService.AddStudent("Max", "Mustermann", 45, 1)
    studentService.AddStudent("Max", "Mustermann", 34, 1)
    studentService.AddStudent("Max", "Mustermann", 72, 1)
    studentService.AddStudent("Max", "Mustermann", 83, 1)
    studentService.AddStudent("Max", "Mustermann", 95, 1)
    studentService.AddStudent("Max", "Mustermann", 345, 1)
    studentService.AddStudent("Max", "Mustermann", 54, 1)
    studentService.AddStudent("Max", "Mustermann", 36, 1)
    studentService.AddStudent("Max", "Mustermann", 73, 1)
    studentService.AddStudent("Max", "Mustermann", 63, 1)
    studentService.AddStudent("Max", "Mustermann", 53, 1)
    studentService.AddStudent("Max", "Mustermann", 31, 1)
    studentService.AddStudent("Max", "Mustermann", 23, 1)

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










    

