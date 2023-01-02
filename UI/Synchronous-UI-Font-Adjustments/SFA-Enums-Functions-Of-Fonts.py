import tkinter as tk
import tkinter.font as tkfont
from enum import Enum

#********************* Font Enums & Functions *********************
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

fontFamily = FontFamily(2)
fontSize = FontSize(3)

selFontFamily = FontFamilyStr(fontFamily.name)
selFontSize = FontSizeStr(fontSize.name)

print("Font Family: " + selFontFamily)
print("Font Size: " + selFontSize)

selFont = tkfont.Font(family=selFontFamily, size=selFontSize)

# Create a label to display the selected font
fontDemoLabel= tk.Label(master=frame, text="Selected Font", font=selFont)
# Pack the widgets into the window
fontDemoLabel.pack()

# Run the main loop
window.mainloop()
