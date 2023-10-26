from tkinter import *
root = Tk()

myLabel = Label(root, text="Are you are dumb?")
myLabel.pack()
b = Button(root, text="Yes")
c = Button(root, text="Hell yeah")
b.pack()
c.pack()

root.mainloop()