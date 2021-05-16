import math
from Chromosome import Chromosome
from random import randint


class GeneticAlgorithm:
    def __init__(self, numberOfChromosomes, maxPossibilityOfReusingParent=30):
        self.__chromosomesList = []
        self.__numberOfChromosomes = numberOfChromosomes
        self.__maxPossibilityOfReusingParent = maxPossibilityOfReusingParent

    def initializeChromosomes(self):
        for i in range(self.__numberOfChromosomes):
            self.__chromosomesList.append(Chromosome(length=self.__numberOfChromosomes))

    def selection(self):
        numberOfParentsForReuse=math.floor(self.__numberOfChromosomes*(randint(0, self.__maxPossibilityOfReusingParent)/100))
        print("numberOfParentsForReuse = ",numberOfParentsForReuse)
        self.printer()
        self.mutationAll()
        print()
        self.printer()

        self.__chromosomesList.sort(key=lambda x: x.getFitnessGrade(), reverse=False)
        # self.printer()
        gradesTempDict={}
        gradeTmp = self.__chromosomesList[0].getFitnessGrade()
        gradesTempDict[(0,gradeTmp)]=self.__chromosomesList[0]

        for chromosomeNum in range(1,self.__numberOfChromosomes):
            gradesTempDict[(gradeTmp,gradeTmp+self.__chromosomesList[chromosomeNum].getFitnessGrade())]=self.__chromosomesList[chromosomeNum]
            gradeTmp+=self.__chromosomesList[chromosomeNum].getFitnessGrade()

        for i in gradesTempDict.keys():
            print(i,"  :  ",   gradeTmp,"  ::  ",gradesTempDict[i].getPath())

        selectedParents=[]
        for i in range(self.__numberOfChromosomes-numberOfParentsForReuse):
            tmp=[]
            tmpGrade1=randint(0, gradeTmp)
            for i in gradesTempDict.keys():
                if tmpGrade1>=i[0] and tmpGrade1<=i[1]:
                    tmp.append(gradesTempDict[i])
                    break
            flg=True
            while flg:
                tmpGrade = randint(0, gradeTmp)
                for i in gradesTempDict.keys():
                    if tmpGrade >= i[0] and tmpGrade <= i[1] :
                        # if gradesTempDict[i]!=tmp[0]:
                          tmp.append(gradesTempDict[i])
                          flg=False
                          break
            selectedParents.append(tmp)




        for i in selectedParents:
            # print(i)
            print(i[0].getPath(),"   =   ",i[1].getPath())

        tmp=[]
        for i in range(len(self.__chromosomesList)-1,len(self.__chromosomesList)-1-numberOfParentsForReuse,-1):
            tmp.append( self.__chromosomesList[i])
            print(self.__chromosomesList[i].getPath(),"   -   ",self.__chromosomesList[i].getFitnessGrade())
        # print(tmp)
        self.__chromosomesList.clear()
        self.__chromosomesList=self.__chromosomesList+tmp
        self.printer()
            # print(self.__chromosomesList[i].getFitnessGrade())
        return selectedParents



    def printer(self):
        for i in self.__chromosomesList:
            print(i.getPath(),"  =  ",i.getFitnessGrade())

    def crossOver(self):
        pass



    def mutationAll(self):
        for i in self.__chromosomesList:
            i.mutation()
