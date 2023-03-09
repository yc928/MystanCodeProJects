"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Build and setup the BreakoutGraphics class.
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
    """
    BreakoutGraphics Class:
    def __init__(): constructor
    def paddle_move(): onmousemoved() event
    def ball_drop(): onmouseclicked event
    def reset_ball(): reset the ball position
    def get_dx(): return dx value
    def get_dy(): return dy value
    def set_dx(): set dx value
    def set_dy(): set dy value
    """

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create score label
        self.score = 0
        self.score_label = GLabel('Score : ' + str(self.score))
        self.score_label.font = '-20'
        self.window.add(self.score_label, x=0, y=self.score_label.height)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width) / 2, y=self.window.height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width) / 2, y=(self.window.height-self.ball.height) / 2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.is_click = True

        # Initialize our mouse listeners
        onmouseclicked(self.ball_drop)
        onmousemoved(self.paddle_move)

        # Calculate bricks
        self.total_bricks = brick_cols * brick_rows

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.bricks = GRect(width=brick_width, height=brick_height)
                self.bricks.filled = True
                if i < 2:
                    self.bricks.fill_color = 'red'
                elif i < 4:
                    self.bricks.fill_color = 'orange'
                elif i < 6:
                    self.bricks.fill_color = 'yellow'
                elif i < 8:
                    self.bricks.fill_color = 'green'
                else:
                    self.bricks.fill_color = 'blue'
                self.window.add(self.bricks, x=(brick_width+brick_spacing) * j, y=brick_offset + (brick_height+brick_spacing) * i)

    # Paddle move event
    def paddle_move(self, mouse):
        self.paddle.x = (mouse.x - self.paddle.width/2)
        if self.paddle.x < 0:
            self.paddle.x = 0
        if self.paddle.x + self.paddle.width > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width

    # Ball drop event
    def ball_drop(self, event):
        if self.is_click:
            self.is_click = False
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    # Reset the ball position
    def reset_ball(self):
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.__dx = 0
        self.__dy = 0
        self.is_click = True

    # Get dx value
    def get_dx(self):
        return self.__dx

    # Get dy value
    def get_dy(self):
        return self.__dy

    # Set dx value
    def set_dx(self, dx):
        self.__dx = dx

    # Set dy value
    def set_dy(self, dy):
        self.__dy = dy

