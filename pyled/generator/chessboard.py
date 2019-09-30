class ChessBoard:

    @staticmethod
    def get_image(leds):
        height = len(leds)
        width = len(leds[0])
        leds = [[[184, 134, 11] for j in range(width)] for i in range(height)]
        top = int((height-8) / 2)
        left = int((width-8) / 2)
        white = True
        for y in range(8):
            white = not white
            for x in range(8):
                white = not white
                if white:
                    leds[y+top][x+left] = [255, 255, 255]
                else:
                    leds[y+top][x+left] = [0, 0, 0]
        return leds
