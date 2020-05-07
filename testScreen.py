from tkinter import *
import mysql.connector
import turtle
import time
# import string

def register():
    print('registration successful')

def login():
    print('session has been started!')

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("450x500")
    
    # screen title
    screen.title("Online Note-Saver V1.0")
    
    Label(text = "Online Note-Saver V1.0", bg="green", width="400", height="2", font=("Calibri", 13)).grid(row=0, column=0)
    
    Button(text = "Login", width="30", height="2", command = login).grid(row=3, column=5)
    Button(text = "Signup", width="30", height="2", command = register).grid(row=6, column=5)
    Label(text = "Forgot Password? Click here", font= ("Calibri", 13)).grid(row=8, column=10)
    
    screen.mainloop()
    
# call the class to execute
main_screen()