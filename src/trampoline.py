from src.sprite import Actor

class Trampoline(Actor):
    def __init__(self, scenes, pos):
        super().__init__(scenes)
        self.x, self.y = pos
        self.another = None
        src = scenes.path + "/images/Traps/Trampoline/"
        self.animation["idle"] = self.get_image(src + "Idle.png", 28, 28, 1)
        self.animation["jump"] = self.get_image(src + "Jump (28x28).png", 28, 28, 8)
        self.reset_status = "idle"
        self.init_data(28, 28, "idle")
        self.scenes.trampolines.append(self)

class TrampolinePair:
    def __init__(self, scenes, pos1, pos2):
        trampoline1 = Trampoline(scenes, pos1)
        trampoline2 = Trampoline(scenes, pos2)
        trampoline1.another = trampoline2
        trampoline2.another = trampoline1