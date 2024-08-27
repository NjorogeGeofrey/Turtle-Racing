from turtle import Turtle, Screen
import random
screen = Screen()

game_on = False
screen.setup(500, 400)
user_bet = screen.textinput(title = "Make your bet.", prompt= "Which turtle will win the race. Enter a color: ")

colors = ["red", "yellow", "purple", "green", "black", "pink"]
y_axis = [-110, -60, -10, 40, 90, 140]

all_turtles = []

for index in range(6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.penup()
    new_turtle.goto(x= -230, y= y_axis[index])
    new_turtle.color(colors[index])
    all_turtles.append(new_turtle)

if user_bet:
    game_on = True

while game_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f" You won! The {winning_turtle} turtle is the winner.")
            else:
                print(f"Aww sorry you did not win. The {winning_turtle} turtle is the winner")
        move = random.randint(0, 10)
        turtle.forward(move)



screen.exitonclick()


#clearscreen() clearing the screen