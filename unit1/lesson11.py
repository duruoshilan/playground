from src.scenes import Scenes
from src.ground import AllAround, DownLeft, GroundTree, Left, LeftRight, NoEntry, NoUp, Right, Up, UpDown, DownRight, Down, NoRight, NoLeft, UpRight, UpLeft, NoDown
from src.player import Player
from src.trampoline import TrampolinePair
from src.fruits import Apple, Banana, Melon
from src.enemies import Chicken, Plant, Duck

grounds = [
  
    [GroundTree, DownRight, LeftRight, Left, GroundTree, GroundTree],
    [DownRight, UpLeft, GroundTree, GroundTree, GroundTree, GroundTree],
    [UpDown, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree],
    [UpDown, GroundTree, GroundTree, GroundTree, GroundTree, GroundTree],
    [UpDown, GroundTree, DownRight, NoUp, Left, GroundTree],
    [UpDown, Right, NoRight, Up, GroundTree, GroundTree],
    [NoLeft, NoUp, UpLeft, GroundTree, GroundTree, GroundTree],
    [UpRight, NoDown, Left, GroundTree, GroundTree, GroundTree],
   
]

scenes = Scenes(grounds)
player = Player(scenes, 1, 5)



def forward():
    player.move_forwrd()

def right():
    player.turn_right()

def left():
    player.turn_left()

def collect_fruit():
    player.collect_fruit()
