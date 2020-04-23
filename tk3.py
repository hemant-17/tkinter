from tkinter import *
import mysql.connector
from PIL import Image , ImageTk

db = mysql.connector.connect(host="localhost",user="root",passwd="hemant1716",database="user")

c = db.cursor()



class Profile:
    def update_profile(self):
        print(self.n_name.get())
        c.execute('UPDATE  register SET name = %s,status=%s,job_profile=%s ,education = %s , email=%s WHERE username = %s',(self.n_name.get(),self.n_status.get(),self.n_jobprofile.get(),self.n_education.get(),self.n_email.get(),self.n_username.get()))
        print("Updated")
        db.commit()




        # # c.execute("""
        # # 		create table if not exists my_table (name TEXT , data BLOB)
        # # 	""")
        c.execute("""
         	UPDATE  register SET image=%s WHERE username =%s""",(data,self.n_username.get()))

        print("ADDED")






    def __init__(self,master,username):
        self.master = master
        self.username = username
        print("Here is your profile ")
        print(self.username)
        find_user = ('SELECT * FROM register WHERE username = %s')
        c.execute(find_user,[(self.username)])
        a=c.fetchall()
        print(str(a))
        # find_user = ('SELECT status FROM register WHERE username = %s')
        # c.execute(find_user,[(self.username)])

        print(a[0][0],a[0][1],a[0][2],a[0][3],a[0][4],a[0][5])
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.n_email = StringVar()
        self.n_status = StringVar()
        self.n_name = StringVar()
        self.n_jobprofile = StringVar()
        self.n_education = StringVar()

        self.n_username.set(a[0][1])
        self.n_name.set(a[0][0])
        self.n_email.set(a[0][5])
        self.n_jobprofile.set(a[0][3])
        self.n_education.set(a[0][4])
        self.n_status.set(a[0][2])
        #db.commit()
        self.master.title = "Profile Page!"
        self.reg_fr = Frame(self.master,bg="white")
        self.reg_fr.place(x=50,y=50)

        #print(self.username.get())
        Label(self.reg_fr,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Label(self.reg_fr,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)


        Label(self.reg_fr,text = 'Name: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.reg_fr,textvariable = self.n_name,bd = 5,font = ('',15)).grid(row=1,column=1)

        Label(self.reg_fr,text = 'Job Profile: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.reg_fr,textvariable = self.n_jobprofile,bd = 5,font = ('',15)).grid(row=2,column=1)

        Label(self.reg_fr,text = 'Education: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.reg_fr,textvariable = self.n_education,bd = 5,font = ('',15)).grid(row=3,column=1)

        Label(self.reg_fr,text = 'Email: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.reg_fr,textvariable = self.n_email,bd = 5,font = ('',15)).grid(row=4,column=1)

        Label(self.reg_fr,text = 'Status: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.reg_fr,textvariable = self.n_status,bd = 5,font = ('',15)).grid(row=5,column=1)

        Button(self.reg_fr,text = 'Update Profile ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.update_profile).grid(row=7,column=2)
