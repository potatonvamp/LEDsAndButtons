#imports
import board
import digitalio as dio
import time


def setup(pin):
    led = dio.DigitalInOut(pin)
    led.direction = dio.Direction.OUTPUT
    return led
    

def blink(first):
    first.value = not first.value
    time.sleep(0.1)
    first.value = not first.value
    time.sleep(0.1)
    
led1 = setup(board.D2)

led2 = setup(board.D3)

led3 = setup(board.D4)

led4 = setup(board.D5)

while True:
    blink(led1)
    blink(led2)
    blink(led3)
    blink(led4)
