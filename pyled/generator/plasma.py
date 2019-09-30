import math


class Plasma:

    def __init__(self):
        self._plasma_step_width = 1
        self._plasma_cell_size_x = 3
        self._plasma_cell_size_y = 3
        self._plasma_counter = 0.0
        self._generate_plasma_lut()

    def _generate_plasma_lut(self):
        self._plasma_lut = [[0, 0, 0] for i in range(1536)]
        for i in range(256):
            self._plasma_lut[(i + 0)][0] = 152
            self._plasma_lut[(i + 0)][1] = i
            self._plasma_lut[(i + 0)][2] = 0

        for i in range(256):
            self._plasma_lut[(i + 256)][0] = (255 - i)
            self._plasma_lut[(i + 256)][1] = 152
            self._plasma_lut[(i + 256)][2] = 0

        for i in range(256):
            self._plasma_lut[(i + 512)][0] = 0
            self._plasma_lut[(i + 512)][1] = 152
            self._plasma_lut[(i + 512)][2] = i

        for i in range(256):
            self._plasma_lut[(i + 768)][0] = 0
            self._plasma_lut[(i + 768)][1] = (255 - i)
            self._plasma_lut[(i + 768)][2] = 152

        for i in range(256):
            self._plasma_lut[(i + 1024)][0] = i
            self._plasma_lut[(i + 1024)][1] = 0
            self._plasma_lut[(i + 1024)][2] = 152

        for i in range(256):
            self._plasma_lut[(i + 1280)][0] = 152
            self._plasma_lut[(i + 1280)][1] = 0
            self._plasma_lut[(i + 1280)][2] = (255 - i)

    def get_image(self, leds):
        width = len(leds[0])
        height = len(leds)
        self._plasma_counter += self._plasma_step_width / 10.0

        calc1 = math.sin(self._plasma_counter * 0.006)
        calc2 = math.sin(self._plasma_counter * -0.06)

        xc = 25.0

        for x in range(width):
            xc += self._plasma_cell_size_x / 10.0
            yc = 25.0
            s1 = 768.0 + 768.0 * math.sin(xc) * calc1
            for y in range(height):
                yc += self._plasma_cell_size_y / 10.0

                s2 = 768.0 + 768.0 * math.sin(yc) * calc2
                s3 = 768.0 + 768.0 * math.sin((xc + yc + self._plasma_counter / 10.0) / 2.0)

                pixel = int((s1 + s2 + s3) / 3.0)

                r = self._plasma_lut[pixel][0]
                g = self._plasma_lut[pixel][1]
                b = self._plasma_lut[pixel][2]

                leds[y][x] = [r, g, b]

        return leds
