import pygame

from pdga.engine.enums import Colors
from pdga.engine.drawables import Cell

class Engine:
    def __init__(self, width=800, height=600, title="Untitled", debug=False):
        """
        Basic engine to render 2D stuff

        Features:
        - set_event_callback: Assign an external event callback
        - set_event_callback: Assign an external event callback
        """
        self._debug = debug
        self._quit = False
        self._draw_callback = None
        self._event_callback = None
        self._background_color = None

        print("initializing engine...")
        self._screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        pygame.init()

    def set_draw_callback(self, func_pointer):
        """
        Configure an external function to call every main loop
        """
        print("Assigning draw callback")
        self._draw_callback = func_pointer

    def set_event_callback(self, func_pointer):
        """
        Configure an external function to call every main loop

        This callback will give a pygame event object
        """
        print("Assigning event callback")
        self._event_callback = func_pointer

    def set_background(self, color: Colors):
        """
        Change the background color.

        If this value is None, not refresh framebuffer
        """
        print("set_background")
        self._background_color = color
        

    def draw_rectangle(self, rect, color, border_width=0):
        """
        Draw a rectangle on the screen.
        """
        pygame.draw.rect(self._screen,
            color, 
            rect,
            border_width)

    def draw_ellipse(self, rect, color, border_width=0):
        """
        Draw a ellipse on the screen.
        """
        pygame.draw.ellipse(self._screen,
            color, 
            rect,
            border_width)

    def draw_line(self, start, end, color, border_width=1):
        """
        Draw an array of lines on the screen.
        """
        pygame.draw.line(self._screen,
            color,
            start,
            end,
            border_width)

    def draw_cell(self, cell: Cell):
        """
        Draw a cell on the screen. It is like a rect but with more
        options.

        It is recommended to use a grid size proportional to cell size
        """
        pygame.draw.rect(self._screen,
            cell.bg_color, 
            cell.rect,
            0)

        # Draw a grid with clipping rect inside
        range_x = round(cell.rect.width/cell.grid_width)
        range_y = round(cell.rect.height/cell.grid_height)
        for x in range(range_x):
            for y in range(range_y):
                grid_rect = pygame.Rect(
                                cell.rect.x + x * cell.grid_width,
                                cell.rect.y + y * cell.grid_height,
                                cell.grid_width,
                                cell.grid_height)

                grid_rect = grid_rect.clip(cell.rect)

                self.draw_rectangle( rect=grid_rect,
                                color=cell.grid_color,
                                border_width=1)

        pygame.draw.rect(self._screen,
            cell.border_color, 
            cell.rect,
            1)

    def run(self):
        """
        Default main loop run until quit signal. Use set_draw_callback
        to configure an external function to render things.

        This runs in same thread, so a sleep or long calculation
        in external run function will delay the input processing
        and the render process.

        Key reference: https://www.pygame.org/docs/ref/key.html
        """
        while not self._quit:
            # Refresh background
            if self._background_color:
                self._screen.fill(self._background_color)

            # Process internal events and external if attached
            for event in pygame.event.get():
                if self._debug:
                    print(event)
                if event.type == pygame.QUIT:
                    self._quit = True
                if self._event_callback:
                    self._event_callback(event)

            # Call external draw function if attached 
            if self._draw_callback:
                self._draw_callback()
            
            # Always update framebuffer
            pygame.display.update()

        print("quiting...")
        pygame.quit()
        

