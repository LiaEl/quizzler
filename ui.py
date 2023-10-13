from tkinter import *
import html

BG_COLOR = "#435B66"
COLOR_ONE = "#FFF4F4"


class QuizInterface:

    def __init__(self, brain):
        self.brain = brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.configure(bg=BG_COLOR)
        self.window.minsize(380, 560)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=4)
        self.window.rowconfigure(2, weight=2)

        yes_img = PhotoImage(file="images/true.png")
        self.button_yes = Button(image=yes_img, command=self.btn_yes)
        self.button_yes.place(x=60, y=400)

        no_img = PhotoImage(file="images/false.png")
        self.button_no = Button(image=no_img, command=self.btn_no)
        self.button_no.place(x=220, y=400)

        self.score_label = Label(text="Score ",
                                 bg=BG_COLOR,
                                 fg=COLOR_ONE,
                                 font=("Courier", 15, "bold"))
        self.score_label.place(x=40, y=20)

        self.canvas = Canvas(width=300, height=250, bg=COLOR_ONE)
        self.question = self.canvas.create_text(150, 100,
                                                  text="",
                                                  width=280,
                                                  font=("Arial", 18, "italic"),
                                                  fill=BG_COLOR)
        self.canvas.place(x=40, y=100)
        self.next_question()

        self.window.mainloop()

    def btn_yes(self):
        self.brain.check_answer(user_answer="True")
        if self.brain.still_has_questions():
            self.next_question()
        else:
            self.end_of_game()

    def btn_no(self):
        self.brain.check_answer(user_answer="False")
        self.next_question()

    def next_question(self):
        score = self.brain.get_score()
        self.score_label.config(text=f"Score {score}")
        self.canvas.itemconfig(self.question, text=html.unescape(self.brain.next_question()))

    def end_of_game(self):
        self.button_yes.place_forget()
        self.button_no.place_forget()
        self.score_label.place_forget()
        score = self.brain.get_score()
        end_text = f"End of the game. \nYour score {score}"
        self.canvas.itemconfig(self.question, text=end_text)
