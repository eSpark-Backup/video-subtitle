import tkinter as tk
from PIL import ImageTk, Image
import time

#Define a function to close the window
def closeWin():
   root.destroy()

#Create main window
root = tk.Tk()
root.title("Subtitle Display")
root.geometry("1920x640");
root.attributes('-fullscreen', True)

# ********* DISPLAYING LOGO **********
# Frame to Display Logo
frame = tk.Frame(root, width=1920, height=640)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("eSpark.png"))
# Create a Label Widget to display the Logo-Image
label = tk.Label(frame, image = img)
label.pack()
root.update()
time.sleep(3) 
frame.destroy()
# ********* DISPLAYING LOGO **********

closeButton = tk.Button(root, text= "Close", font=('Helvetica', 16),command=closeWin)
closeButton.pack(side = tk.BOTTOM)

# #Create text label
text_label = tk.Label(root, font=("Helvetica", 130, "italic"), height=4, width=50, borderwidth= 600) #fontSize = 10; CharSize=14
text_label.pack(side = tk.TOP, pady = 200)

while True:
        try:
                text_label.config(text="HELLO WORLD!")
                root.update()
                time.sleep(2) # Change delay time here

                text_label.config(text="TESTING UI!")
                root.update()
                time.sleep(2) # Change delay time here
        
        except KeyboardInterrupt :
                print("Program terminated manually!")
                raise SystemExit