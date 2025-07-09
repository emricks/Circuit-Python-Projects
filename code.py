import random
import board
import neopixel
import time
from digitalio import DigitalInOut, Direction, Pull

button = DigitalInOut(board.D5)
button.direction = Direction.INPUT
button.pull = Pull.DOWN

def main():
    while True:
        if button.value:
            print("Button is pressed")
        else:
            print("Button is released")
        time.sleep(1)

pixel_pin = board.D10
num_pixels = 166

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False)

RED = (255, 0, 0)
darkred = (80, 0, 0)
ORANGE = (255, 80, 0)
darkorange = (80, 25, 0)
YELLOW = (255, 255, 0)
darkyellow = (80, 80, 0)
CHARTREUSE = (127, 255, 0)
darkchartreuse = (40, 80, 0)
GREEN = (0, 255, 0)
darkgreen = (0, 80, 0)
SEAFOAM = (0, 255, 127)
darkseafoam = (0, 80, 40)
CYAN = (0, 255, 255)
darkcyan = (0, 80, 80)
CORNFLOWER = (0, 127, 255)
darkcornflower = (0, 40, 80)
BLUE = (0, 0, 255)
darkblue = (0, 0, 60)
PURPLE = (127, 0, 255)
darkpurple = (40, 0, 80)
MAGENTA = (255, 0, 255)
darkmagenta = (80, 0, 80)
PINK = (255, 0, 127)
darkpink = (80, 0, 40)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

maincolors = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE, MAGENTA]
colors = [RED, ORANGE, YELLOW, CHARTREUSE, GREEN, SEAFOAM, CYAN, CORNFLOWER, BLUE, PURPLE, MAGENTA, PINK]

def clearLeds():
    time.sleep(1)
    pixels.fill(BLACK)

def snake(speed, colorArray):
    setRange(160, 165, WHITE)
    if speed != 0:
        while True:
            for j in range(160):
                if button.value:
                    setRange(j, (j+20)%160, colorArray[0])
                    setRange((j+20)%160, (j+40)%160, colorArray[1])
                    setRange((j+40)%160, (j+60)%160, colorArray[2])
                    setRange((j+60)%160, (j+80)%160, colorArray[3])
                    setRange((j+80)%160, (j+100)%160, colorArray[4])
                    setRange((j+100)%160, (j+120)%160, colorArray[5])
                    setRange((j+120)%160, (j+140)%160, colorArray[6])
                    setRange((j+140)%160, (j+160)%160, colorArray[7])
                    pixels.show()
                    time.sleep(1/speed/2)
                else:
                    pixels.fill(BLACK)
                    pixels.show()
    else:
        j = 0
        setRange(j, (j + 20) % 160, colorArray[0])
        setRange((j + 20) % 160, (j + 40) % 160, colorArray[1])
        setRange((j + 40) % 160, (j + 60) % 160, colorArray[2])
        setRange((j + 60) % 160, (j + 80) % 160, colorArray[3])
        setRange((j + 80) % 160, (j + 100) % 160, colorArray[4])
        setRange((j + 100) % 160, (j + 120) % 160, colorArray[5])
        setRange((j + 120) % 160, (j + 140) % 160, colorArray[6])
        setRange((j + 140) % 160, (j + 160) % 160, colorArray[7])
        pixels.show()
        return

def cycle(speed):
    pixels.fill(RED)
    if speed == 0:
        return
    while True:
        for i in range(1531*40/speed):
            if button.value:
                i *= speed / 40
                if i < 256:
                    newColor = (255, i, 0)
                    pixels.fill(newColor)
                elif i >= 256 and i < 511:
                    newColor = (255 - (i - 255), 255, 0)
                    pixels.fill(newColor)
                elif i >= 511 and i < 766:
                    newColor = (0, 255, i - 510)
                    pixels.fill(newColor)
                elif i >= 766 and i < 1021:
                    newColor = (0, 255 - (i - 765), 255)
                    pixels.fill(newColor)
                elif i >= 1021 and i < 1276:
                    newColor = (i - 1020, 0, 255)
                    pixels.fill(newColor)
                elif i >= 1276 and i < 1531:
                    newColor = (255, 0, 255 - (i - 1275))
                    pixels.fill(newColor)
            else:
                pixels.fill(BLACK)
                pixels.show()
            pixels.show()

