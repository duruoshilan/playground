from src.scenes import Scenes
from src.ground import AllAround, DownLeft, GroundTree, Left, LeftRight, NoEntry, NoUp, Right, Up, UpDown, DownRight, Down, NoRight, NoLeft, UpRight, UpLeft, NoDown
from src.player import Player
from src.trampoline import TrampolinePair
from src.fruits import Apple, Banana, Melon
from src.enemies import Chicken, Plant, Duck

grounds = [
    [GroundTree, Right, LeftRight, LeftRight, LeftRight, Left],
    [GroundTree, GroundTree, GroundTree, Down, GroundTree, GroundTree],
    [GroundTree, GroundTree, GroundTree, UpDown, GroundTree, GroundTree],
    [GroundTree, Right, LeftRight,AllAround, LeftRight, DownLeft],
    [GroundTree, GroundTree, GroundTree, Up, GroundTree, Up],
    [GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree],
]

scenes = Scenes(grounds)
player = Player(scenes, 5, 4)
apple = Apple(scenes, 2, 0)


def forward():
    player.move_forwrd()

def right():
    player.turn_right()

def left():
    player.turn_left()

def collect_fruit():
    player.collect_fruit()
