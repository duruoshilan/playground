from shutil import move
from unit1.lesson1 import *

def play():
    forward()
    right()
    for i in range(3):
        forward()
        # collect_fruit()
    left()
    left()
    forward()
    forward()
    left()
    forward()
    forward()

scenes.render(play)