"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_wei import BreakoutGraphics

FRAME_RATE = 20         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def check_collision(graphics, dy, score):
    ball_points = [(graphics.ball.x, graphics.ball.y),
                   (graphics.ball.x + graphics.ball.width, graphics.ball.y),
                   (graphics.ball.x, graphics.ball.y + graphics.ball.height),
                   (graphics.ball.x + graphics.ball.width, graphics.ball.y + graphics.ball.height)]

    for x, y in ball_points:
        obj = graphics.window.get_object_at(x, y)

        if obj is not None:
            if obj is graphics.paddle:
                graphics.ball.y = graphics.paddle.y - graphics.ball.width - 1
                # graphics.set_dy(-graphics.get_dy())  # this only change the dy in breakoutgraphics_wei, but dy in this file has not been changed
                graphics.set_dy(-dy)  # what we need to cahnge is dy in this file instead of dy in breakoutgraphics_wei
                dy = graphics.get_dy()  # reset dy in this file
                break  # remember to break once the collision occurs
            else:
                # if graphics.window.contains(graphics.ball):  # 'GWindow' object has no attribute 'contains'
                    # graphics.set_dy(-graphics.get_dy())
                graphics.set_dy(-dy)
                dy = graphics.get_dy()
                graphics.window.remove(obj)
                score += 1
                break
    return dy, score


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    score = 0

    # Add the animation loop here!
    while lives > 0:
        dx = graphics.get_dx()
        dy = graphics.get_dy()

        # check_collision(graphics, dx, dy)
        dy, score = check_collision(graphics, dy, score)  # does not need dx and need a return value to avoid stack frame

        graphics.ball.move(dx, dy)

        if graphics.ball.y > graphics.window.height:
            # 球超出底部，重設位置
            lives -= 1
            graphics.reset_ball()

            if lives == 0:
                print('game over')
                break

        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            print(dx, dy)
            graphics.set_dx(-dx)
            dx = graphics.get_dx()  # update dx in this file
            graphics.ball.move(dx, dy)  # in case it stucks in wall

        if graphics.ball.y <= 0 :
            graphics.set_dy(-dy)
            dy = graphics.get_dy()  # update dy in this file
            graphics.ball.move(dx, dy)  # in case it stucks in wall

        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            lives -= 1
            print('lives remains:'+str(lives))
            graphics.reset_ball()

            # 如果生命值為0，遊戲結束
            if lives == 0:
                break

        if score == graphics.score:
            print('WIN')
            break

        pause(FRAME_RATE)

    print('Game Over')


if __name__ == '__main__':
    main()
