import math
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


def main():
    chromosomeCount = 200
    file = open("levels/level5.txt", 'r')
    input = list(file.read())
    # in board -> 0: default    1: mushroom   2: on ground obstacle   3: in sky obstacle
    for i in range(len(input)):
        if input[i] == "_":
            input[i] = 0
        elif input[i] == "M":
            input[i] = 1
        elif input[i] == "G":
            input[i] = 2
        elif input[i] == "L":
            input[i] = 3
    board = input
    chromosome = Chromosome(11, 10, board, [0,0,1,0,0,0,2,0,0,1,0])
    print(chromosome.getFitnessGrade() - 30)

    geneticAlgorithm = GeneticAlgorithm(board, chromosomeCount)
    geneticAlgorithm.initializeChromosomes()

    geneticAlgorithm.printer()
    print(end="\n\n")

    lastAvg = calculateAvg(chromosomeCount, geneticAlgorithm)

    while True:
        a, b = geneticAlgorithm.selection()
        geneticAlgorithm.crossOver(a, b)
        geneticAlgorithm.printer()
        newAvg = calculateAvg(chromosomeCount, geneticAlgorithm)
        print(lastAvg, "  ", newAvg, "  ", abs(lastAvg - newAvg))
        if math.isclose(lastAvg, newAvg):
            break
        lastAvg = deepcopy(newAvg)
        print(end="\n\n")


if __name__ == "__main__":
    main()
