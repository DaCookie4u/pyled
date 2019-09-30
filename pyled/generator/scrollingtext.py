import time
from PIL import Image, ImageFont, ImageDraw


class ScrollingText:

    def __init__(self):
        self._text = 'Hey Dude!'
        self._speed = 1.0/10
        self._nextrefresh = 0
        self._fontsize = 12
        self._step = 0
        self._started = False

    def get_image(self, leds):
        if time.time() < self._nextrefresh:
            return leds

        width = len(leds[0])
        height = len(leds)

        img = Image.new('RGB', (width, height), (0, 0, 0))
        font = ImageFont.truetype("resources/fonts/CourierNew.ttf", 12)
        draw = ImageDraw.Draw(img)
        draw.text((width-self._step, 0), self._text, (255, 255, 255), font=font)

        done = True
        for y in range(height):
            for x in range(width):
                (r, g, b) = img.getpixel((x, y))
                if [r, g, b] != [0, 0, 0] and self._started:
                    done = False
                elif [r, g, b] != [0, 0, 0]:
                    self._started = True
                elif not self._started:
                    done = False
                leds[y][x] = [r, g, b]

        if done:
            self._step = 0
            self._started = False
        else:
            self._step += 1

        self._nextrefresh = time.time() + self._speed
        return leds
