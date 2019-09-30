import sys
import inspect

from .blm import Blm
from .chessboard import ChessBoard
from .color import Color
from .menschaergeredichnicht import MenschAergereDichNicht
from .plasma import Plasma
from .rainbow import Rainbow
from .rndm import Rndm
from .scrollingtext import ScrollingText


def get_generators():
    generators = []
    for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        generators.append(name)
    return generators


class Black:

    @staticmethod
    def get_image(leds):
        leds = [[[0, 0, 0] for j in range(len(leds[0]))] for i in range(len(leds))]
        return leds
