import turtle

def rektangel(color, width, height):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def rita_svenska_flaggan():
    turtle.penup()
    turtle.goto(-150, 100)
    turtle.pendown()
    rektangel("blue", 300, 200)

    turtle.penup()
    turtle.goto(-150, 185)
    turtle.pendown()
    rektangel("yellow", 300, 30)

    turtle.penup()
    turtle.goto(-50, 100)
    turtle.pendown()
    rektangel("yellow", 30, 200)

def rita_danska_flaggan():
    turtle.penup()
    turtle.goto(-150, 100)
    turtle.pendown()
    rektangel("red", 300, 200)

    turtle.penup()
    turtle.goto(-150, 185)
    turtle.pendown()
    rektangel("white", 300, 40)

    turtle.penup()
    turtle.goto(-50, 100)
    turtle.pendown()
    rektangel("white", 40, 200)

def rita_norska_flaggan():
    turtle.penup()
    turtle.goto(-150, 100)
    turtle.pendown()
    rektangel("red", 300, 200)

    turtle.penup()
    turtle.goto(-150, 185)
    turtle.pendown()
    rektangel("white", 300, 40)

    turtle.penup()
    turtle.goto(-50, 100)
    turtle.pendown()
    rektangel("white", 40, 200)

    turtle.penup()
    turtle.goto(-40, 100)
    turtle.pendown()
    rektangel("blue", 20, 200)

    turtle.penup()
    turtle.goto(-150, 195)
    turtle.pendown()
    rektangel("blue", 300, 20)

def main():
    turtle.speed(2)
    turtle.bgcolor("white")

    choice = turtle.textinput("Flagga", "Vilken flagga vill du rita?\n\n Välj Mellan 1, 2 och 3.\n \n(1) Svenska \n(2) Danska \n(3) Norska ")
    
    if choice == "1":
        rita_svenska_flaggan()
    elif choice == "2":
        rita_danska_flaggan()
    elif choice == "3":
        rita_norska_flaggan()
    else:
        turtle.write("Felaktigt val. Vänligen starta om och välj 1, 2 eller 3.")
    
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
