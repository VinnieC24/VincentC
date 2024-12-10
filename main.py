import turtle


screen=turtle.Screen()
screen.screensize(200,200)
screen.bgcolor("purple")


t=turtle.Turtle()
t2=turtle.Turtle()

t2.penup()
t2.hideturtle()
t.fillcolor("black")
t.begin_fill()
t.pencolor("white")
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.left(45)
t.end_fill()
t.penup()
t.goto(0,200)
t.pendown()
t.write("intro slide", font=("arial", 30, "bold"), align = "center")

turtle.addshape("intropic.gif")
t2.goto(-100,0)
t2.shape("intropic.gif")
a = t2.stamp()
t2.goto(-100,0)

turtle.addshape("gif.gif")
t2.goto(150,0)
t2.shape("gif.gif")
a = t2.stamp()
t2.goto(100,0)

enter=input("Press Enter to continue:")
t.clear()
t2.clearstamps()


screen.bgcolor("navy blue")
t.clear()
t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(0)
t.penup()
t=turtle.Turtle()
t.fillcolor("black")
t.begin_fill()
t.pencolor("white")
t.circle(40)
t.left(45)
t.end_fill()
t.penup()
t.goto(0,200)
t.pendown()
t.write("favorite food", font=("arial", 30, "bold"), align = "center")
t.penup()

t.goto(0,-200)
t.pendown()
t.write("chicken,steak, and mashed potato", font=("arial", 15, "bold"), align = "center")


turtle.addshape("food.gif")
t2.goto(-100,0)
t2.shape("food.gif")
a = t2.stamp()
t2.goto(-100,0)

turtle.addshape("food2.gif")
t2.goto(150,0)
t2.shape("food2.gif")
a = t2.stamp()
t2.goto(100,0)

enter=input("Press Enter to continue:")
t.clear()
t2.clearstamps()


screen.bgcolor("teal")




t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(0)
t.penup()


t=turtle.Turtle()
t.fillcolor("black")
t.begin_fill()
t.pencolor("white")
t.forward(25)
t.left(90)
t.forward(50)
t.left(90)
t.forward(25)
t.left(90)
t.forward(50)
t.left(90)
t.left(45)
t.end_fill()
t.penup()
t.goto(0,200)
t.pendown()
t.write("hobbies", font=("arial", 30, "bold"), align = "center")
t.penup()
t.goto(0,-200)
t.pendown()
t.write("basketball,sleeping,eating,hockey", font=("arial", 20, "bold"), align = "center")


turtle.addshape("hobbie.gif")
t2.goto(-100,0)
t2.shape("hobbie.gif")
a = t2.stamp()
t2.goto(-100,0)

turtle.addshape("hobbie2.gif")
t2.goto(150,0)
t2.shape("hobbie2.gif")
a = t2.stamp()
t2.goto(100,0)

enter=input("Press Enter to continue:")
t.clear()
t2.clearstamps()



screen.bgcolor("orange")


t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(0)
t.penup()


t=turtle.Turtle()
t.pencolor("white")
t.fillcolor("black")
t.begin_fill()
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.end_fill()
t.penup()
t.goto(0,200)
t.pendown()
t.write("favorite movie", font=("arial", 30, "bold"), align = "center")
t.penup()
t.goto(0,-200)
t.pendown()
t.write("sandlot", font=("arial", 30, "bold"), align = "center")


turtle.addshape("movie.gif")
t2.goto(-100,0)
t2.shape("movie.gif")
a = t2.stamp()
t2.goto(-100,0)

turtle.addshape("movie2.gif")
t2.goto(150,0)
t2.shape("movie2.gif")
a = t2.stamp()
t2.goto(100,0)

enter=input("Press Enter to continue:")
t.clear()
t2.clearstamps()


screen.bgcolor("hot pink")


t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(0)
t.penup()


t=turtle.Turtle()
t.fillcolor("black")
t.begin_fill()
t.pencolor("white")
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.penup()
t.goto(0,200)
t.left(45)
t.end_fill()
t.pendown()
t.write("favorite sport", font=("arial", 30, "bold"), align = "center")

t.penup()
t.goto(0,-200)
t.pendown()
t.write("basketball", font=("arial", 30, "bold"), align = "center")

t.clear



turtle.addshape("sport.gif")
t2.goto(-100,0)
t2.shape("sport.gif")
a = t2.stamp()
t2.goto(-100,0)

turtle.addshape("sport2.gif")
t2.goto(150,0)
t2.shape("sport2.gif")
a = t2.stamp()
t2.goto(100,0)

enter=input("Press Enter to continue:")
t.clear()
t2.clearstamps()


