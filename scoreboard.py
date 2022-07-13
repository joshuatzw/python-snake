from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 13, 'normal')

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()


    self.score = 0
    with open ("high_score.txt") as file:
      contents = file.read()
      self.high_score = int(contents)

    self.color("white")
    self.penup()
    self.goto(0, 280) 
    self.update_scoreboard()
    self.hideturtle()
    self.speed("fastest")
    
  def update_scoreboard(self):
    self.clear()
    self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

  def increase_score(self):
    self.score += 1
    self.update_scoreboard()

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open ("high_score.txt", mode="w") as file:
        file.write(f"{self.high_score}")
        
    self.score = 0
    self.update_scoreboard()
    
    
