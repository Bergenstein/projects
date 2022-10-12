from turtle import Turtle, Screen
import turtle, random

my_turtle=Turtle()
colors=["red", "green", "purple", "blue", "yellow", "orange"]
names=['israel, thais, serge, sabine, alyssa', 'jackass filip']
screen=Screen()
screen.setup(height=500, width=600)
#user_bet=screen.textinput(title="make your bet", prompt="pick a turtle name: 'israel, thais, serge, sabine, alyssa:' ")

def color_turles():
    turtle_arr=[]
    for i in range(len((colors))):
        turtle_obj=Turtle('turtle')
        turtle_obj.color(colors[i])
       # turtle_obj.write('name', align='center')
        turtle_arr.append(turtle_obj)
    return turtle_arr


turtle_arr=color_turles()

def randomised_start_positions():
    k=-78   
    for i in range(len(turtle_arr)):
        turtle_arr[i].penup()
        turtle_arr[i].goto(-280, k)
        k+=30


# def game_continues():
#     for i in range(len(turtle_arr)):
#         if(turtle_arr[i].xcor() > 230):
#             return False

def move_forward():
    game_continues=True
    while(game_continues):
        for i in range(len(turtle_arr)):
            turtle_color=turtle_arr[i].pencolor()
            turtle_arr[i].setheading(0)
            turtle_arr[i].forward(random.randint(10,20))
            if(turtle_arr[i].xcor()>260):
                winning_turtle=turtle_color
                print(f"the winner turtle is {turtle_color}")
                screen.textoutput(winning_turtle)
                game_continues=False


screen.listen()

screen.onkey(key="a", fun=move_forward)



randomised_start_positions()


screen.exitonclick()