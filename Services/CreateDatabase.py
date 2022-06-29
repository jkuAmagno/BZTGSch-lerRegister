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

    studentService.AddStudent("Max", "Maus", 36, 1)
    studentService.AddStudent("Tim", "Tastatur", 24, 1)
    studentService.AddStudent("Steffen", "Ameise", 35, 1)
    studentService.AddStudent("Oliver", "Eichhörnchen", 37, 1)
    studentService.AddStudent("Jonas", "Hippo", 75, 1)
    studentService.AddStudent("Margit", "Löwe", 35, 1)
    studentService.AddStudent("Baum", "Vogel", 56, 1)
    studentService.AddStudent("David", "Ente", 32, 1)
    studentService.AddStudent("Dave", "Busch", 25, 1)
    studentService.AddStudent("Donald", "Jonas", 42, 1)
    studentService.AddStudent("Dieter", "Dieter", 24, 1)
    studentService.AddStudent("Max", "Tim", 16, 1)
    studentService.AddStudent("Max2", "Dave", 1, 1)
    studentService.AddStudent("Dave", "Steffen", 24, 1)
    studentService.AddStudent("Jonas", "David", 67, 1)
    studentService.AddStudent("David", "Jonas", 78, 1)
    studentService.AddStudent("Steffen", "Dave", 56, 1)
    studentService.AddStudent("Dave", "Max2", 45, 1)
    studentService.AddStudent("Tim", "Max", 34, 1)
    studentService.AddStudent("Dieter", "Dieter", 72, 1)
    studentService.AddStudent("Jonas", "Donald", 83, 1)
    studentService.AddStudent("Busch", "Dave", 95, 1)
    studentService.AddStudent("Ente", "David", 345, 1)
    studentService.AddStudent("Vogel", "Baum", 54, 1)
    studentService.AddStudent("Löwe", "Margit", 36, 1)
    studentService.AddStudent("Hippo", "Jonas", 73, 1)
    studentService.AddStudent("Eichhörnchen", "Oliver", 63, 1)
    studentService.AddStudent("Ameise", "Steffen", 53, 1)
    studentService.AddStudent("Tastatur", "Tim", 31, 1)
    studentService.AddStudent("Maus", "Max", 23, 1)

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










    

