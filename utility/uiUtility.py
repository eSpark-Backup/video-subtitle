import json
import PIL
import time
import tkinter as tk
import tkinter.font as tkfont
from PIL import ImageTk, Image
from enum import Enum

#********************* Font Enums & Functions *********************
class FontFamily(Enum):
    Calibri             = 1
    Helvetica           = 2
    Verdana             = 3
    Times_New_Roman     = 4

class FontSize(Enum):
    S_100 = 1
    S_120 = 2
    S_140 = 3 

class FontColor(Enum):
    BLACK   = 1
    WHITE   = 2
    RED     = 3
    BLUE    = 4
    GREEN   = 5           

class FontWeight(Enum):
    normal  = 1 
    bold    = 2

class FontStyle(Enum):
    roman   = 1
    italic  = 2
#Function to change Enum.name into meaningul font-Size string
def FontSizeStr(size):
    size = size.lstrip("S_")
    return size

#Function to change Enum.name into meaningul font-family string
def FontFamilyStr(name):
    name = name.replace("_"," ")
    return name

#********************* Font Enums & Functions *********************

#********************* Functions Approach *********************
def createWindow():
    # Create the main Window &  Frame
    window = tk.Tk()
    window.title("Font Selection")
    window.geometry("1920x515")
    #window.attributes('-fullscreen', True)
    frame = tk.Frame(master=window, width=1920, height=515)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    return window, frame

def destroyWindow(window):
    window.destroy()

def characterLimit(frame, font):
    # Finding Character Limit, by referencing an alphabet & calculating the average number of charaters, 
    # which can be displayed on the screen by the given font configuration;
    charLimit = 0
    sampleCharLen = font.measure("0")
    charOffset = font.measure("W")

    # Displaying Text on a Label & figuring out the Characters Limit
    labelCharLimit = tk.Label(master=frame, text="0", fg="white", font=font)
    for x in range(100):
        if(x*sampleCharLen < charOffset):
            continue
        else:
            if(x*sampleCharLen <= 1920 - 2*charOffset) :
                labelCharLimit.place(x=x*sampleCharLen, y=0)
            else :
                charLimit = x-1
                labelCharLimit.destroy()
                break
    print("Character Limit = " + str(charLimit))
    return int(charLimit)
    # Now, we have a value for Character Limit which we can display on each client!

def fontSelection(fontConfig):
    fontSize =      FontSize(   int(fontConfig["fontSize"])    )
    fontStyle =     FontStyle(  int(fontConfig["fontStyle"])   )
    fontWeight =    FontWeight( int(fontConfig["fontWeight"])  )
    fontFamily =    FontFamily( int(fontConfig["fontType"])    )
    #fontColor =     FontColor(  int(fontConfig["fontColor"])   )

    # selFont will be used as the selected font for the UI-Display, it is configured with the selected font configurations
    selFont = tkfont.Font(family=FontFamilyStr(fontFamily.name), size=FontSizeStr(fontSize.name), slant=fontStyle.name, weight=fontWeight.name)
    
    return selFont

def createLabelText(frame, selFont):
    # Create a label to display the selected font
    textLabel= tk.Label(master=frame)

    # Configuring UI font with the selected configuration
    textLabel.config(font=selFont)
    textLabel.config(fg="BLACK")

    # Pack the widgets into the window
    textLabel.pack(side=tk.TOP, pady=200)

    return textLabel