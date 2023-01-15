import turtle as t
t.penup()
t.goto(-200, 300)
t.pendown()
t.write("Choose geometric figur to calculate its surface area and volume")
t.penup()
t.right(90)
t.forward(100)
t.right(90)
t.forward(200)
t.left(90)
t.pendown()
#
# # cube
# for i in range(4):
#     t.forward(150)
#     t.left(90)
# t.goto(-350, 250)
#
# for i in range(4):
#     t.forward(150)
#     t.left(90)
# t.goto(-200, 250)
# t.goto(-250, 200)
# t.goto(-250, 50)
# t.goto(-200, 100)
# t.goto(-350, 100)
# t.goto(-400, 50)
#
# #cuboid
# t.penup()
# t.goto(-100, 200)
# t.pendown()
#
# for i in range(2):
#     t.forward(150)
#     t.left(90)
#     t.forward(100)
#     t.left(90)
#
# t.goto(-50, 250)
#
# for i in range(2):
#     t.forward(150)
#     t.left(90)
#     t.forward(100)
#     t.left(90)
#
# t.goto(50, 250)
# t.goto(0, 200)
# t.goto(0, 50)
# t.goto(50, 100)
# t.goto(-50, 100)
# t.goto(-100, 50)

# cone
t.penup()
t.goto(200, 50)
t.pendown()
t.left(45)

for i in range(2):
    t.circle(80, 90)
    t.circle(20, 90)
t.goto(240, 200)
t.goto(280, 50)

t.exitonclick()

