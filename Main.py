from Chromosome import Chromosome
from GeneticAlgorithm import GeneticAlgorithm


def listToString(s):
    LTS = ""
    for ele in s:
        LTS += str(ele)
        LTS += " "
    return LTS


def main():
    # chromosome = Chromosome(12)
    # print(listToString(chromosome.getPath()))
    # chromosome.mutation()
    # print(listToString(chromosome.getPath()))
    geneticAlgorithm =GeneticAlgorithm(numberOfChromosomes=10)
    geneticAlgorithm.initializeChromosomes()

    geneticAlgorithm.selection()



if __name__ == "__main__":
    main()
