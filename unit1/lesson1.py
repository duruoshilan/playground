from src.scenes import Scenes
from src.ground import AllAround, DownLeft, GroundTree, Left, LeftRight, NoEntry, NoUp, Right, UpDown, DownRight, Down, NoRight, NoLeft, UpRight, UpLeft, NoDown
from src.player import Player
from src.trampoline import TrampolinePair
from src.fruits import Apple, Banana, Melon
from src.enemies import Chicken, Plant, Duck

grounds = [
    [GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree],
    [GroundTree, Right,  NoUp, NoUp, NoUp, Left, GroundTree],
    [GroundTree, Right, NoRight,  UpDown, NoLeft, Left, GroundTree],
    [GroundTree, Right, NoRight,  UpDown, NoLeft, Left, GroundTree],
    [GroundTree, Right, NoRight,  UpDown, NoLeft, Left, GroundTree],
    [GroundTree, Right, NoDown,  NoDown, NoDown, Left, GroundTree],
    [GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree],
]

scenes = Scenes(grounds)
player = Player(scenes, 1, 1)
apple = Apple(scenes, 2, 2)
banana = Banana(scenes, 2, 3)
melon = Melon(scenes, 2, 4)
plant = Plant(scenes, 2, 5)
duck = Duck(scenes, 3, 5)
chicken = Chicken(scenes, 4, 5)
TrampolinePair(scenes, (1, 2), (3, 4))

def forward():
    player.move_forwrd()

def right():
    player.turn_right()

def left():
    player.turn_left()

def collect_fruit():
    player.collect_fruit()
