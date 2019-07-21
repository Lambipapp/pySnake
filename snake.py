import random
import gameboard

class snake:
    #headPos = (0, 0)
    moveDir = (0, 1)   # (1,0) = right    (-1,0) = left    (0,1) = down   (0,-1) = up
    poses = []
    gbsize = (0, 0)
    

    def __init__(self, gb, gbsize):
        self.gbsize = gbsize
        self.poses.append((5, 5)) # places head on 5, 5
        gb.setCellVal(self.poses[0][0], self.poses[0][1], 1)
        gb.spawnApple()
        

    def move(self, gb):
        headPos = self.poses[-1]
        newPos = (headPos[0] + self.moveDir[0], headPos[1] + self.moveDir[1])

        if newPos[0] < 0 or newPos[1] < 0 or newPos[0] >= self.gbsize[0] or newPos[1] >= self.gbsize[1]:
            print("DEAD: Hit Wall")
            return -1

        if gb.getCellVal(newPos[0], newPos[1]) == 1 and newPos != self.poses[0]:
            print("DEAD: Hit tail")
            return -1

        elif gb.getCellVal(newPos[0], newPos[1]) == 2:
            self.poses.append(newPos)
            gb.setCellVal(newPos[0], newPos[1], 1)
            gb.setCellVal(self.poses[0][0], self.poses[0][1], 0)
            gb.spawnApple()
        
        elif gb.getCellVal(newPos[0], newPos[1]) == 0:
            self.poses.append(newPos)
            gb.setCellVal(newPos[0], newPos[1], 1)
            gb.setCellVal(self.poses[0][0], self.poses[0][1], 0)
            self.poses.pop(0)

    def setDirection(self, newDir):
        self.moveDir = newDir
        
    def getDirection(self):
        return self.moveDir
    #def move(self, gb):
        #if self.moveDir == (1, 0) or self.moveDir == (-1, 0) or self.moveDir == (0, 1) or self.moveDir == (0, -1): 

            #newRow = self.headPos[0] + self.moveDir[1]
            #newCollum = self.headPos[1] + self.moveDir[0]
            #print(self.headPos[0], self.headPos[1], newRow, newCollum)



            #if newRow < 0 or newRow >= self.rows or newCollum < 0 or newCollum >= self.collums:
                #print("DEAD SNAKE")
                #return -1

            #if gb[newRow][newCollum] == 0: #move head and pop tail
                #self.headPos = (newRow, newCollum)
                #self.poses.append(self.headPos)
                #self.switchPixel(gb, self.poses[0][0], self.poses[0][1], 0)
                #self.switchPixel(gb, newRow, newCollum, 1)

                #gb[self.headPos[0]][self.headPos[1]] = 1
                #gb[self.poses[0][0]][self.poses[0][1]] = 0
                #self.poses.pop(0)

            
        #else:
            #print("moveDir is wrong:", self.moveDir)
            #return -1

    
    #def switchPixel(self, gb, row, collum, value):
        #gb[row][collum] = 1

    

        