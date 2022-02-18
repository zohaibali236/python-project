from tkinter import*
from tkinter import ttk
import mysql.connector as db
import ctypes

screenSize=[ctypes.windll.user32.GetSystemMetrics(0),ctypes.windll.user32.GetSystemMetrics(1)]

def back():
    from homepage import Showhomepage
    manageShopWindow.destroy()
    Showhomepage()

def ShowOurShops():

    global manageShopWindow
    manageShopWindow=Tk()

    manageShopWindow.geometry(f"{screenSize[0]}x{screenSize[1]}")
    manageShopWindow.resizable(0,0)

    orange_frame=Frame(manageShopWindow,bg="#febe53",width=1524,height=900)
    white_frame=Frame(manageShopWindow,bg="white",width=950,height=730)
    black_frame=Frame(manageShopWindow,bg="grey",width=725,height=690)
    manage_shops=Label(white_frame,text="OURSHOPS",bg="white",fg="#febe53",font=("aerial",25,"bold"))

    back_button = Button(orange_frame, text="Back", bg="#febe53", fg="white", font=("aerial", 13, "italic"), command = back)


    col=("sID","sName","sLoc")

    shops=ttk.Treeview(manageShopWindow,height=32,columns=col)

    shops.column("#0",width=0,minwidth=0)
    shops.column("sID",width=200,minwidth=200,anchor=CENTER)
    shops.column("sName",width=300,minwidth=300,anchor=CENTER)

    shops.column("sLoc",width=200,anchor=CENTER)
    shops.heading("sID",text="ID",anchor=CENTER)
    shops.heading("sName",text="Name",anchor=CENTER)
    shops.heading("sLoc",text="Location",anchor=CENTER)

    dbHandle=db.connect(
        host="localhost",
        user="root",
        password="",
        database="mall"
        )
    mysql_query=dbHandle.cursor()
    mysql_query.execute("SELECT ID,Name,Location FROM `shops`")
    
    cache_rows=mysql_query.fetchall()
    
    for i in cache_rows:
        shops.insert('',END,values=i)
    
    orange_frame.place(x=0,y=0)
    white_frame.place(x=300,y=50)
    black_frame.place(x=415,y=75)
    manage_shops.place(x=440,y=15)
    shops.place(x=426,y=85)
    back_button.place(x=150,y=730)

    manageShopWindow.mainloop()
