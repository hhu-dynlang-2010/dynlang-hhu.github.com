import random, pygame


class Player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.target = (x, y)

    def run(self, screen):
        # this should contain a loop that runs forever, to execute the logic
        # of this player.  The infinite loop should have a "yield None" to
        # suspend until the next iteration (i.e. 1/60th of a second).
        ...


class Attacker(object):
    def __init__(self, player, x, y):
        self.player = player
        self.x = x
        self.y = y

    def run(self, screen):
        # this should contain a loop that runs forever, to execute the logic
        # of an attacker.
        ...


title = "My game"

# The framerate of the game (in milliseconds)
framerate = 60

screen_dimensions = (750, 500)

def main():
    # Initialize pygame elements
    screen, clock = init_screen()

    # Build the state
    player = Player(screen_dimensions[0] - 40,
                    screen_dimensions[1] // 2)
    sprites = [player.run(screen)]
    for i in range(10):
        attacker = Attacker(player, 20, random.randrange(screen_dimensions[1]))
        sprites.append(attacker.run(screen))

    # Even loop
    while True:
        # Erase the drawing, by drawing a blank background screen
        screen.fill((192, 144, 0))

        # Ask each sprite to move one step and draw itself
        for sprmover in sprites:
            sprmover.next()

        # Update the screen
        pygame.display.flip()
        clock.tick(framerate)

        # Look out for window close events:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEMOTION:
                player.target = e.pos
            if e.type == pygame.QUIT:
                return


def init_screen():
    pygame.init()
    screen = pygame.display.set_mode(screen_dimensions)
    pygame.display.set_caption(title)
    clock = pygame.time.Clock()
    return screen, clock

main()
