import Services.StudentService
import Services.ClassService
import Services.TeacherService
import Services.SchoolService

from Models import Class

#clservice = Services.ClassService.ClassService
#stservice = Services.StudentService.StudentService
#teservice = Services.TeacherService.TeacherService
scservice = Services.SchoolService.SchoolService
# Test StudentService
#stservice.AddStudent("keno", "lendzion", 69, 1)
#result = stservice.GetAllStudents()
#print(result)

# Test ClassService
#print(clservice.AddClass("newclass", "12313", "1231231"))
#singleClass = print(clservice.GetClass(2))
#print(singleClass)
#result = clservice.GetAllClasses()
#print(result)


# Test TeacherService
#teservice.AddTeacher("keno", "lendzion", 69)
#result = teservice.GetAllTeachers()
#print(result)

# Test TeacherService
scservice.AddSchool("keno", "lendzion", "69")
result = scservice.GetAllSchools()
print(result)