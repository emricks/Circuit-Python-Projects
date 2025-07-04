import board
import neopixel
import time

pixel_pin = board.D10
num_pixels = 166

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=.3, auto_write=False)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

def main():
    while True:
        pixels.fill(RED)
        pixels.show()
        print("red")
        time.sleep(0.5)
        pixels.fill(BLUE)
        pixels.show()
        print("blue")
        time.sleep(0.5)
        pixels.fill(WHITE)
        pixels.show()
        print("white")
        time.sleep(0.5)

if __name__ == "__main__":
    main()