#Jabari  Mitchell
#December 1 2022
#Temp converter
#Converts temp from celsius to fareinheit and vice versa
from tkinter import *
import tkinter as tk
from tkinter import ttk

from tkinter import *
import tkinter as tk
from tkinter.tix import*
from tkinter import ttk
from tkinter import tix

from tkinter import BOTH, END, LEFT
#Creates tk instances

window = tix.Tk()
tooltip = Balloon(window)
#Creating a text box for user to enter tempature
Tempature_entry = ttk.Entry(window)
Tempature_entry.grid(row= 0, column =1)
tooltip.bind_widget(Tempature_entry, msg = "Enter the desired tempature you would like to convert")
# Creates the window
window.geometry ("400x250")
# minimum window size
window.minsize(width = 900, height = 250)
# window title
window.title("Jabari's Temp Converter")
far_res=tk.StringVar()
cel_res=tk.StringVar()
value=tk.StringVar()
#Defining variables

def close_window():
    window.quit()

#exit function
var1 = tk.IntVar()
var1.set(2)
def function_Name():
    if (var1.get()==1):
        cels=int(Tempature_entry.get())
        result= str("The input converts to ")+str(((cels*9)/(5))+32)+ str(" Fahrenheit")
    elif(var1.get()==2):
        farh=int(Tempature_entry.get())
        result=float((float(farh) - 32) * 5 / 9)
        result= str("The input converts to ")+str(((farh*9)/(5))+32)+ str(" Celsius")
    far_res.set(result)
    cel_res.set(result)

def validations(event=NONE):
    value=Tempature_entry.get()
    try:
        float(value)
    except:
        result=("Error")
        far_res.set(result)
        cel_res.set(result)
        return
    function_Name()
#Defining functions
def ResetButtonfunc():
    far_res.set("")
    cel_res.set("")
    Tempature_entry.delete(0,END)
    Tempature_entry.bind("<0>",ResetButtonfunc)
result=ttk.Label( textvariable=far_res,style="BW.TLabel").grid(row=3,column=8)
result=ttk.Label( textvariable=cel_res,style="BW.TLabel").grid(row=3,column=8)

#Row 0


#Row 1 Widgets:

radio_button_celsius = tk.Radiobutton(text="Farenheit",
      variable=var1, value=1).grid(row=5, column=0)
radio_button_fahrenheit = tk.Radiobutton(text="Celsius",
      variable=var1, value=2).grid(row=4, column=0)
tk.Label(text=("Tempature"), bg='white').grid(row=0,column = 0)

# Row 2: Widgets
#Output Label

#Row 3: Widgets

# Calculate: Button
convert_button= Button (text="Convert",bg ="#90EE90", width = 20,  command=validations)
tooltip.bind_widget(convert_button, msg = "Convert the desired temp")

convert_button.grid(row=3, column=1)
# Exit: Button
exit_button=Button(window, text="Exit",bg ="#FF5733", width = 20,command=close_window)
exit_button.grid(row=3, column=0)
tooltip.bind_widget(exit_button, msg = "Close the program")
#Clear: Button
clear_button=Button(window, text="Clear All",bg ="#FFF5F2", width = 20,command=ResetButtonfunc)
clear_button.grid(row=3, column=2)
tooltip.bind_widget(clear_button, msg = "Restart and clear all information")

#Binding keys
window.bind('<Return>',lambda event:validations())
window.bind('<Alt-R>',lambda event:ResetButtonfunc())
window.bind('<Alt-E>',lambda event:close_window())



#Runs the user interface
window.mainloop()