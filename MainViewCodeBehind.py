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

    #region Main View
    def __init__(self, root):

        #initializecomponent
        MainView.CreateMainWindow(self, root)

    #region start MainView Buttons
    def AddStudentButton_command(self):
        NewStudentView.CreateAddStudentWindow(self, root)
        print("command")

 
        
    def AddClassButton_command(self):
        NewClassView.CreateAddClassWindow(self, root)
        "newClassObj = Models.Class();"    

    def UpdateButton_command(self):  
        self.GetAllClasses() 

    #endregion

    #endregion Main View

    def GetAllClasses(self):
        #Get Class to View
        allClasses = klass.ClassService.GetAllClasses()
        print(allClasses)
        for c in allClasses:
            self.ClassListBox.insert("end", c[1])
            self.UpdateButton_command
    
    def GetAllStudents(self):
        #Get Class to View
        allClasses = klass.ClassService.GetAllClasses()
        print(allClasses)
        for c in allClasses:
            self.ClassListBox.insert("end", c[1])
            self.UpdateButton_command
           
    def UpdateViewd(classId):
        classes = klass.ClassService.GetAllClasses()
        students = klass.ClassService.GetStudentsOfClass(classId)
        teacherProperties = teacher.TeacherService.GetAllTeachers()
    
        App.ClassListBox.insert(classes)
        App.StudentsListBox.insert(students)

        App.GLabel_278.config(text=teacherProperties[1])
        App.GLabel_102.config(text=teacherProperties[2])
        App.GLabel_868.config(text=teacherProperties[3])
    

    

    
             
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()