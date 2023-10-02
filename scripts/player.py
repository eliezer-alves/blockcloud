import pygame
from scripts.settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, cloud_collision, text_score, text_life, life):
        super().__init__(groups)
        self.image = pygame.image.load("assets/pl.png")
        self.text_score = text_score
        self.text_life = text_life
        self.rect = self.image.get_rect(topleft=pos)
        self.cloud_collision = cloud_collision
        self.direction = pygame.math.Vector2()
        self.pts = 0
        self.life = life
        self.speed = 5
        self.jump_force = 8
        self.gravity = 0.1
        self.on_ground = False
        self.flip = False
        self.tick = 0
        self.frame = 0

    def move(self):

        self.rect.x += self.direction.x * self.speed

        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.x > WIDTH - self.rect.w:
            self.rect.x = WIDTH - self.rect.w

        if self.on_ground == False:
            self.image = pygame.transform.flip(self.image, self.flip, False)



    def gravity_force(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.input()
        self.move()
        self.gravity_force()
        if self.direction.y >= 0:
            self.y_collison()
            self.cloud_colision()

    def y_collison(self):
        if self.rect.y >= HEIGHT - self.rect.h:
            self.direction.y = 0
            self.rect.y = HEIGHT - self.rect.h
            if self.pts > 0:
                self.pts = 0
                self.text_score.update_text(str(self.pts), color="white")
                self.life -= 1
                self.text_life.update_text(str(self.life), color="white")
            self.on_ground = True

        # for sprite in self.collision_group:
        #     if sprite.rect.colliderect(self.rect):
        #         if self.direction.y > 0:
        #             self.direction.y = 0
        #             self.rect.bottom = sprite.rect.top
        #             self.on_ground = True
    def cloud_colision(self):
        for cloud in self.cloud_collision:
            if self.rect.colliderect(cloud.rect) and (self.rect.y + self.rect.h) >= cloud.rect.y:
                self.rect.y = (cloud.rect.y - (self.rect.height)) + 5
                self.direction.y = 0
                if not self.on_ground:
                    self.pts += 1
                    self.text_score.update_text(str(self.pts), color="white")
                self.on_ground = True

    def animation(self, speed, n_img, path):
        self.tick+=1
        if self.tick > speed:
            self.tick = 0
            self.frame = (self.frame+1)%n_img
            # self.image=pygame.image.load(path + str(self.frame)+".png")
            # self.image = pygame.transform.flip(self.image, self.flip, False)

    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.direction.x = -1
            self.flip = True
            self.animation(8, 3, "assets/player/walk_")
        elif key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.direction.x = 1
            self.flip = False
            self.animation(8, 3, "assets/player/walk_")
        else:
            self.direction.x = 0
            self.animation(16, 2, "assets/player/walk_")

        if key[pygame.K_SPACE] and self.on_ground:
            self.direction.y = -self.jump_force
            self.on_ground = False

