# importing Tkinter module

from tkinter import *

# from tkinter.ttk import *
# creating master Tkinter window
master = Tk()
master.geometry("175 * 175")
# Tkinter string variable
# able to store any string value
V = StringVar(master, "1")
# dictionary to create multiple buttons
values = {"radio button 1": "1",
          "radio button 2": "2",
          "radio button 3": "3",
          "radio button 4": "4",
          "radio button 5": "5"}

# loop is used to create multiple radio buttons
# rather than creating each button separately
for (text, value) in values.items():
 Radiobutton (master, text=text, variable=V,
 value=value, indicator=0,
 background="light blue").pack(fill=X, ipady=5)

# infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy ())
mainloop()
