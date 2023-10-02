import random
import pygame
from scripts.background import Background
from scripts.obj import Obj
from scripts.player import Player
from scripts.cloud import Cloud
from scripts.scene import Scene
from scripts.fade import Fade

from scripts.settings import *

from scripts.text import Text

class Game(Scene):

    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()
        self.collision_sprites = pygame.sprite.Group()
        # self.bg = Background("assets/bg_1.png", [0, -480], [self.all_sprites])

        self.tick = 0
        self.cloud_colision = pygame.sprite.Group()


        self.score_text = Text("assets/fonts/airstrike.ttf",
                               25, "Score: ", "white", [30,30])
        self.score_pts = Text("assets/fonts/airstrike.ttf",
                               25, "0", "white", [130, 30])

        self.life_text = Text("assets/fonts/airstrike.ttf",
                               25, "Life: ", "white", [260,30])
        self.life_pts = Text("assets/fonts/airstrike.ttf",
                               25, "3", "white", [330, 30])

        self.player = Player([0, 0], [self.all_sprites], self.cloud_colision, self.score_pts, self.life_pts)

    def events(self, event):
        pass

    def update(self):
        self.all_sprites.update()
        self.spaw_cloud()
        self.score_text.draw()
        self.score_pts.draw()
        self.life_text.draw()
        self.life_pts.draw()
        return super().update()

    def spaw_cloud(self):
        self.tick += 1
        if self.tick == 100:
            Cloud("assets/clouds/cloud0.png", [random.randint(0, 150), -100], [self.all_sprites, self.cloud_colision])


        if self.tick == 200:
            Cloud("assets/clouds/cloud0.png", [random.randint(350, 450), -100], [self.all_sprites, self.cloud_colision])
            self.tick = 0

# class Ui:
#     def __init__(self):
#         self.display = pygame.display.get_surface()
#         self.ui_group = pygame.sprite.Group()
#
#         self.hud1 = Obj("assets/player/idle_0.png", [0, 10], [self.ui_group])
#         self.hud2 = Obj("assets/player/idle_0.png", [74, 10], [self.ui_group])
#         self.hud3 = Obj("assets/player/idle_0.png", [144, 10], [self.ui_group])
#
#     def draw(self):
#         self.ui_group.draw(self.display)

# class Level:
#     def __init__(self, worldmap):
#         self.display = pygame.display.get_surface()
#         self.all_sprites = pygame.sprite.Group()
#         self.collision_sprites = pygame.sprite.Group()
#         self.active = True
#         self.gameover = False
#         self.fade = Fade(5)
#         self. finish = Obj("assets/title/finish.png", [0,0], [self.all_sprites])
#
#         self.player = Player([100, 128], [self.all_sprites], self.collision_sprites)
#
#         self.worldmap = worldmap
#         self.generate_map()
#         self.hud_ui = Ui()
#
#     def events(self):
#         pass
#
#     def next_stage(self):
#         if self.player.rect.colliderect(self.finish.rect):
#             self.active = False
#
#     def draw(self):
#         self.all_sprites.costum_draw(self.player)
#         self.hud_ui.draw()
#         self.fade.draw()
#         # self.current_level.draw()
#
#
#     def generate_map(self):
#         for row_index, row in enumerate(self.worldmap):
#             for col_index, col in enumerate(row):
#                 x = col_index * TILE_SIZE
#                 y = row_index * TILE_SIZE
#
#                 if col == 'X':
#                     Obj("assets/title/tile.png", [x, y], [self.all_sprites, self.collision_sprites])
#
#                 elif col == 'C':
#                     self.finish.rect.x = x
#                     self.finish.rect.y = y
#
#                 elif col == 'P':
#                     self.player.rect.x = x
#                     self.player.rect.y = y
#
#
#
#
#     def colision(self):
#         pass
#
#     def gameover(self):
#         pass
#
#     def update(self):
#         self.all_sprites.update()
#         self.next_stage()
#         # self.hud_ui.update()
#
