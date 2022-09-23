from tkinter import *
import datetime

FONT = ("Courier")
DARK_GRAY = "#3d3d3d"
Focus_Time = 1500
Break_Time = 300
counting_down = False
reps = -1
Timer = ""
check = "Finished sessions: "

# Window
window = Tk()
window.title("Pomodoro")
window.config(bg=DARK_GRAY)
window.geometry("400x600")


def Focus():
    """Calls the update_time function with 25 minutes as its starting time."""
    global Focus_Time
    global counting_down
    if not counting_down:  # Only updates time if the timer is not counting down.
        finished_sessions.place(x=25, y=20)
        title_label.config(text="FOCUS SESSION")  # Edits the text in title label to "FOCUS SESSION"
        title_label.place(x=25, y=50)
        update_time(Focus_Time)


def Break():
    global Break_Time
    global counting_down
    global check
    if not counting_down:  # Only updates time if the timer is not counting down.
        title_label.config(text="BREAK TIME")  # Edits the text in title label to "BREAK TIME"
        title_label.place(x=65, y=50)
        check += "✔"
        finished_sessions.config(text=check)
        finished_sessions.place(x=25, y=20)
        update_time(Break_Time)


def update_time(current_time):
    global counting_down
    global Timer

    if current_time >= 0:
        counting_down = True  # Turns countdown to True if timer is counting down
        Timer = window.after(1000, update_time, current_time - 1)
        min_sec = str(datetime.timedelta(seconds=current_time))
        canvas.itemconfig(timer, text=min_sec[-5:])
    else:
        counting_down = False
        loop()  # Calls the function loop again to start over.


def loop():
    global reps

    if reps > 8:  # Checks if there is already 5 focus sessions
        title_label.config(text="5 Sessions Finished!", font=(FONT, 24, "bold"), fg="white")
        title_label.place(x=10, y=60)
        return
    if not counting_down:  # Checks if the timer is counting down.
        reps += 1
        if reps % 2 == 0:
            Focus()  # Sets the timer to 25 minutes.
        else:
            Break()  # Sets the timer to 5 minutes.


def reset():
    global Timer
    global counting_down
    global reps
    global check

    window.after_cancel(Timer)
    canvas.itemconfig(timer, text="00:00")
    title_label.config(text="POMODORO\nTIMER", bg=DARK_GRAY, fg="white", font=(FONT, 32, "bold"))
    title_label.place(x=100, y=0)
    finished_sessions.config(text="")

    counting_down = False
    reps = -1
    Timer = ""
    check = "Finished sessions: "


# TITLE
title_label = Label(text="POMODORO\nTIMER", bg=DARK_GRAY, fg="white", font=(FONT, 32, "bold"))
title_label.place(x=100, y=0)

# CLOCK
canvas = Canvas(width=400, height=600, bg=DARK_GRAY, highlightthickness=0)
clock_img = PhotoImage(file="clock.png")
canvas.create_image(200, 200, image=clock_img)
timer = canvas.create_text(200, 208, text="00:00", fill="white", font=(FONT, 45, "bold"))
canvas.place(x=0, y=100)

# Finished sesh
finished_sessions = Label(bg=DARK_GRAY, fg="white", font=(FONT, 12, "bold"))

# BUTTON
button = Button(text="START", bg=DARK_GRAY, fg="white", font=(FONT, 22, "bold"), command=loop)
button.place(x=80, y=500)

reset_button = Button(text="RESET", bg=DARK_GRAY, fg="white", font=(FONT, 22, "bold"), command=reset)
reset_button.place(x=200, y=500)

window.mainloop()
