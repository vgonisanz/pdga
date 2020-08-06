import time

from pdga.engine.core import Engine
from pdga.engine.enums import Colors
from pdga.engine.objects import Cell

import pygame

wtitle = "Basic example"
wwidth = 800
wheight = 600
initx = wwidth/8
inity = wheight/8
width = wwidth/4
height = wheight/4
grid_size = 10

cells = []

def draw():
    for cell in cells:
        engine.draw_cell(cell)

    time.sleep(0.05)

def events(event):
    if event.type == pygame.KEYDOWN:
        print("Processing keydown...")
    
def init():
    global cells

    cell1 = Cell(initx, inity, width, height,
        bg_color=Colors.MidnightBlue,
        grid_color=Colors.LightSkyBlue,
        border_color=Colors.White,
        grid_width=grid_size,
        grid_height=grid_size
    )

    cell2 = Cell(initx + 20, inity + 20, width, height,
        bg_color=Colors.MidnightBlue,
        grid_color=Colors.LightSkyBlue,
        border_color=Colors.Red,
        grid_width=grid_size,
        grid_height=grid_size
    )

    cells = [ cell1, cell2 ]

if __name__ == "__main__":
    print(f"Initializing engine with {wwidth}, {wheight}")
    engine = Engine(width=wwidth, height=wheight,
                    title=wtitle, debug=True)

    init()
    engine.set_event_callback(events)
    engine.set_draw_callback(draw)
    engine.set_background(Colors.Black)
    engine.run()
