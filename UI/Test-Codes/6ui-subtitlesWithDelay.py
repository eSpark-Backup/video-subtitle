import tkinter as tk
import time

#Create main window
root = tk.Tk()
root.title("Subtitle Display")

#Create text label
text_label = tk.Label(root, font=("Arial", 16))
text_label.pack()

#Open file and read lines
with open("subtitles.txt", "r") as file:
    lines = file.readlines()

#Iterate through lines and display each one with a delay
for line in lines:
    text_label.config(text=line)
    root.update()
    time.sleep(0.5) # Change delay time here

#.mainloop() keeps window open
root.mainloop()