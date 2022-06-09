import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
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

        GListBox_436=tk.Listbox(root)
        GListBox_436["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_436["font"] = ft
        GListBox_436["fg"] = "#333333"
        GListBox_436["justify"] = "center"
        GListBox_436.place(x=30,y=50,width=135,height=427)
        GListBox_436["listvariable"] = "ClassList"
        GListBox_436["selectmode"] = "single"

        GListBox_104=tk.Listbox(root)
        GListBox_104["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_104["font"] = ft
        GListBox_104["fg"] = "#333333"
        GListBox_104["justify"] = "center"
        GListBox_104.place(x=190,y=180,width=585,height=287)
        GListBox_104["listvariable"] = "StudentList"

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
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
