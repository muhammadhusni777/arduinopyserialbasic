'''
BASIC SERIAL TERMINAL PY
WRITTEN BY MUHAMMAD HUSNI WHEN HE IS GABUT
RUN USE THONNY IDE AND PYTHON 3.9.0
I HOPE THIS HELP YOU FOR MAKING TKINTER INTERFACE FOR ARDUINO
'''

import serial
import serial.tools.list_ports
import time
import tkinter as tk
from tkinter import *

ser = serial.Serial()
ser.baudrate = 9600

def connect():
    ser.port = port_select.get()
    ser.open()
    print(port_select.get())
    ser.flushinput()
def led_on():
    message = 'H'
    ser.write(message.encode())

def disconnect():
    ser.close()

def led_off():
    message = 'L'
    ser.write(message.encode())

def send():
    data_send = send_string.get()
    ser.write(data_send.encode())
    
def receive():    
    myData_raw = ser.readline().strip()
    global myData
    myData = myData_raw.decode("utf-8")
    label5.config(text=myData)
        

time.sleep(2) # wait for the serial connection to initialize

master = tk.Tk()
master.title("Basic Python Tkinter Arduino Terminal")
master.geometry('400x500')

port_select = tk.StringVar()
send_string = tk.StringVar()


label1 = tk.Label(master, text = 'ARDUINO PORT : ', font = "BOLD")
label1.place(x=0, y=0)

form_port = tk.Entry(master, textvariable = port_select)
form_port.place(x=140, y=5)

connect_button = tk.Button(master, text='connect', command=connect , width=10, height=1)
connect_button.place(x=100, y=50)

disconnect_button = tk.Button(master, text='disconnect', command=disconnect, width=10, height=1)
disconnect_button.place(x=200, y=50)


label2 = tk.Label(master, text = 'LED BUILDIN TEST : ', font = "BOLD")
label2.place(x=0, y=100)

led_on_button = tk.Button(master, text='led buildin on', command=led_on, width = 10, height=1)
led_on_button.place(x = 100, y=150)

led_off_button = tk.Button(master, text='led buildin off', command=led_off, width=10, height=1)
led_off_button.place (x=200, y = 150)

label3 = tk.Label(master, text = 'SEND STRING TO ARDUINO : ', font = "BOLD")
label3.place(x=0, y=200)

form_data_send = tk.Entry(master, textvariable = send_string, width = 50)
form_data_send.place(x = 0, y=220)

data_send_button = tk.Button(master, text='send data', command=send, width = 10, height =1)
data_send_button.place(x=310, y=220)

label4 = tk.Label(master, text = 'RECEIVE STRING TO ARDUINO : ', font = "BOLD")
label4.place(x=0, y=250)

label5 = tk.Label(master, text = 'myData', font = "BOLD")
label5.place(x=50, y=300)

receive_button = tk.Button(master, text='receive', command=receive, width=10, height=1)
receive_button.place(x=50, y=400)



master.mainloop()

