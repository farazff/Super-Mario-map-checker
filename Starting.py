from copy import deepcopy

from GeneticAlgorithm import GeneticAlgorithm
from GuiHandler import GuiHandler


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
    for i in range(len(averages) - 25, len(averages) - 1):
        if i >= 0 and averages[i] != flag:
            return False
    return True


def start(population, lvlNum, mutationPercentage, maxPossOfReusing):
    x = [0]
    y = []
    chromosomeCount = population
    filePath = "levels/level" + str(lvlNum) + ".txt"
    file = open(filePath, 'r')
    inoutFile = list(file.read())
    guiHandler = GuiHandler(map=deepcopy(inoutFile))
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

    geneticAlgorithm = GeneticAlgorithm(board, chromosomeCount, mutationPercentage, maxPossOfReusing)
    geneticAlgorithm.initializeChromosomes()

    geneticAlgorithm.printer()
    print(end="\n\n")

    Avg = calculateAvg(chromosomeCount, geneticAlgorithm)
    y.append(Avg)
    averages = [deepcopy(Avg)]

    count = int(0)
    while True:
        a, b = geneticAlgorithm.selection()
        geneticAlgorithm.crossOver(a, b)
        geneticAlgorithm.printer()
        Avg = calculateAvg(chromosomeCount, geneticAlgorithm)
        averages.append(deepcopy(Avg))
        print(Avg)
        count = count + 1
        x.append(count)
        y.append(Avg)
        if checkDone(averages):
            guiHandler.mapDisplay(
                geneticAlgorithm.getChromosomeList()[len(geneticAlgorithm.getChromosomeList()) - 1].getPath())

            break
        print(end="\n\n")

    # plt.style.use("dark_background")
    # plt.xlabel('Generation')
    # plt.ylabel('Average')
    # plt.title('Population = 500')
    # plt.plot(x, y)
    # plt.show()
