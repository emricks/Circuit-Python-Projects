import asyncio
import math

RED = (255, 0, 0)
BLACK = (0, 0, 0)

async def blink_fill(pixels, spec: dict):
    pixels.fill(spec["color"])
    pixels.show()
    await asyncio.sleep(spec["speed"])
    pixels.fill(BLACK)
    pixels.show()
    await asyncio.sleep(spec["speed"])

async def solid_fill(pixels, spec: dict):
    pixels.fill(spec["color"])
    pixels.show()

async def blank(pixels):
    pixels.fill(BLACK)
    pixels.show()

async def slayer(pixels, spec: dict):
    print(spec["xpcurrent"]/spec["xpgoal"])
    num = 166*spec["xpcurrent"]/spec["xpgoal"]
    darkcolor = [math.floor(spec["color"][0] / 50), math.floor(spec["color"][1] / 50), math.floor(spec["color"][2] / 50)]
    print(spec["color"])
    for i in range(166):
        if i > 166-num:
            pixels[i] = spec["color"]
        else:
            pixels[i] = darkcolor
    if spec["xpcurrent"]==spec["xpgoal"]:
        pixels.fill([255, 255, 255])




    #for i in range(166):
     #   if pixels[i] != spec["color"]:
      #      pixels[i] = darkcolor
    pixels.show()