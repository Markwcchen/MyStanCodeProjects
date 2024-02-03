"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(self.window.width - paddle_width)/2, y=(self.window.height-paddle_offset))
        self.paddle.filled = True
        self.paddle.color = 'black'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        ball = GOval(ball_radius * 2, ball_radius * 2, x=(window_width - ball_radius) / 2,
                     y=(window_height - ball_radius) / 2)
        ball.filled = True
        self.window.add(ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Draw bricks
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                brick_x = col * (BRICK_WIDTH + BRICK_SPACING)
                brick_y = BRICK_OFFSET + row * (BRICK_HEIGHT + BRICK_SPACING)
                brick = GRect(width=BRICK_WIDTH, height=BRICK_HEIGHT, x=brick_x, y=brick_y)
                brick.filled = True
                if row // 2 == 0:
                    brick.fill_color = 'red'
                elif row // 2 == 1:
                    brick.fill_color = 'orange'
                elif row // 2 == 2:
                    brick.fill_color = 'yellow'
                elif row // 2 == 3:
                    brick.fill_color = 'green'
                elif row // 2 == 4:
                    brick.fill_color = 'blue'
                self.window.add(brick)

        # Initialize our mouse listeners
        # onmouseclicked
        onmouseclicked(self.clicked)

    def clicked(self, event):
        if self.__dy == 0:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

        onmousemoved(self.handle_move)

    def handle_move(self, event):
        paddle_x = event.x - self.paddle.width/2
        paddle_x = max(0, min(paddle_x, self.window.width - self.paddle.width))
        self.paddle.x = paddle_x














