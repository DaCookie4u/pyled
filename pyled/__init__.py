import threading
import time
import logging
import inspect
from . import generator
from . import driver


class PyLED(threading.Thread):

    def __init__(self, drv):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()
        self.driver = drv
        self.daemon = True
        self._maxfps = 24
        self._generator = generator.Black()

    def _stopped(self):
        return self._stop_event.is_set()

    def run(self):
        while not self._stopped():
            self.driver.leds = self._generator.get_image(self.driver.leds)
            self.driver.display_image()
            time.sleep(1.0/self._maxfps)

    def stop(self):
        self._stop_event.set()

    def get_generator_options(self):
        options = []
        for name, obj in inspect.getmembers(self._generator, inspect.ismethod):
            if name.startswith('set_'):
                options.append(name[4:])
        return options

    def set_generator_option(self, option, args):
        methodname = 'set_%s' % option
        method = getattr(self._generator, methodname)
        try:
            return method(args.split())
        except:
            return False

    def set_generator(self, g):
        if g in generator.get_generators():
            logging.info('Changing generator to ' + g)
            generator_class = getattr(generator, g)
            self._generator = generator_class()
            return True
        else:
            return False

    def set_brightness(self, v):
        return self.driver.set_brightness(v)

    def set_max_fps(self, v):
        self._maxfps = int(v)
        return True
