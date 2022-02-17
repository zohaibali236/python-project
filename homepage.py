from tkinter import  *
from PIL import Image , ImageTk
from tkinter import ttk
import tkinter as tk
import ctypes

from loginpage import ShowLoginPage

screenSize = [ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)]


def loginPageinit():
    homepagewindow.destroy()
    ShowLoginPage()

homepagewindow = Tk()
homepagewindow.title("Elegante Shopping Mall")
homepagewindow.geometry(f"{screenSize[0]}x{screenSize[1]}")

image = Image.open(r"images\title.jpg")
imagenew = ImageTk.PhotoImage(image)
imagelabel = Label(homepagewindow, image=imagenew)
imagelabel.place(x=0,y=0)
#logo
f1=Frame(homepagewindow)
f1.place(x=10,y=10,width=260,height=250)
logo = PhotoImage(file=r'images\my.png')
label = ttk.Label(f1, image = logo)
PhotoImage(file=r'images\my.png')
label.pack()
#text
l1= Label(homepagewindow,text="Elegante Shopping Mall" , bg="black", fg="white",padx=15, pady=15,font=("Segoe Script",25,"bold"))
l1.pack()
#buttons
p1=PhotoImage(file=r'images\2.png')
b1=tk.Button(homepagewindow,image=p1,bg="DodgerBlue4",height=100,width=250, command=loginPageinit)
b1.place(x=270,y=100)

p2=PhotoImage(file=r'images\tg1.png')
b2=tk.Button(homepagewindow,image=p2,bg="DarkGoldenrod2",height=100,width=250)
b2.place(x=530,y=100)

p3=PhotoImage(file=r'images\a1.png')
b3=tk.Button(homepagewindow,image=p3,bg="white",height=100,width=250,)
b3.place(x=790,y=100)

p4=PhotoImage(file=r'images\c1.png')
b4=tk.Button(homepagewindow,image=p4,bg="white",height=100,width=250)
b4.place(x=1050,y=100)

homepagewindow.mainloop()
