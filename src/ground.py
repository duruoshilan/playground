import random, pygame
from src.player import Face
from src.sprite import Sprite

class Ground(Sprite):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.left = True
        self.right = True
        self.up = True
        self.down = True
        self.image = pygame.image.load(self.scenes.path + "/images/medievalRTS_spritesheet@2.png")
        name = self.__class__.__name__
        data = self.scenes.grounds_data[name]
        x, y, w, h = data[random.randint(0, len(data)-1)]
        self.w = w
        self.h = h
        self.s_w = int(self.scenes.scale * self.w)
        self.s_h = int(self.scenes.scale * self.h)
        self.image = self.image.subsurface((x, y, w, h))
        self.image = pygame.transform.scale(self.image, (self.scenes.s_w, self.scenes.s_h))
        self.rect = self.image.get_rect()

    def check_move(self, player_heading):
        if player_heading == Face.Left:
            return self.left
        elif player_heading == Face.Right:
            return self.right
        elif player_heading == Face.Up:
            return self.up
        elif player_heading == Face.Down:
            return self.down

class Tree(Ground):
    def __init__(self, scenes):
        self.scale = scenes.scale * 0.2
        super().__init__(scenes)
        self.image = pygame.transform.scale(self.image, (self.s_w, self.s_h))
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.scenes.trees.append(self)

    def update(self):
        w = self.scenes.s_w
        h = self.scenes.s_h
        self.rect.topleft = self.x * w + (w - self.s_w), self.y * h + (h - self.s_h)

class GroundTree(Ground):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.left = False
        self.right = False
        self.up = False
        self.down = False

class NoEntry(Ground):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.left = False
        self.right = False
        self.up = False
        self.down = False

class Right(Ground):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.left = False
        self.up = False
        self.down = False

class Left(Ground):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.up = False
        self.down = False
        self.right = False

class Down(Ground):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.up = False
        self.left = False
        self.right = False

class Up(Ground):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.down = False
        self.left = False
        self.right = False

class LeftRight(Ground):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.up = False
        self.down = False

class UpDown(Ground):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.left = False
        self.right = False

class DownLeft(Ground):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.up = False
        self.right = False

class DownRight(Ground):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.up = False
        self.left = False

class UpLeft(Ground):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.down = False
        self.right = False

class UpRight(Ground):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.down = False
        self.left = False

class AllAround(Ground):
    def __init__(self, scenes):
        super().__init__(scenes)

class NoDown(Ground):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.down = False

class NoLeft(Ground):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.left = False

class NoRight(Ground):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.right = False

class NoUp(Ground):
    def __init__(self, scenes):
        super().__init__(scenes)
        self.up = False
