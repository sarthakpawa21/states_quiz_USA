import turtle as tt

class Pen(tt.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def writestatename(self,state,x,y):

        self.goto(x,y)
        self.write(state, align='center', font=('Arial', 10, 'bold'))


