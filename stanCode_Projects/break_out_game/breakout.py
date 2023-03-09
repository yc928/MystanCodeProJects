"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program plays a Python game 'Bricks game'.
Click the left button of the mouse can start the Bricks game.
User can control the paddle with mouse.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    This program plays a Python game 'Bricks game'.
    This is the main function, use BreakoutGraphics class.
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    touch_paddle = True  # This is the flag to avoid the ball bouncing up and down on the paddle
    # Add the animation loop here!
    while True:
        if lives > 0 and graphics.score != graphics.total_bricks:   # still have lives and bricks
            # get the velocity of vx and vy
            vx = graphics.get_dx()
            vy = graphics.get_dy()
            graphics.ball.move(vx, vy)

            # Ball touch the left or the right of the window
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
                # vx = -vx
                graphics.set_dx(-vx)
                touch_paddle = True

            # Ball touch the top of the window
            if graphics.ball.y <= 0:
                # vy = -vy
                graphics.set_dy(-vy)
                touch_paddle = True

            # Ball touch the bottom of the window
            if graphics.ball.y + graphics.ball.height > graphics.window.height:
                lives -= 1
                graphics.reset_ball()
                touch_paddle = True

            # Use 2 for loop to check 4 points ((x, y) (x+2r, y) (x, y+2r), (x+2r, y+2r)) around the ball
            for i in range(2):
                for j in range(2):
                    maybe_obj = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width*j, graphics.ball.y+graphics.ball.height*i)
                    if maybe_obj is not None and maybe_obj is not graphics.score_label:
                        if maybe_obj is graphics.paddle:
                            if i != 0:  # Only ball bottom touch the paddle can change the velocity
                                if touch_paddle:    # Avoid the ball bouncing up and down on the paddle
                                    touch_paddle = False
                                    graphics.set_dy(-vy)
                        else:
                            graphics.window.remove(maybe_obj)
                            touch_paddle = True
                            graphics.set_dy(-vy)
                            graphics.score += 1
                            graphics.score_label.text = 'Score : ' + str(graphics.score)
        else:
            break
        # pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
