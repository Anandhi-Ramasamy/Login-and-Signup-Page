from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql
#functionality part

def forget_pass():
    def change_password():
        if user_entry.get()=='' or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error', 'All fields are Required', parent=window)
        elif newpass_entry.get()!= confirmpass_entry.get():
            messagebox.showerror('Error','Password and Confirm Password not matching', parent=window)
        else:
            connection=pymysql.connect(host='localhost', user='root', password='Anandhi@sql',database='usersdata')
            mycursor=connection.cursor()
            query='select * from data where username=%s'
            mycursor.execute(query,(user_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect Username', parent=window)
            else:
                query='Update data set password=%s where username=%s'
                mycursor.execute(query,(newpass_entry.get(), user_entry.get()))
                connection.commit()
                connection.close()
                messagebox.showinfo('Success', 'Password is reset, please login with new password', parent=window)
                window.destroy()
                
            
    
    window=Toplevel()
    window.title('Change Pasword')

    bgPic= ImageTk.PhotoImage(file='background.jpg')
    bglabel=Label(window, image=bgPic)
    bglabel.grid()
    heading_label=Label(window, text='RESET PASSWORD', font=('arial','18','bold'),
                        bg='white', fg='magenta2')
    heading_label.place(x=488, y=60)

    user_label=Label(window, text='Username', font=('arial','12','bold'),
                        bg='white', fg='orchid1')
    user_label.place(x=470, y=130)

    user_entry=Entry(window, width=25, font=('arial','11','bold'),
                        bd=0, fg='magenta2')
    user_entry.place(x=470, y=160)

    Frame(window, width=258, height=2, bg='orchid1').place(x=470,y=180)

    passwordlabel=Label(window, text='New Password', font=('arial','12','bold'),
                        bg='white', fg='orchid1')
    passwordlabel.place(x=470, y=210)

    newpass_entry=Entry(window, width=25, font=('arial','11','bold'),
                        bd=0, fg='magenta2')
    newpass_entry.place(x=470, y=240)

    Frame(window, width=258, height=2, bg='orchid1').place(x=470,y=260)

    confirmpasslabel=Label(window, text='Confirm Password', font=('arial','12','bold'),
                        bg='white', fg='orchid1')
    confirmpasslabel.place(x=470, y=290)

    confirmpass_entry=Entry(window, width=25, font=('arial','11','bold'),
                        bd=0, fg='magenta2')
    confirmpass_entry.place(x=470, y=320)

    Frame(window, width=258, height=2, bg='orchid1').place(x=470,y=340)

    submitButton=Button(window, text='Submit', bd=0, bg='magenta2', fg='white', font=('Open Sans','16','bold'),
                        width=19, cursor='hand2', activebackground='magenta2', activeforeground='white', command=change_password)
    submitButton.place(x=470, y=390)
    
    window.mainloop()

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','all fields are required')
    else:
        try:
            connection=pymysql.connect(host='localhost', user='root', password='Anandhi@sql')
            mycursor=connection.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query='use usersdata'
        mycursor.execute(query)
        query="select *from data where username=%s and password=%s"
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Errror','Invalid username or password')
        else:
            messagebox.showinfo('welcome', 'Login is successfull')
            
def signup():
    login.destroy()
    import Signup
    
def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
                

#GUI part
login=Tk()
login.geometry('990x660+50+50')
login.resizable(0,0)
bgImage = ImageTk.PhotoImage(file='bg.jpg')


bgLabel=Label(login,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login,text='USER LOGIN', font=('Microsoft Yahei UI Light',23,'bold'),bg='white', fg='firebrick1')
heading.place(x=610,y=120)

usernameEntry=Entry(login,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0, fg='firebrick1')
usernameEntry.place(x=585,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login,width=250,height=2,bg='firebrick1')
frame1.place(x=585,y=222)

passwordEntry=Entry(login,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0, fg='firebrick1')
passwordEntry.place(x=585,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login,width=250,height=2,bg='firebrick1')
frame2.place(x=585,y=282)

openeye=PhotoImage(file='openeye.PNG')

eyeButton=Button(login,image=openeye, bd=0, bg='white', activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800, y=255)

forgetButton=Button(login,text='Forgot Password?', bd=0, bg='white', activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'),
                    fg='firebrick1',activeforeground='firebrick1',command=forget_pass)
forgetButton.place(x=715, y=295)

loginButton=Button(login,text='Login', font=('Open Sans',16,'bold'),
                   fg='white',bg='firebrick1', activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=19, command=login_user)
loginButton.place(x=578,y=350)


urLabel=Label(login, text='---------------OR---------------', font=('Open Sans',16), fg="firebrick1",bg='white')
urLabel.place(x=583, y=400)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login,image=facebook_logo, bg='white')
fbLabel.place(x=640, y=448)

google_logo=PhotoImage(file='google.png')
googleLabel=Label(login,image=google_logo, bg='white')
googleLabel.place(x=690, y=448)

twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(login,image=twitter_logo, bg='white')
twitterLabel.place(x=740, y=448)

signupLabel=Label(login, text='Dont have an account? ', font=('Open Sans',9,'bold'), fg="firebrick1",bg='white')
signupLabel.place(x=590, y=508)

newaccountButton=Button(login,text='Create New One', font=('Open Sans',9,'bold underline'),
                   fg='blue',bg='white', activeforeground='blue', activebackground='white', cursor='hand2', bd=0, command=signup)
newaccountButton.place(x=727,y=508)


login.mainloop()


















