from graphix import Window, Text, Circle, Line, Point


def hello_graphics():
    win = Window()
    message = Text(Point(100, 100), "Hello graphics!")
    message.draw(win)
    win.get_mouse()


def draw_stick_figure():
    win = Window("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    # Add your code here
    win.get_mouse()


def draw_line():
    win = Window("Line drawer")
    message = Text(Point(100, 100), "Click on first point")
    message.draw(win)
    p1 = win.get_mouse()
    message.text = "Click on second point"
    p2 = win.get_mouse()
    line = Line(p1, p2)
    line.draw(win)
    message.text = ""
