import turtle

class Point(object):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    
    def draw_action(self):
        turtle.dot()

class Box(Point):
    def __init__(self, x1, y1, w, h, color):
        super().__init__(x1, y1, color)
        self.w = w
        self.h = h

    def draw_action(self):
        for i in range(2):
            turtle.forward(self.w)
            turtle.right(90)
            turtle.forward(self.h)
            turtle.right(90)

class filled_Box(Box):
    def __init__(self, x1, y1, w, h, color, fillcolor):
        super().__init__(x1, y1, w, h, color)
        self.fillcolor = fillcolor
    
    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):
    def __init__(self, x1, y1, radius, fillcolor):
        super().__init__(x1, y1, fillcolor)
        self.radius = radius

    def draw_action(self):
        turtle.circle(self.radius)

class CircleFilled(Circle):
    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()
if __name__ == '__main__':
    p = Point(100, 100, 'green')
    p.draw()
    b = Box(10,20, 50, 100, 'red')
    bf = filled_Box(-100, 20, 50, 100, 'yellow', 'blue')
    bf.draw()
    c = CircleFilled(-300, 150, 50, 'black', 'red')
    c.draw()
    cf = CircleFilled(-300, 150, 50, 'red', 'yellow')
    cf.draw()
    turtle.hideturtle()
    turtle.draw()