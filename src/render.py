import sys, pygame

class Render:
    def __init__(self, screnes):
        self.screnes = screnes
        self.sprite_group = pygame.sprite.Group()

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(self.screnes.size)
        clock = pygame.time.Clock()

        self.sprite_group.add(self.screnes.grounds)
        self.sprite_group.add(self.screnes.player)
        self.sprite_group.add(self.screnes.trees)
        self.sprite_group.add(self.screnes.trampolines)
        self.sprite_group.add(self.screnes.fruits)
        self.sprite_group.add(self.screnes.enemies)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill(self.screnes.bgcolor)

            self.sprite_group.draw(screen)
            self.sprite_group.update()

            clock.tick(20)
            pygame.display.update()