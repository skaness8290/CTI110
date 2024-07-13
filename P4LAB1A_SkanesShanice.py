import turtle

screen = turtle.Screen()
screen.title("Shapes")
t = turtle.Turtle()


for _ in range(4):
    t.forward(100)
    t. right(90)

t.penup()
t.forward(150)
t.pendown()

count = 0
while count < 3:
    t.forward(100)
    t.left(120)
    count += 1
    