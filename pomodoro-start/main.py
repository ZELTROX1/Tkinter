from tkinter import *
import math
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
mark = ""
timer1 = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer1
    global reps
    global mark
    window.after_cancel(timer1)
    reps = 0
    timer.config(text="Timer")
    tick.config(text="")
    mark = ""
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps%8 == 0:
        timer.config(text="Time for LONG BREAK")
        count_down(LONG_BREAK_MIN*60)
        window.attributes('-topmost', True)
    elif reps%2 == 0:
        timer.config(text="Time for BREAK")
        count_down(SHORT_BREAK_MIN*60)
        window.attributes('-topmost', True)
    else:
        timer.config(text="Time to WORK")
        count_down(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec<10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer1
        timer1 = window.after(1000, count_down, count-1)  #This make the window to pop up over other windows
    elif count == 0:
        start_timer()
        global reps
        global mark
        if reps % 2 != 0:
            mark += "✔"
        tick.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

timer = Label(text="Timer",font=("Times New Roman",25),bg=YELLOW)
timer.grid(column=1, row=0)

canvas = Canvas(width=200,height=223,bg=YELLOW,highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 110,image=tomato)
timer_text=canvas.create_text(100,127,text="00:00",font=("Times New Roman",25,"bold"))
canvas.grid(column=1,row=1)
start = Button(text="Start",highlightthickness=0,command=start_timer)
start.grid(column=0, row=2)


reset = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset.grid(column=2,row=2)

tick = Label(fg=GREEN,bg=YELLOW,font=("Arial",15))
tick.grid(column=1, row=3)



window.mainloop()