from random import randint


class Chromosome:

    def __init__(self, length, *args):

        self.__mutationPercentage = 25
        self.__length = length
        self.__path = []
        self.__fitnessGrade = randint(0,10)
        if len(args) == 0:
            self.__path = self.generateRandomPath()
        else:
            self.__path = args[0]
    def getFitnessGrade(self):
        return self.__fitnessGrade

    def getPath(self):
        return self.__path

    def generateRandomPath(self) -> list:
        length = self.__length
        path = []
        for i in range(length):
            temp = randint(0, 2)
            path.append(temp)
        return path

    def mutation(self):
        path = self.__path
        doMutation = randint(0, 100)
        if doMutation >= self.__mutationPercentage:
            return
        thisIndex = randint(0, self.__length - 1)
        thisInt = int(path[thisIndex])
        while 1:
            newInt = randint(0, 2)
            if newInt != thisInt:
                break
        path[thisIndex] = newInt

    def getPath(self):
        return self.__path
