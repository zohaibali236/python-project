from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import ctypes
import pyodbc


screenSize = [ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)]


   
def back():
   manageShopWindow.destroy()
   from cpanel import showCpanel
   showCpanel()


def logout():
   manageShopWindow.destroy()
   from loginpage import ShowLoginPage
   ShowLoginPage()

def add():
   if(shopName.get() == "" or shopRent.get() == "" or shopLoc.get() == ""):
      return messagebox.showerror("Error!", "Fields cannot be empty")

   dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=.\shopping mall.accdb;')

   cur1 = dbHandle.cursor()
   cur1.execute(f"INSERT INTO shops (sID, sName, sLoc, sRent) VALUES('{shopID.get()}', '{shopName.get()}', '{shopRent.get()}', '{shopLoc.get()}')")
   dbHandle.commit()
   dbHandle.close()
   display()
   messagebox.showinfo("Information", f"{cur1.rowcount} new shop added")

def updateForEdit(_):
    current = shops.focus()
    currentItem = shops.item(current)
    currentItem = currentItem["values"]

    shopID.set(currentItem[0])
    shopName.set(currentItem[1])
    shopLoc.set(currentItem[2])
    shopRent.set(currentItem[3])


def edit():
   dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=.\shopping mall.accdb;')
   cur2 = dbHandle.cursor()
   q = f"update shops set sName='{shopName.get()}', sLoc='{shopLoc.get()}', sRent='{shopRent.get()}' where sID='{shopID.get()}'"
   cur2.execute(q)   
   dbHandle.commit()
   dbHandle.close()
   display()
   messagebox.showinfo("Information", f"{cur2.rowcount} shop updated")
  
  
      
def delete():
   if(shopID.get() == ""): return messagebox.showerror("Error!", "ID cannot be empty")
   dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=.\shopping mall.accdb;')
   cur3 = dbHandle.cursor()
   cur3.execute(f"DELETE FROM shops WHERE sID = '{shopID.get()}'")
   dbHandle.commit()
   dbHandle.close()
   display()
   messagebox.showinfo("Information", f"{cur3.rowcount} shop deleted")
   

def display():
   dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=.\shopping mall.accdb;')
   cur4 = dbHandle.cursor()
   cur4.execute("SELECT * FROM shops ORDER BY `sID` ASC")
   
   for rows in shops.get_children():
      shops.delete(rows)
   
   all_data = cur4.fetchall()
   if(len(all_data) == 0): return messagebox.showerror("Error!", "No data found to be displayed")

   j=0
   for i in all_data:
        id = i[0]
        name = i[1]
        loc = i[2]
        rent = i[3]
        if j % 2 == 0:
            shops.insert(parent='', index='end', iid=j, values=(id, name, loc, rent),tags=("even",))
        else:
            shops.insert(parent='', index='end', iid=j, values=(id, name, loc, rent), tags=("odd",))
        j += 1
   shops.tag_configure("even", foreground="black", background="gray82")
   shops.tag_configure("odd", foreground="black", background="white")
   dbHandle.close()

   shopID.set("")
   shopName.set("")
   shopRent.set("")
   shopLoc.set("")


def showManageShop():

   global manageShopWindow
   manageShopWindow = Tk()

   manageShopWindow.geometry(f"{screenSize[0]}x{screenSize[1]}")
   manageShopWindow.resizable(0,0)

   global shopID, shopName, shopRent, shopLoc

   shopID = StringVar()
   shopName = StringVar()
   shopRent= StringVar()
   shopLoc = StringVar()

   orange_frame = Frame(manageShopWindow, bg="#febe53", width=1524, height=900)
   white_frame = Frame(manageShopWindow, bg="white", width=1220, height=730)
   black_frame = Frame(manageShopWindow, bg="grey", width=1025, height=310 )
   manage_shops = Label(white_frame, text="MANAGE SHOPS", bg="white", fg="#febe53", font=("aerial", 25, "bold"))
   id = Label(white_frame, text="SHOP ID", bg="white", fg="#febe53", font=("aerial", 15, "bold"))
   name = Label(white_frame, text="NAME", bg="white", fg="#febe53", font=("aerial", 15, "bold"))
   rent = Label(white_frame, text="RENT", bg="white", fg="#febe53", font=("aerial", 15, "bold"))
   location = Label(white_frame, text="LOCATION", bg="white", fg="#febe53", font=("aerial", 15, "bold"))
   shops_label = Label(white_frame, text="SHOPS LIST", bg="white", fg="#febe53", font=("aerial", 25, "bold"))

   global shops
   col = ("sID", "sName", "sLoc", "sRent")
   shops = ttk.Treeview(manageShopWindow, height=13, columns=col)

   shops.column("#0", width=0, minwidth=0)
   shops.column("sID", width=200, minwidth=200, anchor=CENTER)
   shops.column("sName", width=300, minwidth=300, anchor=CENTER)
   shops.column("sLoc", width=300, minwidth=300, anchor=CENTER)
   shops.column("sRent", width=200, anchor=CENTER)

   shops.heading("sID", text="ID", anchor=CENTER)
   shops.heading("sName", text="Name", anchor=CENTER)
   shops.heading("sLoc", text="Location", anchor=CENTER)
   shops.heading("sRent", text="Rent", anchor=CENTER)

   shops.place(x=426, y=460)

   back_button = Button(orange_frame, text="Back", bg="#febe53", fg="white", font=("aerial", 13, "italic"), command = back)
   logout_button = Button(orange_frame, text="Logout", bg="#febe53", fg="white", font=("aerial", 13, "italic"), command = logout)
   add_button = Button(white_frame, text="ADD", bg="#febe53", fg="white", width=7, height=1,
                        font=("aerial", 15, "italic"), command=add)
   edit_button = Button(white_frame, text="EDIT", bg="#febe53", fg="white", width=7, height=1,
                           font=("aerial", 15, "italic"), command=edit)
   delete_button = Button(white_frame, text="DELETE", bg="#febe53", fg="white", width=7, height=1,
                           font=("aerial", 15, "italic"), command=delete)
   display_button = Button(white_frame, text="DISPLAY", bg="#febe53", fg="white", width=7, height=1,
                           font=("aerial", 15, "italic"), command=display)

   id_entry = Entry(white_frame, bg="white", textvariable=shopID, bd=3, width=25)
   name_entry = Entry(white_frame, bg="white", textvariable=shopName, bd=3, width=25)
   rent_entry = Entry(white_frame, bg="white", textvariable=shopRent, bd=3, width=25)
   location_entry = Entry(white_frame, bg="white", textvariable=shopLoc, bd=3, width=25)

   orange_frame.place(x=0, y=0)
   white_frame.place(x=300, y=50)
   black_frame.place(x=415, y=450)
   logout_button.place(x=150, y=730)
   manage_shops.place(x=440, y=15)
   id.place(x=100, y=110)
   id_entry.place(x=235, y=113)
   name.place(x=100, y=160)
   name_entry.place(x=235, y=163)
   rent.place(x=700, y=110)
   rent_entry.place(x=850, y=110)
   location.place(x=700, y=160)
   location_entry.place(x=850, y=160)
   add_button.place(x=250, y=270)
   edit_button.place(x=450, y=270)
   delete_button.place(x=650, y=270)
   display_button.place(x=850, y=270)
   shops_label.place(x=475, y=350)
   back_button.place(x=150, y=690)
   
   shops.bind("<Double-Button-1>", updateForEdit)

   manageShopWindow.mainloop()