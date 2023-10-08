# Make sure to install all the Python libraries
# pip install python
 
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os, time, winsound

def createWidgets():

    label1= Label(root, text="Enter the time in HH:MM -")
    label1.grid(row=0, column=0, padx=5, pady=5)

    global entry1
    entry1=Entry(root, width=15)
    entry1.grid(row=0, column=1)

    label2= Label(root, text="Enter the message of alarm: ")
    label2.grid(row=1, column=0, padx=5, pady=5)

    global entry2
    entry2=Entry(root, width=15)
    entry2.grid(row=1, column=1)

    but=Button(root, text="Submit",width=10, command=submit)
    but.grid(row=2, column=1)

    global label3
    label3=Label(root, text="")
    label3.grid(row=3,column=0)

def message():

    global entry1,label3
    Alamtimelabel= entry1.get()
    label3.config(text="The Alarm is counting ....")
    messagebox.showinfo("Alarm Clock", f"The Alarm time is:{Alamtimelabel}")

def submit():
    global entry1, entry2, label3

    Alarmtime=entry1.get()
    message()

    currenttime= time.strftime("%H:%M")

    alarmmessage=entry2.get()

    print(f"The Alarm time is:{Alarmtime}")

    while Alarmtime != currenttime:
        currenttime= time.strftime("%H:%M")
        time.sleep()

    if Alarmtime==currenttime:
        print("Playing sound")
        winsound.PlaySound("*", winsound.SND_ASYNC)
        label3.config(text="Alarm Sound Playing>>>")
        messagebox.showinfo("Alarm message", f"the message is:{alarmmessage}")
 
root=tk.Tk()
root.title("Alarm Clock")
root.geometry("400x150")

createWidgets()

root.mainloop()
