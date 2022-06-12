import Services.StudentService
import Services.ClassService
import Services.TeacherService
import Services.SchoolService

from Models import Class

clservice = Services.ClassService.ClassService
stservice = Services.StudentService.StudentService
teservice = Services.TeacherService.TeacherService
scservice = Services.SchoolService.SchoolService

# Test StudentService
# Test GetAllStudents()
print("-------------------------------------")
print("Test: GetAllStudents")
result = stservice.GetAllStudents()
print(result)

# Test AddStudent()
print("-------------------------------------")
print("Test: AddStudent")
stservice.AddStudent("Keno", "Lendzion", 25, 1)
stservice.GetAllStudents()

# Test ClassServices
clservice.AddClassWithoutTeacherSchoolIds("KenosKlasse")
result = clservice.GetAllClasses()
print(result)
#clservice.AddClass("newclass", "12313", "1231231")

#stservice.AddStudent("Keno", "Lendzion", 69, 1)
#stservice.AddStudent("Keno", "Lendzion", 69, 1)
#stservice.AddStudent("Keno", "Lendzion", 69, 1)
#stservice.AddStudent("Keno", "Lendzion", 69, 1)
#stservice.AddStudent("Keno", "Lendzion", 69, 1)
#stservice.AddStudent("Keno", "Lendzion", 69, 1)
#stservice.AddStudent("Keno", "Lendzion", 69, 1)
#stservice.AddStudent("Keno", "Lendzion", 69, 1)
#singleClass = print(clservice.GetClass(2))
#print(singleClass)
#result = clservice.GetAllClasses()
#result = clservice.GetStudentsOfClass(1)
#
#print(result)

# Test TeacherService
#teservice.AddTeacher("keno", "lendzion", 69)

#teservice.AddTe
#result = teservice.GetAllTeachers()
#print(result)

# Test TeacherService
#scservice.AddSchool("keno", "lendzion", "69")
#result = scservice.GetAllSchools()
#print(result)