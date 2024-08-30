#imports
import board
from digitalio import DigitalInOut, Direction
import time

#setup / initialization
led = DigitalInOut(board.D2)
led.direction = Direction.OUTPUT
led.value = True

#infinite loop
while True:
    led.value = not led.value
    time.sleep(0.07)
