import csv
import pandas as pd
import turtle as tt
from pen import Pen

screen = tt.Screen()
screen.setup(height=500,width=750)
screen.title('States Game USA')
screen.bgpic('blank_states_img.gif')

pen = Pen()

data = pd.read_csv('50_states.csv')
states_list = [name.lower() for name in data['state']]

names_guessed = 0
while names_guessed < 50:
    user_guess = screen.textinput(f'{names_guessed}/50','Enter the name of a State :')
    if user_guess.lower() in states_list:
        index = states_list.index(user_guess.lower())
        x = int(data['x'][index])
        y = int(data['y'][index])

        pen.writestatename(user_guess,x,y)
        names_guessed +=1
        states_list.remove(user_guess.lower())

pen.goto(0,0)
pen.write("YOU WIN", align='center', font=('Arial', 40, 'bold'))



screen.exitonclick()
