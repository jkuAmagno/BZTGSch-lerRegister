from optparse import Values
import tkinter as tk
import tkinter.font as tkFont
from  Services.ClassService import ClassService as klass
import Services.StudentService as student
import Services.TeacherService as teacher
import Services.ClassService as klass
import Models.Class
import MainView
import NewClassView
import NewStudentView

#root = tk.Tk()
class App:

    def __init__(self, root):

        #initializecomponent
        MainView.CreateMainWindow(self, root)

#region MainView Buttons
    def AddStudentButton_command(self):
        NewStudentView.CreateAddStudentWindow(self, root)
        print("command")
    
    def AddClassButton_command(self):
        NewClassView.CreateAddClassWindow(self, root)
        "newClassObj = Models.Class();"    

    def UpdateButton_command(self):  
        self.GetAllClasses() 

#endregion

#region MainView Methoden

    def GetAllClasses(self):
        #Get Class to View
        allClasses = klass.ClassService.GetAllClasses(self)
        print(allClasses)
        for c in allClasses:
            self.ClassListBox.insert("end", c[1])
            
    def GetAllStudents(self):
        #Get Class to View
        allClasses = klass.ClassService.GetAllClasses(self)
        print(allClasses)
        for c in allClasses:
            self.ClassListBox.insert("end", c[1])
                    
    def UpdateView(self, classId, teacherId ):
        #classes = klass.ClassService.GetAllClasses(self)
        teacherProperties = teacher.TeacherService.GetTeacher(self, teacherId)
        students = klass.ClassService.GetStudentsOfClass(self, classId)
        for student in students:
            self.StudentTree.insert("", "end", values = (student[0], student[1], student[2]))          
       
        for techer in teacherProperties:           
            self.FirstnameLabel.config(text=techer[1])
            self.LastnameLabel.config(text=techer[2])
            self.AgeLabel.config(text=techer[3])
  
    def class_selected(self, event):
        selectedList = self.ClassListBox.curselection()
        selectedClass = ",".join([self.ClassListBox.get(i) for i in selectedList])
        classesrProperties = klass.ClassService.GetClassByName(self, selectedClass)  
        for calssObj in classesrProperties:
            classId = calssObj[0]
            teacherId = calssObj[2] 
        self.UpdateView(classId, teacherId)

#endregion 
#region NewClassView Methoden

    global selectedTeacherId 
    def teacher_selected(self, event ):    
        selectedList = self.TeacherListBox.curselection()
        selectedTeacher = ",".join([self.TeacherListBox.get(i) for i in selectedList])
        teacherProperties = teacher.TeacherService.GetTeacherByName(self, selectedTeacher)
        for teacherObj in teacherProperties:
            selectedTeacherId = teacherObj[0]

        NewClassName = self.ClassnameInputEntry.get()    
        klass.ClassService.AddClassWithoutSchoolId(self, NewClassName, selectedTeacherId)

    def AddClass_command(self): 
          NewClassName = self.ClassnameInputEntry.get()
          print(self.selectedTeacherv)

#endregion

#region NewStudentView Commands
    def AddStudent_command(self):
        print("command")

    def selected_classInStudentView(self, event):
        selectedList = self.ClassListBoxInStudentView.curselection()
        selectedClass = ",".join([self.ClassListBoxInStudentView.get(i) for i in selectedList])
        classesrProperties = klass.ClassService.GetClassByName(self, selectedClass)  

        for calssObj in classesrProperties:
            classId = calssObj[0]
        self.AddStudent(classId)
    """
    def GetStudentInputData(self):
        StudentFirstname = self.FirstnameInputEntry.get()
        StudentLastname = self.LastnameInputEntry.get()
        StudentAge = self.AgeInputEntry.get()
    """
    def AddStudent(self, selectedClassId):
        StudentFirstname = self.FirstnameInputEntry.get()
        StudentLastname = self.LastnameInputEntry.get()
        StudentAge = self.AgeInputEntry.get()
        student.StudentService.AddStudent(self, StudentFirstname, StudentLastname, StudentAge, selectedClassId)

#endregion
                     
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()