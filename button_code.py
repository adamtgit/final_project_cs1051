from tkinter import *
 
root = Tk()             
 
root.geometry('100x100')
 
btn = Button(root, text = 'Help !', bd = '5',
                          command = root.destroy)
 
btn.pack(side = 'bottom')   
 
root.mainloop()

##from geeksforgeeks
