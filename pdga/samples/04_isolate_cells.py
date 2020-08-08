import time

from pdga.engine.core import Engine
from pdga.engine.enums import Colors
from pdga.engine.drawables import Cell
from pdga.engine.factories import Generators

import pygame

wtitle = "Basic example"
wwidth = 800
wheight = 600
initx = wwidth/8*3
inity = wheight/8*3
width = wwidth/8
height = wheight/8
grid_size = 10

cells = []

def isolate_cells(cell0, cell1):
    # Move X axi
    xsubtract = cell1.rect.left - cell0.rect.left

    if xsubtract > 0:
        cell1.move_right()
    elif xsubtract < 0:
        cell0.move_left()
    # Move Y axi
    ysubtract = cell1.rect.top - cell0.rect.top

    if ysubtract > 0:
        cell1.move_down()
    elif ysubtract < 0:
        cell0.move_up()

def draw():
    for cell in cells:
        engine.draw_cell(cell)
    # Idea, buscar el más alejado, y terminar de alejarlo
    # primero X y luego Y
    print("Update physics")
    for x in range(len(cells) - 1):
        for y in range(x + 1, len(cells)):
            print(f"combine {x} and {y}")
            cell0 = cells[x]
            cell1 = cells[y]
            if cell0.rect.colliderect(cell1.rect):
                isolate_cells(cell0=cell0, cell1=cell1)
    time.sleep(0.05)

def events(event):
    if event.type == pygame.KEYDOWN:
        print("Processing keydown...")
    
def init():
    global cells
 
    for x in range(10):
        cell = Generators.cell_random(initx, inity, width, height, 3, grid_size)
        cells.append(cell)


if __name__ == "__main__":
    print(f"Initializing engine with {wwidth}, {wheight}")
    engine = Engine(width=wwidth, height=wheight,
                    title=wtitle, save=True, debug=True)

    init()
    engine.set_event_callback(events)
    engine.set_draw_callback(draw)
    engine.set_background(Colors.Black)
    engine.run()
