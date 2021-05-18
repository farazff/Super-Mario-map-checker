import math
from copy import deepcopy
from random import randint

from Chromosome import Chromosome


class GeneticAlgorithm:
    def __init__(self, board, numberOfChromosomes, maxPossibilityOfReusingParent=30, mutationPercentage=10):
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
            self.__chromosomesList[0].getFitnessGrade()
            tmpGrade1 = randint(self.__chromosomesList[0].getFitnessGrade(), gradeTmp)
            for j in gradesTempDict.keys():
                if j[0] <= tmpGrade1 <= j[1]:
                    tmp.append(gradesTempDict[j])
                    break
            flg = True
            while flg:
                tmpGrade = randint(self.__chromosomesList[0].getFitnessGrade(), gradeTmp)
                for k in gradesTempDict.keys():
                    if k[0] <= tmpGrade <= k[1]:
                        if gradesTempDict[k] != tmp[0]:
                            tmp.append(gradesTempDict[k])
                            flg = False
                            break
            selectedParents.append(deepcopy(tmp))

        tmp = []
        for i in range(len(self.__chromosomesList) - 1, len(self.__chromosomesList) - 1 - numberOfParentsForReuse, -1):
            tmp.append(self.__chromosomesList[i])
        return selectedParents, numberOfParentsForReuse

    def printer(self):
        for i in self.__chromosomesList:
            print(i.getPath(), "  =  ", i.getFitnessGrade() - 30)

    def crossOver(self, selectedParents, numberOfParentsForReuse):
        newGeneration = []
        for i in selectedParents:
            while True:
                placeToCross = randint(1, self.__chromosomesLength - 1)
                child = []
                if i[0].getPath()[placeToCross - 1] == 1:
                    if i[1].getPath()[placeToCross] == 1 or i[1].getPath()[placeToCross] == 2:
                        continue
                if i[0].getPath()[placeToCross - 1] == 2:
                    if i[1].getPath()[placeToCross] == 1:
                        continue

                child.extend(i[0].getPath()[0:placeToCross])
                child.extend(i[1].getPath()[placeToCross:self.__chromosomesLength])
                newChromosome = Chromosome(self.__chromosomesLength, self.__mutationPercentage, self.__board,
                                           deepcopy(child))
                newGeneration.append(newChromosome)
                break
        newGeneration.sort(key=lambda x: x.getFitnessGrade(), reverse=False)
        self.__chromosomesList.sort(key=lambda x: x.getFitnessGrade(), reverse=False)
        for i in range(numberOfParentsForReuse):
            newGeneration[i] = deepcopy(self.__chromosomesList[-1 - i])
        self.__chromosomesList = None
        self.__chromosomesList = deepcopy(newGeneration)

    def mutationAll(self):
        for i in self.__chromosomesList:
            i.mutation()

    def getChromosomeList(self):
        return self.__chromosomesList
