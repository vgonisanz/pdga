import time

from pdga.engine.core import Engine
from pdga.engine.enums import Colors

from pygame import Rect

wtitle = "Basic example"
wwidth = 800
wheight = 600
initx = 0
inity = wheight/2
width = wwidth/2
height = wheight/2
toggle = 0

def draw():
    global initx, toggle

    # Update elements
    if toggle:
        initx -= wwidth/2
    else:
        initx += wwidth/2

    toggle = not toggle

    rect1 = Rect(0, 0, width, height)
    rect2 = Rect(initx, inity, width, height)

    # Re-draw
    engine.draw_rectangle(rect1, color=Colors.BLUE)
    engine.draw_rectangle(rect2, color=Colors.RED, border_width=1)
    print(f"draw {toggle}")
    time.sleep(0.5)

if __name__ == "__main__":
    print(f"Initializing engine with {wwidth}, {wheight}")
    engine = Engine(width=wwidth, height=wheight,
                    title=wtitle, debug=True)

    engine.set_run_bucle(draw)
    engine.set_background(Colors.WHITE)
    engine.run()
