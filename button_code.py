from tkinter import *
 
root = Tk()             
 
root.geometry('100x100')
 
btn = Button(root, text = 'Help !', bd = '5',
                          command = root.destroy)
 
btn.pack(side = 'bottom')   
 
root.mainloop()

##from geeksforgeeks

#How to add a button that prints something

import tkinter as tk
from tkinter import ttk

root = tk.Tk()


def button_clicked():
    print('Patient has died')


button = ttk.Button(root, text='Increase meds', command=button_clicked)
button.pack()

root.mainloop()
