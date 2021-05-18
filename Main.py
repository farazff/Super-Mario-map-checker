from copy import deepcopy
from GeneticAlgorithm import GeneticAlgorithm
from Chromosome import Chromosome


def listToString(s):
    LTS = ""
    for ele in s:
        LTS += str(ele)
        LTS += " "
    return LTS


def calculateAvg(chromosomeCount, geneticAlgorithm) -> float:
    avg = float(0.0)
    for i in range(chromosomeCount):
        avg = avg + geneticAlgorithm.getChromosomeList()[i].getFitnessGrade()
    return avg / chromosomeCount


def checkDone(averages):
    flag = averages[-1]
    for i in range(len(averages) - 50, len(averages) - 1):
        if i >= 0 and averages[i] != flag:
            return False
    return True


def main():
    chromosomeCount = 200
    file = open("levels/level1.txt", 'r')
    inoutFile = list(file.read())
    # in board -> 0: default    1: mushroom   2: on ground obstacle   3: in sky obstacle
    for i in range(len(inoutFile)):
        if inoutFile[i] == "_":
            inoutFile[i] = 0
        elif inoutFile[i] == "M":
            inoutFile[i] = 1
        elif inoutFile[i] == "G":
            inoutFile[i] = 2
        elif inoutFile[i] == "L":
            inoutFile[i] = 3
    inoutFile.append(0)
    board = inoutFile

    geneticAlgorithm = GeneticAlgorithm(board, chromosomeCount)
    geneticAlgorithm.initializeChromosomes()

    geneticAlgorithm.printer()
    print(end="\n\n")

    Avg = calculateAvg(chromosomeCount, geneticAlgorithm)
    averages = [deepcopy(Avg)]

    while True:
        a, b = geneticAlgorithm.selection()
        geneticAlgorithm.crossOver(a, b)
        geneticAlgorithm.printer()
        Avg = calculateAvg(chromosomeCount, geneticAlgorithm)
        averages.append(deepcopy(Avg))
        print(Avg)
        if checkDone(averages):
            break
        print(end="\n\n")


if __name__ == "__main__":
    main()
