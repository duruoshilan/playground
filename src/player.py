import pygame
from src.sprite import Actor, Face

class Player(Actor):
    def __init__(self, scenes, x, y):
        super().__init__(scenes)
        self.x, self.y = x, y
        src = scenes.path + "/images/MainCharacters/VirtualGuy/"
        self.animation["idle"] = self.get_image(src + "Idle(32x32).png", 32, 32, 11)
        self.animation["run"] = self.get_image(src + "Run(32x32).png", 32, 32, 12)
        self.animation["jump"] = self.get_image(src + "Jump(32x32).png", 32, 32, 1)
        self.animation["doublejump"] = self.get_image(src + "DoubleJump(32x32).png", 32, 32, 6)
        self.init_data(32, 32, "run")
        self.scenes.player = self

    def move_forwrd(self):
        self.forward()
        self.jump()



    def collect_fruit(self):
        fruit = self.scenes.get_fruit(self.x, self.y)
        if fruit:
            fruit.index = 0
            fruit.status = "collected"

    def jump(self):
        trampoline = self.scenes.get_trampoline(self.x, self.y)
        if trampoline:
            self.status = "doublejump"
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
            
