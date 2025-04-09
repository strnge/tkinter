import tkinter as tk
from tkinter import ttk
#root is the root of the window(top level window)
root = tk.Tk()
root.title("Hello World")
root.geometry("640x480+250+250")
frm = ttk.Frame(root, width=160, height=160, padding=10)#creates a frame widget that is fit inside the root window
frm.grid()#initializes a relative grid for the window within the frame
# titleframe = ttk.Frame(frm,padding=10).grid(column=2,row=1)
hWorld = tk.StringVar()
uname = tk.StringVar()
namebox = ttk.Entry(frm, textvariable=uname).grid(column=2, row=3)

ttk.Label(frm, textvariable=uname).grid(column=0,row=0)#inserts a static label , using columns and rows for relative positioning within the previously created grid
ttk.Button(frm, text="Quit",command=root.destroy).grid(column=2,row=2)#creates a Quit button to the relative right of the label previously created
root.mainloop()#puts everything onto the display, runs main program loop/responds to user input until program is terminated
