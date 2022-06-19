import tkinter as tk
import tkinter.font as tkFont

def CreateAddClassWindow(self, root):
    newWindow = tk.Toplevel(root)
    #setting title
    newWindow.title("Klasse Hinzufügen")
    #setting window size
    width=400
    height=400
    screenwidth = newWindow.winfo_screenwidth()
    screenheight = newWindow.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    newWindow.geometry(alignstr)
    newWindow.resizable(width=False, height=False)

    GLabel_315=tk.Label(newWindow)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_315["font"] = ft
    GLabel_315["fg"] = "#333333"
    GLabel_315["justify"] = "center"
    GLabel_315["text"] = "Klassen name eingeben:"
    GLabel_315.place(x=20,y=30,width=159,height=30)

    GLineEdit_296=tk.Entry(newWindow)
    GLineEdit_296["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_296["font"] = ft
    GLineEdit_296["fg"] = "#333333"
    GLineEdit_296["justify"] = "center"
    GLineEdit_296["text"] = "Entry"
    className =GLineEdit_296.get()
    GLineEdit_296.place(x=190,y=30,width=173,height=30)
    
    GButton_924=tk.Button(newWindow)
    GButton_924["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=10)
    GButton_924["font"] = ft
    GButton_924["fg"] = "#000000"
    GButton_924["justify"] = "center"
    GButton_924["text"] = "Ok"
    GButton_924.place(x=300,y=350,width=70,height=25)
    #GButton_924["command"] = self.SendNewClassData_Button_command

def SendNewClassData_Button_command(self):
    #Services.ClassService.ClassService.AddClassWithoutTeacherSchoolIds(className)
    print("command")
    