def switch(rate, type, colorArray):
    nextColor = random.choice(colors)
    while True:
        if button.value:
            if type == 'random':
                thisColor = nextColor
                pixels.fill(thisColor)
                pixels.show()
                if rate == 0:
                    return
                time.sleep(1 / rate)
                nextColor = random.choice(colors)
                while nextColor == thisColor:
                    nextColor = random.choice(colors)
            if type == 'order':
                for color in colorArray:
                    pixels.fill(color)
                    pixels.show()
                    if rate == 0:
                        return
                    time.sleep(1 / rate)
        else:
            pixels.fill(BLACK)
            pixels.show()


def flash(rate, type, colorArray):
    while True:
        if button.value:
            if type == 'random':
                for i in range(2):
                    if i == 0:
                        pixels.fill(random.choice(colorArray))
                        if rate == 0:
                            pixels.show()
                            return
                    else:
                        pixels.fill(BLACK)
                    pixels.show()
                    time.sleep(1 / rate / 2)
            elif type == 'single':
                for i in range(2):
                    if i == 0:
                        pixels.fill(colorArray[i])
                        if rate == 0:
                            pixels.show()
                            return
                    else:
                        pixels.fill(BLACK)
                    pixels.show()
                    time.sleep(1 / rate / 2)
            elif type == 'order':
                for color in colorArray:
                    for i in range(2):
                        if i == 0:
                            pixels.fill(color)
                            if rate == 0:
                                pixels.show()
                                return
                        else:
                            pixels.fill(BLACK)
                        pixels.show()
                        time.sleep(1 / rate / 2)
        else:
            pixels.fill(BLACK)
            pixels.show()

def demogorgon():
    while True:
        if button.value:
            for i in range(2):
                if i == 0:
                    pixels.fill(WHITE)
                    time.sleep(random.random() * 0.15)
                else:
                    pixels.fill(BLACK)
                    time.sleep(random.random() * 0.15)
                pixels.show()
        else:
            pixels.fill(BLACK)
            pixels.show()

def solid(color):
    while True:
        if button.value:
            pixels.fill(color)
            pixels.show()
        else:
            pixels.fill(BLACK)
            pixels.show()

def fillbounce(color, color2, speed):
    for i in range(166):
        pixels[i] = color
        pixels.show()
        time.sleep(0.02)
    time.sleep(1)
    if speed == 0:
        pixels.fill(color)
        pixels.show()
        return
    while True:
        if button.value:
            for j in range(2):
                for i in range(42):
                    pixels[83 + i] = color2
                    pixels[82 - i] = color2
                    pixels.show()
                    time.sleep(1 / speed / 2)
                for i in range(42):
                    pixels[124 - i] = color
                    pixels[41 + i] = color
                    pixels.show()
                    time.sleep(1 / speed / 2)
        else:
            pixels.fill(BLACK)
            pixels.show()

def alternate(color, color2, rate):
    for i in range(166):
        pixels[165 - i] = color
        pixels.show()
        time.sleep(0.02)
    time.sleep(1)
    if rate == 0:
        pixels.fill(color)
        pixels.show()
        return
    while True:
        if button.value:
            for j in range(4):
                for i in range(166):
                    if i % 2 == 0:
                        pixels[i + 1] = color
                        pixels[i] = color2
                pixels.show()
                time.sleep(1 / rate)
                for i in range(166):
                    if i % 2 == 0:
                        pixels[i] = color
                        pixels[i + 1] = color2
                pixels.show()
                time.sleep(1 / rate)
        else:
            pixels.fill(BLACK)
            pixels.show()

