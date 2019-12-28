import turtle
import time

jai_turtle = turtle.Turtle()
n = 5
def square():    
    jai_turtle.forward(100)
    jai_turtle.right(90)
    jai_turtle.forward(100)
    jai_turtle.right(90)
    jai_turtle.forward(100)
    jai_turtle.right(90)
    jai_turtle.forward(100)
    

i = 0
while i < n:
    square()
    i = i + 1


jai_turtle.forward(100)
square()
square()
time.sleep(3)
