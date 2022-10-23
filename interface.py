from asyncore import read
import tkinter as tk
from tkinter import *
from turtle import color
from list_wifi import *
from plotsignal  import plot_signal
from connect_ner import *

rows=[]
def search_wifi():
   records=read_data_from_cmd()
   y='\n'.join(f"({','.join(str(x) for x in item)})" for item in records)
   return(y)

wifi=read_data_from_cmd()
window = tk.Tk()
window.title('wifi interface')
window.config(bg='white')

#SEARCH EVERY WIFI AVAILABLE
x=search_wifi()
greeting = tk.Label(window,text=x,font=("weight",13))
greeting.place(x=500,y=120)
greeting.config(bg='white',fg='black')
window.geometry('1250x800')


#PLOT BUTTON
plotbutton=tk.Button(window, text='show signal analysis',command=lambda:plot_signal(),bg='green').place(x=1100,y=50)


#STATUS
y=read_data_from_cmd()
if len(y)==0:
        CurrentWifi='NOT CONNECTED TO ANY WiFi'
else:
        CurrentWifi='CONNECTED TO '+(str(y[len(y)-1][0]))

currentconnection=tk.Label(window,text=CurrentWifi,font=("weight",25))
currentconnection.pack()
currentconnection.config(bg='white',fg='green')


window.mainloop()
