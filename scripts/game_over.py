import pygame
import sys
from scripts.background import Background
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text
from scripts.button import Button

class GameOver(Scene):

    def __init__(self):
        super().__init__()
        self.bg = Background("assets/bg_1.png", [0, -480], [self.all_sprites])

        self.btn_menu = Button("white", 64, 520, "Back Menu", self.next_scene)
        self.btn_quit = Button("white", 64, 600, "Quit", self.quit_game)

        self.title = Text("assets/fonts/airstrike.ttf",
                               40, "GAME OVER", "white", [150, 100])

    
    def events(self, event):
        self.btn_quit.events(event)
        self.btn_menu.events(event)

        return super().events(event)

    def next_scene(self):
        self.active = False

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.bg.update()
        self.title.draw()
        self.btn_quit.draw()
        self.btn_menu.draw()

        return super().update()




