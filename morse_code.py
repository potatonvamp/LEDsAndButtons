import board
from digitalio import DigitalInOut, Direction
import time

led = DigitalInOut(board.D2)
led.direction = Direction.OUTPUT

def dash():
    led.value = True
    time.sleep(1)

def dot():
    led.value = True
    time.sleep(0.5)

def space():
    led.value = False
    time.sleep(1.5)

def seperator():
    led.value = False
    time.sleep(0.25)

def O():
    dash()
    seperator()
    dash()
    seperator()
    dash()

def L():
    dot()
    seperator()
    dash()
    seperator()
    dot()
    seperator()
    dot()

def Y():
    dash()
    seperator()
    dot()
    seperator()
    dash()
    seperator()
    dash()

def C():
    dash()
    seperator()
    dot()
    seperator()
    dash()
    seperator()
    dot()

def N():
    dash()
    seperator()
    dot()

O()
L()
Y()
C()
O()
L()
O()
N()
