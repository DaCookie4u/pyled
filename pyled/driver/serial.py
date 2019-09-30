from .driver import Driver


class Serial(Driver):

    def __init__(self, width, height, mode, serial):
        Driver.__init__(self, width, height)
        self._mode = mode
        self._tty = serial

    # Main Method to display the image. Serial will send a chr(1) as a reset
    # character, and after that 3 bytes(G, R, and B) for each pixel
    # The order of the pixels depends on the mode selected.
    #   HS_TR:  Horizontal Snake, starting Top Right
    def display_image(self):
        # reset frame on arduino
        self._tty.write(chr(1))

        # Horizontal Snake, starting Top Right
        if self._mode == 'HS_TR':
            for led in range(self._width * self._height):
                y = led // self._width   # row is led div number of columns
                x = led % self._width    # column is led modulo number of columns
                if y % 2 == 0:           # column run reverse on even rows
                    x = self._width - x - 1
                # Write triple to serial, but do not send chr(1), instead send chr(2)
                (r, g, b) = self.get_pixel(x, y)
                self._tty.write(chr(2 if g == 1 else g))
                self._tty.write(chr(2 if r == 1 else r))
                self._tty.write(chr(2 if b == 1 else b))

        # wait until all data is sent
        while self._tty.out_waiting > 0:
            pass
