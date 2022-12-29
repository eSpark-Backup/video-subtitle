import tkinter as tk
import tkinter.font as tkfont

# Create a Main Window
window = tk.Tk()
window.geometry("1920x640")

#Create a Frame
frame = tk.Frame(master=window, width=1920, height=500)
frame.pack()

# Define a Font and measure its average characterspace
subFont = tkfont.Font(family="Helvetica", 
                size=150, 
                weight = 'normal',
                slant='italic')
m_len = subFont.measure("0")
print(m_len)

# Displaying Text on a Label & figuring out the Characters Limit
for x in range(100):
    if(x*m_len <= 1920) :
        label1 = tk.Label(master=frame, text="x", bg="red", font= subFont)
        label1.place(x=x*m_len, y=0)
    else :
        print("Character Limit = " + str(x-1))
        break

window.mainloop()