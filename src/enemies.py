from src.sprite import Actor, Face

class Plant(Actor):
    def __init__(self, scenes, x, y):
        super().__init__(scenes)
        self.x, self.y = x, y
        src = scenes.path + "/images/Enemies/Plant/"
        self.base_flip = False
        self.is_flip = True
        self.animation["idle"] = self.get_image(src + "Idle (44x42).png", 44, 42, 11)
        self.init_data(44 // 1.5, 42 // 1.5, "idle")
        self.scenes.enemies.append(self)

class Duck(Actor):
    def __init__(self, scenes, x, y):
        super().__init__(scenes)
        self.x, self.y = x, y
        src = scenes.path + "/images/Enemies/Duck/"
        self.base_flip = False
        self.is_flip = True
        self.animation["idle"] = self.get_image(src + "Idle (36x36).png", 36, 36, 10)
        self.init_data(36 // 1.5, 36 // 1.5, "idle")
        self.scenes.enemies.append(self)

class Chicken(Actor):
    def __init__(self, scenes, x, y):
        super().__init__(scenes)
        self.x, self.y = x, y
        src = scenes.path + "/images/Enemies/Chicken/"
        self.base_flip = False
        self.is_flip = True
        self.animation["idle"] = self.get_image(src + "Idle (32x34).png", 32, 34, 13)
        self.animation["run"] = self.get_image(src + "Run (32x34).png", 32, 34, 14)
        self.init_data(32 // 1.5, 34 // 1.5, "idle")
        self.scenes.enemies.append(self)
