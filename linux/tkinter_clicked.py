from tkinter import *

root=Tk()
root.title('test')
root.geometry("400x400")

def clicker(event):
	mylabel=Label(root,text="you clicked a button")
	mylabel.pack()	


mybutton=Button(root,text="click Me")
mybutton.bind("<Return>",clicker)
mybutton.pack(pady=20)
	
root.mainloop()