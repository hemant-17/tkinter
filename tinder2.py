from tkinter import *
import tkinter.messagebox as tkmsg
from PIL import ImageTk, Image
import mysql.connector 
import itertools

myconnector = mysql.connector.connect(host='localhost', user='root', passwd="Soham@123", database="tinder")
mycursor = myconnector.cursor()

class tinderapp(Tk):
    def __init__(self):
        super().__init__()
        self._frame = None
        self.switch_frame(signup)
        self.geometry("700x500")
        self.title("tinder")
        print(self._frame)
        def donothing():
            pass

        menubar = Menu(self)
        usermenu = Menu(menubar, tearoff=0)
        # settings = Menu(menubar, tearoff=0)
        usermenu.add_command(label="homepage", command= lambda : self.switch_frame(homepage))
        usermenu.add_command(label="request", command= lambda : self.switch_frame(request))
        usermenu.add_command(label="profile", command= lambda : self.switch_frame(profile))
        usermenu.add_separator()
        usermenu.add_command(label="signout", command= lambda : self.switch_frame(signup))
        usermenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="user", menu=usermenu)

        
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.config(menu=menubar)
        
        self.user_entry = StringVar() 
        self.pass_entry = StringVar()

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        print(new_frame)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row=0,column=0)


class signup(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self)
        user_entry = StringVar() 
        pass_entry = StringVar()
        Label(self, text='signup',padx=50).grid()
        Entry(self, textvariable=user_entry).grid()
        Entry(self, textvariable=pass_entry).grid()
        Button(self, text='submit', command= lambda : self.check_existing_user(user_entry.get(), pass_entry.get())).grid()
        Button(self, text='already a user', command= lambda: master.switch_frame(Login), padx=10).grid()

    def check_existing_user(self, username, password):
        mycursor.execute(f" select * from accounts where username = \'{username}\' ")
        result = mycursor.fetchone()
        if result is not None :
            tkmsg.showwarning(title='signup error', message='the username already exist')
        else:
            mycursor.execute("INSERT INTO accounts(username,user_password) VALUES (%s,%s)", (username,password) )
            myconnector.commit()
            self.master.switch_frame(Login)

class Login(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self)
        user_entry = StringVar() 
        pass_entry = StringVar()
        Label(self, text='login',padx=50).grid()
        Entry(self, textvariable=user_entry).grid()
        Entry(self, textvariable=pass_entry).grid()
        Button(self, text='submit', command= lambda : self.login(user_entry.get(), pass_entry.get())).grid()

    def login(self, username, password):
        mycursor.execute(f" select * from accounts where username = \'{username}\' and user_password = \'{password}' ")
        result = mycursor.fetchone()
        if result is None :
            tkmsg.showwarning(title='login error', message="error in username or password")
        else:
            self.master.user_entry = username
            print(self.master.user_entry)
            self.master.switch_frame(profile)


class profile(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self)
        # username = StringVar()
        username = self.master.user_entry

        name = StringVar()
        name.set(username)
        Label(self, text="name").grid(row=0, column=0, sticky = W)
        Entry(self, textvariable=name).grid(row=0, column=1, sticky = W)
        
        mycursor.execute(fr"select img from user_profile where username = '{username}' ")
        result = mycursor.fetchone()

        img_path = StringVar()
        img_path.set(result[0])
        Label(self, text='enter new image path').grid(row=2, column=0)
        Entry(self, textvariable=img_path).grid(row=2, column=1, pady=7)      
        print(result)
        if result is None:
            img = Image.open(r'C:\Users\patkar\Pictures\blank.png')
        else:
            img = Image.open(fr'{result[0]}')
        img = img.resize((150,150), Image.ANTIALIAS)
        mylabel = ImageTk.PhotoImage(img)
        ImageLabel = Label(self, image=mylabel)
        ImageLabel.image = mylabel
        ImageLabel.grid(row=1, column=5)

        bio = StringVar()
        bio.set("just joined tinder")
        Label(self, text="bio").grid(row=4, column=0)
        Entry(self, textvariable=bio).grid(row=4, column=1, pady=7)

        sex = StringVar()
        if username is None:
            sex.set('m')
        else:
            mycursor.execute(f"select sex from user_profile where username = \'{username}\' ")
            sex_val = mycursor.fetchone()
            sex.set(sex_val)
        Label(self, text="sex").grid(row=5, column=0)
        Radiobutton(self, text="male", variable=sex, value='m').grid(row=5, column=1)
        Radiobutton(self, text="female", variable=sex, value='f').grid(row=5, column=2, pady=7)

        interest = StringVar()
        if username is None:           
            interest.set('straight')
        else:
            mycursor.execute(f"select interest from user_profile where username = \'{username}\' ")
            interest_val = mycursor.fetchone()
            interest.set(interest_val)
        Label(self, text='interest').grid(row=5, column=0)
        Radiobutton(self, text="straight", variable=interest, value='straight').grid(row=6, column=1)
        Radiobutton(self, text="bi", variable=interest, value='bi').grid(row=6, column=2)

        Button(self, text='ok', command= lambda : self.set_bio(username, img_path.get(), sex.get(), interest.get(), bio.get()) ).grid(row=7, column=1)
        Button(self, text='home page', command= lambda : self.master.switch_frame(homepage) ).grid(row=8, column=4)

    def set_bio(self, username, img_path, sex, interest, bio):
        mycursor.execute(f" select * from user_profile where username = \'{username}\' ")
        present = mycursor.fetchone()
        if present is None :
            mycursor.execute("insert into user_profile(username,img,sex,interest,bio) values(%s, %s ,%s ,%s ,%s)",(username,img_path,sex,interest,bio))
            myconnector.commit()
        else:
            print(img_path)
            print(sex)
            print(interest[0])
            print(bio)
            mycursor.execute(f" update user_profile set img = \'{img_path}\' ,bio = \'{bio}\' where username = \'{username}\' ")
            myconnector.commit()


