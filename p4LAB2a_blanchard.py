import turtle
wn = turtle.Screen()
bob = turtle.Turtle()
bob.shape("turtle")

for i in range(4):
    bob.forward(100)
    bob.left(90)

bob.penup()
bob.left(180)
bob.forward(100)
bob.pendown()

for i in range(3):
    bob.forward(100)
    bob.right(120)

wn.mainloop()
