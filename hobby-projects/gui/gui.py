import tkinter as tk

# Set the root and its width and height
root = tk.Tk()
root.geometry("500x500")

# Set the root's title and icon
root.title("CS50 Final Project")
icon = tk.PhotoImage(file="assets/luffy.png")
root.iconphoto(True, icon)

# Run the root gui
root.mainloop()