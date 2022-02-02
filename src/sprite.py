import pygame
from enum import Enum

class Face(Enum):
    Right = 0
    Up = 1
    Left = 2
    Down = 3
    
    def forward(self, x, y, delaytime = 1):
        if self.value == self.Right.value:
            return x + delaytime, y
        elif self.value == self.Left.value:
            return x - delaytime, y
        elif self.value == self.Up.value:
            return x, y - delaytime
        elif self.value == self.Down.value:
            return x, y + delaytime

    def turn_left(self):
        return Face((self.value + 1) % len(Face))
    
    def turn_right(self):
        return Face((self.value - 1) % len(Face))
    
    def turn_around(self):
        return Face((self.value + 2) % len(Face))

class Sprite(pygame.sprite.Sprite):
    def __init__(self, scenes):
        super().__init__()
        self.x, self.y = 0, 0
        self.image = None
        self.rect = None
        self.scale = scenes.scale * 1.8
        self.w = None
        self.h = None
        self.s_w = None
        self.s_h = None
        self.scenes = scenes

    def update(self):
        w = self.scenes.s_w
        h = self.scenes.s_h
        self.image = pygame.transform.scale(self.image, (self.s_w, self.s_h))
        self.rect.topleft = self.x * w, self.y * h

class Actor(Sprite):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.animation = {}
        self.status = None
        self.reset_status = None
        self.speed = 15
        self.wait_time = 60
        self.animation_once_kill = None
        self.reset_status = None
        self.heading = Face.Right
        self.base_flip = True
        self.is_flip = False
        self.index = 0

    def get_image(self, src, w, h, count):
        surface = pygame.image.load(src)
        return surface, w, h, count

    def init_data(self, w, h, status):
        self.w = w
        self.h = h
        self.s_w = int(self.w * self.scale)
        self.s_h = int(self.h * self.scale)
        self.status = status
        self.offset = (self.scenes.s_w // 2 - self.s_w // 2), (self.scenes.s_h // 2 - self.s_h // 2)
        self.image = self.animation[status][0].subsurface((0, 0, w, h))
        self.rect = self.image.get_rect()

    def forward(self, status="run", back_status = "idle"):
        next_x, next_y = self.heading.forward(self.x, self.y)
        this_ground = self.scenes.get_ground(self.x, self.y)
        next_ground = self.scenes.get_ground(next_x, next_y)

        pygame.time.delay(self.wait_time * 5)
        self.status = status

        if self.heading == Face.Right:
            self.is_flip = not self.base_flip
        if self.heading == Face.Left:
            self.is_flip = self.base_flip

        delaytime = 1 / self.speed
        if this_ground.check_move(self.heading) and next_ground.check_move(self.heading.turn_around()):
            for i in range(self.speed):
                self.x, self.y = self.heading.forward(self.x, self.y, delaytime)
                pygame.time.delay(self.wait_time)
        else:
            for i in range(self.speed // 4):
                self.x, self.y = self.heading.forward(self.x, self.y, delaytime)
                pygame.time.delay(self.wait_time)
            for i in range(self.speed // 4):
                self.x, self.y = self.heading.forward(self.x, self.y, -delaytime)
                pygame.time.delay(self.wait_time)

        self.status = back_status

    def turn_left(self):
        self.heading = self.heading.turn_left()

    def turn_right(self):
        self.heading = self.heading.turn_right()

    def update(self):
        for status in self.animation.keys():
            if self.status == status:
                surface, w, h, count = self.animation[status]
                if self.index > count - 1:
                    if self.reset_status is not None:
                        self.status = self.reset_status
                    if self.animation_once_kill == self.status:
                        pygame.sprite.Sprite.kill(self)
                    self.index = 0
                self.image = surface.subsurface(self.index * w, 0, w, h)
                self.image = pygame.transform.flip(self.image, self.is_flip, False)
                self.rect = self.image.get_rect()
                w = self.scenes.s_w
                h = self.scenes.s_h
                self.image = pygame.transform.scale(self.image, (self.s_w, self.s_h))
                self.rect.topleft = self.x * w + self.offset[0], self.y * h + self.offset[1]
                self.index += 1
                
