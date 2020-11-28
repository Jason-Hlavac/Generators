import numpy as np
import turtle
from tkinter import *

#Graph Initilization Function
def graph_initialization():
    myCanvas.delete("all")
    try:
        print("Start pressed with the following parameters: ")
        print("Outside circle size: " + outside.get())
        print("Inside circle size: "+ inside.get())
        print("Distance from edge: " + str(penNumber.get()))
        print("Rotation Value: " + str(penSpace.get()))
        if (int(outside.get()) >= int(inside.get())):
            graph(int(outside.get()),int(inside.get()), int(penNumber.get()), int(penSpace.get()))
        else: 
            print("Please make the inside circle smaller than or equal to the large circle")
            pass
    except:
        print("Something went wrong")
            
#Creating Spirograph on the Canvas 
def graph(outsideSize, insideSize, penDistance, penNumber):
    x= 2*outsideSize
    y = 2*insideSize
    myCanvas.config(width = x, height= x)
    t1 = turtle.RawTurtle(myCanvas)
    t1.hideturtle()
    t1.speed(0)
    
    pen = turtle.RawTurtle(myCanvas)
    pen.hideturtle()
    pen.speed(0)
    
    theta = 0.2 * penNumber
    angle = 0
    pen.up()
    pen.goto(outsideSize-insideSize+outsideSize , 0)
    pen.down()
    
    steps = (6*np.pi/theta)
    
    for t in range(0,int(steps)):
        t1.clear()
        t1.penup()
        t1.setheading(0)
        t1.goto(0,-outsideSize)
        t1.color("red")
        t1.pendown()
        t1.circle(outsideSize)
        angle+=theta
    
        a = (outsideSize - insideSize) * np.cos(angle)
        b = (outsideSize - insideSize) * np.sin(angle)
        t1.penup()
        t1.goto(a,b-insideSize)
        t1.color("black")
        t1.pendown()
        t1.circle(insideSize)
        t1.penup()
        t1.goto(a,b)
        t1.dot(5)
    
        a = (outsideSize - insideSize) * np.cos(angle) + penDistance * np.cos(((outsideSize-insideSize)/insideSize)*angle)
        b = (outsideSize - insideSize) * np.sin(angle) - penDistance * np.sin(((outsideSize-insideSize)/insideSize)*angle)
        
        t1.goto(a,b)
        t1.pendown()

        t1.dot(5)
        pen.goto(t1.pos())
    
        t1.getscreen().update() 
            

#Creating application window
master = Tk()
Label(master, text= "Outside Circle Size: ").grid(row = 1)
Label(master, text= "Inside Circle Size: ").grid(row = 2)
Label(master, text = "Distance from edge:  ").grid(row = 3)
Label(master, text= "Rotation Value: ").grid(row = 4)

outside = Entry(master)
inside = Entry(master)
penNumber = Scale(master, from_=1, to= 500, orient=HORIZONTAL)
penSpace = Scale(master, from_=1, to=10, orient=HORIZONTAL)

outside.grid(row = 1, column = 2)
inside.grid(row = 2, column = 2)
penNumber.grid(row = 3, column = 2)
penSpace.grid(row = 4, column = 2)

myCanvas =Canvas(master, bg = "white")
myCanvas.grid(padx=2, pady=2, row=8, column=0, rowspan=10, columnspan=10)

sub =  Button(master, text = "Start", command = graph_initialization)
sub.grid(row = 6, column = 1)


mainloop()
