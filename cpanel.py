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

def showCpanel():
    global Cpanel
    Cpanel = Tk()
    Cpanel.geometry(f"{screenSize[0]}x{screenSize[1]}")
    Cpanel.resizable(0,0)

    frame = Frame(Cpanel, bg="orange", width=screenSize[0], height=screenSize[1])

    shopIcon = PhotoImage(file=r"images\shopicon.png")
    itemsIcon = PhotoImage(file=r"images\itemsicon.png")

    shops_button = Button(frame, image=shopIcon, bg="orange", fg="white", activebackground="orange", command = manageShopInit)
    items_button = Button(frame, image=itemsIcon, bg="orange", fg="white", activebackground="orange", command = manageItemInit)


    frame.place(x = 0, y = 0)
    shops_button.place(x = 550, y = 350)
    items_button.place(x = 760, y = 350)

    Cpanel.mainloop()
