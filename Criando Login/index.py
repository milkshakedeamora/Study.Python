from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
import Database 

jan = Tk()
jan.title("Login")
jan.geometry("400x200")
jan.configure(background = "black")
jan.resizable(width=False, height = False)
jan.attributes ("-alpha",0.7)
Frame = Frame(jan, width = 400, height=400, bg = "#9acddc", relief = "raise")
Frame.pack(expand = True)

UserLabel = Label(Frame, text = "Username:", font = ("Century Gothic",20), bg = "#9acddc", fg= "black")
UserLabel.place(x=1, y = 20)
UserEntry = Entry(Frame, width= 40)
UserEntry.place(x =150, y = 35)

PassLabel = Label(Frame, text = "Password:", font = ("Century Gothic",20), bg = "#9acddc", fg= "black")
PassLabel.place(x=1, y = 60)
PassEntry = Entry(Frame, width= 40, show = "✩")
PassEntry.place(x =150, y = 75)

def Login():
    User = UserEntry.get();
    Pass = PassEntry.get();
    Database.cursor.execute(""" SELECT * FROM Users WHERE username = ? AND password = ? """,(User,Pass))
    verify = Database.cursor.fetchone()
    try:
        if(User in verify and Pass in verify):
            messagebox.showinfo(title = "Logado.", message = "Login realizado.")
    except:
        messagebox.showwarning(title = "Acesso Negado", message= "Acesso Não Permitido. Verifique a senha e login.")

LoginButton = ttk.Button(Frame, text = "Login", width = 40, command= Login)
LoginButton.place( x = 100, y = 100)





jan.mainloop()