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

def draw_five_circles():
    screen = turtle.Screen()
    circles_turtle = turtle.Turtle()
    circles_turtle.speed(50)

    # Set up 5 circles
    num_circles = 5
    radius_core = 50
    spacing = 2 * radius_core  # Adjust the spacing between circles

    # Draw the bottom circle
    draw_circle(circles_turtle, 0, -spacing, radius_core)

    # Draw a line connecting the bottom to the middle circle
    draw_line(circles_turtle, (0, -spacing), (0, 0))

    # Draw the middle circle
    draw_circle(circles_turtle, 0, 0, radius_core)

    # Draw a line connecting the middle to the top circle
    draw_line(circles_turtle, (0, 0), (0, spacing))

    # Draw the top circle
    draw_circle(circles_turtle, 0, spacing, radius_core)

    # Draw two circles on the left side, one above the other
    # First circle
    draw_circle(circles_turtle, -spacing, spacing/2, radius_core)
    
    # Draw a line connecting the left circle to the middle circle
    draw_line(circles_turtle, (-spacing, spacing/2), (0, 0))

    # Second circle
    draw_circle(circles_turtle, -spacing, -spacing/2, radius_core)

    # Draw a line connecting the left circle to the middle circle
    draw_line(circles_turtle, (-spacing, -spacing/2), (0, 0))

    turtle.mainloop()

# Draw 5 circles with two on the left side, one above the other
draw_five_circles()
