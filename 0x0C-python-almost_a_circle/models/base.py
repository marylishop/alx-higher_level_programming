def draw(list_rectangles, list_squares):
    """draws our shapes"""
    turtle.getscreen()
    turtle.shape("turtle")

    # Set up color mode and define colors
    turtle.colormode(255)
    red = (255, 0, 0)
    blue = (0, 0, 255)

    for rect in list_rectangles:
        turtle.pencolor(red)
        turtle.setpos(rect.x, rect.y)
        turtle.pendown()
        for i in range(2):
            turtle.forward(rect.height)
            turtle.left(90)
            turtle.forward(rect.width)
            turtle.left(90)
        turtle.penup()

    for sq in list_squares:
        turtle.pencolor(blue)
        turtle.setpos(sq.x, sq.y)
        turtle.pendown()
        for i in range(4):
            turtle.forward(sq.height)
            turtle.left(90)
        turtle.penup()

    # Keep the Turtle graphics window open until clicked
    turtle.exitonclick()
