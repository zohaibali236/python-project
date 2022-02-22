from tkinter import *
import ctypes
from manageshop import showManageShop
from manageitem import showItemManage

screenSize = [ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)]

def manageShopInit():
    Cpanel.destroy()
    showManageShop()

def manageItemInit():
    Cpanel.destroy()
    showItemManage()

def logout():
   from loginpage import ShowLoginPage
   Cpanel.destroy()
   ShowLoginPage()


def showCpanel():
    global Cpanel
    Cpanel = Tk()
    Cpanel.geometry(f"{screenSize[0]}x{screenSize[1]}")
    Cpanel.resizable(0,0)

    frame = Frame(Cpanel, bg="#febe53", width=screenSize[0], height=screenSize[1])

    shopIcon = PhotoImage(file=r"images\shopicon.png")
    itemsIcon = PhotoImage(file=r"images\itemsicon.png")

    shops_button = Button(frame, image=shopIcon, bg="#febe53", fg="white", activebackground="#febe53", command = manageShopInit)
    items_button = Button(frame, image=itemsIcon, bg="#febe53", fg="white", activebackground="#febe53", command = manageItemInit)
    logout_button = Button(frame, text="Logout", bg="#febe53", fg="white", font=("aerial", 13, "italic"), command = logout)


    frame.place(x = 0, y = 0)
    shops_button.place(x = 550, y = 350)
    items_button.place(x = 760, y = 350)
    logout_button.place(x=150, y=730)

    Cpanel.mainloop()

showCpanel()