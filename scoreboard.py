from turtle import Turtle
FONT = ('Courier', 23, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # setup playerscore and get highScore from saveFile'highscore.txt'
        self.player_score = 0
        with open("highscore.txt", mode="r") as saveFile:
            self.saved_highscore = saveFile.read()

        # Setup scoreBoard
        self.penup()
        self.pencolor("white")
        self.setposition(0, 270)
        self.hideturtle()
        self.fillcolor("white")

    def increase_player_score(self):
        self.player_score += 1

    def print_scoreboard(self):
        """Updates the scoreBoard"""
        self.clear()
        self.write(f"Score:{self.player_score}   HighScore:{self.saved_highscore}", False, align="center", font=FONT)

    def reset(self):
        # if playerScore is bigger than highScore: new highScore
        if self.player_score > int(self.saved_highscore):
            self.saved_highscore = self.player_score
            # save new highscore even after gameExit, in highscore.txt
            with open("highscore.txt", mode="w") as saveFile:
                saveFile.write(str(self.saved_highscore))
        self.player_score = 0
        self.print_scoreboard()
