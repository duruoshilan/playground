from turtle import up
from src.scenes import Scenes
from src.ground import AllAround, DownLeft, GroundTree, Left, LeftRight, NoEntry, NoUp, Right, Up, UpDown, DownRight, Down, NoRight, NoLeft, UpRight, UpLeft, NoDown
from src.player import Player
from src.trampoline import TrampolinePair
from src.fruits import Apple, Banana, Melon
from src.enemies import Chicken, Plant, Duck

grounds = [
    [GroundTree, GroundTree, Right, NoUp, LeftRight, Left,GroundTree],
    [GroundTree, GroundTree, GroundTree, UpDown, GroundTree, GroundTree,GroundTree],
    [GroundTree, GroundTree, GroundTree, UpDown, GroundTree, GroundTree,GroundTree],
    [GroundTree, Down, GroundTree, Up, GroundTree, Down,GroundTree],
    [GroundTree, UpRight, Left, GroundTree, Right, UpLeft,GroundTree],
    [GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree,GroundTree],
]

scenes = Scenes(grounds)
player = Player(scenes, 5, 0)
apple = Apple(scenes, 2,4 )


def forward():
    player.move_forwrd()

def right():
    player.turn_right()

def left():
    player.turn_left()

def collect_fruit():
    player.collect_fruit()
