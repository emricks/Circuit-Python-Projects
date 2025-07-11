import asyncio
import json
import time

import board
import neopixel
import os
import wifi

from asyncio import sleep as async_sleep
from asyncio import run, gather, create_task

from adafruit_httpserver import POST, OPTIONS, Request, Server, Response, Headers
import animate_functions
import socketpool

hostname = "leds1"
http_port = 80
animation = "none"
animation_spec = {}

######################
#### system setup ####
######################

#set up HTTP server
# First, connect to wifi. Be sure to create a settings.toml file on the device's
# filesystem by hand to set WIFI_SSID and WIFI_PASSWORD
ssid=os.getenv('WIFI_SSID')
print("Connecting to wifi %s" % ssid)

connected = False
while not connected:
    try:
        if wifi.radio.connect(ssid=ssid,password=os.getenv('WIFI_PASSWORD')) is None:
            connected = True
    except:
        print("Failed to connect to wifi, retrying")
        time.sleep(1)

print("my IP addr:", wifi.radio.ipv4_address)

## now set up HTTP server
pool = socketpool.SocketPool(wifi.radio)

## default path for static files is /html
server = Server(pool, "/html", debug=True)
server.headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "*",
    "Access-Control-Allow-Headers": "*",
}

## set up neopixel
pixel_pin = board.GP10
num_pixels = int(os.getenv('NUM_PIXELS'))
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

########################
#### main functions ####
########################

# Run forever polling for work and handling it
async def run_webserver():
    while True:
        # Process any waiting requests
        server.poll()
        await async_sleep(0)

# Triggers when HTTP request to change led animate comes in
@server.route("/leds/animate/<animation_name>", POST)
def pattern(request: Request, animation_name: str):
    global animation, animation_spec
    animation = animation_name
    print("request body: %s" % request.body)
    animation_spec = json.loads(request.body)
    print("animation spec: %s" % animation_spec)

@server.route("/leds/....", OPTIONS)
def options(request: Request):
    return Response(request, "Allowed methods: OPTIONS, GET, POST", content_type="application/json", headers=Headers({"Allow": "OPTIONS, GET, POST"}))

# Run currently chosen LED animation, looping forever
async def run_animate():
    while True:
        if animation == "none":
            await animate_functions.blank(pixels)
        elif animation == "blink_fill":
            await animate_functions.blink_fill(pixels, animation_spec)
        await asyncio.sleep(0)

# launch both the animation and the web server, async
async def main():
    server.start(str(wifi.radio.ipv4_address), port=http_port)
    await gather(
        create_task(run_animate()),
        create_task(run_webserver()),
    )

if __name__ == "__main__":
   run(main())