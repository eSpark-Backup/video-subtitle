import json
import tkinter as tk
import tkinter.font as tkfont
from enum import Enum

# [Demo] Received Font Configuration in JSON Format:
recvJSON =  '{ "f_type":"3", "f_size":3, "f_color":"1", "f_style":"2", "f_weight":"2" }'

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
window.geometry("1920x640")
frame = tk.Frame(master=window, width=1920, height=640)
frame.pack()

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

# Create a label to display the selected font
UIDemoLabel= tk.Label(master=frame, text="Selected Font")

# Configuring UI font with the selected configuration
UIDemoLabel.config(font=selFont)
UIDemoLabel.config(fg=fontColor.name)

# Pack the widgets into the window
UIDemoLabel.pack()

# Run the main loop
window.mainloop()

