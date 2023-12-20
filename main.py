import pandas as pd
import turtle
from data import Generator

state = Generator()
win = turtle.Turtle()
win.penup()
win.hideturtle()
data = pd.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("USA State")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

chose_user = 0

while chose_user < state.numer_of_states:
  user_write = screen.textinput(
      f'{chose_user}/{state.numer_of_states} States Correct',
      prompt="Write the State:").title()
  if user_write == "Exit":
    state.creat_csv()
    break
  if state.compare_state(user_write):
    chose_user += 1
    state.get_coordinates(user_write)
win.write(f"Game over", align="center", font=("Arial", 30, "bold"))
screen.exitonclick()
