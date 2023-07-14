# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 13:22:35 2023

@author: new-kensyu
"""

from tkinter import *
import datetime
import time
import winsound
from threading import *

#creating a clock class and defining its attributes
class Clock():
    def __init__(self, root):
        self.root = root
        self.label = Label(root, text="", font=("TimesNewRoman", 20), fg="black")
        self.label.pack(pady=20)
        self.update_clock()
       
        #updating the every time in the window
    def update_clock(self):
        now = time.strftime("%Y年%m月%d日  %H時%M分%S秒")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

#thread to set an alarm
#helps to activate the alarm
def Threading():
    t1 = Thread(target=alarm)
    t1.start()

#defining alarm and its attributes
def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)
#if alarm and time is same then play the ring tone
        if current_time == set_alarm_time:
            print("Time to Wake up")
            #change the alarm sound if you want to , by changing the file name .wav
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

#mappint the window size
root = Tk()
root.geometry("600x600")
root.title("Alarm Clock")

#calling the clock class
app = Clock(root)

#labeling the size of the title in the root(windows)
Label(root, text="Alarm Clock", font=("Algerian", 20, "bold"), fg="red").pack(pady=10)

frame = Frame(root)
frame.pack()

#setting alarm hours
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24')
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

#setting alarm minutes
#tuple represent data that consists of a combination of multiple data.
minute = StringVar(root)
minutes = tuple("{:02d}".format(i) for i in range(60))
minute.set(minutes[0])
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

#setting alarm seconds
#A tuple is an unfamiliar word, but it is also called a set, and refers to a value in which multiple elements are arranged in a fixed order.
second = StringVar(root)
seconds = tuple("{:02d}".format(i) for i in range(60))
second.set(seconds[0])
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

#creating a set alarm button to activate the alarm
Button(root, text="Set Alarm", font=("Algerian", 20), command=Threading).pack(pady=20)

root.mainloop()
