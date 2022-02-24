USE_SQL_SERVER = True

"""Importing modules"""
from tkinter import*

from datetime import datetime
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
"""End of importing modules"""


"""Connecting to DB"""
if(USE_SQL_SERVER):
    import mysql.connector as db
    try:
        dbHandle = db.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database = "mall"
        )
    except db.Error as error:
        print(error, datetime.now())

else:
    import pyodbc
    dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                          r'DBQ=C:\Users\Xmart\Documents\shopping mall.accdb;')

"""Getting screen size"""
screenSize = [ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)]

"""windows"""
m1 = Tk()


"""window sizes"""
m1.state('zoomed')

"""window titles"""
m1.title("Shopping mall")

def manageShopWindow():
    manageshopwindow = Tk()

    global shopID, shopName, shopRent, shopLoc

    shopID = StringVar()
    shopName = StringVar()
    shopRent= StringVar()
    shopLoc = StringVar()


    #frames and windows
    orange_frame = Frame(manageshopwindow, bg="orange", width=1524, height=900)
    white_frame = Frame(manageshopwindow, bg="white", width=1220, height=730)
    black_frame = Frame(manageshopwindow, bg="grey", width=1025, height=310 )
    manage_shops = Label(white_frame, text="MANAGE SHOPS", bg="white", fg="orange", font=("aerial", 25, "bold"))
    id = Label(white_frame, text="SHOP ID", bg="white", fg="orange", font=("aerial", 15, "bold"))
    name = Label(white_frame, text="NAME", bg="white", fg="orange", font=("aerial", 15, "bold"))
    rent = Label(white_frame, text="RENT", bg="white", fg="orange", font=("aerial", 15, "bold"))
    location = Label(white_frame, text="LOCATION", bg="white", fg="orange", font=("aerial", 15, "bold"))

    global shops
    shops = Label(white_frame, text="SHOPS LIST", bg="white", fg="orange", font=("aerial", 25, "bold"))

    #columns
    col = ("sID", "sName", "sRent", "sLoc")
    shops = ttk.Treeview(manageshopwindow, height=13, columns=col)
    shops.column("#0", width=0, minwidth=0)
    shops.column("sID", width=200, minwidth=200, anchor=CENTER)
    shops.column("sName", width=300, minwidth=300, anchor=CENTER)
    shops.column("sRent", width=300, minwidth=300, anchor=CENTER)
    shops.column("sLoc", width=200, anchor=CENTER)
    shops.heading("sID", text="ID", anchor=CENTER)
    shops.heading("sName", text="Name", anchor=CENTER)
    shops.heading("sRent", text="Rent", anchor=CENTER)
    shops.heading("sLoc", text="Location", anchor=CENTER)

    #buttons
    logout_button = Button(orange_frame, text="Logout", bg="orange", fg="white", font=("aerial", 13, "italic"))
    add_button = Button(white_frame, text="ADD", bg="orange", fg="white", width=7, height=1,
                        font=("aerial", 15, "italic"), command=manageShopWindow_add)
    edit_button = Button(white_frame, text="EDIT", bg="orange", fg="white", width=7, height=1,
                            font=("aerial", 15, "italic"), command=lambda: manageShopWindow_edit(0))
    delete_button = Button(white_frame, text="DELETE", bg="orange", fg="white", width=7, height=1,
                            font=("aerial", 15, "italic"), command=manageShopWindow_delete)
    display_button = Button(white_frame, text="DISPLAY", bg="orange", fg="white", width=7, height=1,
                            font=("aerial", 15, "italic"), command=manageShopWindow_display)

    # entry boxes
    id_entry = Entry(white_frame, bg="white", textvariable=shopID, bd=3, width=25)
    name_entry = Entry(white_frame, bg="white", textvariable=shopName, bd=3, width=25)
    rent_entry = Entry(white_frame, bg="white", textvariable=shopRent, bd=3, width=25)
    location_entry = Entry(white_frame, bg="white", textvariable=shopLoc, bd=3, width=25)

    #placing widgets
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
    shops.place(x=426, y=460)


    manageshopwindow.mainloop()

def manageShopWindow_add():
   if(shopName.get() == "" or shopRent.get() == "" or shopLoc.get() == ""):
      return messagebox.showerror("Error!", "Fields cannot be empty")

   mysql_query = dbHandle.cursor(buffered = True)
   mysql_query.execute(f"INSERT INTO `shops` (`Name`, `Rent`, `Location`) VALUES ('{shopName.get()}', {shopRent.get()}, '{shopLoc.get()}')")
   dbHandle.commit()
   messagebox.showinfo("Information", f"{mysql_query.rowcount} Rows affected")
   mysql_query.close()
   display()


