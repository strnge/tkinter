import tkinter as tk
from tkinter import ttk
class Tkinter_Test:
    def __init__(self, root):
        root.title("Hello World")
        root.geometry("160x160+250+250")
        frm = ttk.Frame(root, width=160, height=160, padding=10)#creates a frame widget that is fit inside the root window
        frm.grid()#initializes a relative grid for the window within the frame
        self.uname = tk.StringVar()
        self.uname_display = tk.StringVar()

        ttk.Label(frm, textvariable=self.uname_display).grid(column=2, row=1)#inserts a static label , using columns and rows for relative positioning within the previously created grid
        ttk.Entry(frm, textvariable=self.uname).grid(column=2, row=2)
        ttk.Button(frm, text="Submit",command=self.submit_name).grid(column=2, row=3)#creates a Quit button to the relative right of the label previously created
        ttk.Button(frm, text="Quit",command=root.destroy).grid(column=2, row=4)#creates a Quit button to the relative right of the label previously created


    def submit_name(self):
        try:
            self.uname_display.set(self.uname.get())
        except ValueError:
            pass

#root is the root of the window(top level window)
root = tk.Tk()
Tkinter_Test(root)
root.mainloop()#puts everything onto the display, runs main program loop/responds to user input until program is terminated
