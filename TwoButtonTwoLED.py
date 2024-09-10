# imports
import board
from digitalio import DigitalInOut, Direction
import time

# pin configuration / setup
button_black = DigitalInOut(board.D2)
button_red = DigitalInOut(board.D3)

button_black.direction = Direction.INPUT
button_red.direction = Direction.INPUT

led = DigitalInOut(board.D4)
led.direction = Direction.OUTPUT

led2 = DigitalInOut(board.D5)
led2.direction = Direction.OUTPUT

both_led = False
led_switch = False

while True:
    if not button_black.value:
        both_led = not both_led
        time.sleep(0.2)
        
    if both_led:
        both_led = False
        led.value = not led.value
        led2.value = led.value
        
    if not button_red.value:
        led_switch = not led_switch
        time.sleep(0.2)
        
    if led_switch:
        led_switch = False
        led.value = not led.value
        led2.value = not led.value



