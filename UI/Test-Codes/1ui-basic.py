from tkinter import Tk, Text

root = Tk()
root.resizable(False, False)
root.title("Text Widget Example")

#  the height argument specifies the number of rows of the Text widget.
text = Text(root, height=8)
text.pack()


# The first argument of the insert() method is the position where you want to insert the text.
# The position has the following format:
# 'line.column'
# ‘1.0’ means line 1, character 0, which is the first character of the first line on the text area.
text.insert('1.0', 'This is a Text widget demo')

root.mainloop()