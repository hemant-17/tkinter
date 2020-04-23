from tkinter import *
import mysql.connector
import sqlite3
import tkinter.messagebox as ms
from tk2 import HomePage
# with sqlite3.connect('quit.db') as db:
#     c = db.cursor()
db = mysql.connector.connect(host="localhost",user="root",passwd="hemant1716",database="user")

c = db.cursor()

# c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
# db.commit()
# db.close()

class Login:
    def __init__(self,master):
        self.master = root
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.n_email = StringVar()
        self.n_status = StringVar()
        self.n_name = StringVar()
        self.n_jobprofile = StringVar()
        self.n_education = StringVar()
        self.v0=IntVar()
        self.v0.set(1)
        self.widgets()




        #Login Function
    def login(self):
    	#Establish Connection
        # with sqlite3.connect('quit.db') as db:
        #     c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user1 WHERE username = %s and passwd = %s')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
             self.logf.pack_forget()
             self.head.pack_forget()
             print(self.username.get())
             self.homepage = HomePage(self.master,self.username.get())
            # self.head['text'] = self.username.get() + '\n Loged In'
            # self.head['pady'] = 150
        else:
            ms.showerror('Oops!','Username Not Found.')

    def new_user(self):
    	#Establish Connection
        # with sqlite3.connect('quit.db') as db:
        #     c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user1 WHERE username = %s')
        c.execute(find_user,[(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account
        insert = 'INSERT INTO user1(username,passwd) VALUES(%s,%s)'

        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])

        # if self.n_name == "":
        #     self.n_name = "N"
        # elif self.n_status =="":
        #     self.n_status == "N"
        # elif self.n_email =="":
        #     self.n_email == "N"
        # elif self.n_jobprofile =="":
        #     self.n_jobprofile == "N"
        # elif self.n_education =="":
        #     self.n_education == "N"

        insert1 = 'INSERT INTO register(name,username,status,job_profile,education,email) VALUES (%s,%s,%s,%s,%s,%s)'
        c.execute(insert1,[(self.n_name.get()),(self.n_username.get()),(self.n_status.get()),(self.n_jobprofile.get()),(self.n_education.get()),(self.n_email.get())])

       # c.execute(insert1,[(self.n_)])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        self.master.geometry("755x600")
        Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()

        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Username: ',font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,text = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,text = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)

        Label(self.crf,text = 'Name: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,text = self.n_name,bd = 5,font = ('',15)).grid(row=2,column=1)

        Label(self.crf,text = 'Gender: ',font = ('',20),pady=5,padx=5).grid(sticky = W)

        r1=Radiobutton(self.crf, text="male",font = ('',15),variable=self.v0,value=1).grid(row=3,column=1)
        r2=Radiobutton(self.crf, text="female",font = ('',15),variable=self.v0,value=2).grid(row=3,column=2)



        Label(self.crf,text = 'Job Profile: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,text = self.n_jobprofile,bd = 5,font = ('',15)).grid(row=4,column=1)

        Label(self.crf,text = 'Education: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,text = self.n_education,bd = 5,font = ('',15)).grid(row=5,column=1)

        Label(self.crf,text = 'Email: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,text = self.n_email,bd = 5,font = ('',15)).grid(row=6,column=1)

        Label(self.crf,text = 'Status: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_status,bd = 5,font = ('',15)).grid(row=7,column=1)

        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid(row=8,column=0)
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=15,pady=5,command=self.log).grid(row=8,column=1)





root= Tk()
obj = Login(root)
root.mainloop()