def manageShopWindow_edit(step):
   if(step == 0):
      if(shopID.get() == ""): return messagebox.showerror("Error!", "ID cannot be empty")
      elif(shopName.get() == "" or shopRent.get() == "" or shopLoc.get() == ""):
         manageShopWindow_edit(1)
      else: manageShopWindow_edit(2)
   elif(step == 1):
         if(shopName.get() == "" or shopRent.get() == "" or shopLoc.get() == ""):
            mysql_query = dbHandle.cursor(dictionary = True)
            mysql_query.execute(f"SELECT `Name`, `Rent`, `Location` FROM `shops` WHERE ID = '{shopID.get()}'")

            cache_result = mysql_query.fetchall()
            cache_result = cache_result[0]

            if(shopName.get() == ""): shopName.set(cache_result["Name"])
            if(shopRent.get() == ""): shopRent.set(cache_result["Rent"])
            if(shopLoc.get() == ""): shopLoc.set(cache_result["Location"])
   elif(step == 2):
      mysql_query = dbHandle.cursor(buffered = True)
      mysql_query.execute(f"UPDATE `shops` SET `Name`='{shopName.get()}', `Rent`='{shopRent.get()}', `Location`='{shopLoc.get()}' WHERE `ID`='{shopID.get()}'")
      dbHandle.commit()
      messagebox.showinfo("Information", f"{mysql_query.rowcount} Rows affected")
      display()
 
      
def manageShopWindow_delete():
   if(shopID.get() == ""): return messagebox.showerror("Error!", "ID cannot be empty")
   mysql_query = dbHandle.cursor(buffered = True)
   mysql_query.execute(f"DELETE FROM `shops` WHERE `ID` = '{shopID.get()}'")
   messagebox.showinfo("Information", f"{mysql_query.rowcount} Rows affected")
   manageShopWindow_display ()

def manageShopWindow_display():
   mysql_query = dbHandle.cursor(buffered = True)
   mysql_query.execute("SELECT * FROM `shops`")

   if(not mysql_query.rowcount): return messagebox.showerror("Error!", "No data found to be displayed")

   for rows in shops.get_children():
      shops.delete(rows)

   fetch = mysql_query.fetchall()
   for i in fetch:
      shops.insert('', END, values=i)
   mysql_query.close()


def cmd():

    m1.destroy()
    global loginPage
    loginPage = Tk()
    loginPage.title("Login")
    loginPage.configure(bg="white")
    loginPage.state('zoomed')

    backgroundimage = ImageTk.PhotoImage(file=r"images\icon.jpg", master = loginPage)
    Label(loginPage, image=backgroundimage, bd=0).pack(side=TOP)

    Frame(loginPage, width = 340, height=338, bd=0, bg="pink").place(x = 550, y = 350)

    Label(loginPage, text="User Name", bd = 0, bg = "green", width=10).place(x=696, y=400, anchor="center")

    global e1
    e1 = Entry(loginPage)
    e1.place(x=722, y=420, anchor="center")

    Label(loginPage, text="Password", width=10, bg="green").place(x=698, y=450, anchor="center")

    global e2
    e2 = Entry(loginPage, show="*")
    e2.place(x=722, y=472, anchor="center")

    Button(loginPage, text="Login", command=login, bg="blue", width=10).place(x=712, y=510, anchor="center")
    loginPage.mainloop()


def login():
    mysql_query = dbHandle.cursor(dictionary = True, buffered = True)

    mysql_query.execute(f"SELECT * FROM `USERS` WHERE `NAME` = '{e1.get()}' AND `PASSWORD` = '{e2.get()}'")

    if(not mysql_query.rowcount): return messagebox.showerror("Error!", "Invalid Credentials\nPlease try again!")

    print(mysql_query.fetchall())
    loginPage.destroy()


# shops items management screen
   # labels
orange_frame = Frame(m1, bg="orange", width=1524, height=788)
white_frame = Frame(m1, bg="white", width=1220, height=730)
black_frame = Frame(m1, bg="grey", width=1025, height=310 )
seller_label = Label(orange_frame, text="SELLER", bg="orange", fg="white", font=("aerial", 30))
categories_label = Label(orange_frame, text="CATEGORIES", bg="orange", fg="white", font=("aerial", 30))
manage_products = Label(white_frame, text="MANAGE PRODUCTS", bg="white", fg="orange", font=("aerial", 25, "bold"))
id = Label(white_frame, text="ProductID", bg="white", fg="orange", font=("aerial", 15, "bold"))
name = Label(white_frame, text="NAME", bg="white", fg="orange", font=("aerial", 15, "bold"))
quantity = Label(white_frame, text="QUANTITY", bg="white", fg="orange", font=("aerial", 15, "bold"))
price = Label(white_frame, text="PRICE", bg="white", fg="orange", font=("aerial", 15, "bold"))
category = Label(white_frame, text="CATEGORY", bg="white", fg="orange", font=("aerial", 15, "bold"))
product_lis = Label(white_frame, text="PRODUCTS LIST", bg="white", fg="orange", font=("aerial", 25, "bold"))


# creating combo box
cur = dbHandle.cursor()
cur.execute("select shopname from shops")
shops = cur.fetchall()
categories = []
for i in range(len(shops)):
    a = list(shops[i])
    categories.extend(a)
combo_box = ttk.Combobox(white_frame, value=categories, width=22)
combo_box.insert(0, "Type")



# creating and placing treeview
col = ("pid", "pname", "pquantity", "price")
product_list = ttk.Treeview(m1, height=13, columns=col)

