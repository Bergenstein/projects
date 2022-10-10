# import colorgram,
import turtle, random
from turtle import Screen
# colors=colorgram.extract('image.jpg', 20)
# print(colors)
# def extract_colors():
#     color_array=[]
#     for _ in colors:
#         color_array.append(tuple(_.rgb))
#     return color_array
# color_array = extract_colors()
# print(color_array)
color_array=[(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]

turtle.colormode(255)
color=input("pick your favorite turtle color: ")
def lazy_turtle_properties(_shape):
    lazy_turtle = turtle.Turtle()
    lazy_turtle.shape(_shape)
    lazy_turtle.color(color)
    lazy_turtle.shapesize(4,4,2)
    return lazy_turtle
lazy_turtle=lazy_turtle_properties('turtle')
speed=input("pick a speed 'fastest', 'fast', 'slow'? ")
num_dots=int(input("pick a number of dots: "))
dot_size=int(input("pick a dot size: (30, 20, 40): "))
def lazy_turtle_the_artist(_speed=speed, _num_dots=num_dots, _dot_size=dot_size):
    lazy_turtle.setheading(225)
    lazy_turtle.speed(_speed)
    lazy_turtle.penup()
    lazy_turtle.forward(400)
    lazy_turtle.setheading(0)
    for i in range(1, _num_dots):
        lazy_turtle.dot(_dot_size, random.choice(color_array))
        lazy_turtle.forward(50)
        if i % 10 ==0:
            lazy_turtle.setheading(90)
            lazy_turtle.forward(50)
            lazy_turtle.setheading(180)
            lazy_turtle.forward(500)
            lazy_turtle.setheading(0)
lazy_turtle_the_artist(speed, num_dots, dot_size)

screen=Screen()
screen.exitonclick()