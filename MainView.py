import tkinter as tk
import tkinter.font as tkFont

def CreateMainWindow(self, root):
    #setting title    
    root.title("undefined")
    #setting window size
    width=800
    height=500
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)
    """
    def class_selected(event):
    selectedList = self.ClassListBox.curselection()
    selectedClass = ",".join([self.ClassListBox.get(i) for i in selectedList])
    self.UpdateView(selectedClass[0])
    """

    self.ClassListBox=tk.Listbox(root, )
    self.ClassListBox["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    self.ClassListBox["font"] = ft
    self.ClassListBox["fg"] = "#333333"
    self.ClassListBox["justify"] = "center"
    self.ClassListBox.place(x=30,y=50,width=135,height=382)
    self.ClassListBox["listvariable"] = "ClassList"
    self.ClassListBox["selectmode"] = "single"
    #self.ClassListBox.bind('<<ListboxSelect>>', class_selected)

    StudentsListBox=tk.Listbox(root)
    StudentsListBox["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    StudentsListBox["font"] = ft
    StudentsListBox["fg"] = "#333333"
    StudentsListBox["justify"] = "center"
    StudentsListBox.place(x=190,y=180,width=567,height=251)
    StudentsListBox["listvariable"] = "StudentList"

    #region start labels
    GLabel_693=tk.Label(root)
    ft = tkFont.Font(family='Times',size=16)
    GLabel_693["font"] = ft
    GLabel_693["fg"] = "#333333"
    GLabel_693["justify"] = "left"
    GLabel_693["text"] = "Schüler"
    GLabel_693.place(x=190,y=150,width=102,height=30)

    GLabel_313=tk.Label(root)
    ft = tkFont.Font(family='Times',size=16)
    GLabel_313["font"] = ft
    GLabel_313["fg"] = "#333333"
    GLabel_313["justify"] = "center"
    GLabel_313["text"] = "Klassen"
    GLabel_313.place(x=30,y=20,width=70,height=25)

    GLabel_908=tk.Label(root)
    ft = tkFont.Font(family='Times',size=16)
    GLabel_908["font"] = ft
    GLabel_908["fg"] = "#333333"
    GLabel_908["justify"] = "center"
    GLabel_908["text"] = "Lehrer"
    GLabel_908.place(x=190,y=20,width=70,height=25)

    GLabel_98=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_98["font"] = ft
    GLabel_98["fg"] = "#333333"
    GLabel_98["justify"] = "right"
    GLabel_98["text"] = "Nachname:"
    GLabel_98.place(x=200,y=90,width=70,height=25)

    GLabel_28=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_28["font"] = ft
    GLabel_28["fg"] = "#333333"
    GLabel_28["justify"] = "right"
    GLabel_28["text"] = "Vorname:"
    GLabel_28.place(x=200,y=60,width=70,height=25)

    GLabel_429=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_429["font"] = ft
    GLabel_429["fg"] = "#333333"
    GLabel_429["justify"] = "right"
    GLabel_429["text"] = "Alter:"
    GLabel_429.place(x=200,y=120,width=70,height=25)

    GLabel_429=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_429["font"] = ft
    GLabel_429["fg"] = "#333333"
    GLabel_429["justify"] = "right"
    GLabel_429["text"] = "Alter:"
    GLabel_429.place(x=200,y=120,width=70,height=25)

    GLabel_278=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_278["font"] = ft
    GLabel_278["fg"] = "#333333"
    GLabel_278["justify"] = "left"
    GLabel_278["text"] = "label"
    GLabel_278.place(x=300,y=60,width=450,height=25)

    GLabel_102=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_102["font"] = ft
    GLabel_102["fg"] = "#333333"
    GLabel_102["justify"] = "left"
    GLabel_102["text"] = "label"
    GLabel_102.place(x=300,y=90,width=446,height=25)

    GLabel_868=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_868["font"] = ft
    GLabel_868["fg"] = "#333333"
    GLabel_868["justify"] = "left"
    GLabel_868["text"] = "label"
    GLabel_868.place(x=300,y=120,width=450,height=25)

    #endregion end labels

    #region start Main Button
    UpdateButton=tk.Button(root)
    UpdateButton["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=10)
    UpdateButton["font"] = ft
    UpdateButton["fg"] = "#000000"
    UpdateButton["justify"] = "center"
    UpdateButton["text"] = "Update"
    UpdateButton.place(x=680,y=440,width=74,height=30)
    UpdateButton["command"] = self.UpdateButton_command

    AddStudentButton = tk.Button(root)
    AddStudentButton["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times', size=10)
    AddStudentButton["font"] = ft
    AddStudentButton["fg"] = "#000000"
    AddStudentButton["justify"] = "center"
    AddStudentButton["text"] = "Schüler Hinzufügen"
    AddStudentButton.place(x=540, y=440, width=119, height=30)
    AddStudentButton["command"] = self.AddStudentButton_command

    AddClassButton = tk.Button(root)
    AddClassButton["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times', size=10)
    AddClassButton["font"] = ft
    AddClassButton["fg"] = "#000000"
    AddClassButton["justify"] = "center"
    AddClassButton["text"] = "Klasse Hinzufügen"
    AddClassButton.place(x=370, y=440, width=146, height=30)
    AddClassButton["command"] = self.AddClassButton_command


