from tkinter import *
import mysql.connector
import turtle
import time
# import string

def register_user():
    username_info = username.get()
    password_info = password.get()
    
    # fopen a file to write users credentials and save it as a text folder file
    file=open("Users_Registration_Credentials"+"/"+username_info+".txt", "w")
    file.write("Username ="+username_info+"\n")
    file.write("Password ="+password_info)
    file.close()
    
    # save users credentials to the database
    DB = mysql.connector.connect(host="localhost", user="root", passwd="", database="note_saver")
    sqlCursor = DB.cursor()
    sql = "INSERT INTO users(username, password) VALUES(%s, %s)"
    values = (username_info, password_info)
    
    sqlCursor.execute(sql, values)
    DB.commit()
    # commit = DB.commit()
    
    # if commit == True:
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(signup_screen, text = "registered successfully! Login to access your saved work", fg="green",  font=("Calibri", 11)).pack()
    # else:
        # return
    
def register():
    global signup_screen
    signup_screen = Toplevel(screen)
    signup_screen.title("Register Account")
    signup_screen.geometry("450x500")
    # globalise username&password&the entries
    global username
    global password
    global username_entry
    global password_entry
    
    # declare some datatypes to variables/declare variables.
    username = StringVar()
    password = StringVar()
    Label(signup_screen, text = "").pack()
    Label(signup_screen, text = "").pack()
    Label(signup_screen, text = "").pack()
    
    Label(signup_screen, text = "Please Register Below To Continue", font=("Calibri", 13)).pack()
    Label(signup_screen, text = "").pack()
    Label(signup_screen, text = "").pack()
    
    Label(signup_screen, text = "Username * ").pack()
    username_entry=Entry(signup_screen, textvariable = username)
    username_entry.pack()
    
    Label(signup_screen, text = "").pack()
    
    Label(signup_screen, text = "Password * ").pack()
    password_entry=Entry(signup_screen, textvariable = password) 
    password_entry.pack()
    
    Label(signup_screen, text = "").pack()
    Label(signup_screen, text = "").pack()
    Label(signup_screen, text = "").pack()
    Button(signup_screen, text = "Signup", width="10", height="1", command = register_user).pack()
    
    
    
def login():
    # print("Login session just Started")
    username_info = username.get()
    password_info = password.get()
    
    DB = mysql.connector.connect(host="localhost", user="root", passwd="", database="note_saver")
    sqlCursor = DB.cursor()
    
    sql = "SELECT * FROM users WHERE username='username_info'AND password='password_info'"
    sqlCursor.execute(sql)
    
    fetchResult = sqlCursor.fetchall()
    
    while True:
        global login_screen
        login_screen = Toplevel(screen)
        login_screen.title("Welcome to Note Saver")
        login_screen.geometry("450x500")
    else:
        Label(login_screen, text = "Please check your username and password correctly", fg="green",  font=("Calibri", 11)).pack()

# main screen
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("450x500")
    
    # screen title
    screen.title("Online Note-Saver V1.0")
    
    Label(text = "Online Note-Saver V1.0", bg="green", width="400", height="2", font=("Calibri", 13)).pack()
    Label(text = "").pack()
    Label(text = "").pack()
    
    # globalise username&password&the entries
    global username
    global password
    global username_entry
    global password_entry
    
    # declare some datatypes to variables/declare variables.
    username = StringVar()
    password = StringVar()
    
    Label(text = "Login below to access your work", font=("Calibri", 13)).pack()
    Label(text = "").pack()
    Label(text = "").pack()
    
    Label(text = "Username * ").pack()
    username_entry=Entry(textvariable = username)
    username_entry.pack()
    
    Label(text = "").pack()
    
    Label(text = "Password * ").pack()
    password_entry=Entry(textvariable = password) 
    password_entry.pack()
    
    Label(text = "").pack()
    Button(text = "Login", width="30", height="2", command = login).pack()
    Label(text = "").pack()
    Button(text = "Signup", width="30", height="2", command = register).pack()
    Label(text = "").pack()
    Label(text = "Forgot Password? Click here", font= ("Calibri", 13)).pack()
    
    screen.mainloop()
    
# call the class to execute
main_screen()