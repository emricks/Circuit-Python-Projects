import time
import board
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

if __name__ == "__main__":
    main()