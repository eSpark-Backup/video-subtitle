import socket
import tkinter as tk
from tkinter import * 
from tkinter import font
import threading as th

HOST = "192.168.18.150"  # The server's hostname or IP address
PORT = 65432  # The port used by the server


def sock_fun():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            while True:
                data = s.recv(1024)
                label.config(text=data.decode())
        except:
            print()



def thread():
    t1 = th.Thread(target=sock_fun)
    t1.start()
    
window = tk.Tk()
window.title("Font Selection")
window.geometry("1920x515")
window.configure(bg="black")

text_string = " "
fnt = font.Font(family="Helvetica", size=60)
label = tk.Label(window, text=text_string, font=fnt ,fg="white", bg='black', pady=250)

label.pack() 

window.bind("<Return>", lambda e: window.destroy())
thread()
window.attributes('-fullscreen', True)
window.mainloop()