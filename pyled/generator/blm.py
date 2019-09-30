import random
import time
import os


class Blm:

    def __init__(self):
        self._file = random.choice(os.listdir("resources/blm"))
        self._nextframe = 0
        self._seek = 0

    def get_image(self, leds):
        # skip if frame is not supposed to change yet
        if time.time() < self._nextframe:
            return leds

        width = len(leds[0])
        height = len(leds)

        # Flush screen
        leds = [[[0, 0, 0] for j in range(width)] for i in range(height)]

        # Start animation
        framepause = 0
        y = 0
        done = True
        with open('resources/blm/' + self._file, 'r') as f:
            for i in range(self._seek):
                next(f)

            for line in f:
                self._seek += 1
                x = 0
                if line.startswith('#'):
                    continue
                elif y > height:
                    continue
                elif line.startswith('@'):
                    framepause = float(line[1:].strip())
                elif line.strip() == '' and y > 0:
                    break
                elif line.strip() == '':
                    continue
                else:
                    done = False
                    for b in line.rstrip():
                        if x >= width:
                            continue
                        if int(b) == 1:
                            leds[y][x] = [255, 255, 255]
                        else:
                            leds[y][x] = [0, 0, 0]
                        x += 1
                    y += 1

            # If no lines where processed, reset animation
            if done:
                self._file = random.choice(os.listdir("resources/blm"))
                self._seek = 0

        f.close()
        self._nextframe = time.time() + framepause/1000.0
        return leds
