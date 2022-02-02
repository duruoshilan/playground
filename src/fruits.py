from src.sprite import Actor

class Apple(Actor):
    def __init__(self, scenes, x, y):
        super().__init__(scenes)
        self.x, self.y = x, y
        src = scenes.path + "/images/Items/Fruits/"
        self.animation["idle"] = self.get_image(src + "Apple.png", 32, 32, 17)
        self.animation["collected"] = self.get_image(src + "Collected.png", 32, 32, 6)
        self.animation_once_kill = "collected"
        self.init_data(32, 32, "idle")
        self.scenes.fruits.append(self)

class Banana(Actor):
    def __init__(self, scenes, x, y):
        super().__init__(scenes)
        self.x, self.y = x, y
        src = scenes.path + "/images/Items/Fruits/"
        self.animation["idle"] = self.get_image(src + "Bananas.png", 32, 32, 17)
        self.animation["collected"] = self.get_image(src + "Collected.png", 32, 32, 6)
        self.animation_once_kill = "collected"
        self.init_data(32, 32, "idle")
        self.scenes.fruits.append(self)

class Melon(Actor):
    def __init__(self, scenes, x, y):
        super().__init__(scenes)
        self.x, self.y = x, y
        src = scenes.path + "/images/Items/Fruits/"
        self.animation["idle"] = self.get_image(src + "Melon.png", 32, 32, 17)
        self.animation["collected"] = self.get_image(src + "Collected.png", 32, 32, 6)
        self.animation_once_kill = "collected"
        self.init_data(32, 32, "idle")
        self.scenes.fruits.append(self)