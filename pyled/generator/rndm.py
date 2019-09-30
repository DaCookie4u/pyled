import random
import time


class Rndm:

    def __init__(self):
        self._nextrefresh = 0

    def get_image(self, leds):
        if time.time() < self._nextrefresh:
            return leds

        for y in range(len(leds)):
            for x in range(len(leds[0])):
                leds[y][x] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

        self._nextrefresh = time.time() + 0.5
        return leds
