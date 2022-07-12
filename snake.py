from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTIONS = {"UP": 90, "DOWN": 270, "RIGHT": 0, "LEFT": 180}


class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  def create_snake(self):
    for position in STARTING_POSITIONS:
      new_segment = Turtle(shape="square")
      new_segment.color("white")
      new_segment.penup()
      new_segment.goto(position)
      self.segments.append(new_segment)

  def move(self): 
    # range(start, stop, step)
    for seg_num in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)
      
  def up(self):
    if self.head.heading() != DIRECTIONS["DOWN"]:
      self.head.setheading(DIRECTIONS["UP"])
    else:
      pass

  def right(self):
    if self.head.heading() != 180:
      self.head.setheading(0)
    else: 
      pass

  def down(self):
    if self.head.heading() != 90:
      self.head.setheading(270)
    else:
      pass
      
  def left(self):
    if self.head.heading() != 0:
      self.head.setheading(180)
    else:
      pass

  
