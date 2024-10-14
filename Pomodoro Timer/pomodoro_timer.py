from tkinter import *
import math
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
COUNT_TRACKER = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global COUNT_TRACKER
    COUNT_TRACKER = 0
    window.after_cancel(TIMER)
    timer_label.config(text="TIMER")
    check_mark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global COUNT_TRACKER
    COUNT_TRACKER += 1
    work_sec = WORK_MIN* 60
    short_break_sec = SHORT_BREAK_MIN* 60
    long_break_sec = LONG_BREAK_MIN* 60

    if COUNT_TRACKER % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break")
        remind_break("Time for a long break! Stretch and hydrate.")
    elif COUNT_TRACKER % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break")
        remind_break("Take a short break!")
    else:
        count_down(work_sec)
        timer_label.config(text="Work Time")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(COUNT_TRACKER / 2)
        for _ in range(work_session):
            mark += "✔"
        check_mark_label.config(text=mark)


# ----------------------------BREAK REMINDER ------------------------------- #

def remind_break(message):
    messagebox.showinfo("Break Reminder", message)


# ---------------------------- UI SETUP ------------------------------- #
# Window Configuration
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas Configuration
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 125, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Label Configuration
timer_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)

check_mark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
check_mark_label.grid(column=1, row=4)

# Button Configuration
start = Button(text="Start", bg=YELLOW, activeforeground=GREEN, command=start_timer)
start.grid(column=0, row=3)

reset = Button(text="Reset", bg=YELLOW, activeforeground=GREEN, command=reset_timer)
reset.grid(column=2, row=3)

window.mainloop()