class homepage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self)

        user = self.master.user_entry
        mycursor.execute(f" select interest from user_profile where username = \'{user}\' ")
        user_interest = mycursor.fetchone()
        if user_interest[0] == 'straight' :
            mycursor.execute(f" select sex from user_profile where username = \'{user}\' ")
            user_sex = mycursor.fetchone()
            mycursor.execute(f" select img from user_profile where sex != \'{user_sex[0]}\' ")
            img = mycursor.fetchall()
            imgs = [path[0] for path in img] 
            self.create_slide_show(imgs)
        else:
            mycursor.execute(f" select img from user_profile where username != \'{user}\' ")
            img = mycursor.fetchall()
            imgs = [path[0] for path in img] 
            self.create_slide_show(imgs)

    def create_slide_show(self, img1, i=0):
        img = Image.open(f'{img1[i]}')
        img = img.resize((150,150), Image.ANTIALIAS)
        mylabel = ImageTk.PhotoImage(img)
        ImageLabel = Label(self, image=mylabel)
        ImageLabel.image = mylabel
        ImageLabel.grid(row=1, column=5)
        print(img1)

        new_img = img1[i]
        next_img = new_img.replace('\\', '\\\\')
        print(next_img)
        mycursor.execute(fr" select username from user_profile where img = '{next_img}' ")
        name = mycursor.fetchone()
        print(name)
        Label(self, text=f"{name[0]}").grid(row=3,column=5, padx=5, pady=5)

        mycursor.execute(fr" select bio from user_profile where img = '{next_img}' ")
        bio = mycursor.fetchone()
        Label(self, text=f"{bio[0]}").grid(row=4,column=5)
        Button(self, text='next', command= lambda : self.create_slide_show(img1, i=i+1)).grid(row=5, column=3)
        Button(self, text='back', command= lambda : self.create_slide_show(img1, i=i-1)).grid(row=5, column=1)
        Button(self, text='send request', command= lambda : self.send_request(name)).grid(row=5, column=2)
    
    def send_request(self, target):
        username = self.master.user_entry
        print(username, target)
        mycursor.execute(" insert into request(username, target, sent_request, accept) values(%s, %s, %s, %s)",(username, target[0], 1, None))
        myconnector.commit()
        tkmsg.showinfo(title='request', message='request sent')

class request(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self)
        username = self.master.user_entry
        mycursor.execute(f" select * from request where username = \'{username}\' or target = \'{username}\' ")
        result = mycursor.fetchall()
        print(result)
        if result is not None:
            for (match,i) in zip(result,range(len(result))):
                if match[0]==username:
                    Label(self, text=f"{match[1]}").grid(row=i, column=0)
                    print(match[1])

                    if match[2]==1 and match[3] is not None:
                        Label(self, text="accepted").grid(row=i, column=1)
                    
                    elif match[2]==1 and match[3] is None:
                        Label(self, text="pending").grid(row=i, column=1)

                elif match[1]==username and match[2]==1 and match[3] is None:
                    Label(self, text=f"{match[0]}").grid(row=i, column=0)
                    print(match[1])
                    Label(self, text="sent to you").grid(row=i, column=1)
                    Button(self, text="accept request", command= lambda : self.accept(match)).grid(row=i,column=2)

    
    def accept(self, match):
        username = match[0]
        target = match[1]
        print(username,target)
        mycursor.execute(f" update request set accept = 1 where username=\'{username}\' and target=\'{target}\' ")
        myconnector.commit()
        tkmsg.showinfo(title=request, message="request accepted")

if __name__ == "__main__":
    window = tinderapp()
    window.mainloop()