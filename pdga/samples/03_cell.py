import time

from pdga.engine.core import Engine
from pdga.engine.enums import Colors
from pdga.engine.objects import Cell

import pygame

wtitle = "Basic example"
wwidth = 800
wheight = 600
initx = wwidth/4
inity = wheight/4
width = wwidth/2
height = wheight/2
grid_size = 20

cell = Cell(initx, inity, width, height,
    bg_color=Colors.MidnightBlue,
    grid_color=Colors.LightSkyBlue,
    border_color=Colors.White,
    grid_width=grid_size,
    grid_height=grid_size)

def events(event):
    if event.type == pygame.KEYDOWN:
        print(f"Processing keydown {event.key}")
        if event.key == (pygame.K_LEFT or pygame.K_a):
            print("move_left")
            cell.move_left(grid_size)
        if event.key == (pygame.K_RIGHT or pygame.K_d):
            print("move_right")
            #cell.move_left()
        if event.key == (pygame.K_UP or pygame.K_w):
            print("move_up")
            #cell.move_left()
        if event.key == (pygame.K_DOWN or pygame.K_s):
            print("move_down")
            #cell.move_left()
            
def draw():
    engine.draw_cell(cell)
    print(cell.rect)
    time.sleep(0.5)

if __name__ == "__main__":
    print(f"Initializing engine with {wwidth}, {wheight}")
    engine = Engine(width=wwidth, height=wheight,
                    title=wtitle, debug=True)

    engine.set_event_callback(events)
    engine.set_draw_callback(draw)
    engine.set_background(Colors.Black)
    engine.run()
