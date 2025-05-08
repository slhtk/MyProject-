import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("yellow")
drawing_board.title("Kare Cizimi")
turtle_instance = turtle.Turtle()

for i in range(5):
    turtle_instance.forward(200)
    turtle_instance.right(144)

'''
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
'''

'''
turtle_instance.forward(300)
turtle_instance.right(90)
turtle_instance.forward(300)
turtle_instance.right(90)
turtle_instance.forward(300)
turtle_instance.right(90)
turtle_instance.forward(300)
turtle_instance.right(90)
'''


turtle.done()

