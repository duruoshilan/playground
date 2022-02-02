from hmac import trans_36
from multiprocessing.connection import wait
import pygame
from src.sprite import Actor
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

class Player(Actor):
    def __init__(self, scenes, x, y):
        super().__init__(scenes)
        self.x, self.y = x, y
        src = scenes.path + "/images/MainCharacters/VirtualGuy/"
        self.animation["idle"] = self.get_image(src + "Idle(32x32).png", 32, 32, 11)
        self.animation["run"] = self.get_image(src + "Run(32x32).png", 32, 32, 12)
        self.animation["jump"] = self.get_image(src + "Jump(32x32).png", 32, 32, 1)
        self.speed = 15
        self.wait_time = 60
        self.init_data(32, 32, "run")
        self.offset = (scenes.s_w // 2 - self.s_w // 2), (scenes.s_h // 2 - self.s_h // 2)
        self.heading = Face.Right
        self.scenes.player = self

    def move_forwrd(self):
        nextX, nextY = self.heading.forward(self.x, self.y)
        this_ground = self.scenes.get_ground(self.x, self.y)
        next_ground = self.scenes.get_ground(nextX, nextY)

        pygame.time.delay(self.wait_time * 5)

        self.status = "run"

        if self.heading == Face.Right or self.heading == Face.Left:
            self.is_flip = True if self.heading == Face.Left else False

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
        
        self.status = "idle"

        self.jump()

    def turn_left(self):
        self.heading = self.heading.turn_left()

    def turn_right(self):
        self.heading = self.heading.turn_right()

    def collect_fruit(self):
        fruit = self.scenes.get_fruit(self.x, self.y)
        if fruit:
            fruit.index = 0
            fruit.status = "collected"

    def jump(self):
        trampoline = self.scenes.get_trampoline(self.x, self.y)
        if trampoline:
            self.status = "jump"
            if trampoline:
                trampoline.index = 0
                trampoline.status = "jump"

            for j in range(round(self.y) + 1):
                for i in range(self.speed // 3):
                    self.y -= 1 / (self.speed // 3)
                    pygame.time.delay(self.wait_time // 2)

            self.x = trampoline.another.x
            pygame.time.delay(self.wait_time)

            for j in range(trampoline.another.y + 1):
                for i in range(self.speed // 3):
                    self.y += 1 / (self.speed // 3)
                    pygame.time.delay(self.wait_time // 2)
            
            self.status = "idle"
            
