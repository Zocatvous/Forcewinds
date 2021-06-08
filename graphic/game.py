
import pygame
impoer
class Forcewinds:
    #overall game class

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        drivers = ['directfb', 'fbcon', 'svgalib','']

        found = False
        for driver in drivers:
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
            try:
                pygame.display.init()
            except pygame.error:
                print('Driver: {0} failed.'.format(driver))
                continue
            found = True
            break

        if not found:
            raise Exception('No suitable video driver found!')

        self.screen_window = pygame.display.set_mode((2880, 1800))
        pygame.display.set_caption("Another")

        """Setting background color"""
        self.background_color = (230, 230, 255)



    def run_game(self):
        #
        while True:
            # Watch for keyboard and mouse actions
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Redraw the screen during each pass through the loop.
            #self.screen_window.fill(self.settings.background_color)
            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == "__main__":
    """Make a game instance, and run the game"""
    ac = Forcewinds()
    ac.run_game()