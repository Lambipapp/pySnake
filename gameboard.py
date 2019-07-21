import random

class gameboard:

    gb = []
    size = (0, 0)

    def __init__(self, width, height):
        self.size = (width, height)
        
        for y in range(height):
            row = []
            for x in range(width):
                row.append(0)
            self.gb.append(row)
        #self.setCellVal(1, 5, 1)
        #print(self.gb)

    def setCellVal(self, xPos, yPos, val):
        self.gb[yPos][xPos] = val

    def getCellVal(self, xPos, yPos):
        return self.gb[yPos][xPos]

    def spawnApple(self):
        noApple = True
        while noApple:
            x = random.randrange(self.size[0])
            y = random.randrange(self.size[1])

            if self.getCellVal(x, y) == 0:
                self.setCellVal(x, y, 2)
                noApple = False
        pass