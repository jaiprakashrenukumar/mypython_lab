import turtle
import time
jai_turtle = turtle.Turtle()
def square():    
    jai_turtle.forward(100)
    jai_turtle.right(90)
    jai_turtle.forward(100)
    jai_turtle.right(90)
    jai_turtle.forward(100)
    jai_turtle.right(90)
    jai_turtle.forward(100)

a = 20
b = 10

if a > b:
   square()
else:
   jai_turtle.forward(100)
time.sleep(3)
