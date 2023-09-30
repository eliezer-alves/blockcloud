import pygame
from scripts.obj import Obj

class Background:
    def __init__(self, img, pos, group):
        self.bg = Obj(img, pos, group)
    
    def update(self):
        pass
