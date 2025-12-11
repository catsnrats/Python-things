import turtle
import math

def draw_circle(t, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.circle(radius)

def draw_line(t, start, end):
    t.penup()
    t.goto(start)
    t.pendown()
    t.goto(end)

def draw_metatrons_cube():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    t.color("white")
    t.hideturtle()

    radius = 50
    distance = radius * 2  # distance between centers

    centers = []

    # 1. Center circle
    centers.append((0, 0))

    # 2. Inner hexagon (6 circles)
    for i in range(6):
        angle = math.radians(i * 60)
        x = distance * math.cos(angle)
        y = distance * math.sin(angle)
        centers.append((x, y))

    # 3. Outer hexagon (6 circles)
    for i in range(6):
        angle = math.radians(i * 60)
        x = 2 * distance * math.cos(angle)
        y = 2 * distance * math.sin(angle)
        centers.append((x, y))

    # Draw all circles
    for center in centers:
        draw_circle(t, center[0], center[1], radius)

    # Draw lines connecting every circle to every other
    for i in range(len(centers)):
        for j in range(i + 1, len(centers)):
            draw_line(t, centers[i], centers[j])

    turtle.done()

draw_metatrons_cube()
