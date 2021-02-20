from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
# creating a starting window
window = Tk()
window.title("Pomodoro clock")
window.config(padx=100, pady=50)
# creating a canvas
"""
so what is canvas ?
Canvas is a tkinter widget that allow us to place a things on top of each other.
"""
canvas = Canvas(height=224, width=200)  # our image is 200X223 pixel that why we take this value
tomato_img = PhotoImage(file="tomato.png")  # fetch an image
canvas.create_image(100, 112,
                    image=tomato_img)  # to place an image in center of scren we will half a height and half of width
canvas.pack()  # show a image on screen
window.mainloop()
