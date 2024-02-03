"""
File: 
Name: Mark
-------------------------
TODO: Click on two points and draw a line
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 5
window = GWindow()
start = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(clicked)


def clicked(event):
    global start

    x = event.x
    y = event.y

    if start is None:
        # draw first circle
        circle = GOval(SIZE * 2, SIZE * 2)
        circle.filled = False
        circle.color = "black"
        window.add(circle, x - SIZE, y - SIZE)

        start = (x, y)

    else:
        # remove first circle
        window.remove(window.get_object_at(start[0], start[1]))
        end = (x, y)
        line = GLine(start[0], start[1], end[0], end[1])
        window.add(line)

        start = None


window.clicked = clicked

if __name__ == "__main__":
    main()
