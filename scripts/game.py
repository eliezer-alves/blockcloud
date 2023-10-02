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
        self.cloud_tick = 0
        self.cloud_colision = pygame.sprite.Group()


        self.score_text = Text("assets/fonts/airstrike.ttf",
                               25, "Score: ", "white", [20,20])
        self.score_pts = Text("assets/fonts/airstrike.ttf",
                               25, "0", "white", [120, 20])

        self.life_text = Text("assets/fonts/airstrike.ttf",
                               25, "Life: ", "white", [20,50])
        self.life_pts = Text("assets/fonts/airstrike.ttf",
                               25, "5", "white", [90, 50])

        self.player = Player([0, 0], [self.all_sprites], self.cloud_colision, self.score_pts, self.life_pts, 5)

    def events(self, event):
        pass

    def next_stage(self):
        if self.player.life <= 0:
            self.active = False

    def update(self):
        self.all_sprites.update()
        self.spaw_cloud()
        self.score_text.draw()
        self.score_pts.draw()
        self.life_text.draw()
        self.life_pts.draw()
        self.next_stage()
        return super().update()

    def spaw_cloud(self):
        self.tick += 1

        file_path = f'assets/clouds/cl{random.randint(0, 4)}.png'
        if self.tick == 50:
            Cloud(file_path, [random.randint(0, 150), random.randint(100, 200)*-1], [self.all_sprites, self.cloud_colision])

        if self.tick == 150:
            Cloud(file_path, [random.randint(350, 450), random.randint(200, 300)*-1], [self.all_sprites, self.cloud_colision])

        if self.tick == 250:
            Cloud(file_path, [random.randint(50, 250), random.randint(200, 300)*-1], [self.all_sprites, self.cloud_colision])

        if self.tick == 400:
            Cloud(file_path, [random.randint(200, 300), random.randint(150, 200) * -1],
                  [self.all_sprites, self.cloud_colision])
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
