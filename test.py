import tkinter as tk
# from tkinter import 
from tkinter.ttk import *
import tkinter.messagebox as tm
import time
from astropy.table import Table, Column

class Timely(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames={}
        for F in (startpage, login_page, my_account, timer, report):
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
        # txt_password.grid(column=1,row=1)

        
        log_in = tk.Button(self, text="log in to my account",command=lambda: self.clicked(controller))
        log_in.pack()

    def clicked(self,controller):        
        res_name = self.txt_name.get()
        res_password = self.txt_password.get()    
        if res_name == "john" and res_password == "123456":
            tm.showinfo("Login info ", "Welcome John")
            controller.show_frame(my_account)
        else:
            tm.showerror("Login error ", "Incorrect user name or password ")

class my_account(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        account = tk.Label(self, text = "My Account", font = ("Arial", 14))
        account.pack(pady=20, padx=20)

#################
        # web = tk.Label(self, text = "Please enter the website you want to block: ", font = ("Arial", 14))
        # web.pack(pady=10, padx=10)
        # self.web_name = tk.Entry(self, width=20)
        # self.web_name.pack()
        
        button = tk.Button(self, text="Set time", command=lambda: controller.show_frame(timer))
        button.pack()
        button_report = tk.Button(self, text="See my report", command=lambda: controller.show_frame(report))
        button_report.pack()
    # def block(self, controller):
    #     path = r'C:\Windows\System32\drivers\etc\hosts'

    #     website= self.web_name.get()

    #     with open(path, 'a') as f:
    #         f.write(f'127.0.0.1 {website}')
        # controller.show_frame(timer)
class report(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        my_report = tk.Label(self, text="My Monthly Report", font=("Arial", 14))
        my_report.pack()
        quit_button = tk.Button(self, text='Quit', command=self.destroy)
        quit_button.pack()
        # Month = tk.Button(self, text = "December", command=show)
        # Month.pack()
        # label = tk.Label(self, text="High Scores", font=("Arial",30)).grid(row=0, columnspan=3)
        # create Treeview with 3 columns
        cols = ('date', 'set time', 'cumulative set time')
        self.listBox = Treeview(self, columns=cols, show='headings')
        # set column headings
        for col in cols:
            self.listBox.heading(col, text=col)    
        
        # listBox.grid(row=1, column=0, columnspan=2)

        DecReport = tk.Button(self, text="Dec Report", width=15, command= self.show)
        DecReport.pack()
        # closeButton = tk.Button(self, text="Close", width=15, command=exit).grid(row=4, column=1)

    def show(self):

        tempList = [['100','100'], ['60','160'], ['30','190'], ['180','370']]
        tempList.sort(key=lambda e: e[1], reverse=True)
        print(tempList)

        for i, (name, score) in enumerate(tempList, start=1):
            self.listBox.insert("", "end", values=(i, name, score))
        self.listBox.pack()

    # def table(self, controller):
    #     data_rows= [('12/01/18', '100','100'),
    #                 ('12/02/18', '60','160'),
    #                 ('12/03/18', '30','190'),
    #                 ('12/04/18', '180','370')]
    #     cols = ('date','time set', 'cumulative time set')
    #     t=Table(rows=data_rows, names = ('date','time set', 'cumulative time set'))
    #     listBox = Treeview(data_rows, columns=cols, show='headings')
        
    #     for col in cols:
    #         listBox.heading(col, text=col)    
    #     listBox.grid(row=1, column=0, columnspan=2)

        # self.time_str = tk.StringVar()
        # screen = tk.Label(self, textvariable=self.time_str, font="helvetica", bg='white', 
        # fg='blue', relief='raised', bd=3)
        # screen.pack(fill='x', padx=5, pady=5)
        


class timer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        enter = tk.Label(self, text="Please enter your goal time in seconds: ", font=("Arial", 14))
        enter.pack()
        self.my_time = tk.Entry(self, width = 10)
        self.my_time.pack()

        website= tk.Label(self, text="Please enter the website you want to block: ", font=("Arial", 14))
        website.pack()
        self.site = tk.Entry(self, width = 30)
        self.site.pack()

        # button = tk.Button(self,text = "set goal time", command=lambda: self.count_down(controller))
        # button.pack()
        start = tk.Button(self, text='Count Start', command=lambda: self.count_down(controller))
        start.pack()
        quit_button = tk.Button(self, text='Quit', command=self.destroy)
        quit_button.pack()
        self.time_str = tk.StringVar()
        screen = tk.Label(self, textvariable=self.time_str, font="helvetica", bg='white', 
        fg='blue', relief='raised', bd=3)
        screen.pack(fill='x', padx=5, pady=5)

    def count_down(self, controller):
        goal =self.my_time.get()
        print(goal)
        goaltime= int(goal)

        website_block = self.site.get()
        path = r'C:\Windows\System32\drivers\etc\hosts'


        with open(path, 'a') as f:
            f.write(f'\n127.0.0.1 {website_block}')
            print('block success!')


        for t in range(goaltime, -1, -1):
            sf = "{:02d}:{:02d}".format(*divmod(t, 60))
        #print(sf)  # test
            self.time_str.set(sf)
        # delay one second
            self.update()
            time.sleep(1)

        with open(path, 'w') as f:
            f.write(f'\n #127.0.0.1 {website_block}')
            print('unblock success!')
        
           

app = Timely()
app.mainloop()


