import pygame, sys
from pygame.locals import *

class GuiController(object):
    def __init__(self, width, height, caption, data_file):
        self.width = width
        self.height = height
        self.data_file = data_file
        pygame.init()
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
    def update_screen(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()                
        pygame.display.update()
    def draw_start(self):
        Start = pygame.Rect(self.width * 0.25, self.height * 0.1,
                            self.width * 0.15, self.height * 0.05)
        pygame.draw.rect(self.screen, pygame.Color(0, 255, 0),
                         Start, int(min(self.width * 0.01, self.height * 0.01)))
    def main(self):
        self.draw_start()
        while 1:
            self.update_screen()
            self.clock.tick(60)

if __name__ == "__main__":
    #testing
    a = GuiController(500, 500, "abcd", "atat")
    a.main()