def bounce(color, color2, speed):
    for i in range(166):
        pixels[i] = color
        pixels.show()
        time.sleep(0.02)
    time.sleep(1)
    if speed == 0:
        pixels.fill(color)
        pixels.show()
        return
    while True:
        if button.value:
            for i in range(151):
                setRange(i, i + 15, color2)
                pixels[i - 1] = color
                pixels.show()
                time.sleep(1/speed/2)
            for i in range(151):
                setRange(150 - i, 165 - i, color2)
                pixels[165 - i] = color
                pixels.show()
                time.sleep(1/speed/2)
        else:
            pixels.fill(BLACK)
            pixels.show()

def randomfill(color, color2, rate):
    for i in range(166):
        pixels[165 - i] = color
        pixels.show()
        time.sleep(0.02)
    time.sleep(1)
    if rate == 0:
        pixels.fill(color)
        pixels.show()
        return
    while True:
        if button.value:
            pixels.fill(color2)
            arr = []
            for i in range(166):
                arr.append(i)
            for i in range(166):
                rand = random.choice(arr)
                pixels[rand] = color
                pixels.show()
                arr.remove(rand)
                time.sleep(1 / rate)
            time.sleep(1)
        else:
            pixels.fill(BLACK)
            pixels.show()

def run(color, color2, speed):
    setRange(160, 165, WHITE)
    for i in range(166):
        pixels[i] = color
        pixels.show()
        time.sleep(0.02)
    time.sleep(1)
    if speed == 0:
        pixels.fill(color)
        pixels.show()
        return
    while True:
        for j in range(160):
            if button.value:
                setRange(j, (j + 20) % 160, color)
                setRange((j + 20) % 160, (j + 40) % 160, color2)
                setRange((j + 40) % 160, (j + 60) % 160, color)
                setRange((j + 60) % 160, (j + 80) % 160, color2)
                setRange((j + 80) % 160, (j + 100) % 160, color)
                setRange((j + 100) % 160, (j + 120) % 160, color2)
                setRange((j + 120) % 160, (j + 140) % 160, color)
                setRange((j + 140) % 160, (j + 160) % 160, color2)
                pixels.show()
                time.sleep(1 / speed / 2)
            else:
                pixels.fill(BLACK)
                pixels.show()

def enter(color, color2, speed):
    for i in range(166):
        pixels[165 - i] = color
        pixels.show()
        time.sleep(0.02)
    time.sleep(1)
    while True:
        pixels.fill(color)
        for i in range(78):
            if button.value:
                pixels.fill(color)
                setRange(83 + i, 88 + i, color2)
                setRange(77 - i, 82 - i, color2)
                pixels.show()
                time.sleep(1/speed/2)
            else:
                pixels.fill(BLACK)
                pixels.show()
        for i in range(5):
            if button.value:
                pixels[4 - i] = color
                pixels[160 + i] = color
                pixels.show()
                time.sleep(1 / speed / 2)
            else:
                pixels.fill(BLACK)
                pixels.show()
        for i in range(2):
            if button.value:
                pixels.fill(color2)
                pixels.show()
                time.sleep(20 / speed)
                pixels.fill(color)
                pixels.show()
                time.sleep(20 / speed)
            else:
                pixels.fill(BLACK)
                pixels.show()
        time.sleep(1)

