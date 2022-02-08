"""Importing modules"""
import tkinter as tk
import mysql.connector as db
import ctypes
"""End of importing modules"""

"""Getting screen size"""
screenSize = [ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)]



masterWindow = tk.Tk()

masterWindow.geometry(f"{screenSize[0]}x{screenSize[1]}")


masterWindow.tk.mainloop()