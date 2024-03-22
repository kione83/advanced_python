import tkinter as tk

def create_window():
    window = tk.Toplevel()
    window.title("New Window")
    window.geometry("600x600")
    window.mainloop()

#i want a canvas in the new window
def create_canvas(window):
    canvas = tk.Canvas(window, width=600, height=600)
    canvas.pack()
    canvas.create_rectangle(50, 25, 150, 75, fill="blue")
    window.mainloop()

    