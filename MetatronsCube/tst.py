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

def draw_six_circles():
    screen = turtle.Screen()
    circles_turtle = turtle.Turtle()
    circles_turtle.speed(50)

    # Set up 7 circles
    num_circles = 7
    radius_core = 50
    angle_core = 360 / 6  # Hexagon has 6 sides
    spacing = 2 * radius_core  # Adjust the spacing between circles

    # Draw central circle
    draw_circle(circles_turtle, 0, 0, radius_core)

    # Draw surrounding 6 circles
    for i in range(1, num_circles):
        angle_i = math.radians(i * angle_core)
        x_i = spacing * math.cos(angle_i)
        y_i = spacing * math.sin(angle_i)
        draw_circle(circles_turtle, x_i, y_i, radius_core)

        # Draw lines connecting the center to the surrounding circles
        draw_line(circles_turtle, (0, 0), (x_i, y_i))

    turtle.mainloop()

# Draw 7 circles with the central circle surrounded by six circles
draw_six_circles()