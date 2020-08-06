import time

from pdga.engine.core import Engine
from pdga.engine.enums import Colors

from pygame import Rect

wtitle = "Basic example"
wwidth = 800
wheight = 600
initx = wwidth/4
inity = wheight/4
width = wwidth/2
height = wheight/2

def draw():
    rect = Rect(initx, inity, width, height)

    engine.draw_cell(rect,
        bg_color=Colors.MidnightBlue,
        grid_color=Colors.LightSkyBlue,
        border_color=Colors.White)
    time.sleep(0.5)

if __name__ == "__main__":
    print(f"Initializing engine with {wwidth}, {wheight}")
    engine = Engine(width=wwidth, height=wheight,
                    title=wtitle, debug=True)

    engine.set_run_bucle(draw)
    engine.set_background(Colors.Black)
    engine.run()
