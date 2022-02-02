import pygame

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
        self.animation_once_kill = None
        self.index = 0

    def get_image(self, src, w, h, count):
        surface = pygame.image.load(src)
        return surface, w, h, count

    def init_data(self, w, h, status):
        self.w = w
        self.h = h
        self.s_w = int(self.w * self.scale)
        self.s_h = int(self.h * self.scale)
        self.offset = (self.scenes.s_w // 2 - self.s_w // 2), (self.scenes.s_h // 2 - self.s_h // 2) * 1.3
        self.status = status
        self.is_flip = False
        self.image = self.animation[status][0].subsurface((0, 0, w, h))
        self.rect = self.image.get_rect()

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
                
