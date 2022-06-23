import tkinter as tk
import tkinter.font as tkFont
import Services.ClassService as klass

def CreateAddStudentWindow(self, root):
    newWindow = tk.Toplevel(root)
    #setting title
    newWindow.title("Schüler Hinzufügen")
    #setting window size
    width=600
    height=500
    screenwidth = newWindow.winfo_screenwidth()
    screenheight = newWindow.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    newWindow.geometry(alignstr)
    newWindow.resizable(width=False, height=False)

    self.ClassListBoxInStudentView=tk.Listbox(newWindow)
    self.ClassListBoxInStudentView["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    self.ClassListBoxInStudentView["font"] = ft
    self.ClassListBoxInStudentView["fg"] = "#333333"
    self.ClassListBoxInStudentView["justify"] = "center"
    self.ClassListBoxInStudentView.place(x=380,y=50,width=201,height=425)
    classProperty = klass.ClassService.GetAllClasses(self)
    for classObj  in classProperty:
        print(classObj[1])
        self.ClassListBoxInStudentView.insert("end", classObj[1])
        self.ClassListBoxInStudentView.bind('<<ListboxSelect>>', self.selected_classInStudentView)
    
    self.SelectClassLeabel=tk.Label(newWindow)
    ft = tkFont.Font(family='Times',size=10)
    self.SelectClassLeabel["font"] = ft
    self.SelectClassLeabel["fg"] = "#333333"
    self.SelectClassLeabel["justify"] = "center"
    self.SelectClassLeabel["text"] = "Bitte Klasse auswählen"
    self.SelectClassLeabel.place(x=370,y=10,width=204,height=30)

    self.FirstnameLabel=tk.Label(newWindow)
    ft = tkFont.Font(family='Times',size=10)
    self.FirstnameLabel["font"] = ft
    self.FirstnameLabel["fg"] = "#333333"
    self.FirstnameLabel["justify"] = "center"
    self.FirstnameLabel["text"] = "Vorname: "
    self.FirstnameLabel.place(x=0,y=50,width=97,height=30)

    self.FirstnameInputEntry=tk.Entry(newWindow)
    self.FirstnameInputEntry["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    self.FirstnameInputEntry["font"] = ft
    self.FirstnameInputEntry["fg"] = "#333333"
    self.FirstnameInputEntry["justify"] = "center"
    self.FirstnameInputEntry["text"] = ""
    self.FirstnameInputEntry.place(x=120,y=50,width=213,height=30)

    self.LastnameLabel=tk.Label(newWindow)
    ft = tkFont.Font(family='Times',size=10)
    self.LastnameLabel["font"] = ft
    self.LastnameLabel["fg"] = "#333333"
    self.LastnameLabel["justify"] = "center"
    self.LastnameLabel["text"] = "Nachname: "
    self.LastnameLabel.place(x=20,y=110,width=70,height=25)

    self.LastnameInputEntry=tk.Entry(newWindow)
    self.LastnameInputEntry["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    self.LastnameInputEntry["font"] = ft
    self.LastnameInputEntry["fg"] = "#333333"
    self.LastnameInputEntry["justify"] = "center"
    self.LastnameInputEntry["text"] = ""
    self.LastnameInputEntry.place(x=120,y=110,width=213,height=30)

    self.AgeLabel=tk.Label(newWindow)
    ft = tkFont.Font(family='Times',size=10)
    self.AgeLabel["font"] = ft
    self.AgeLabel["fg"] = "#333333"
    self.AgeLabel["justify"] = "center"
    self.AgeLabel["text"] = "Alter: "
    self.AgeLabel.place(x=0,y=170,width=70,height=25)

    self.AgeInputEntry=tk.Entry(newWindow)
    self.AgeInputEntry["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    self.AgeInputEntry["font"] = ft
    self.AgeInputEntry["fg"] = "#333333"
    self.AgeInputEntry["justify"] = "center"
    self.AgeInputEntry["text"] = "Entry"
    self.AgeInputEntry.place(x=120,y=170,width=212,height=30)

    self.AddNewStudentButton=tk.Button(newWindow)
    self.AddNewStudentButton["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=10)
    self.AddNewStudentButton["font"] = ft
    self.AddNewStudentButton["fg"] = "#000000"
    self.AddNewStudentButton["justify"] = "center"
    self.AddNewStudentButton["text"] = "Schüler Hinzufügen"
    self.AddNewStudentButton.place(x=30,y=450,width=249,height=34)
    self.AddNewStudentButton["command"] = self.AddStudent_command

def SendNewStudentData_Button_command():
    print("command")
