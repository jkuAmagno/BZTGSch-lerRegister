import tkinter as tk
import tkinter.font as tkFont

def CreateAddStudentWindow(self, root):
    newWindow = tk.Toplevel(root)
    #setting title
    newWindow.title("Schüler Hinzufügen")
    #setting window size
    width=400
    height=400
    screenwidth = newWindow.winfo_screenwidth()
    screenheight = newWindow.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    newWindow.geometry(alignstr)
    newWindow.resizable(width=False, height=False)

    GLabel_112=tk.Label(newWindow)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_112["font"] = ft
    GLabel_112["fg"] = "#333333"
    GLabel_112["justify"] = "center"
    GLabel_112["text"] = "Vorname:"
    GLabel_112.place(x=40,y=40,width=70,height=25)

    GLineEdit_890=tk.Entry(newWindow)
    GLineEdit_890["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_890["font"] = ft
    GLineEdit_890["fg"] = "#333333"
    GLineEdit_890["justify"] = "center"
    GLineEdit_890["text"] = "Entry"
    GLineEdit_890.place(x=160,y=40,width=169,height=30)
    firstnameEntry = GLineEdit_890.get()

    GLabel_405=tk.Label(newWindow)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_405["font"] = ft
    GLabel_405["fg"] = "#333333"
    GLabel_405["justify"] = "center"
    GLabel_405["text"] = "Nachname:"
    GLabel_405.place(x=40,y=90,width=70,height=25)

    GLineEdit_802=tk.Entry(newWindow)
    GLineEdit_802["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_802["font"] = ft
    GLineEdit_802["fg"] = "#333333"
    GLineEdit_802["justify"] = "center"
    GLineEdit_802["text"] = "Entry"
    GLineEdit_802.place(x=160,y=90,width=170,height=30)
    lastnameEntry = GLineEdit_802.get()

    GLabel_69=tk.Label(newWindow)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_69["font"] = ft
    GLabel_69["fg"] = "#333333"
    GLabel_69["justify"] = "center"
    GLabel_69["text"] = "Alter:"
    GLabel_69.place(x=30,y=140,width=70,height=25)

    GLineEdit_591=tk.Entry(newWindow)
    GLineEdit_591["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_591["font"] = ft
    GLineEdit_591["fg"] = "#333333"
    GLineEdit_591["justify"] = "center"
    GLineEdit_591["text"] = "Entry"
    GLineEdit_591.place(x=160,y=140,width=171,height=30)
    ageEntry = GLineEdit_591.get()

    GButton_175=tk.Button(newWindow)
    GButton_175["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_175["font"] = ft
    GButton_175["fg"] = "#000000"
    GButton_175["justify"] = "center"
    GButton_175["text"] = "Ok"
    GButton_175.place(x=300,y=360,width=70,height=25)
    #GButton_175[Command]
    
    

def SendNewStudentData_Button_command():
    """student.StudentService.AddStudent(firstnameEntr)"""
    print("command")
