from graphix import Window, Point, Circle, Line, Rectangle, Polygon, Text, Entry


def hello_graphix():
    win = Window()
    message = Text(Point(100, 100), "Hello graphix!")
    message.draw(win)
    win.get_mouse()


def two_points():
    my_win = Window("My Window", 330, 160)
    p = Point(30, 90)
    p.draw(my_win)
    p.move(70, -40)

    q = Point(200, 125)
    q.draw(my_win)

    p.outline_colour = "blue"
    q.outline_colour = "red"


def hello_circles():
    win = Window()
    centre = Point(200, 200)
    circle_1 = Circle(centre, 20)
    circle_1.draw(win)

    circle_2 = Circle(Point(150, 100), 50)
    circle_2.draw(win)

    circle_1.outline_width = 7
    circle_1.outline_colour = "blue"
    circle_2.outline_colour = "red"
    circle_2.fill_colour = "green"
    circle_1.fill_colour = "yellow"

    circle_2.move(100, 150)
    print("circle_2's radius =", circle_2.radius)
    print("circle_2's centre =", circle_2.radius)


def hello_lines():
    win = Window()
    line_1 = Line(Point(50, 150), Point(350, 250))
    line_1.draw(win)

    line_1.move(0, 100)
    line_1.outline_width = 5
    line_1.outline_colour = "red"

    start = Point(0, 200)
    end = Point(200, 0)
    line_2 = Line(start, end)
    line_2.draw(win)

    print("line_1 starts at", line_1.get_p1())
    print("line_1 ends at", line_1.get_p2())


def hello_rectangles():
    win = Window()
    rectangle = Rectangle(Point(50, 190), Point(350, 310))
    rectangle.draw(win)
    rectangle.fill_colour = "black"

    square = Rectangle(Point(150, 50), Point(250, 150))
    square.draw(win)
    square.fill_colour = "white"


def hello_triangle():
    win = Window()
    points = [Point(200, 50), Point(50, 250), Point(350, 250)]
    triangle = Polygon(points)
    triangle.draw(win)
    triangle.fill_colour = "red"
    win.get_mouse()


def hello_hexagon():
    win = Window()
    points = [
        Point(200, 50), Point(150, 100), Point(150, 200),
        Point(200, 250), Point(250, 200), Point(250, 100)
    ]
    hexagon = Polygon(points)
    hexagon.draw(win)
    hexagon.fill_colour = "blue"
    win.get_mouse()

    hello_hexagon()


def hello_text():
    win = Window()
    message = Text(Point(200, 200), "Hello World")
    message.draw(win)
    message.size = 20
    message.typeface = "times roman"
    message.text_colour = "magenta"

    win.get_mouse()
    message.text = "Goodbye"


def hello_entry():
    win = Window("Greeter", 400, 400)
    message = Text(Point(200, 100), "Enter your name & click on the window")
    message.draw(win)

    input_box = Entry(Point(200, 200), 10)
    input_box.draw(win)

    win.get_mouse()
    message.text = "Hello, " + input_box.text


def click_test():
    win = Window("Keep on clicking me!")
    for i in range(10):
        p = win.get_mouse()
        x = p.x
        y = p.y
        location = Text(p, str(x) + " " + str(y))
        location.draw(win)

# Solutions below:
