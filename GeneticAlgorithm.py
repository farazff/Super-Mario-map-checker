import math
from random import randint

from Chromosome import Chromosome


class GeneticAlgorithm:
    def __init__(self, numberOfChromosomes, maxPossibilityOfReusingParent=30, mutationPercentage=25):
        self.__chromosomesList = []
        self.__numberOfChromosomes = numberOfChromosomes
        self.__maxPossibilityOfReusingParent = maxPossibilityOfReusingParent
        self.__mutationPercentage = mutationPercentage

    def initializeChromosomes(self):
        for i in range(self.__numberOfChromosomes):
            self.__chromosomesList.append(
                Chromosome(length=self.__numberOfChromosomes, mutationPercentage=self.__mutationPercentage))

    def selection(self):
        numberOfParentsForReuse = math.floor(
            self.__numberOfChromosomes * (randint(0, self.__maxPossibilityOfReusingParent) / 100))
        print("numberOfParentsForReuse  =  ", numberOfParentsForReuse)

        self.__chromosomesList.sort(key=lambda x: x.getFitnessGrade(), reverse=False)
        gradesTempDict = {}
        gradeTmp = self.__chromosomesList[0].getFitnessGrade()
        gradesTempDict[(0, gradeTmp)] = self.__chromosomesList[0]

        for chromosomeNum in range(1, self.__numberOfChromosomes):
            gradesTempDict[(gradeTmp, gradeTmp + self.__chromosomesList[chromosomeNum].getFitnessGrade())] = \
                self.__chromosomesList[chromosomeNum]
            gradeTmp += self.__chromosomesList[chromosomeNum].getFitnessGrade()

        selectedParents = []
        for i in range(self.__numberOfChromosomes):
            tmp = []
            tmpGrade1 = randint(0, gradeTmp)
            for j in gradesTempDict.keys():
                if j[0] <= tmpGrade1 <= j[1]:
                    tmp.append(gradesTempDict[j])
                    break
            flg = True
            while flg:
                tmpGrade = randint(0, gradeTmp)
                for k in gradesTempDict.keys():
                    if k[0] <= tmpGrade <= k[1]:
                        tmp.append(gradesTempDict[k])
                        flg = False
                        break
            selectedParents.append(tmp)

        for i in selectedParents:
            print(i[0].getPath(), "   =   ", i[1].getPath())

        tmp = []
        for i in range(len(self.__chromosomesList) - 1, len(self.__chromosomesList) - 1 - numberOfParentsForReuse, -1):
            tmp.append(self.__chromosomesList[i])
        self.printer()
        return selectedParents, numberOfParentsForReuse

    def printer(self):
        for i in self.__chromosomesList:
            print(i.getPath(), "  =  ", i.getFitnessGrade())

    def crossOver(self):
        pass

    def mutationAll(self):
        for i in self.__chromosomesList:
            i.mutation()
