import socket
import tkinter as tk
from tkinter import * 
from tkinter import font
import pysrt
import time

subs = pysrt.open('Windfall.srt', encoding='iso-8859-1')
sub_size = len(subs)
window = tk.Tk()


HOST = "192.168.18.150"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
PORT2 = 50000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    server_socket.bind((HOST, PORT2))
    server_socket.listen()
    conn2,addr2 = server_socket.accept()
    with conn:
        while True:
            for i in range(0,sub_size):
                sub = subs[i]
                result = (sub.text).replace('\n','').replace('-','')
                fnt = font.Font(family="Helvetica", size=40)
                width = fnt.measure(result)
                time_delay = (sub.end - sub.start).seconds
                if width > 1250:
                    split_result= result.split()
                    middle_index=len(split_result)//2
                    str1=split_result[:middle_index]
                    str2=split_result[middle_index:]
                    str1 = ' '.join(str1) 
                    str2 = ' '.join(str2)  
                    conn.sendall(str1.encode())
                    conn2.sendall(str2.encode())
                    time.sleep(time_delay)
                else:
                    conn.sendall(result.encode())
                    conn2.sendall(b"    ")
                    time.sleep(time_delay)
            conn.sendall(b'END')
            conn2.sendall(b"")
            break
