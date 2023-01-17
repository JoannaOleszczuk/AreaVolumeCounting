import turtle as t
import math

t.hideturtle()
t.penup()
t.goto(-200, 300)
t.pendown()
t.write("Choose geometric figur to calculate its surface area and volume", font=("Arial", 14, "normal"))
t.penup()
t.right(90)
t.forward(100)
t.right(90)
t.forward(200)
t.left(90)
t.pendown()

# cube
t.fillcolor("red")
t.begin_fill()

for i in range(4):
    t.forward(150)
    t.left(90)
t.goto(-350, 250)

for i in range(4):
    t.forward(150)
    t.left(90)
t.goto(-200, 250)
t.goto(-250, 200)
t.goto(-250, 50)
t.goto(-200, 100)
t.goto(-350, 100)
t.goto(-400, 50)
t.end_fill()

#cuboid
t.penup()
t.goto(-100, 200)
t.pendown()
t.fillcolor("violet")
t.begin_fill()

for i in range(2):
    t.forward(150)
    t.left(90)
    t.forward(100)
    t.left(90)

t.goto(-50, 250)

for i in range(2):
    t.forward(150)
    t.left(90)
    t.forward(100)
    t.left(90)

t.goto(50, 250)
t.goto(0, 200)
t.goto(0, 50)
t.goto(50, 100)
t.goto(-50, 100)
t.goto(-100, 50)
t.end_fill()

# sphere
t.penup()
t.goto(150, 150)
t.pendown()
t.fillcolor("pink")
t.begin_fill()
t.circle(70)
t.left(40)
t.end_fill()

for i in range(2):
    t.circle(97, 90)
    t.circle(5, 90)

# general
t.penup()
t.goto(-200, -50)
t.pendown()
t.pencolor("green")
t.write("Type 1, 2 or 3 to choose cube, cuboid or sphere. ", font=("Arial", 14, "bold"))

def cube():
    t.bye()
    a = int(input("You choose cube. Type the side length: "))
    SurfaceArea = 6 * a**2
    Volume = a**3
    print("Surface area: " + str(SurfaceArea) + " and volume: " + str(Volume))

def cuboid():
    t.bye()
    a = int(input("You choose cuboid. Type the a length: "))
    b = int(input("Type the b length: "))
    c = int(input("Type the c length: "))
    SurfaceArea = 2*a*b + 2*a*c + 2*b*c
    Volume = a*b*c
    print("Surface area: " + str(SurfaceArea) + " and volume: " + str(Volume))
def sphere():
    t.bye()
    r = int(input("You choose sphere. Type radius length: "))
    SurfaceArea = 4 * math.pi * r**2
    Volume = 4/3 * math.pi * r**3
    print("Surface area: " + str(SurfaceArea) + " and volume: " + str(Volume))

t.listen()
t.onkey(cube, "1")
t.onkey(cuboid, "2")
t.onkey(sphere, "3")

t.exitonclick()

