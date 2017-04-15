import pygame, sys
from pygame.locals import *

class gui_interface(object):
    def __init__(self, width, height, data_file):
        self.width = width
        self.height = height
        self.data_file = data_file
    
