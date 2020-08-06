import pygame

from pdga.engine.enums import Colors

class Engine:
    def __init__(self, width=800, height=600, title="Untitled", debug=False):
        self._debug = debug
        self._quit = False
        self._run = None
        self._background_color = None

        print("initializing engine...")
        self._screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        pygame.init()

    def set_run_bucle(self, func_pointer):
        """
        Configure an external function to call every main loop
        """
        self._run = func_pointer

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

    def draw_cell(self, rect, bg_color, grid_color=Colors.Red, border_color=Colors.White):
        """
        Draw a cell on the screen. It is like a rect but with more
        options
        """
        pygame.draw.rect(self._screen,
            bg_color, 
            rect,
            0)

        pygame.draw.rect(self._screen,
            border_color, 
            rect,
            1)

    def run(self):
        """
        Default main loop run until quit signal. Use set_run_bucle
        to configure an external function to render things.

        This runs in same thread, so a sleep or long calculation
        in external run function will delay the input processing
        and the render process.
        """
        while not self._quit:
            for event in pygame.event.get():
                if self._debug:
                    print(event)
                if event.type == pygame.QUIT:
                    self._quit = True
            if self._run:
                if self._background_color:
                    self._screen.fill(self._background_color)
                self._run()
                pygame.display.update()

        print("quiting...")
        pygame.quit()
        

