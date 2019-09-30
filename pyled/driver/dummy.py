from .driver import Driver


class Dummy(Driver):

    # Main Method to display the image.
    def display_image(self):
        # pass
        f = open('dummy.txt', 'w')
        for y in range(self._height):
            line = ''
            for x in range(self._width):
                (r, g, b) = self.get_pixel(x, y)
                line += '\033[48;2;%d;%d;%d;249m \033[0;0m' % (r, g, b)
            f.write(line + '\n')
        f.close()
