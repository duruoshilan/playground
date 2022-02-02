import threading, os
from xml.dom import minidom
from src.render import Render
from src.ground import Tree

class Scenes:
    def __init__(self, grounds):
        self.path = os.path.abspath(".")
        self.player = None
        self.grounds = grounds
        self.trees = []
        self.fruits = []
        self.enemies = []
        self.trampolines = []
        self.w = 128
        self.h = 128
        self.bgcolor = 255, 255, 255
        self.player = None
        self.scale = 0.8
        self.s_w = int(self.w * self.scale)
        self.s_h = int(self.h * self.scale)
        self.size = None
        self.grounds_data = {"NoEntry": [], "Right": [], "Left": [], "Down": [], "Up": [], "LeftRight": [], "UpDown": [], "DownLeft": [], "DownRight": [], "UpLeft": [],
        "UpRight": [], "AllAround": [], "NoDown": [], "NoLeft": [], "NoRight": [], "NoUp": [], "GroundTree": [], "Tree": []}

        self.init_grounds_pos_data()
        self.set_ground_pos()

        self.renderer = Render(self)

    def init_grounds_pos_data(self):
        doc = minidom.parse(self.path + "/images/medievalRTS_spritesheet@2.xml")
        data = doc.getElementsByTagName("SubTexture")
        for key in self.grounds_data.keys():
            for node in data:
                if node.getAttribute("name") == key+".png":
                    x, y, w, h = int(node.getAttribute("x")), int(node.getAttribute("y")), int(node.getAttribute("width")), int(node.getAttribute("height"))
                    self.grounds_data[key].append((x, y, w, h))

    def set_ground_pos(self):
        x = len(self.grounds[0])
        y = len(self.grounds)
        for i in range(y):
            for j in range(x):
                ground = self.grounds[i][j](self)
                ground.x, ground.y = j, i
                self.grounds[i][j] = ground

                tree = Tree(self)
                tree.x, tree.y = j, i

        self.size = self.s_w * x, self.s_h * y
    
    def render(self, player):
        t = threading.Thread(target=player, name="playerjob")
        t.setDaemon(True)
        t.start()
        self.renderer.run()

    def get_ground(self, x, y):
        x, y = round(x), round(y)
        return self.grounds[y][x]

    def get_fruit(self, x, y):
        x, y = round(x), round(y)
        for fruit in self.fruits:
            if fruit.x == x and fruit.y == y:
                return fruit

    def get_trampoline(self, x, y):
        x, y = round(x), round(y)
        for trampoline in self.trampolines:
            if trampoline.x == x and trampoline.y == y:
                return trampoline