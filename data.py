from turtle import Turtle
import pandas as pd
data = pd.read_csv("50_states.csv")

class Generator(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.numer_of_states = len(data["state"])
        self.position_x = 0
        self.position_y = 0
        self.list_state = [i for i in data["state"]]


    def compare_state(self, answer):
        for state in data["state"]:
            if state.lower() == answer.lower():
                self.list_state.remove(state)
                return True

    def get_coordinates(self, answer):

        states = data[data["state"] == answer]

        self.position_x = int(states["x"])
        self.position_y = int(states["y"])
        self.goto(self.position_x, self.position_y)
        return self.write(f"{answer.capitalize()}", align="center", font=("Arial", 10, "bold"))

    def creat_csv(self):
        data_learn = pd.DataFrame(self.list_state)
        data_learn.to_csv("learn state")


