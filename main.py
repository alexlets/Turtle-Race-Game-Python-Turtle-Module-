import random
from turtle import Turtle, Screen

screen = Screen()

screen.setup(500,400)
while True:
    user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race(red, orange, yellow, green, blue, purple)? Enter a color: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    if user_bet.lower() in colors:
        break
    else:
        print("Please choose between the available colors")

all_turtles = []

y_position = -100

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, y=y_position)
    y_position += 40
    all_turtles.append(new_turtle)

race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() > 230:
            race_is_on = False
            turtle_color = turtle.pencolor()
            if user_bet == turtle_color:
                print(f"You got it right. The winning color is {turtle_color}")
            else:
                print(f"You are wrong. The winning color is {turtle_color}")
            break




screen.exitonclick()