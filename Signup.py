from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)


def connect_database():
    
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif passwordEntry.get() != confirmEntry.get():
         messagebox.showerror('Error', 'Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error', 'Please Accept Terms & Conditions')
    else:
        try:
            connection=pymysql.connect(host='localhost', user='root', password='Anandhi@sql')
            mycursor=connection.cursor()
            messagebox.showinfo("Success", "Database connected successfully!")
        except pymysql.MySQLError as e:
            messagebox.showerror('Error', 'Database connectivity issue, Please try again!!!:{e}')
            return
        try:
            '''query='drop database if exists userdata'
            mycursor.execute(query)'''
            query='create database usersdata'
            mycursor.execute(query)
            query='use usersdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100),password  varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use usersdata')

        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get(),))

        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror('Error', 'Username already exists')
        else:
            query='INSERT INTO data(email,username,password) VALUES(%s, %s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            connection.commit()
            messagebox.showinfo('Success','Registration is successfully')
            connection.close()
            
            clear()
            signup.destroy()
            import Login
            
        
        
        
        

def login():
    signup.destroy()
    import Login

signup=Tk()
signup.title('Signup Page')
signup.resizable(False, False)
background=ImageTk.PhotoImage(file='bg.jpg')


bgLabel=Label(signup,image=background)
bgLabel.grid()

frame=Frame(signup, bg='white')
frame.place(x=554, y=100)


heading=Label(frame, text='CREATE AN ACCOUNT', font=("Micrsoft Yahei UI Light", 18,'bold'),
              bg='white',fg='firebrick1')
heading.grid(row=0,column=0, padx=10, pady=10)

emailLabel=Label(frame, text='Email', font=('Micrsoft Yahei UI Light', 10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1, column=0, sticky='w', padx=25,pady=(10,0))

emailEntry=Entry(frame,width=30, font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
emailEntry.grid(row=2,column=0, sticky='w', padx=25)

usernameLabel=Label(frame, text='Username', font=('Micrsoft Yahei UI Light', 10,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10,0))

usernameEntry=Entry(frame,width=30, font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0, sticky='w', padx=25)

passwordLabel=Label(frame, text='Password', font=('Micrsoft Yahei UI Light', 10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10,0))

passwordEntry=Entry(frame,width=30, font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0, sticky='w', padx=25)

confirmLabel=Label(frame, text='Confirm Password', font=('Micrsoft Yahei UI Light', 10,'bold'),bg='white',fg='firebrick1')
confirmLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10,0))

confirmEntry=Entry(frame,width=30, font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
confirmEntry.grid(row=8,column=0, sticky='w', padx=25)

check=IntVar()
terms=Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1',bg='white',activebackground='white', activeforeground='firebrick1',cursor='hand2', variable=check)
terms.grid(row=9, column=0, pady=10, padx=15)

signupButton=Button(frame,text='Signup',font=('open sans',16,'bold'),fg='white',bg='firebrick1',
                    activebackground='firebrick1',activeforeground='white',width=17, command=connect_database)
signupButton.grid(row=10, column=0, pady=10)

already=Label(frame,text="Already have an account?", font=('Open sans','9', 'bold'),bg='white',fg='firebrick1')
already.grid(row=11,column=0,sticky='w',padx=25, pady=10)

loginButton=Button(frame, text='Log in', font=('Open sans', 9, 'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login)
loginButton.place(x=170,y=393)



signup.mainloop()
