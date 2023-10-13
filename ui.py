from tkinter import *
import html
from quiz_brain import QuizBrain

BG_COLOR = "#435B66"
COLOR_ONE = "#FFF4F4"


class QuizInterface:

    def __init__(self, brain: QuizBrain):
        self.brain = brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.configure(pady=20, padx=20, bg=BG_COLOR)

        yes_img = PhotoImage(file="images/true.png")
        self.button_yes = Button(image=yes_img, command=self.btn_yes, highlightthickness=0)
        self.button_yes.grid(column=0, row=2)

        no_img = PhotoImage(file="images/false.png")
        self.button_no = Button(image=no_img, command=self.btn_no, highlightthickness=0)
        self.button_no.grid(column=1, row=2)

        self.score_label = Label(text="Score ",
                                 bg=BG_COLOR,
                                 fg=COLOR_ONE,
                                 font=("Courier", 20, "bold"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg=COLOR_ONE)
        self.question = self.canvas.create_text(150, 125,
                                                  text="",
                                                  width=280,
                                                  font=("Arial", 18, "italic"),
                                                  fill=BG_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.get_next_question()
        self.window.mainloop()

    def btn_yes(self):
        self.brain.check_answer(user_answer="True")
        if self.brain.still_has_questions():
            self.get_next_question()
        else:
            self.end_of_game()

    def btn_no(self):
        self.brain.check_answer(user_answer="False")
        if self.brain.still_has_questions():
            self.get_next_question()
        else:
            self.end_of_game()

    def get_next_question(self):
        score = self.brain.get_score()
        self.score_label.config(text=f"Score {score}")
        self.canvas.itemconfig(self.question, text=html.unescape(self.brain.next_question()))

    def end_of_game(self):
        self.button_yes.grid_forget()
        self.button_no.grid_forget()
        self.score_label.grid_forget()
        score = self.brain.get_score()
        end_text = f"End of the game. \nYour score {score}"
        self.canvas.itemconfig(self.question, text=end_text)
