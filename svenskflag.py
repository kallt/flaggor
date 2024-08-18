import turtle

# Funktion för att rita en rektangel med en given färg och storlek
def draw_rectangle(color, width, height):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Funktioner för att rita flaggor
def draw_swedish_flag():
    turtle.penup()
    turtle.goto(-150, 100)
    turtle.pendown()
    draw_rectangle("blue", 300, 200)

    turtle.penup()
    turtle.goto(-150, 185)
    turtle.pendown()
    draw_rectangle("yellow", 300, 30)

    turtle.penup()
    turtle.goto(-50, 100)
    turtle.pendown()
    draw_rectangle("yellow", 30, 200)

def draw_danish_flag():
    turtle.penup()
    turtle.goto(-150, 100)
    turtle.pendown()
    draw_rectangle("red", 300, 200)

    turtle.penup()
    turtle.goto(-150, 185)
    turtle.pendown()
    draw_rectangle("white", 300, 40)

    turtle.penup()
    turtle.goto(-50, 100)
    turtle.pendown()
    draw_rectangle("white", 40, 200)

def draw_norwegian_flag():
    turtle.penup()
    turtle.goto(-150, 100)
    turtle.pendown()
    draw_rectangle("red", 300, 200)

    turtle.penup()
    turtle.goto(-150, 185)
    turtle.pendown()
    draw_rectangle("white", 300, 40)

    turtle.penup()
    turtle.goto(-50, 100)
    turtle.pendown()
    draw_rectangle("white", 40, 200)

    turtle.penup()
    turtle.goto(-40, 100)
    turtle.pendown()
    draw_rectangle("blue", 20, 200)

    turtle.penup()
    turtle.goto(-150, 195)
    turtle.pendown()
    draw_rectangle("blue", 300, 20)

# Huvudfunktion
def main():
    turtle.speed(2)
    turtle.bgcolor("white")

    # Användarens val
    choice = turtle.textinput("Flagga", "Vilken flagga vill du rita?\n1: Svenska\n2: Danska\n3: Norska")
    
    if choice == "1":
        draw_swedish_flag()
    elif choice == "2":
        draw_danish_flag()
    elif choice == "3":
        draw_norwegian_flag()
    else:
        turtle.write("Felaktigt val. Vänligen starta om och välj 1, 2 eller 3.", align="center", font=("Arial", 16, "bold"))
    
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()