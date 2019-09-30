class Driver:

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.leds = [[[0, 0, 0] for j in range(self._width)] for i in range(self._height)]
        self._brightness = 255

    # This will return the RGB values of the Pixel at XY, with brightness
    # already applied
    def get_pixel(self, x, y):
        r = int(self.leds[y][x][0] * self._brightness / 255)
        g = int(self.leds[y][x][1] * self._brightness / 255)
        b = int(self.leds[y][x][2] * self._brightness / 255)
        return r, g, b

    # Get the current brightness
    def get_brightness(self):
        return self._brightness

    # Set the brightness to value v
    def set_brightness(self, v):
        value = int(v)
        if value in range(256):
            self._brightness = value
            return True
        else:
            return False
