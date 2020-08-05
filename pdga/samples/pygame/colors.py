import pygame

def init():
    print("initializing...")
    screen = pygame.display.set_mode((640, 240))

    pygame.init()

def run():
    running = True

    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False

    print("quiting...")
    pygame.quit()

if __name__ == "__main__":
    init()
    run()