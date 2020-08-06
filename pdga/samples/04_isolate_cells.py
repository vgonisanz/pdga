import time

from pdga.engine.core import Engine
from pdga.engine.enums import Colors

from pygame import Rect

wtitle = "Basic example"
wwidth = 800
wheight = 600
initx = wwidth/8
inity = wheight/8
width = wwidth/4
height = wheight/4

state = 0

def draw_state_0():
    rect = Rect(initx, inity, width, height)
    rect2 = Rect(initx + 20, inity + 20, width, height)

    engine.draw_cell(rect,
        bg_color=Colors.MidnightBlue,
        grid_color=Colors.LightSkyBlue,
        border_color=Colors.White)

    engine.draw_cell(rect2,
        bg_color=Colors.MidnightBlue,
        grid_color=Colors.LightSkyBlue,
        border_color=Colors.White)

def draw_state_1():
    rect = Rect(initx, inity, width, height)
    rect2 = Rect(initx + 20, inity + 20, width, height)

    engine.draw_cell(rect,
        bg_color=Colors.MidnightBlue,
        grid_color=Colors.LightSkyBlue,
        border_color=Colors.White)

    engine.draw_cell(rect2,
        bg_color=Colors.MidnightBlue,
        grid_color=Colors.LightSkyBlue,
        border_color=Colors.White)


def draw():
    if state == 0:
        draw_state_0()
    elif state == 1:
        draw_state_1()

    time.sleep(0.5)

if __name__ == "__main__":
    print(f"Initializing engine with {wwidth}, {wheight}")
    engine = Engine(width=wwidth, height=wheight,
                    title=wtitle, debug=True)

    engine.set_run_bucle(draw)
    engine.set_background(Colors.Black)
    engine.run()
