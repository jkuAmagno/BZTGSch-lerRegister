import tkinter as tk
import tkinter.font as tkFont
import Services.TeacherService as teacher

def CreateAddClassWindow(self, root):
    newWindow = tk.Toplevel(root)
    #setting title
    newWindow.title("Klasse Hinzufügen")
    #setting window size
    width=600
    height=500
    screenwidth = newWindow.winfo_screenwidth()
    screenheight = newWindow.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    newWindow.geometry(alignstr)
    newWindow.resizable(width=False, height=False)

    self.TeacherListBox=tk.Listbox(newWindow)
    self.TeacherListBox["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    self.TeacherListBox["font"] = ft
    self.TeacherListBox["fg"] = "#333333"
    self.TeacherListBox["justify"] = "center"
    self.TeacherListBox.place(x=20,y=50,width=201,height=425)
    teacherProperty = teacher.TeacherService.GetAllTeachers(self)
    for teacherObj  in teacherProperty:
        print(teacherObj[1])
        self.TeacherListBox.insert("end", teacherObj[2])
    self.selectedTeacherv = self.TeacherListBox.bind('<<ListboxSelect>>', self.teacher_selected)
    
    self.SelectTeacherLabel=tk.Label(newWindow)
    ft = tkFont.Font(family='Times',size=10)
    self.SelectTeacherLabel["font"] = ft
    self.SelectTeacherLabel["fg"] = "#333333"
    self.SelectTeacherLabel["justify"] = "center"
    self.SelectTeacherLabel["text"] = "Bitte Klassen Lehrer*in auswählen"
    self.SelectTeacherLabel.place(x=20,y=10,width=204,height=30)

    self.ClassLabel=tk.Label(newWindow)
    ft = tkFont.Font(family='Times',size=10)
    self.ClassLabel["font"] = ft
    self.ClassLabel["fg"] = "#333333"
    self.ClassLabel["justify"] = "center"
    self.ClassLabel["text"] = "Bitte klassen beziehungen eingeben: "
    self.ClassLabel.place(x=240,y=10,width=248,height=34)

    self.ClassnameInputEntry=tk.Entry(newWindow)
    self.ClassnameInputEntry["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    self.ClassnameInputEntry["font"] = ft
    self.ClassnameInputEntry["fg"] = "#333333"
    self.ClassnameInputEntry["justify"] = "center"
    self.ClassnameInputEntry["text"] = ""
    self.ClassnameInputEntry.place(x=260,y=50,width=213,height=30)

    self.AddClassButton=tk.Button(newWindow)
    self.AddClassButton["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=10)
    self.AddClassButton["font"] = ft
    self.AddClassButton["fg"] = "#000000"
    self.AddClassButton["justify"] = "center"
    self.AddClassButton["text"] = "Klasse Hinzufügen"
    self.AddClassButton.place(x=330,y=450,width=249,height=34)
    self.AddClassButton["command"] = self.AddClass_command
