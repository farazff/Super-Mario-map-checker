from Chromosome import Chromosome


def listToString(s):
    LTS = ""
    for ele in s:
        LTS += str(ele)
        LTS += " "
    return LTS


def main():
    chromosome = Chromosome(12)
    print(listToString(chromosome.getPath()))
    chromosome.mutation()
    print(listToString(chromosome.getPath()))


if __name__ == "__main__":
    main()
