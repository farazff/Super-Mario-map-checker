import math
from copy import deepcopy
from random import randint

from Chromosome import Chromosome


class GeneticAlgorithm:
    def __init__(self, board, numberOfChromosomes, maxPossibilityOfReusingParent=30, mutationPercentage=25):
        self.__chromosomesList = []
        self.__board = board
        self.__chromosomesLength = len(board) - 1
        self.__numberOfChromosomes = numberOfChromosomes
        self.__maxPossibilityOfReusingParent = maxPossibilityOfReusingParent
        self.__mutationPercentage = mutationPercentage

    def initializeChromosomes(self):
        for i in range(self.__numberOfChromosomes):
            self.__chromosomesList.append(
                Chromosome(length=self.__chromosomesLength, mutationPercentage=self.__mutationPercentage,
                           board=self.__board))

    def selection(self):
        numberOfParentsForReuse = math.floor(
            self.__numberOfChromosomes * (randint(0, self.__maxPossibilityOfReusingParent) / 100))
        # print("numberOfParentsForReuse  =  ", numberOfParentsForReuse)

        self.__chromosomesList.sort(key=lambda x: x.getFitnessGrade(), reverse=False)
        gradesTempDict = {}
        gradeTmp = self.__chromosomesList[0].getFitnessGrade()
        gradesTempDict[(0, gradeTmp)] = self.__chromosomesList[0]

        for chromosomeNum in range(1, self.__numberOfChromosomes):
            gradesTempDict[(gradeTmp, gradeTmp + self.__chromosomesList[chromosomeNum].getFitnessGrade())] = \
                self.__chromosomesList[chromosomeNum]
            gradeTmp += self.__chromosomesList[chromosomeNum].getFitnessGrade()

        print()
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
            selectedParents.append(deepcopy(tmp))

        # for i in selectedParents:
        #     print(i[0].getPath(), "   =   ", i[1].getPath())

        tmp = []
        for i in range(len(self.__chromosomesList) - 1, len(self.__chromosomesList) - 1 - numberOfParentsForReuse, -1):
            tmp.append(self.__chromosomesList[i])
        return selectedParents, numberOfParentsForReuse

    def printer(self):
        for i in self.__chromosomesList:
            print(i.getPath(), "  =  ", i.getFitnessGrade())

    def crossOver(self, selectedParents, numberOfParentsForReuse):
        newGeneration = []
        for i in selectedParents:
            placeToCross = randint(1, self.__chromosomesLength - 1)
            child = []
            child.extend(i[0].getPath()[0:placeToCross])
            child.extend(i[1].getPath()[placeToCross:self.__chromosomesLength])
            newChromosome = Chromosome(self.__chromosomesLength, self.__mutationPercentage, self.__board,
                                       deepcopy(child))
            newGeneration.append(newChromosome)
        self.__chromosomesList = None
        self.__chromosomesList = deepcopy(newGeneration)
        # self.printer()

    def mutationAll(self):
        for i in self.__chromosomesList:
            i.mutation()

    def getChromosomeList(self):
        return self.__chromosomesList