def swap(color, color2, rate):
    for i in range(166):
        pixels[i] = color
        pixels.show()
        time.sleep(0.02)
    time.sleep(1)
    while True:
        for i in range(2):
            if button.value:
                pixels.fill(color2)
                pixels.show()
                time.sleep(1 / rate)
                pixels.fill(color)
                pixels.show()
                time.sleep(1 / rate)
            else:
                pixels.fill(BLACK)
                pixels.show()
        for i in range(2):
            if button.value:
                setRange(0, 83, color2)
                setRange(83, 165, color)
                pixels.show()
                time.sleep(1 / rate)
                setRange(0, 83, color)
                setRange(83, 165, color2)
                pixels.show()
                time.sleep(1 / rate)
            else:
                pixels.fill(BLACK)
                pixels.show()
        for i in range(2):
            if button.value:
                setRange(0, 42, color2)
                setRange(42, 82, color)
                setRange(82, 125, color2)
                setRange(125, 165, color)
                pixels.show()
                time.sleep(1 / rate)
                setRange(0, 42, color)
                setRange(42, 82, color2)
                setRange(82, 125, color)
                setRange(125, 165, color2)
                pixels.show()
                time.sleep(1 / rate)
            else:
                pixels.fill(BLACK)
                pixels.show()
        for i in range(2):
            if button.value:
                setRange(0, 20, color2)
                setRange(20, 41, color)
                setRange(41, 62, color2)
                setRange(62, 83, color)
                setRange(83, 104, color2)
                setRange(104, 125, color)
                setRange(125, 146, color2)
                setRange(146, 166, color)
                pixels.show()
                time.sleep(1 / rate)
                setRange(0, 20, color)
                setRange(20, 41, color2)
                setRange(41, 62, color)
                setRange(62, 83, color2)
                setRange(83, 104, color)
                setRange(104, 125, color2)
                setRange(125, 146, color)
                setRange(146, 166, color2)
                pixels.show()
                time.sleep(1 / rate)
            else:
                pixels.fill(BLACK)
                pixels.show()
        pixels.fill(color)
        pixels.show()
        time.sleep(1)

def cycle2(length, speed):
    colorArray = []
    for i in range(round(1531*length/100)):
        i *= 100/length
        if i < 256:
            colorArray.append((255, i, 0))
        elif i >= 256 and i < 511:
            colorArray.append((255 - (i - 255), 255, 0))
        elif i >= 511 and i < 766:
            colorArray.append((0, 255, i - 510))
        elif i >= 766 and i < 1021:
            colorArray.append((0, 255 - (i - 765), 255))
        elif i >= 1021 and i < 1276:
            colorArray.append((i - 1020, 0, 255))
        elif i >= 1276 and i < 1531:
            colorArray.append((255, 0, 255 - (i - 1275)))
    while True:
        for j in range(round(1531 * length / 100)):
            for i in range(166):
                if button.value:
                    pixels[i] = colorArray[(j + i) % (len(colorArray) - 1)]
                else:
                    pixels.fill(BLACK)
                    pixels.show()
            pixels.show()
            time.sleep(1/speed/2)


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
   solid(RED)

# GUIDE:

# SNAKE: Colors travel across the LED strip
# enter a speed 0-100
# enter an array of 8 colors.

# CYCLE: Colors smoothly cycle through hues
# enter a speed 0-100.

# CYCLE2: Colors smoothly cycle through hues across the LED strip
# enter a length 1-100, or the percentage of colors used in the cycle

# SWITCH: Colors change from one color to another
# enter a switch rate
# enter a type: 'random' or 'order'
# ender an array of colors

# FLASH: LED strip flashes on and off
# enter a flash rate
# enter a type: 'random', 'single', or 'order'
# enter an array of colors. If using 'single' type, enter only one color in the array.

# DEMOGORGON: Lights flash as if there is a monster from the Upside Down nearby

# SOLID: LED strip fills with a singular color
# enter a color to be displayed

# FILLBOUNCE: Color fills the LED strip and another color oscillates in the center
# enter a primary color
# enter a secondary color
# enter a speed 0 to 100

# ALTERNATE: Color fills the LED strip and every LED flashes between the two colors
# enter a primary color
# enter a secondary color
# enter the rate of flashing

# BOUNCE: Color fills the LED strip and a group of another color bounces back and forth
# enter a primary color
# enter a secondary color
# enter a speed 0 to 100

# RANDOMFILL: Color fills the LED strip, switches to another color, and the original color randomly fills the strip
# enter a primary color
# enter a secondary color
# enter the rate of refill in LEDs per second

# RUN: Color fills the LED strip, and alternating colors travel across the LED strip
# enter a primary color
# enter a secondary color
# enter a speed 0 to 100

# ENTER: Color fills the LED strip, another color shoots outward from the middle and LED strip flashes between colors
# enter a primary color
# enter a secondary color
# enter a speed 0 to 100

# SWAP: Color fills the LED strip, and it flashes between two colors breaking into smaller segments
# enter a primary colors
# enter a secondary color
# enter a rate 0 to 100