product_list.column("#0", width=0, minwidth=0)
product_list.column("pid", width=200, minwidth=200, anchor=CENTER)
product_list.column("pname", width=300, minwidth=300, anchor=CENTER)
product_list.column("pquantity", width=300, minwidth=300, anchor=CENTER)
product_list.column("price", width=200, anchor=CENTER)

product_list.heading("pid", text="Product ID", anchor=CENTER)
product_list.heading("pname", text="Product NAME", anchor=CENTER)
product_list.heading("pquantity", text="Product QUANTITY", anchor=CENTER)
product_list.heading("price", text="PRICE", anchor=CENTER)

product_list.place(x=426, y=460)


def search(event):
    global val
    val = event.widget.get()
    if val == "":
        combo_box['value'] = categories
    else:
        data=[]
        for categ in categories:
            if val.lower() in categ.lower():
                data.append(categ)
        combo_box['value'] = data


var_id = StringVar()
var_name = StringVar()
var_quantity= IntVar()
var_price = IntVar()

    
def display():
    dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=C:\Users\Xmart\Documents\shopping mall.accdb;')
    cur4 = dbHandle.cursor()
    global val
    global all_data
    cur4.execute(f"SELECT pid,pname,pquantity,price FROM shopdata WHERE category='{val}'")
    all_data = cur4.fetchall()
    for row in product_list.get_children():
        product_list.delete(row)
    j=0
    for i in all_data:
        id = i[0]
        name = i[1]
        qty = i[2]
        pr = i[3]
        if j % 2 == 0:
            product_list.insert(parent='', index='end', iid=j, values=(id, name, qty, pr),tags=("even",))
        else:
            product_list.insert(parent='', index='end', iid=j, values=(id, name, qty, pr), tags=("odd",))
        j += 1
    product_list.tag_configure("even", foreground="black", background="gray82")
    product_list.tag_configure("odd", foreground="black", background="white")
    dbHandle.close()

def add():
    dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=C:\Users\Xmart\Documents\shopping mall.accdb;')
    cur1 = dbHandle.cursor()
    global val
    cur1.execute(f"insert into shopdata(pid,pname,pquantity,price,category) "
                f"values('{var_id.get()}','{var_name.get()}','{var_quantity.get()}','{var_price.get()}','{val}')")

    dbHandle.commit()
    dbHandle.close()
    display()


def edit():
    dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=C:\Users\Xmart\Documents\shopping mall.accdb;')
    cur2 = dbHandle.cursor()
    global val
    cur2.execute(f"update shopdata set pname='{var_name.get()}',"
                f" pquantity='{var_quantity.get()}', price='{var_price.get()}' where pid='{var_id.get()}'")

    dbHandle.commit()
    dbHandle.close()
    display()


def delete():
    dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=C:\Users\Xmart\Documents\shopping mall.accdb;')
    cur3 = dbHandle.cursor()
    cur3.execute(f"delete from shopdata where pid='{var_id.get()}' AND category='{val}'")
    dbHandle.commit()
    dbHandle.close()
    display()

   # buttons
logout_button = Button(orange_frame, text="Logout", bg="orange", fg="white", font=("aerial", 13, "italic"))
add_button = Button(white_frame, text="ADD", bg="orange", fg="white", width=7, height=1,
                       font=("aerial", 15, "italic"), command=cmd)
edit_button = Button(white_frame, text="EDIT", bg="orange", fg="white", width=7, height=1,
                        font=("aerial", 15, "italic"), command=edit)
delete_button = Button(white_frame, text="DELETE", bg="orange", fg="white", width=7, height=1,
                          font=("aerial", 15, "italic"), command=delete)
clear_button = Button(white_frame, text="DISPLAY", bg="orange", fg="white", width=7, height=1,
                         font=("aerial", 15, "italic"), command=display)


   # entry boxes
id_entry = Entry(white_frame, bg="white", textvariable=var_id, bd=3, width=25)
name_entry = Entry(white_frame, bg="white", textvariable=var_name, bd=3, width=25)
quantity_entry = Entry(white_frame, bg="white", textvariable=var_quantity, bd=3, width=25)
price_entry = Entry(white_frame, bg="white", textvariable=var_price, bd=3, width=25)




# putting on screen

orange_frame.place(x=3, y=1)
white_frame.place(x=300, y=50)
black_frame.place(x=415, y=450)
seller_label.place(x=5, y=200)
categories_label.place(x=5, y=250)
logout_button.place(x=150, y=730)
manage_products.place(x=440, y=15)
id.place(x=100, y=110)
id_entry.place(x=235, y=113)
name.place(x=100, y=160)
name_entry.place(x=235, y=163)
quantity.place(x=700, y=110)
quantity_entry.place(x=850, y=110)
price.place(x=700, y=160)
price_entry.place(x=850, y=160)
category.place(x=100, y=210)
add_button.place(x=250, y=270)
edit_button.place(x=450, y=270)
delete_button.place(x=650, y=270)
clear_button.place(x=850, y=270)
product_lis.place(x=475, y=350)
combo_box.place(x=236, y=214)
combo_box.bind("<KeyRelease>", search)

m1.mainloop()

