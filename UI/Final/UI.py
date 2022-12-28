import tkinter as tk
import time

#Define a function to close the window
def closeWin():
   root.destroy()

#Create main window
root = tk.Tk()
root.title("Subtitle Display")
root.geometry("1920x640");
root.attributes('-fullscreen', True)

closeButton = tk.Button(root, text= "Close", font=('Poppins bold', 16),command=closeWin)
closeButton.pack(side = tk.BOTTOM)

# #Create text label
text_label = tk.Label(root, font=("Calibiri", 120), height=4, width=50) #fontSize = 10; CharSize=14
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