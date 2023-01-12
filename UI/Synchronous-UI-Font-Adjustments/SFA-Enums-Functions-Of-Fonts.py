import json
import PIL
import time
import tkinter as tk
import tkinter.font as tkfont
from PIL import ImageTk, Image
from enum import Enum

# [Demo] Received Font Configuration in JSON Format:
recvJSON =  '{ "f_type":"3", "f_size":1, "f_color":"1", "f_style":"2", "f_weight":"2" }'

# parse recvJSON:
fC = json.loads(recvJSON)

# the result fC(fontConfig) is a Python dictionary:
print(fC["f_type"], fC["f_size"], fC["f_color"], fC["f_style"], fC["f_weight"])

#********************* Font Enums & Functions *********************
class FontStyle(Enum):
    roman   = 1
    italic  = 2

class FontWeight(Enum):
    normal  = 1
    bold    = 2

class FontColor(Enum):
    BLACK   = 1
    WHITE   = 2
    RED     = 3
    BLUE    = 4
    GREEN   = 5           

class FontSize(Enum):
    S_100 = 1
    S_120 = 2
    S_140 = 3 

class FontFamily(Enum):
    Calibri             = 1
    Helvetica           = 2
    Verdana             = 3
    Times_New_Roman     = 4

#Function to change Enum.name into meaningul font-Size string
def FontSizeStr(size):
    size = size.lstrip("S_")
    return size

#Function to change Enum.name into meaningul font-family string
def FontFamilyStr(name):
    name = name.replace("_"," ")
    return name

#********************* Font Enums & Functions *********************

# Create the main Window &  Frame
window = tk.Tk()
window.title("Font Selection")
window.geometry("1920x515")
#window.attributes('-fullscreen', True)
frame = tk.Frame(master=window, width=1920, height=515)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

#******************** LOGO Display ********************
# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("eSpark.png"))
# Create a Label Widget to display the Logo-Image
imgLabel = tk.Label(frame, image=img)
imgLabel.pack()
window.update()
time.sleep(3)
imgLabel.destroy()
#******************** LOGO Display ********************

fontSize =      FontSize(   int(fC["f_size"])    )
fontColor =     FontColor(  int(fC["f_color"])   )
fontStyle =     FontStyle(  int(fC["f_style"])   )
fontWeight =    FontWeight( int(fC["f_weight"])  )
fontFamily =    FontFamily( int(fC["f_type"])    )

# selFont will be used as the selected font for the UI-Display, it is configured with the selected font configurations
selFont = tkfont.Font(family=FontFamilyStr(fontFamily.name), size=FontSizeStr(fontSize.name), slant=fontStyle.name, weight=fontWeight.name)

#Printing the Font Configurations:
print("Font Family: " + selFont.cget('family'))
print("Font Size: " + str( selFont.cget('size') ) )
print("Font Color: " + fontColor.name)
print("Font Style: " + fontStyle.name)
print("Font Weight: " + fontWeight.name)

# Finding Character Limit, by referencing an alphabet & calculating the average number of charaters, 
# which can be displayed on the screen by the given font configuration;
charLimit = 0
sampleCharLen = selFont.measure("M")
print(sampleCharLen)

# Displaying Text on a Label & figuring out the Characters Limit
labelCharLimit = tk.Label(master=frame, text="a", fg="white", font=selFont)
for x in range(100):
    if(x*sampleCharLen <= 1920) :
        labelCharLimit.place(x=x*sampleCharLen, y=0)
    else :
        charLimit = x-1
        labelCharLimit.destroy()
        break
print("Character Limit = " + str(charLimit)) #str(x-1)
# Now, we have a value for Character Limit which we can display on each client!

# Create a label to display the selected font
UIDemoLabel= tk.Label(master=frame)

# Configuring UI font with the selected configuration
UIDemoLabel.config(font=selFont)
UIDemoLabel.config(fg=fontColor.name)

# Pack the widgets into the window
UIDemoLabel.pack(side=tk.TOP, pady=200)

# Run the main loop
while True:
    UIDemoLabel.config(text="Selected Font")
    window.update()
    time.sleep(3)

    UIDemoLabel.config(text="Testing 123")
    window.update()
    time.sleep(3)
