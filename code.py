import random

import board
import neopixel
import time
import math

pixel_pin = board.D10
num_pixels = 166

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

RED = (255, 0, 0)
ORANGE = (255, 127, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (127, 0, 255)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

colors = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE, MAGENTA]

def main():
    while True:
        for j in range(160):
            setRange(j, (j+20)%160, RED)
            setRange((j+20)%160, (j+40)%160, ORANGE)
            setRange((j+40)%160, (j+60)%160, YELLOW)
            setRange((j+60)%160, (j+80)%160, GREEN)
            setRange((j+80)%160, (j+100)%160, CYAN)
            setRange((j+100)%160, (j+120)%160, BLUE)
            setRange((j+120)%160, (j+140)%160, PURPLE)
            setRange((j+140)%160, (j+160)%160, MAGENTA)
            pixels.show()
            time.sleep(0.02)

def testing2():
    while True:
        for j in range(160):
            setRange(j, (j+20)%160, RED)
            setRange((j+20)%160, (j+40)%160, ORANGE)
            setRange((j+40)%160, (j+60)%160, YELLOW)
            setRange((j+60)%160, (j+80)%160, GREEN)
            setRange((j+80)%160, (j+100)%160, CYAN)
            setRange((j+100)%160, (j+120)%160, BLUE)
            setRange((j+120)%160, (j+140)%160, PURPLE)
            setRange((j+140)%160, (j+160)%160, MAGENTA)
            pixels.show()
            time.sleep(0.02)

def testing():
    pixels.fill(RED)
    while True:
        for i in range(1530):
            if i < 256:
                newColor = (255, i, 0)
                pixels.fill(newColor)
            elif i >= 256 and i < 511:
                newColor = (255-(i-255), 255, 0)
                pixels.fill(newColor)
            elif i >= 511 and i < 766:
                newColor = (0, 255, i-510)
                pixels.fill(newColor)
            elif i >= 766 and i < 1021:
                newColor = (0, 255-(i-765), 255)
                pixels.fill(newColor)
            elif i >= 1021 and i < 1276:
                newColor = (i-1020, 0, 255)
                pixels.fill(newColor)
            elif i >= 1276 and i < 1531:
                newColor = (255, 0, 255-(i-1275))
                pixels.fill(newColor)
            #print(newColor)
            pixels.show()

def setRange(start, end, color):
    if start < end:
        for i in range(start, end):
            pixels[i] = color
    elif start > end:
        for i in range(start, 160):
            pixels[i] = color
        for i in range(0, end):
            pixels[i] = color
    else:
        pixels[start] = color

if __name__ == "__main__":
    testing()