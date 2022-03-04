from turtle import up
from src.scenes import Scenes
from src.ground import AllAround, DownLeft, GroundTree, Left, LeftRight, NoEntry, NoUp, Right, UpDown, DownRight, Down, NoRight, NoLeft, UpRight, UpLeft, NoDown
from src.player import Player
from src.trampoline import TrampolinePair
from src.fruits import Apple, Banana, Melon
from src.enemies import Chicken, Plant, Duck

grounds = [
    [GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree,GroundTree],
    [GroundTree, GroundTree, GroundTree, Down, GroundTree, GroundTree,GroundTree],
    [GroundTree, Down, GroundTree, NoLeft, LeftRight, Left,GroundTree],
    [GroundTree, UpDown, GroundTree, UpDown, GroundTree, GroundTree,GroundTree],
    [GroundTree, UpRight, LeftRight, UpLeft, GroundTree, GroundTree,GroundTree],
    [GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree,GroundTree],
]

scenes = Scenes(grounds)
player = Player(scenes, 1, 2)
apple = Apple(scenes, 2,4 )


def forward():
    player.move_forwrd()

def right():
    player.turn_right()

def left():
    player.turn_left()

def collect_fruit():
    player.collect_fruit()
