from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as db
import ctypes



screenSize = [ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)]


dbHandle = db.connect(
      host = "localhost",
      user = "root",
      password = "",
      database = "mall"
      )

def logout():
   from loginpage import ShowLoginPage
   manageShopWindow.destroy()
   ShowLoginPage()

def add():
   if(shopName.get() == "" or shopRent.get() == "" or shopLoc.get() == ""):
      return messagebox.showerror("Error!", "Fields cannot be empty")

   mysql_query = dbHandle.cursor(buffered=True)
   mysql_query.execute(f"INSERT INTO `shops` (`Name`, `Rent`, `Location`) VALUES ('{shopName.get()}', {shopRent.get()}, '{shopLoc.get()}')")
   dbHandle.commit()
   messagebox.showinfo("Information", f"{mysql_query.rowcount} Rows affected")
   mysql_query.close()
   display()

def edit(step):
   if(step == 0):
      if(shopID.get() == ""): return messagebox.showerror("Error!", "ID cannot be empty")
      elif(shopName.get() == "" or shopRent.get() == "" or shopLoc.get() == ""):
         edit(1)
      else: edit(2)
   elif(step == 1):
         if(shopName.get() == "" or shopRent.get() == "" or shopLoc.get() == ""):
            mysql_query = dbHandle.cursor(dictionary = True, buffered = True)
            mysql_query.execute(f"SELECT `Name`, `Rent`, `Location` FROM `shops` WHERE ID = '{shopID.get()}'")

            cache_result = mysql_query.fetchall()
            cache_result = cache_result[0]

            if(shopName.get() == ""): shopName.set(cache_result["Name"])
            if(shopRent.get() == ""): shopRent.set(cache_result["Rent"])
            if(shopLoc.get() == ""): shopLoc.set(cache_result["Location"])
   elif(step == 2):
      mysql_query = dbHandle.cursor(buffered=True)
      mysql_query.execute(f"UPDATE `shops` SET `Name`='{shopName.get()}', `Rent`='{shopRent.get()}', `Location`='{shopLoc.get()}' WHERE `ID`='{shopID.get()}'")
      dbHandle.commit()
      messagebox.showinfo("Information", f"{mysql_query.rowcount} Rows affected")
      mysql_query.close()
      display()
      
def delete():
   if(shopID.get() == ""): return messagebox.showerror("Error!", "ID cannot be empty")
   mysql_query = dbHandle.cursor(buffered=True)
   mysql_query.execute(f"DELETE FROM `shops` WHERE `ID` = '{shopID.get()}'")
   messagebox.showinfo("Information", f"{mysql_query.rowcount} Rows affected")
   dbHandle.commit()
   mysql_query.close()
   display()

def display():
   mysql_query = dbHandle.cursor(buffered=True)
   mysql_query.execute("SELECT * FROM `shops`")
   
   for rows in shops.get_children():
      shops.delete(rows)

   if(not mysql_query.rowcount): return messagebox.showerror("Error!", "No data found to be displayed")

   fetch = mysql_query.fetchall()
   for i in fetch:
      shops.insert('', END, values=i)
   mysql_query.close()

def showManageShop():

   global manageShopWindow
   manageShopWindow = Tk()

   manageShopWindow.geometry(f"{screenSize[0]}x{screenSize[1]}")

   global shopID, shopName, shopRent, shopLoc

   shopID = StringVar()
   shopName = StringVar()
   shopRent= StringVar()
   shopLoc = StringVar()

   orange_frame = Frame(manageShopWindow, bg="orange", width=1524, height=900)
   white_frame = Frame(manageShopWindow, bg="white", width=1220, height=730)
   black_frame = Frame(manageShopWindow, bg="grey", width=1025, height=310 )
   manage_shops = Label(white_frame, text="MANAGE SHOPS", bg="white", fg="orange", font=("aerial", 25, "bold"))
   id = Label(white_frame, text="SHOP ID", bg="white", fg="orange", font=("aerial", 15, "bold"))
   name = Label(white_frame, text="NAME", bg="white", fg="orange", font=("aerial", 15, "bold"))
   rent = Label(white_frame, text="RENT", bg="white", fg="orange", font=("aerial", 15, "bold"))
   location = Label(white_frame, text="LOCATION", bg="white", fg="orange", font=("aerial", 15, "bold"))
   shops_label = Label(white_frame, text="SHOPS LIST", bg="white", fg="orange", font=("aerial", 25, "bold"))

   global shops
   col = ("sID", "sName", "sRent", "sLoc")
   shops = ttk.Treeview(manageShopWindow, height=13, columns=col)

   shops.column("#0", width=0, minwidth=0)
   shops.column("sID", width=200, minwidth=200, anchor=CENTER)
   shops.column("sName", width=300, minwidth=300, anchor=CENTER)
   shops.column("sRent", width=300, minwidth=300, anchor=CENTER)
   shops.column("sLoc", width=200, anchor=CENTER)

   shops.heading("sID", text="ID", anchor=CENTER)
   shops.heading("sName", text="Name", anchor=CENTER)
   shops.heading("sRent", text="Rent", anchor=CENTER)
   shops.heading("sLoc", text="Location", anchor=CENTER)

   shops.place(x=426, y=460)

   logout_button = Button(orange_frame, text="Logout", bg="orange", fg="white", font=("aerial", 13, "italic"), command = logout)
   add_button = Button(white_frame, text="ADD", bg="orange", fg="white", width=7, height=1,
                        font=("aerial", 15, "italic"), command=add)
   edit_button = Button(white_frame, text="EDIT", bg="orange", fg="white", width=7, height=1,
                           font=("aerial", 15, "italic"), command=lambda: edit(0))
   delete_button = Button(white_frame, text="DELETE", bg="orange", fg="white", width=7, height=1,
                           font=("aerial", 15, "italic"), command=delete)
   display_button = Button(white_frame, text="DISPLAY", bg="orange", fg="white", width=7, height=1,
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

   manageShopWindow.mainloop()