import turtle
import math

def draw_circle(t, x, y, radius): # to draw a circle with the specified radius
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.circle(radius)

def draw_line(t, start_point, end_point): # actions for pen
    t.penup()
    t.goto(start_point)
    t.pendown()
    t.goto(end_point)

def draw_metatrons_cube(): # function for drawing Metatron's Cube base
    screen = turtle.Screen()
    metatron_turtle = turtle.Turtle()
    metatron_turtle.speed(10) # drawing speed

    # set up 13 circles    
    num_circles = 13
    radius_core = 50
    radius_side = 35
    angle_core = 360 / 7
    angle_side = 360 / 6    
    
    # draw central 7 circles
    for i in range(7):
        angle_i = math.radians(i * angle_core)
        x_i = radius_core * math.cos(angle_i)
        y_i = radius_core * math.sin(angle_i)
        draw_circle(metatron_turtle, x_i, y_i, radius_core)        

    # draw side 6 circles
    for _ in range(3):
        angle_i = math.radians(i * angle_side)
        x_i = radius_core * math.cos(angle_i)
        y_i = radius_core * math.sin(angle_i)
        draw_circle(metatron_turtle, x_i, y_i, radius_side)    

    for i in range(3, 6):
        angle_i = math.radians(i * angle_side)
        x_i = 2 * radius_core * math.cos(angle_i)
        y_i = 2 * radius_core * math.sin(angle_i)
        draw_circle(metatron_turtle, x_i, y_i, radius_side)        

    # draw lines connecting the circles
    for i in range(7):
        for j in range(i + 1, 7):
            angle_i = math.radians(i * angle_core)
            angle_j = math.radians(j * angle_core)

            x_i = radius_core * math.cos(angle_i)
            y_i = radius_core * math.sin(angle_i)            

            x_j = radius_core * math.cos(angle_j)
            y_j = radius_core * math.sin(angle_j)            

            draw_line(metatron_turtle, (x_i, y_i), (x_j, y_j))

    # Keep the window open
    turtle.mainloop()

# draw Metatron's Cube
draw_metatrons_cube()