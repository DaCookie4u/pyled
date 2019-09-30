class MenschAergereDichNicht:

    @staticmethod
    def get_image(leds):
        x = len(leds[0])
        y = len(leds)
        top = int((y-11) / 2)
        left = int((x-11) / 2)

        background = [32, 32, 32]
        player1 = [255, 0, 0]
        player2 = [0, 0, 225]
        player3 = [0, 127, 0]
        player4 = [192, 192, 0]
        path = [255, 255, 255]

        leds = [[background for j in range(x)] for i in range(y)]

        leds[1+top][1+left] = player1
        leds[1+top][2+left] = player1
        leds[2+top][1+left] = player1
        leds[2+top][2+left] = player1
        leds[5+top][1+left] = player1
        leds[5+top][2+left] = player1
        leds[5+top][3+left] = player1
        leds[5+top][4+left] = player1
        leds[4+top][0+left] = player1

        leds[1+top][8+left] = player2
        leds[1+top][9+left] = player2
        leds[2+top][8+left] = player2
        leds[2+top][9+left] = player2
        leds[1+top][5+left] = player2
        leds[2+top][5+left] = player2
        leds[3+top][5+left] = player2
        leds[4+top][5+left] = player2
        leds[0+top][6+left] = player2

        leds[8+top][8+left] = player3
        leds[8+top][9+left] = player3
        leds[9+top][8+left] = player3
        leds[9+top][9+left] = player3
        leds[5+top][6+left] = player3
        leds[5+top][7+left] = player3
        leds[5+top][8+left] = player3
        leds[5+top][9+left] = player3
        leds[6+top][10+left] = player3

        leds[8+top][1+left] = player4
        leds[8+top][2+left] = player4
        leds[9+top][1+left] = player4
        leds[9+top][2+left] = player4
        leds[6+top][5+left] = player4
        leds[7+top][5+left] = player4
        leds[8+top][5+left] = player4
        leds[9+top][5+left] = player4
        leds[10+top][4+left] = player4

        leds[4+top][1+left] = path
        leds[4+top][2+left] = path
        leds[4+top][3+left] = path
        leds[4+top][4+left] = path
        leds[3+top][4+left] = path
        leds[2+top][4+left] = path
        leds[1+top][4+left] = path
        leds[0+top][4+left] = path
        leds[0+top][5+left] = path
        leds[1+top][6+left] = path
        leds[2+top][6+left] = path
        leds[3+top][6+left] = path
        leds[4+top][6+left] = path
        leds[4+top][7+left] = path
        leds[4+top][8+left] = path
        leds[4+top][9+left] = path
        leds[4+top][10+left] = path
        leds[5+top][10+left] = path
        leds[6+top][9+left] = path
        leds[6+top][8+left] = path
        leds[6+top][7+left] = path
        leds[6+top][6+left] = path
        leds[7+top][6+left] = path
        leds[8+top][6+left] = path
        leds[9+top][6+left] = path
        leds[10+top][6+left] = path
        leds[10+top][5+left] = path
        leds[9+top][4+left] = path
        leds[8+top][4+left] = path
        leds[7+top][4+left] = path
        leds[6+top][4+left] = path
        leds[6+top][3+left] = path
        leds[6+top][2+left] = path
        leds[6+top][1+left] = path
        leds[6+top][0+left] = path
        leds[5+top][0+left] = path

        return leds
