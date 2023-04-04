from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.show_score(self.score)

    def show_score(self, score):
        self.goto(0, 245)
        self.write(f"SCORE: {score}", align="center", font=("Courier", 40, "normal"))

    def update_score(self):
        self.clear()
        self.show_score(self.score)

    def brick_broken(self):
        self.score += 1

    def game_over(self, player_wins):
        self.home()
        self.color("red")
        message = "GAME OVER"
        if player_wins:
            message += "\n🥳🥳 YOU WIN! 🎉🎉"
        else:
            message += "\nYOU LOSE! 😢"
        self.write(message, align="center", font=("Century", 20, "bold"))
