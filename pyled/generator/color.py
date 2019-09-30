class Color:

    def __init__(self):
        self._color = [0, 192, 0]

    def get_image(self, leds):
        width = len(leds[0])
        height = len(leds)
        leds = [[self._color for j in range(width)] for i in range(height)]
        return leds

    def set_color(self, rgb):
        if len(rgb) == 3:
            r = int(rgb[0])
            g = int(rgb[1])
            b = int(rgb[2])
            if r in range(256) and g in range(256) and g in range(256):
                self._color = [r, g, b]
                return True
        else:
            return False
