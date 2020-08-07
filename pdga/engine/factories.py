import random

from pdga.engine.enums import Colors
from pdga.engine.drawables import Cell

class Generators(object):
    @staticmethod
    def cell_random(x0, y0, rwidth, rheight, threshold, grid_size):
        grid_threshold = threshold * grid_size

        fixed_width = int(rwidth)
        fixed_height = int(rheight)
        
        initx = random.randrange(x0 - grid_threshold, x0 + rwidth + grid_threshold)
        inity = random.randrange(y0 - grid_threshold, y0 + rheight + grid_threshold)
        width = random.randrange(fixed_width - grid_threshold, fixed_width + grid_threshold)
        height = random.randrange(fixed_height - grid_threshold, fixed_height + grid_threshold)

        print(f"Generating cell at({initx},{inity}) size({width},{height})")

        cell = Cell(initx, inity, width, height,
            bg_color=Colors.MidnightBlue,
            grid_color=Colors.LightSkyBlue,
            border_color=Colors.White,
            grid_width=grid_size,
            grid_height=grid_size
        )
        return cell