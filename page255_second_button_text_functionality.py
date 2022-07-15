
import tkinter as tk
from tkinter import *
m=Tk()
m.title("Hi")
btn=Button()
def clicked():
	
 print("Hi")

btn['command']=clicked
btn.pack()
m.geometry('300x300')
m.mainloop()
