from random import randint


class Chromosome:

    def __init__(self, length, mutationPercentage, board, *args):

        self.__mutationPercentage = mutationPercentage
        self.__length = length
        self.__path = []
        self.__board = board
        if len(args) == 0:
            self.__path = self.generateRandomPath()
        else:
            self.__path = args[0]
        self.__fitnessGrade = self.fitnessFunction()

    def getFitnessGrade(self):
        return self.__fitnessGrade

    def getPath(self):
        return self.__path

    def setPath(self, path):
        self.__path = path

    def generateRandomPath(self) -> list:
        length = self.__length
        path = []
        while len(path) < length:
            temp = randint(0, 2)
            path.append(temp)
            if temp == 1:
                path.append(0)
            if temp == 2:
                temp2 = randint(0, 1)
                if temp2 == 1:
                    temp2 = 2
                path.append(temp2)
        if len(path) >= length:
            path = path[0: length]
        return path

    def mutation(self):
        path = self.__path
        doMutation = randint(0, 100)
        if doMutation >= self.__mutationPercentage:
            return
        thisIndex = randint(0, self.__length - 1)
        path[thisIndex] = 0

    # in board 0: default    1: mushroom   2: on ground obstacle   3: in sky obstacle
    def fitnessFunction(self):
        board = self.__board
        path = self.__path
        inSky = False
        loc = int(0)
        maxPathLen = int(0)
        score = int(30)

        for i in range(self.__length):
            if path[i] == 0:
                if inSky is True and board[i + 1] == 2:
                    score = score + 2
                if board[i + 1] == 0 or board[i + 1] == 1 or (board[i + 1] == 2 and inSky is True):
                    maxPathLen = maxPathLen + 1
                else:
                    maxPathLen = 0
                inSky = False

            if path[i] == 1:
                if board[i + 1] != 3:
                    maxPathLen = maxPathLen + 1
                else:
                    maxPathLen = 0
                inSky = True
                score = score - 1

            if path[i] == 2:
                if board[i + 1] != 2:
                    maxPathLen = maxPathLen + 1
                else:
                    maxPathLen = 0
                score = score - 1

            loc = loc + 1
            if board[loc] == 1 and not inSky:
                score = score + 2

        score = score + maxPathLen
        if maxPathLen == self.__length:
            score = score + 5
        if path[self.__length - 1] == 1:
            score += 2
        return score
