from src.scenes import Scenes
from src.ground import AllAround, DownLeft, GroundTree, Left, LeftRight, NoEntry, NoUp, Right, UpDown, DownRight, Down, NoRight, NoLeft, UpRight, UpLeft, NoDown
from src.player import Player
from src.trampoline import TrampolinePair
from src.fruits import Apple, Banana, Melon
from src.enemies import Chicken, Plant, Duck

grounds = [
    
    [GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree],
    [Right, LeftRight, LeftRight, LeftRight, LeftRight, NoUp, Left, GroundTree],
    [GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, UpDown, GroundTree, GroundTree],
    [GroundTree, GroundTree, GroundTree, GroundTree, GroundTree, UpDown, GroundTree, GroundTree],
    [Right, LeftRight, DownLeft, GroundTree, GroundTree, UpDown, GroundTree, GroundTree],
    [GroundTree, GroundTree, UpDown, GroundTree, GroundTree, UpDown, GroundTree, GroundTree],
    [GroundTree, GroundTree, UpRight, LeftRight, LeftRight, NoDown, LeftRight, Left],
    
]

scenes = Scenes(grounds)
player = Player(scenes, 2, 6)
apple = Apple(scenes, 5, 6)


def forward():
    player.move_forwrd()

def right():
    player.turn_right()

def left():
    player.turn_left()

def collect_fruit():
    player.collect_fruit()
