from pickle import FALSE


USE_SQL_SERVER = FALSE

"""Importing modules"""
import tkinter as tk
import ctypes
from datetime import datetime
"""End of importing modules"""

"""Connecting to DB"""
if(USE_SQL_SERVER):
    import mysql.connector as db
    try:
        dbHandle = db.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database = ""
        )
    except db.Error as error:
        print(error, datetime.now())
else:
    import pyodbc
    dbHandle = pyodbc.connect()

"""Getting screen size"""
screenSize = [ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)]

"""master window #1"""
m1 = tk.Tk()

m1.geometry(f"{screenSize[0]}x{screenSize[1]}")


m1.tk.mainloop()