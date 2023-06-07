from graphics import *


def helloGraphics():
    myWin = GraphWin("My Window", 330, 160)
    p = Point(30, 90)
    x = p.getX()
    y = p.getY()
    print("x =", x, "y =", y)
    p.draw(myWin)
    p.move(70, -40)
    x = p.getX()
    y = p.getY()
    print("x =", x, "y =", y)


def twoPoints():
    win = GraphWin("Two points", 250, 250)
    p1 = Point(50, 25)
    p2 = Point(200, 225)
    p1.draw(win)
    p2.draw(win)
    p1.setOutline("red")
    p2.setOutline("blue")


def helloCircles():
    win = GraphWin()
    centre = Point(100, 100)
    circle1 = Circle(centre, 20)
    circle1.draw(win)
    circle2 = Circle(Point(30, 30), 10)
    circle2.draw(win)

    circle1.setWidth(7)

    circle1.setOutline("blue")
    circle2.setOutline("purple")

    circle2.setFill("green")
    circle1.setFill("yellow")

    circle2.move(50, 75)

    print("circle2's radius =", circle2.getRadius())
    print("circle2's centre =", circle2.getCenter())


def helloLines():
    win = GraphWin()
    line1 = Line(Point(50, 25), Point(150, 75))
    line1.draw(win)
    line1.setWidth(5)
    line1.setOutline("red")
    line1.move(0, 100)
    print("line1's start =", line1.getP1(), "end =", line1.getP2())

    start = Point(0, 50)
    end = Point(200, 50)
    line2 = Line(start, end)
    line2.draw(win)
    line2.setArrow("both")


def helloRectangles():
    win = GraphWin()
    rectangle = Rectangle(Point(110, 30), Point(140, 100))
    rectangle.draw(win)
    rectangle.setFill("black")

    square = Rectangle(Point(50, 50), Point(100, 100))
    square.draw(win)
    square.setFill("white")
    square.setOutline("black")


def helloTriangle():
    win = GraphWin()
    triangle = Polygon(Point(100, 30), Point(30, 100), Point(170, 100))
    triangle.draw(win)
    triangle.setFill("red")


def helloHexagon():
    win = GraphWin()
    points = [Point(100, 30), Point(30, 70), Point(30, 130),
              Point(100, 170), Point(170, 130), Point(170, 70)]
    hexagon = Polygon(points)
    
    hexagon.draw(win)
    hexagon.setFill("blue")
    hexagon.move(30, -30)


def helloText():
    win = GraphWin()
    message = Text(Point(100, 100), "Hello World")
    message.draw(win)
    message.setSize(20)
    message.setFace("times roman")
    message.setTextColor("magenta")

    win.getMouse()
    message.setText("Goodbye")


def helloEntry():
    win = GraphWin("Greeter", 300, 150)
    message = Text(Point(150, 50), "Enter your name & click on the window")
    message.draw(win)

    inputBox = Entry(Point(150, 100), 10)
    inputBox.draw(win)

    win.getMouse()
    message.setText("Hello, " + inputBox.getText())


def clickTest():
    win = GraphWin("Click Me!")
    # p = win.getMouse()
    # print(p.getX(), p.getY())
    # p.draw(win)

    for i in range(10):
        p = win.getMouse()
        location = Text(p, str(p.getX()) + " " + str(p.getY()))
        location.draw(win)


def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)


def drawLine():
    win = GraphWin("Line drawer")
    message = Text(Point(100, 100), "Click on first point")
    message.draw(win)
    p1 = win.getMouse()
    message.setText("Click on second point")
    p2 = win.getMouse()
    line = Line(p1, p2)
    line.draw(win)
    message.setText("")
