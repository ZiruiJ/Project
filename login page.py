import tkinter as tk
# from tkinter import 
from tkinter.ttk import *
import tkinter.messagebox as tm

class Timely(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames={}
        for F in (startpage, login_page, my_account):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(startpage)
    def show_frame(self, cont):
        frame=self.frames[cont]
        frame.tkraise()

class startpage(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to Timely", font="Arial")
        label.pack(pady=10,padx=10)
        button = tk.Button(self, text="Log in",command=lambda: controller.show_frame(login_page))
        button.pack()

class login_page(tk.Frame):

    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        lbl_name = tk.Label(self, text = "User Name: ", font = ("Arial", 14) )
        lbl_name.pack(pady=10,padx=10)

        # self.entry_password = Entry(self)
        self.txt_name = tk.Entry(self,width=10) 
        self.txt_name.pack()

        lbl_pass = tk.Label(self, text = "Password: ", font = ("Arial", 14))
        lbl_pass.pack(pady=10,padx=10)
        
        # txt_name.grid(column=1,row=0)
        self.txt_password = tk.Entry(self,show="*", width=10)
        self.txt_password.pack()
        # txt_password.grid(column=1,row=1) ????

        
        log_in = tk.Button(self, text="log in to my account",command=lambda: self.clicked(controller))
        log_in.pack()

    def clicked(self,controller):        
        res_name = self.txt_name.get()
        res_password = self.txt_password.get()    
        if res_name == "john" and res_password == "123456":
            tm.showinfo("Login info ", "Welcome John")
            # button_name = tk.Label(window, text="My Account", font="Arial")
            # button_name.pack(pady=10, padx=10)
            # button_name = tk.Button(window, text="My Account")
            # button_name.pack()
            controller.show_frame(my_account)
        else:
            tm.showerror("Login error ", "Incorrect user name or password ")

class my_account(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        account = tk.Label(self, text = "My Account", font = ("Arial", 14))
        account.pack(pady=20, padx=20)

    


app = Timely()
app.mainloop()

