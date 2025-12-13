from tkinter import*
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
turn = 0
timer = ""
marks = ""
is_start = False

def reset_timer():
    window.after_cancel(timer)
    lbl_timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text= "00:00")
    global marks
    marks = ""
    global turn
    turn = 0
    global is_start
    is_start = False
    lbl_check.config(text="")
def count_down(count):
    count_sec = count % 60
    if count_sec < 10:
        count_sec =f"0{count_sec}"
    count_min = count // 60
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer= window.after(1000, count_down, count-1)
    else:
        start_counting()
        global marks
        marks = ""
        for i in range(turn//2):
            marks+= "✅️"
        lbl_check.config(text=marks)
def start_counting():
    global is_start
    if not is_start:
        global turn
        turn+=1
        if turn%2 == 1:
            count_down(WORK_MIN*60)
            lbl_timer.config(text="Work", fg=GREEN)
        elif turn%8 ==0:
            count_down(LONG_BREAK_MIN*60)
            lbl_timer.config(text="Long Break", fg=RED)
        else:
            count_down(SHORT_BREAK_MIN*60)
            lbl_timer.config(text="Break", fg=PINK)
    is_start = True
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")
lbl_timer = Label(text="Timer", font=(FONT_NAME, 26, "bold"), fg=GREEN, bg= YELLOW)
lbl_timer.grid(row= 0, column=1)
canvas = Canvas(width= 200, height= 224, bg=YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image= tomato_img)
timer_text= canvas.create_text(100, 130, text="00:00",font=("", 20, "bold"), fill="#fff")
canvas.grid(row=1, column=1)
btn_start = Button(text="Start", font=("", 12), width= 5, command= start_counting)
btn_start.grid(row= 2, column= 0)
lbl_check = Label(font=("", 18), fg=GREEN, bg=YELLOW )
lbl_check.grid(row=3, column=1)
btn_reset = Button(text="Reset", font=("", 12), width= 5, command= reset_timer)
btn_reset.grid(row=2, column=2)
window.mainloop()
