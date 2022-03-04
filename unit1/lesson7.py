from turtle import up
from src.scenes import Scenes
from src.ground import AllAround, DownLeft, GroundTree, Left, LeftRight, NoEntry, NoUp, Right, Up, UpDown, DownRight, Down, NoRight, NoLeft, UpRight, UpLeft, NoDown
from src.player import Player
from src.trampoline import TrampolinePair
from src.fruits import Apple, Banana, Melon
from src.enemies import Chicken, Plant, Duck

grounds = [
    [GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree],
    [GroundTree, Down, GroundTree, GroundTree, Down, GroundTree],
    [GroundTree,  UpDown, Right, NoUp, NoRight, GroundTree],
    [GroundTree, NoLeft, LeftRight, NoDown, NoRight, GroundTree],
    [GroundTree, Up, GroundTree, GroundTree, Up, GroundTree],
]

scenes = Scenes(grounds)
player = Player(scenes, 4, 4)
apple = Apple(scenes, 3,2 )


def forward():
    player.move_forwrd()

def right():
    player.turn_right()

def left():
    player.turn_left()

def collect_fruit():
    player.collect_fruit()
