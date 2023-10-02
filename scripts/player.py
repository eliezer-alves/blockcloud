import pygame
from scripts.settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collison_group):
        super().__init__(groups)
        self.image = pygame.image.load("assets/nave0.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.collision_group = collison_group
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.jump_force = 10
        self.gravity = 0.2
        self.on_ground = False
        self.flip = False
        self.tick = 0
        self.frame = 0

    def move(self):
        self.rect.x += self.direction.x * self.speed
        if self.on_ground == False:
            self.image = pygame.transform.flip(self.image, self.flip, False)



    def gravity_force(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.input()
        self.move()
        self.gravity_force()
        self.y_collison()

    def y_collison(self):
        if self.rect.y >= HEIGHT - 100:
            self.direction.y = 0
            self.rect.y = HEIGHT - 100
            self.on_ground = True

        for sprite in self.collision_group:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.direction.y = 0
                    self.rect.bottom = sprite.rect.top
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
            print("Direita")
        else:
            self.direction.x = 0
            self.animation(16, 2, "assets/player/walk_")

        if key[pygame.K_SPACE] and self.on_ground:
            self.direction.y = -self.jump_force
            self.on_ground = False

