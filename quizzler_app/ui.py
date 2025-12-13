from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzler")
        self.lbl_score = Label(text=f"Score: {self.quiz.score}",bg=THEME_COLOR, fg="white", font=("Arial", 12, "bold"))
        self.lbl_score.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Question Text", font=("Arial",18,"italic"), width=280, justify="center")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_img = PhotoImage(file="images/true.png")
        self.btn_true = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.btn_true.grid(row=2, column=0)
        false_img = PhotoImage(file="images/false.png")
        self.btn_false = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.btn_false.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
            self.lbl_score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz your final score was:{self.quiz.score}/10")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")


    def false_pressed(self):
            self.give_feedback("False")

    def true_pressed(self):
            self.give_feedback("True")


    def give_feedback(self, answer):
            self.window.after(1000, self.get_next_question)
            if self.quiz.check_answer(answer):
                self.canvas.config(bg="green")
            else:
                self.canvas.config(bg="red")



