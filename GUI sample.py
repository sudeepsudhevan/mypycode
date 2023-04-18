from tkinter import *

window = Tk()


label=Label(window,text="Welcome")

def hello():
    print("button clicked")
button=Button(text="ok",command=hello)


button.pack()
label.pack()

window.mainloop()
