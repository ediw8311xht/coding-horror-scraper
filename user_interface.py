import pygame, sys
from pygame.locals import *

class GuiController(object):
    def __init__(self, width, height, caption, data_file):
        self.width = width
        self.height = height
        self.data_file = data_file
        pygame.init()
        pygame.display.set_caption(caption)
        self.update_screen_size()
        self.clock = pygame.time.Clock()
        self.draw_state = 1
        self.draw_update = True
    def update_screen_size(self):
        self.screen = pygame.display.set_mode((self.width, self.height), RESIZABLE)
    def update_screen(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == VIDEORESIZE:
                self.width = event.w
                self.height = event.h
                self.update_screen_size()
                self.draw_update = True
        pygame.display.update()
    def draw_start(self):
        self.courier = pygame.font.SysFont("courier", 15)
        margin = min(self.width * 0.05, self.height * 0.05)
        rect_hsize = self.height * 0.25 - margin
        Start = pygame.Rect(margin, self.height - margin - rect_hsize, self.width * 0.4 - margin, self.height * 0.25 - margin)
        pygame.draw.rect(self.screen, pygame.Color(0, 255, 0), Start, 0)
        self.screen.blit(self.font.render('Hello!', True, (255,0,0)), (200, 100))
    def draw(self):
        if self.draw_state == 1:
            self.draw_start()
    def main(self):
        while 1:
            self.update_screen()
            if self.draw_update == True:
                self.draw()
                self.draw_update = False
            self.clock.tick(60)

if __name__ == "__main__":
    #testing
    a = GuiController(500, 500, "abcd", "atat")
    a.main()
