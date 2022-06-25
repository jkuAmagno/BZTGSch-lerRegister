import Services.StudentService
import Services.ClassService
import Services.TeacherService
import Services.SchoolService

from Models import Class

clservice = Services.ClassService.ClassService
stservice = Services.StudentService.StudentService
teservice = Services.TeacherService.TeacherService
scservice = Services.SchoolService.SchoolService

# Tests 

# School Service Tests
def TestAddSchool():
    print("-------------------------------------")
    print("Test: TestAddSchool")        
    scservice.AddSchool(scservice, "BBS HAARENTOR", "Oldenburg", 23155)
    print(scservice.GetAllSchools(teservice))

def TestGetAllSchools():
    print("-------------------------------------")
    print("Test: TestGetAllSchools")        
    result = scservice.GetAllSchools(scservice)
    print(result)

# Student Service Tests
def TestGetAllStudents():
    print("-------------------------------------")
    print("Test: GetAllStudents")
    result = stservice.GetAllStudents(stservice)
    print(result)

def TestAddStudent():
    print("-------------------------------------")
    print("Test: AddStudent")
    stservice.AddStudent("Keno", "Lendzion", 25, 1)
    print(stservice.GetAllStudents(stservice))

# Teacher Service Tests
def TestAddTeacher():
    print("-------------------------------------")
    print("Test: TestAddTeacher")        
    teservice.AddTeacher(teservice, "Keno", "Lendzion", 223)
    print(teservice.GetTeacherByName(teservice, "Lendzion"))

def TestGetAllTeachers():
    print("-------------------------------------")
    print("Test: TestGetAllTeachers")   
    print(teservice.GetAllTeachers(teservice))

def TestGetTeacher():
    print("-------------------------------------")
    print("Test: TestGetTeacher")     
    print(teservice.GetTeacher(teservice, 1))

def TestGetTeacherByName():
    print("-------------------------------------")
    print("Test: TestGetTeacherByName")        
    print(teservice.GetTeacherByName(teservice, "Lendzion"))

# Class Service Tests
def TestAddClass():
    print("-------------------------------------")
    print("Test: TestAddClass")  
    clservice.AddClass(clservice, "FA2C", 1, 1)
    print(clservice.GetAllClasses(clservice))

def TestAddClassWithoutSchoolId():
    print("-------------------------------------")
    print("Test: TestAddClassWithoutSchoolId")  
    clservice.AddClassWithoutSchoolId(clservice, "FA2C", 1)
    print(clservice.GetAllClasses(clservice))

def TestGetClass():
    print("-------------------------------------")
    print("Test: TestGetClass")  
    print(clservice.GetClass(clservice,1))

def TestGetAllClasses():
    print("-------------------------------------")
    print("Test: TestGetAllClasses")  
    print(clservice.GetAllClasses(clservice))

def TestGetClassByName():
    print("-------------------------------------")
    print("Test: TestGetClassByName")  
    print(clservice.GetClassByName(clservice,"FA2C"))

def TestGetStudentsOfClass():
    print("-------------------------------------")
    print("Test: TestGetStudentsOfClass")  
    print(clservice.GetStudentsOfClass(clservice, 1))
    
# Call specific  Tests Here
TestGetStudentsOfClass()
