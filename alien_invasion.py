import sys
import pygame

class AlienInvasion:
    """ Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200 ,800))
        pygame.display.set_caption("Alien Invasion")

        # make an instance of clock to control frame rate
        self.clock = pygame.time.Clock()

        #set the background color
        self.bg_color = (230,200,150)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #watch out for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            #make the most recent draw screen visible
            pygame.display.flip() 

            #set the frame rate using the clock
            self.clock.tick(60)

            #set the background color
            self.screen.fill(self.bg_color)

if __name__ == '__main__':
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()