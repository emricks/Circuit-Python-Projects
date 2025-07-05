import random

import board
import neopixel
import time
import math

pixel_pin = board.D10
num_pixels = 166

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False)

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

def snake(speed):
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
            time.sleep(0.0625-0.0625*speed/100)

def fade(speed):
    pixels.fill(RED)
    while True:
        for i in range(1531):
            if speed > 20:
                i = round(i/speed*100)
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
            pixels.show()
            if speed < 20:
                time.sleep(20/speed/200)


def switch(rate, type):
    nextColor = random.choice(colors)
    while True:
        if type == 'random':
            thisColor = nextColor
            pixels.fill(thisColor)
            pixels.show()
            time.sleep(1/rate)
            nextColor = random.choice(colors)
            while nextColor == thisColor:
                nextColor = random.choice(colors)
        else:
            for color in colors:
                pixels.fill(color)
                pixels.show()
                time.sleep(1/rate)

def flash(rate, color):
    while True:
        if color == 'random':
            for i in range(2):
                if i == 0:
                  pixels.fill(random.choice(colors))
                else:
                    pixels.fill(BLACK)
                pixels.show()
                time.sleep(1/rate)
        else:
            for i in range(2):
                if i == 0:
                  pixels.fill(color)
                else:
                    pixels.fill(BLACK)
                pixels.show()
                time.sleep(1/rate/2)

def demogorgon():
    while True:
        for i in range(2):
            if i == 0:
                pixels.fill(WHITE)
                time.sleep(random.random()*0.15)
            else:
                pixels.fill(BLACK)
                time.sleep(random.random()*0.15)
            pixels.show()

def solid(color):
    while True:
        pixels.fill(color)
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
    fade(20)