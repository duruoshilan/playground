from src.scenes import Scenes
from src.ground import AllAround, DownLeft, GroundTree, Left, LeftRight, NoEntry, NoUp, Right, Up, UpDown, DownRight, Down, NoRight, NoLeft, UpRight, UpLeft, NoDown
from src.player import Player
from src.trampoline import TrampolinePair
from src.fruits import Apple, Banana, Melon
from src.enemies import Chicken, Plant, Duck

grounds = [
    [GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree],
    [GroundTree, DownRight,  LeftRight, LeftRight, LeftRight, DownLeft, GroundTree],
    [GroundTree, UpDown, GroundTree,  GroundTree, GroundTree, UpDown, GroundTree],
    [GroundTree, Up, GroundTree,  GroundTree, GroundTree, Up, GroundTree],
    [GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree],
]

scenes = Scenes(grounds)
player = Player(scenes, 5, 3)
apple = Apple(scenes, 3, 1)
# banana = Banana(scenes, 2, 3)
# melon = Melon(scenes, 2, 4)
# plant = Plant(scenes, 2, 5)
# duck = Duck(scenes, 3, 5)
# chicken = Chicken(scenes, 4, 5)
# TrampolinePair(scenes, (1, 2), (3, 4))

def forward():
    player.move_forwrd()

def right():
    player.turn_right()

def left():
    player.turn_left()

def collect_fruit():
    player.collect_fruit()
