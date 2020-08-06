import pygame

from pdga.engine.enums import Colors

class Cell:
    def __init__(self, x0, y0, width, height,
        bg_color, grid_color=Colors.Red, border_color=Colors.White,
        grid_width=20, grid_height=20):

        self.rect = pygame.Rect(x0, y0, width, height)
        self.bg_color = bg_color
        self.grid_color = grid_color
        self.border_color = border_color
        self.grid_width = grid_width
        self.grid_height = grid_height

    def move_left(self, amount=1):
        self.rect = self.rect.move(-amount, 0)