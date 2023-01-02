import tkinter as tk
import tkinter.font as tkfont

# Create the main Window &  Frame
window = tk.Tk()
window.title("Font Selection")
window.geometry("1920x640")
frame = tk.Frame(master=window, width=1920, height=640)
frame.pack()

# Create a list of font families
font_families = ("Calibri", "Helvetica", "Verdana", "Times New Roman")
# Create a list of font sizes
font_sizes = ["100","120","140"]
# Create a list of font styles
font_styles = ["normal", "bold", "italic", "bold italic"]

# Create a dropdown menu for selecting the font family
font_family_var = tk.StringVar(master=frame)
font_family_var.set(font_families[1])  # default value
font_family_menu = tk.OptionMenu(frame, font_family_var, *font_families)
font_family_menu.config( width=20, height=1 )

# Create a dropdown menu for selecting the font size
font_size_var = tk.StringVar(master=frame)
font_size_var.set(str(font_sizes[1]))  # default value
font_size_menu = tk.OptionMenu(frame ,font_size_var, *font_sizes)
font_size_menu.config( width=20, height=1 )

# Create a dropdown menu for selecting the font style
font_style_var = tk.StringVar(master=frame)
font_style_var.set(font_styles[2])  # default value
font_style_menu = tk.OptionMenu(frame ,font_style_var, *font_styles)
font_style_menu.config( width=20, height=1 )

# Saving the default configuration of font
defaultFont = (font_family_var.get(), font_size_var.get(), font_style_var.get())

# Define a function to update the fontDemolabel's font when the selection changes
def update_font(*args):
    global font

    if(font_style_var.get() == "normal" or font_style_var.get() == "bold"):
        font = tkfont.Font(family=font_family_var.get(), size=font_size_var.get(), weight=font_style_var.get())
    elif(font_style_var.get() == "italic"):
        font = tkfont.Font(family=font_family_var.get(), size=font_size_var.get(), slant=font_style_var.get())
    else:
        style = font_style_var.get().split(" ")
        font = tkfont.Font(family=font_family_var.get(), size=font_size_var.get(), weight=style[0], slant=style[1])

    fontDemoLabel.config(font=font)
    charSize = font.measure("0")

    # char_len_Label is test-run label, which helps to specify the limit of characters avaiable on the selected font.
    char_len_Label = tk.Label(master=frame, font=font)
    for x in range(100):
        if(x*charSize <= 1920) :
            char_len_Label.place(x = x*charSize, y=0)
        else :
            char_len_Label.destroy()
            print("Character Limit = " + str(x-1))
            break


# Call the update_font function whenever the selection changes
font_family_var.trace("w", update_font)
font_size_var.trace("w", update_font)
font_style_var.trace("w", update_font)

# Create a label to display the selected font
fontDemoLabel= tk.Label(master=frame, text="Selected Font", font=defaultFont)
# Pack the widgets into the window
fontDemoLabel.pack()
font_family_menu.pack()
font_size_menu.pack()
font_style_menu.pack()

# Run the main loop
window.mainloop()
