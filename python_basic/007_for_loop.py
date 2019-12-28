import turtle
import time

jai_turtle = turtle.Turtle()
jai_turtle.speed(1)
def square():    
    jai_turtle.forward(100)
    jai_turtle.right(90)
    jai_turtle.forward(100)
    jai_turtle.right(90)
    jai_turtle.forward(100)
    jai_turtle.right(90)
    jai_turtle.forward(100)
    
for i in range(5):
    square()  
jai_turtle.forward(200)

time.sleep(3)
