import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a label to display the subtitles
label = tk.Label(root, text="", font=("Arial", 16))
label.pack()

# Open the text file with the subtitles
with open("subtitles.txt", "r") as f:
    # Read the subtitles one line at a time
    for line in f:
        # Update the label with the current subtitle
        label["text"] = line
        # Wait for 2 seconds before displaying the next subtitle
        root.after(10000, lambda: label.update())
        # Process any pending events
        root.update()

# Run the main loop
root.mainloop()
