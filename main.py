import math
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Reset a timer to 00:00"""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer")
    check_label.config(font=(FONT_NAME, 18), fg=GREEN, bg=YELLOW)
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Start a timer"""
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break)
    elif reps % 2 == 0:
        timer_label.config(text="Short break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Start a count down"""
    count_min = math.floor(count / 60)  # min
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# creating a starting window
window = Tk()
window.title("Pomodoro clock")
window.config(padx=100, pady=50, bg=YELLOW)
# After method for ex:
# def something(*args):
#     for n in args:
#         print(n)

#
# """
# syntax for after method
# window.after(seconds_in_ms,function_name,unlimited_positional_agrs_pass_to_that_function)
# """
# window.after(1000, something, 2, 3, 4, 5, 6)  # this after method will run after certain delay

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
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)  # show a image on screen

# Creating a button
start_button = Button(text="start", bg=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

# Creating a checkmark
check_label = Label(font=(FONT_NAME, 18), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)
# reset button
reset_button = Button(text="reset", bg=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)
window.mainloop()
