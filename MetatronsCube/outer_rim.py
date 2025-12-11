import turtle
import math

def draw_circle(t, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.circle(radius)

def draw_line(t, start_point, end_point):
    t.penup()
    t.goto(start_point)
    t.pendown()
    t.goto(end_point)

def draw_three_circles_vertical():
    screen = turtle.Screen()
    circles_turtle = turtle.Turtle()
    circles_turtle.speed(2)

    # Set up 3 circles forming a vertical line
    num_circles = 3
    radius_core = 50
    spacing = 2 * radius_core  # Adjust the spacing between circles

    # Draw the bottom circle
    draw_circle(circles_turtle, 0, -spacing, radius_core)

    # Draw the middle circle
    draw_circle(circles_turtle, 0, 0, radius_core)

    # Draw a line connecting the bottom to the middle circle
    draw_line(circles_turtle, (0, -spacing), (0, 0))

    # Draw the top circle
    draw_circle(circles_turtle, 0, spacing, radius_core)

    # Draw a line connecting the middle to the top circle
    draw_line(circles_turtle, (0, 0), (0, spacing))

    turtle.mainloop()

# Draw 3 circles forming a vertical line
draw_three_circles_vertical()
