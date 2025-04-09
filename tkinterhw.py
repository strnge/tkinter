from tkinter import *
from tkinter import ttk
#root is the root of the window(top level window)
root = Tk()
frm = ttk.Frame(root, padding=10)#creates a frame widget that is fit inside the root window
frm.grid()#initializes a relative grid for the window within the frame
hWorld = "Hello World"
ttk.Label(frm, text=hWorld).grid(column=0, row=0)#inserts a static label , using columns and rows for relative positioning within the previously created grid
ttk.Button(frm, text="Quit",command=root.destroy).grid(column=1,row=0)#creates a Quit button to the relative right of the label previously created
root.mainloop()#puts everything onto the display, runs main program loop/responds to user input until program is terminated
