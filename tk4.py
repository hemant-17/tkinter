from tkinter import *
import mysql.connector
import tkinter.messagebox as ms
from PIL import Image , ImageTk
from tkinter import ttk
import webbrowser
from tk5 import Chat_window


db = mysql.connector.connect(host="localhost",user="root",passwd="hemant1716",database="user")

c = db.cursor()

class Chat:


    def myfunction(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=200,height=200)

    def chat_window(self,to):
        self.chatwindow = Chat_window(self.master,self.username,to)
        ms.showinfo("Chat","Chatting is on")





    def __init__(self,master,username):
        self.master = master
        self.username = username
        print(self.username)

        # mysql query
        find_user = ('SELECT name , status FROM register WHERE username != %s')
        c.execute(find_user,[(self.username)])
        a=c.fetchall()
        print(len(a))
        # for i in range(2):
        #     for j in range(len(a)):
        #         print(i,j)
        #         print(a[i][j])
                #print(a[i])




        # scrollbar function
        sizex = 800
        sizey = 600
        posx  = 100
        posy  = 100
        self.master.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

        self.myframe=Frame(self.master,relief=GROOVE,width=50,height=100,bd=1)
        self.myframe.place(x=10,y=10)

        self.canvas=Canvas(self.myframe)
        self.frame=Frame(self.canvas)
        self.myscrollbar=Scrollbar(self.myframe,orient="vertical",command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.myscrollbar.set)

        self.myscrollbar.pack(side="right",fill="y")
        self.canvas.pack(side="left")
        self.canvas.create_window((0,0),window=self.frame,anchor='nw')
        self.frame.bind("<Configure>",self.myfunction)
        for i in range(len(a)):
            print(a[i][0])
            self.name = a[i][0]
            # Label(self.frame, textvariable = self.name ).grid(row=i,column=1)
            Button(self.frame,text = self.name,bd = 5 ,font = ('',15),padx=5,pady=5,bg="black",fg="white",command=lambda: self.chat_window(self.name)).grid(row=i,column=1)
            print(self.name)
            #link2.bind("<Button-1>", lambda e: self.callback("http://www.ecosia.org"))
            #Label(self.frame,text="..........").grid(row=i,column=2)







        # self.chat_fr = Frame(self.master,bg="white",width=700,height=500)
        # self.chat_fr.place(x=0,y=0)
