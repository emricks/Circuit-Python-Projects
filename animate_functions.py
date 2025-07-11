import asyncio

RED = (255, 0, 0)
BLACK = (0, 0, 0)

async def blink_fill(pixels, spec: dict):
    pixels.fill(spec["color"])
    pixels.show()
    await asyncio.sleep(spec["speed"])
    pixels.fill(BLACK)
    pixels.show()
    await asyncio.sleep(spec["speed"])

async def blank(pixels):
    pixels.fill(BLACK)
    pixels.show()