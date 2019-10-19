import turtle
bob = turtle.Turtle()
bob.speed(0)
def square(length, angle):
    for i in range(4):
        bob.forward(length)
        bob.left(angle)

for i in range(100):
    bob.pencolor("blue")
    square(100,90)
    bob.left(13) # choose a number that should not divide 360 degree, or it will repeats itself 

