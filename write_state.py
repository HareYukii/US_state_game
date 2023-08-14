from turtle import Turtle
FONT = ("Courier", 20, "normal")


class WriteState(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state_name(self, guess, x_pos, y_pos):
        self.setposition(x_pos, y_pos)
        self.write(f"{guess}", False, "center", FONT)
