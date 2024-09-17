import turtle

numbers = input()

# turtle.hideturtle()
# turtle.tracer()
turtle.speed(1)
    
def one():
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.pendown()

    turtle.left(45)
    turtle.forward(20 * 2**0.5)
    turtle.right(135)
    turtle.forward(40)
    turtle.left(90)
    

def two():
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(45)
    turtle.forward(27)
    turtle.left(135)
    turtle.forward(20)
    
def three():
    turtle.forward(20)
    turtle.right(135)
    turtle.forward(27)
    turtle.left(135)
    turtle.forward(20)
    turtle.right(135)
    turtle.forward(27)
    turtle.left(135)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

def draw_number(N, pos):
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    
    if N == 1: one()
    if N == 2: two()
    if N == 3: three()

X = -10
for n in numbers:
    draw_number(int(n), (X, 0))
    X += 30
    
turtle.update()
turtle.mainloop()