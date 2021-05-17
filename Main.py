from Chromosome import Chromosome


def listToString(s):
    LTS = ""
    for ele in s:
        LTS += str(ele)
        LTS += " "
    return LTS


def main():
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    chromosome = Chromosome(12, 100, board)
    chromosome.setPath([0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
    print(listToString(chromosome.getPath()))
    chromosome.fitnessFunction()
    # chromosome.mutation()
    # print(listToString(chromosome.getPath()))

    # geneticAlgorithm =GeneticAlgorithm(numberOfChromosomes=10)
    # geneticAlgorithm.initializeChromosomes()
    #
    # geneticAlgorithm.selection()


if __name__ == "__main__":
    main()
