import tkinter as tk
from tkinter import ttk


class Tkinter_Test:
    def __init__(self, root):
        self.utitle = tk.StringVar(value="Default title")
        root.title(self.utitle.get())
        root.geometry("320x240+250+250")
        root.rowconfigure((0,1,2,3,4,5,6),weight=1)
        root.columnconfigure(0, weight=1)
        frm = ttk.Frame(root, borderwidth=2, relief="sunken", width=240, height=240, padding=10)#creates a frame widget that is fit inside the root window
        frm.grid(rowspan=7, columnspan=2, sticky="nsew")#initializes a relative grid for the window within the frame
        frm.columnconfigure((0,1), weight=1)#used to control resize behavior of columns and rows, can either be used on a per row/col basis or on a list of rows/columns
        frm.rowconfigure((0,1,2,3,4,5,6), weight=1)

        self.ulabel = tk.StringVar(value="Label")#these tk stringvars are bound to python vars, and when updated are automatically reflected in the ui
        self.ulabel_display = tk.StringVar(value="Label")

        ttk.Label(frm, textvariable=self.ulabel_display).grid(column=0, row=0,)#inserts a static label , using columns and rows for relative positioning within the previously created grid
        ttk.Entry(frm, textvariable=self.ulabel).grid(column=0, row=1)#input field for user text
        ttk.Button(frm, text="Submit Label",command=self.submit_label).grid(column=0, row=2)#creates a submit button that will change the label above it directly below
        
        ttk.Label(frm, text="Window Title").grid(column=1, row=0)
        ttk.Entry(frm, textvariable=self.utitle).grid(column=1, row=1)#input field for user text
        ttk.Button(frm, text="Submit Title",command=self.submit_title).grid(column=1, row=2)#creates a submit button that will change the window title
        
        rightsideFrm = ttk.Frame(root, borderwidth=2, relief="groove", padding=5, width=80, height=240)#generates subframe for rightside
        rightsideFrm.grid(columnspan=2, column=2, rowspan=7, row=0, sticky="nsew")#sets up grid for placement control
       
        self.win_width = tk.StringVar(value="0")
        self.win_height = tk.StringVar(value="0")
        root.bind("<Configure>",self.on_resize)#binds the <Configure> event to callback the on_resize function, which will update the size display

        #create size display widgets
        ttk.Label(rightsideFrm, text="Width(px)").grid(column=0,row=1,rowspan=3)
        ttk.Label(rightsideFrm, textvariable=self.win_width).grid(column=1,row=1,rowspan=3,ipadx=3)
        ttk.Label(rightsideFrm, text="Height(px)").grid(column=0,row=4,rowspan=3)
        ttk.Label(rightsideFrm, textvariable=self.win_height).grid(column=1,row=4,rowspan=3,ipadx=3)

        #bottom span widget that contains 4x checkboxes
        bottomFrm = ttk.Frame(root, borderwidth=2, relief="groove", padding=5)
        bottomFrm.grid(columnspan=4, column=0, row=7, sticky="we")
        bottomFrm.columnconfigure((0,1,2,3), weight=1)
        
        ttk.Checkbutton(bottomFrm, text="Check 1").grid(column=0, row=7)
        ttk.Checkbutton(bottomFrm, text="Check 2").grid(column=1, row=7)
        ttk.Checkbutton(bottomFrm, text="Check 3").grid(column=2, row=7)
        ttk.Checkbutton(bottomFrm, text="Check 4").grid(column=3, row=7)
        
        ttk.Button(frm, text="Quit",command=root.destroy).grid(column=0, row=6, columnspan=2)#creates a Quit button
    
    def on_resize(self, event):
        try:
            container = str(event.widget)
            if (container == "."):
                if(self.win_height.get() != event.height or self.win_width.get() != event.width):
                    self.win_height.set(str(event.height))
                    self.win_width.set(str(event.width))
        except ValueError:
            pass
    def submit_label(self):
        try:
            self.ulabel_display.set(self.ulabel.get())
        except ValueError:
            pass
    def submit_title(self):
        try:
            root.title(self.utitle.get())
        except ValueError:
            pass        

#root is the root of the window(top level window)
root = tk.Tk()
Tkinter_Test(root)
root.mainloop()#puts everything onto the display, runs main program loop/responds to user input until program is terminated
