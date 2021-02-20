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
window.config(padx=100, pady=50, bg=YELLOW)
# creating a label .
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)

# creating a canvas
"""
so what is canvas ?
Canvas is a tkinter widget that allow us to place a things on top of each other.
"""
canvas = Canvas(height=224, width=200, bg=YELLOW,
                highlightthickness=0)  # our image is 200X223 pixel that why we take this value
tomato_img = PhotoImage(file="tomato.png")  # fetch an image
canvas.create_image(100, 112,
                    image=tomato_img)  # to place an image in center of scren we will half a height and half of width
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)  # show a image on screen

# Creating a button
start_button = Button(text="start",bg=YELLOW)
start_button.grid(row=2, column=0)

# Creating a checkmark
check_label = Label(text="✓", font=(FONT_NAME, 18), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)
# reset button
reset_button = Button(text="reset",bg=YELLOW)
reset_button.grid(row=2, column=2)
window.mainloop()
