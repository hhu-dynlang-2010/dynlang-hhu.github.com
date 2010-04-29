import random, pygame

title = "window title"

# The framerate of the game (in milliseconds)
framerate = 60

screen_dimensions = (500, 500)

def main():

    # Initialize pygame elements
    screen, bg, clock = init_screen()

    # Even loop
    while True:
        clock.tick(framerate)

        # Draw some random rectangles:
        for i in range(100):
            # a rectangle is a tuple
            # (x, y, sizex, sizey)
            x = random.randrange(screen_dimensions[0])
            y = random.randrange(screen_dimensions[1])
            sizex = random.randrange(20)
            sizey = random.randrange(20)
            rectangle =  (x, y, sizex, sizey)
            # a colour is a tuple (red, green, blue)
            red = random.randrange(255)
            green = random.randrange(255)
            blue = random.randrange(255)
            colour = (red, green, blue)
            pygame.draw.rect(bg, colour, rectangle)

        # draw the background screen to the actual one
        screen.blit(bg, (0,0))
        # update the screen
        pygame.display.flip()

        # look out for window close events:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return

def init_screen():

    pygame.init()
    screen = pygame.display.set_mode(screen_dimensions)
    pygame.display.set_caption(title)
    bg = pygame.Surface(screen_dimensions)
    clock = pygame.time.Clock()
    return screen, bg, clock


main()

