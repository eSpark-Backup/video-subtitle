import tkinter as tk
from tkinter import BOTH, END, LEFT

win = tk.Tk(screenName="Video Subtitles")
win.geometry("10x50")  

#Define a function to clear the input text
def clearTextInput():
    # if  > :
        t1.delete("1.0","end")
    # elif a == b:
        # print("a and b are equal")

font1=('Times',14)
t1 = tk.Text(win, width=10, height=1, font=font1) #text box
t1.grid(row=1, column=2, columnspan=2, pady=1) 

t1.insert(tk.END, "WE'RE JUST TWO LOST SOULS, SWIMMING IN A FISHBOWL.")

# for x in range(5):
#     t1.insert(tk.END,"H");
#     if x == :
# clearTextInput()

win.mainloop()