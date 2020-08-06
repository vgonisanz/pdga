import time

from pdga.engine.core import Engine
from pdga.engine.enums import Colors

import pygame
from pygame import Rect

wtitle = "Basic example"
wwidth = 800
wheight = 600
initx = wwidth/8
inity = wheight/8
width = wwidth/4
height = wheight/4

state = 0

# Cells attributes
rect = Rect(initx, inity, width, height)
rect2 = Rect(initx + 20, inity + 20, width, height)
bg_color=Colors.MidnightBlue,
grid_color=Colors.LightSkyBlue,
border_color=Colors.White

def draw_state_0():
    engine.draw_cell(rect,
        bg_color=bg_color,
        grid_color=grid_color,
        border_color=border_color)

    engine.draw_cell(rect2,
        bg_color=bg_color,
        grid_color=grid_color,
        border_color=Colors.Red)

def draw_state_1():
    engine.draw_cell(rect,
        bg_color=bg_color,
        grid_color=grid_color,
        border_color=border_color)

    engine.draw_cell(rect2,
        bg_color=bg_color,
        grid_color=grid_color,
        border_color=Colors.Red)

def draw():
    if state == 0:
        draw_state_0()
    elif state == 1:
        draw_state_1()
    else:
        draw_state_0()

    time.sleep(0.5)

def events(event):
    global state

    if event.type == pygame.KEYDOWN:
        print("Processing keydown...")
        if event.key == pygame.K_n:
            print("state + 1")
            state += 1
    

if __name__ == "__main__":
    print(f"Initializing engine with {wwidth}, {wheight}")
    engine = Engine(width=wwidth, height=wheight,
                    title=wtitle, debug=True)

    engine.set_event_callback(events)
    engine.set_draw_callback(draw)
    engine.set_background(Colors.Black)
    engine.run()
