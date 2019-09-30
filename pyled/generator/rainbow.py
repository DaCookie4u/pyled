import colorsys
import math


class Rainbow:

    def __init__(self):
        self._step = 0
        self._steps = 360

    def _to_rad(self, deg):
        return deg * (math.pi / 180)

    def get_image(self, leds):
        width = len(leds[0])
        height = len(leds)

        self._step = (self._step + 1) % self._steps

        y_hue_delta = (math.sin(self._to_rad(self._step)) * (350/14)) % 255
        x_hue_delta = (math.cos(self._to_rad(self._step)) * (310/14)) % 255

        line_start_hue = self._step
        for y in range(height):
            line_start_hue += y_hue_delta
            pixel_hue = line_start_hue
            for x in range(width):
                pixel_hue += x_hue_delta
                rgb = colorsys.hsv_to_rgb(pixel_hue/255.0, 1, 1)
                leds[y][x] = [int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255)]

        # if self._step < self._steps:
        #     self._step += 1
        # else:
        #     self._step = 0

        return leds
