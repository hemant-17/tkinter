from tkinter import *
import PIL.Image , PIL.ImageTk
import tkinter.messagebox as ms
from tk3 import Profile
from tk4 import Chat
from tk5 import Chat_window


# class HomePage:
#     def __init__(self,master):
class HomePage:
    def logout(self):
        #self.rightFrame.pack_forget()
        self.log_fr.pack_forget()
        self.log_fr.place_forget()
        ms.showinfo("Logged out","Successfully! Logged out")







    def __init__(self,master,username):
        self.master = master
        self.username = username
        print(self.username)
        # self.rightframe = Frame
        # self.rightFrame = Frame(self.master, width=755, height = 600)
        # self.rightFrame.pack()
        # self.master.geometry("700x440")
        # def HomePage(self):

        #self.rightFrame.grid(row=0, column=1, padx=10, pady=2)
        self.master.title("HomePage for Tinder")
        image = PIL.Image.open("tin1.jpg")
        image = image.resize((755,600), PIL.Image.ANTIALIAS)
        self.bg_icon = PIL.ImageTk.PhotoImage(image)



        self.bg_lbl = Label(self.master,image=self.bg_icon).pack()
        self.log_fr = Frame(self.master,bg="white")
        self.log_fr.place(x=50,y=500)
        Button(self.log_fr,text = ' Logout ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.logout).grid(row=4,column=0,padx=10)
        Button(self.log_fr,text = ' Profile ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.Profile).grid(row=4,column=1,padx=10)
        Button(self.log_fr,text = ' Match ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.logout).grid(row=4,column=2,padx=10)
        Button(self.log_fr,text = ' Chat Box ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.Chat).grid(row=4,column=3,padx=10)
    def Profile(self):
        #self.bg_lbl.pack_forget()
        self.prof = Profile(self.master,self.username)
        ms.showinfo("Profile","Taking you to profile")

    def Chat(self):
        # self.bg_lbl.place_forget()
        self.chat = Chat(self.master,self.username)
        ms.showinfo("Chat","Chatting is on")





# root=Tk()
# obj = HomePage(root)
# root.mainloop()
