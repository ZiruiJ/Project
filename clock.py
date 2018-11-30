try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
import time
goal = input('Enter your goal time in seconds: ')  #怎么做出 分钟 秒
goaltime= int (goal)
def count_down():
    for t in range(goaltime, -1, -1):
        # format as 2 digit integers, fills with zero to the left
        # divmod() gives minutes, seconds
        sf = "{:02d}:{:02d}".format(*divmod(t, 60)) #how to add hour
        #print(sf)  # test
        time_str.set(sf)
        root.update()
        # delay one second
        time.sleep(1)
# create root/main window
root = tk.Tk()
time_str = tk.StringVar()
# create the time display label, give it a large font
# label auto-adjusts to the font
label_font = ('helvetica', 40)
tk.Label(root, textvariable=time_str, font=label_font, bg='white', 
         fg='blue', relief='raised', bd=3).pack(fill='x', padx=5, pady=5)
# create start and stop buttons
# pack() positions the buttons below the label
tk.Button(root, text='Count Start', command=count_down).pack()
# stop simply exits root window
tk.Button(root, text='Quit', command=root.destroy).pack()
# start the GUI event loop
root.mainloop()