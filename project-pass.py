from tkinter import *
import tkinter.messagebox as tm
import tkinter as tk

# from tkinter.ttk import *
window = Tk()
window.title("Timely App")
window.geometry('350x200') #set window size
#create a label 
lbl_name = Label(window, text = "User Name: ", font = ("Arial", 14) )
lbl_name.grid(column=0, row=0)

lbl_pass = Label(window, text = "Password: ", font = ("Arial", 14))
lbl_pass.grid(column=0, row=1)

txt_name = Entry(window,width=10) 
txt_name.grid(column=1,row=0)
txt_password = Entry(window,show="*", width=10)
txt_password.grid(column=1,row=1)
        
# log_in = tk.Button(self, text="login",command=lambda: controller.show_frame(my_account_page))
# button.pack()
# click button
def clicked():
    res_name = txt_name.get()
    res_password = txt_password.get()
    if res_name == "john" and res_password == "123456":
        tm.showinfo("Login info ", "Welcome John")
        # button_name = tk.Label(window, text="My Account", font="Arial")
        # button_name.pack(pady=10, padx=10)
        # button_name = tk.Button(window, text="My Account")
        # button_name.pack()
    else:
        tm.showerror("Login error ", "Incorrect user name or password ")
# add a button
btn = Button(window, text="Login", bg = "black", fg = "white", command = clicked)
btn.grid(column=2, row=0)    


#checkbox: use to select the web you want to block

chk_state = IntVar()
chk_state.set(0) #uncheck
chk_state.set(1) #check
chk = Checkbutton(window, text='Remember me')
chk.grid(column=0, row=2)

#create a message box

window.mainloop()
