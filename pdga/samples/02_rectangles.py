import time

from pdga.engine.core import Engine
from pdga.engine.enums import Colors

from pygame import Rect

initx = 5
inity = 5
width = 5
height = 5

def draw():
    global initx, inity

    rect2 = Rect(initx, inity, width, height)
    engine.draw_rectangle(rect2, color=Colors.RED, border_width=1)
    
    initx += 1
    inity += 1

if __name__ == "__main__":
    rect1 = Rect(0, 0, 5, 5)

    engine = Engine(width=800, height=600,
                    title="Basic example", debug=True)

    engine.set_run_bucle(draw)
    engine.set_background(Colors.WHITE)
    engine.draw_rectangle(rect1, color=Colors.BLUE)
    engine.run()
