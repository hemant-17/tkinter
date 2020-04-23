from tkinter import *
import mysql.connector
from PIL import Image , ImageTk
import tkinter.messagebox as ms
from tkinter import ttk
import webbrowser
import cv2


db = mysql.connector.connect(host="localhost",user="root",passwd="hemant1716",database="user")

c = db.cursor()

class Chat_window:
    def myfunction(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=200,height=200)

    def write_file(self,data, filename):
    # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)

    def __init__(self,master,username,to):
        self.master = master
        self.username = username
        self.name = to
        print("This is the person you want to chat with",self.name)
        print(self.username)
        # self.sizex = 800
        # self.sizey = 600
        # self.posx  = 100
        # self.posy  = 100
        self.msg_content = StringVar()

        find_user = ('SELECT msg_content FROM message WHERE from1 = %s and to1 = %s')
        c.execute(find_user,[(self.username),(self.name)])
        a=c.fetchall()
        print(f"{a}\n")
        print(a[0][0])
        print(a[1][0])
        for i in range(len(a)):
            print(a[i][0])

        find_user = ('SELECT msg_content FROM message WHERE from1 = %s and to1 = %s')
        c.execute(find_user,[(self.name),(self.username)])
        b=c.fetchall()
        print(f"{a}\n")
        for i in range(len(b)):
            print(b[i][0])

        ####
        img = cv2.imread('pass.jpg')
        # insert = 'INSERT INTO picture1 (image_id,image) VALUES 10,load_file(''C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\images\\pass.jpg'')'
        # c.execute('Select image from picture1 where image_id=7')
        # a = c.fetchall()
        # self.write_file(a, photo)
        # print("done")
        # db.commit()


        ##### Tkinter GUI
        # self.master.wm_geometry("%dx%d+%d+%d" % (self.sizex, self.sizey, self.posx, self.posy))

        self.myframe=Frame(self.master,relief=GROOVE,width=500,height=500,bd=1,bg="white")
        self.myframe.place(x=10,y=10)

        self.canvas=Canvas(self.myframe,width=500,height=500)
        self.frame=Frame(self.canvas,width=500,height=500)
        self.myscrollbar=Scrollbar(self.myframe,orient="vertical",command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.myscrollbar.set)

        self.myscrollbar.pack(side="right",fill="y")
        self.canvas.pack(side="left")
        self.canvas.create_window((0,0),window=self.frame,anchor='nw',width=500,height=500)
        # self.frame.bind("<Configure>",self.myfunction)

        #Label(self.frame,text=self.name).grid(row=0,column=0)
        for i in range(len(a)):
            Label(self.frame,text=a[i][0],font="Helvetica 15 ",bg="white").grid(row=i+2,column=1)
        for i in range(len(b)):
            Label(self.frame,text=b[i][0],font="Helvetica 15 ",bg="white").grid(row=i+1,column=1)

        self.ent = Entry(self.frame,font="Helvetica 10 bold",textvariable = self.msg_content,relief=SUNKEN,bd=2,width=50).grid(sticky=W,padx=5,pady=10,ipady=3)
        Button(self.frame,text="Send",font="Helvetica 8 bold" ,relief=GROOVE,padx=15,pady=5,command=self.send).grid(sticky=W)



    def send(self):
        print("sending")
        print(self.msg_content.get())
        insert = 'INSERT INTO message (from1,to1,msg_content) VALUES(%s,%s,%s)'

        c.execute(insert,[(self.username),(self.name),(self.msg_content.get())])
        print("done")
        db.commit()
        self.msg_content.set("")
