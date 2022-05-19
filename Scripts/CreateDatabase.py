import sqlite3
import os
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

StudentTable = """
    CREATE TABLE IF NOT EXISTS Students(
        StudentId INTEGER PRIMARY KEY AUTOINCREMENT
        ,Firstname VARCHAR(50)
        ,Lastname VARCHAR(50)
        ,Age INTEGER
        ,ClassId Integer
    )"""
ClassTable = """ 
    CREATE TABLE IF NOT EXISTS Classes(
        ClassId INTEGER PRIMARY KEY AUTOINCREMENT
        ,Name VARCHAR(50)
        ,TeacherId INTEGER
        ,SchoolId INTEGER
    )"""
TeacherTable = """
    CREATE TABLE IF NOT EXISTS Teacher(
        TeacherId INTEGER PRIMARY KEY AUTOINCREMENT
        ,Firstname VARCHAR(50)
        ,Lastname VARCHAR(50)
        ,Age INTEGER
    )"""
SchoolTable = """
    CREATE TABLE IF NOT EXISTS Teacher(
        SchoolId INTEGER PRIMARY KEY AUTOINCREMENT
        ,Name VARCHAR(50)
        ,City VARCHAR(50)
        ,Zip VARCHAR(50)
    )"""


# Create Script
CreateDatabase();
CreateTable(StudentTable)
CreateTable(ClassTable)
CreateTable(TeacherTable)
CreateTable(SchoolTable)





