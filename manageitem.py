from tkinter import *
from tkinter import ttk
import pyodbc
import ctypes
screenSize = [ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)]

def back():
    m1.destroy()
    from cpanel import showCpanel
    showCpanel()

def logout():
   from loginpage import ShowLoginPage
   m1.destroy()
   ShowLoginPage()

def search(event):
    global val
    global combo_box
    global cate
    global categories
    val = event.widget.get()
    if val == "":
        combo_box['value'] = categories
    else:
        data=[]
        for categ in categories:
            if val.lower() in categ.lower():
                data.append(categ)
        combo_box['value'] = data

  
    
def display():
    dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=.\shopping mall.accdb;')
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
                              r'DBQ=.\shopping mall.accdb;')
    cur1 = dbHandle.cursor()
    global val
    cur1.execute(f"insert into shopdata(pid,pname,pquantity,price,category) "
                f"values('{var_id.get()}','{var_name.get()}','{var_quantity.get()}','{var_price.get()}','{val}')")

    dbHandle.commit()
    dbHandle.close()
    display()


def edit():
    dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=.\shopping mall.accdb;')
    cur2 = dbHandle.cursor()
    global val
    cur2.execute(f"update shopdata set pname='{var_name.get()}',"
                f" pquantity='{var_quantity.get()}', price='{var_price.get()}' where pid='{var_id.get()}'")

    dbHandle.commit()
    dbHandle.close()
    display()


def delete():
    dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=.\shopping mall.accdb;')
    cur3 = dbHandle.cursor()
    cur3.execute(f"delete from shopdata where pid='{var_id.get()}' AND category='{val}'")
    dbHandle.commit()
    dbHandle.close()
    display()


def showItemManage():
    global m1
    m1 = Tk()

    m1.geometry(f"{screenSize[0]}x{screenSize[1]}")

    global var_id, var_name, var_price, var_quantity
    var_id = StringVar()
    var_name = StringVar()
    var_quantity= IntVar()
    var_price = IntVar()


    # shops items management screen
    # labels
    orange_frame = Frame(m1, bg="#febe53", width=1524, height=screenSize[1])
    white_frame = Frame(m1, bg="white", width=1220, height=730)
    black_frame = Frame(m1, bg="grey", width=1025, height=310 )
    seller_label = Label(orange_frame, text="SELLER", bg="#febe53", fg="white", font=("aerial", 30))
    categories_label = Label(orange_frame, text="CATEGORIES", bg="#febe53", fg="white", font=("aerial", 30))
    manage_products = Label(white_frame, text="MANAGE PRODUCTS", bg="white", fg="#febe53", font=("aerial", 25, "bold"))
    id = Label(white_frame, text="ProductID", bg="white", fg="#febe53", font=("aerial", 15, "bold"))
    name = Label(white_frame, text="NAME", bg="white", fg="#febe53", font=("aerial", 15, "bold"))
    quantity = Label(white_frame, text="QUANTITY", bg="white", fg="#febe53", font=("aerial", 15, "bold"))
    price = Label(white_frame, text="PRICE", bg="white", fg="#febe53", font=("aerial", 15, "bold"))
    category = Label(white_frame, text="CATEGORY", bg="white", fg="#febe53", font=("aerial", 15, "bold"))
    product_lis = Label(white_frame, text="PRODUCTS LIST", bg="white", fg="#febe53", font=("aerial", 25, "bold"))


    try:
        dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                                  r'DBQ=.\shopping mall.accdb;')
    except Exception as e:
        print(e)
    # creating combo box
    cur = dbHandle.cursor()
    cur.execute("select sName from shops")
    shops = cur.fetchall()
    categories = []
    for i in range(len(shops)):
        a = list(shops[i])
        categories.extend(a)
    combo_box = ttk.Combobox(white_frame, value=categories, width=22)
    combo_box.insert(0, "Type")



    # creating and placing treeview
    col = ("pid", "pname", "pquantity", "price")
    global product_list
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

    # buttons
    back_button = Button(orange_frame, text="Back", bg="#febe53", fg="white", font=("aerial", 13, "italic"), command = back)

    logout_button = Button(orange_frame, text="Logout", bg="#febe53", fg="white", font=("aerial", 13, "italic"), command = logout)
    add_button = Button(white_frame, text="ADD", bg="#febe53", fg="white", width=7, height=1,
                        font=("aerial", 15, "italic"), command=add)
    edit_button = Button(white_frame, text="EDIT", bg="#febe53", fg="white", width=7, height=1,
                            font=("aerial", 15, "italic"), command=edit)
    delete_button = Button(white_frame, text="DELETE", bg="#febe53", fg="white", width=7, height=1,
                            font=("aerial", 15, "italic"), command=delete)
    clear_button = Button(white_frame, text="DISPLAY", bg="#febe53", fg="white", width=7, height=1,
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
    back_button.place(x=150, y=690)
    combo_box.place(x=236, y=214)
    combo_box.bind("<KeyRelease>", search)

    m1.mainloop()
