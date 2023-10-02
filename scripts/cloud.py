from scripts.settings import *
from scripts.obj import Obj

class Cloud(Obj):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.speed = 1
        self.life = 3

    def destruction(self):
        if self.life <=0:
            self.kill()

    def limits(self):
        if self.rect.y > HEIGHT + self.image.get_height():
            self.kill()

    def move(self):
        self.rect.y += self.speed

    def update(self):
        self.destruction()
        self.limits()
        self.move()