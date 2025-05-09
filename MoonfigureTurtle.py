import turtle

# Ekranı ayarla
screen = turtle.Screen()
screen.bgcolor("black")

# Kalemi ayarla
hilal = turtle.Turtle()
hilal.color("white")
hilal.speed(3)
hilal.pensize(3)

# Büyük daire (arka plan)
hilal.penup()
hilal.goto(0, -100)
hilal.pendown()
hilal.begin_fill()
hilal.circle(100)
hilal.end_fill()

# Küçük daire (ön tarafı silerek hilal görünümü verecek)
hilal.color("black")
hilal.penup()
hilal.goto(30, -100)
hilal.pendown()
hilal.begin_fill()
hilal.circle(80)
hilal.end_fill()

# Bitir
hilal.hideturtle()
turtle.done()
