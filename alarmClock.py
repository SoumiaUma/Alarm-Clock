#Importing libraries needed for GUI alarm clock 
from tkinter import *
import datetime
import time
import winsound

#Function to play noice when set time has been reached
def alarm(alarmTime):
    while True:
        time.sleep(1)
        currentTime = datetime.datetime.now()
        exactCurrentTime = currentTime.strftime("%H:%M:%S")
        date = currentTime.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(exactCurrentTime)
        if exactCurrentTime == alarmTime:
            print("Time is up!")
            #Playing windows default noice
            winsound.PlaySound("*",winsound.SND_ASYNC)
            break

#Retreiving the actual time
def actualTime():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

#Creating the GUI for the alarm clock
clock = Tk()
#Setting the name of the application
clock.title("Soumia's Alarm Clock")
#Setting a background colour for the GUI
clock.configure(background='deeppink')
#Setting the size for the GUI
clock.geometry("420x180")
#Creating the text boxes for the GUI with information for setting the alarm and displaying the headers for input
time_format=Label(clock, text= "Please Enter Time for Alarm in 24 Hour Format!", fg="black",bg="deeppink",font="Impact").place(x=210, y=20, anchor=CENTER)
addTime = Label(clock,text = "Hour   Minute  Second",bg="deeppink",font=80).place(x=200, y=80, anchor=CENTER)

#Creating variables to take user input for setting the alarm:
hour = StringVar()
min = StringVar()
sec = StringVar()

#User input text fields for getting the hour, minute and second the user wants to set the alarm (in 24-hour format)
hourTime= Entry(clock,textvariable = hour,bg = "MediumPurple", width = 15).place(x=95, y=90)
minTime= Entry(clock,textvariable = min,bg = "MediumPurple",  width=15).place(x=160, y=90)
secTime = Entry(clock,textvariable = sec,bg = "MediumPurple",  width=15).place(x=225, y=90)

#Creating a button to set the alarm:
submit = Button(clock,text = "Set Alarm",fg="black",bg="pink",width = 10,command = actualTime).place(x=220,y=140, anchor=CENTER)

#To execute the application
clock.mainloop()


