# Potentiometer-based LED Heat Indicator for Pico 2 W
# Author: Jacob F. (https://github.com/tenshi-net)
# Not meant to be used as a real sensor (for now).
# Might develop into a real project in the future but it's just a demonstration of ADC and if statements from a course I'm taking.
# Feel free to use this as a framework for your own projects if you'd like!
# No credit necessary since most of this is based off of code from a YouTube course by Paul McWhorter (https://www.youtube.com/playlist?list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5)

from machine import Pin
from time import sleep

# variables for the potentiometer pin assignment
pot_pin = 28
pot_converter = machine.ADC(pot_pin)

# variables for LED pins
blue = Pin(15,Pin.OUT)
green = Pin(14,Pin.OUT)
red = Pin(13,Pin.OUT)

while True:
    # gathers value of potentiometer and assigns to pot_val variable in bits
    pot_val = pot_converter.read_u16()
    # converts bits to a scale of 0-100
    percent = round(pot_val * 100 / 65535)
    print(percent)
    sleep(.1)

    # takes percentage value and uses it to control the "heat indicator" level of LEDs from blue (cool) to red (hot)
    if percent < 80:
        blue.value(1)
        green.value(0)
        red.value(0)
    if percent >= 80:
        blue.value(0)
        green.value(1)
        red.value(0)
    if percent >= 95:
        blue.value(0)
        green.value(0)
        red.value(1)
        print("DANGER: High temperatures! Power off immediately!")
