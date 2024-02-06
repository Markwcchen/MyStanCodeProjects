"""
File: 
Name: Mark
-------------------------
TODO: create a bouncing ball
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
x = START_X
y = START_Y
bounces = 0
ball = GOval(SIZE, SIZE)
ball.filled = True
window.add(ball, x, y)
switch = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global x, y, bounces, switch
    onmouseclicked(start_move)
    while True:
        if switch:
            animate_ball()
        switch = False
        pause(DELAY)


def start_move(event):
    global bounces, switch
    if bounces < 3:
        switch = True


def animate_ball():
    global x, y, bounces
    vy = 0

    while True:
        vy += GRAVITY
        x += VX
        y += vy

        ball.x = x
        ball.y = y

        # down to floor
        if y + SIZE >= window.height:
            vy = -vy * REDUCE  # 速度90%
            y = window.height - SIZE

        # 超出右側視窗3次，球回起點
        if bounces > 3 and x >= window.width:
            reset_ball()
            break

        if x > window.width:
            bounces += 1
            reset_ball()
            break
        pause(DELAY)


def reset_ball():
    global x, y, bounces
    x = START_X
    y = START_Y
    ball.x = x
    ball.y = y


if __name__ == "__main__":
    main()
