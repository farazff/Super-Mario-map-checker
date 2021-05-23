import pygame, random,math

class GuiHandler():
    def __init__(self, map):
        self.__mario = pygame.image.load("./images/mario2.png")
        self.__mario2 = pygame.image.load("./images/mario2.png")
        self.__jumpingMario = pygame.image.load("./images/marioJumping.png")
        self.__wallpaper = pygame.image.load("./images/wallpaper6.jpg")
        self.__sittingMario = pygame.image.load("./images/sittingMario.png")
        self.__winnerMario = pygame.image.load("./images/winnerMario.png")
        self.__block = pygame.image.load("./images/block.png")
        self.__lakitu = pygame.image.load("./images/lakitu.png")
        self.__lakitu1 = pygame.image.load("./images/lakitu1.png")
        self.__lakitu2 = pygame.image.load("./images/lakitu2.png")
        self.__goomba = pygame.image.load("./images/goomba3.png")
        self.__goomba1 = pygame.image.load("./images/goomba1.png")
        self.__goomba2 = pygame.image.load("./images/goomba2.png")
        self.__mushroom = pygame.image.load("./images/mushroom.png")
        self.__winner = pygame.image.load("./images/winner.png")
        self.__map = map
        self.__screen = None
        self.__lenght = 1000
        self.__height = 600

    def mapDisplay(self, path):
        pygame.init()
        self.__screen = pygame.display.set_mode((self.__lenght, self.__height))

        notClosed = True
        ani = 0
        animForMario=0
        anit = True
        rndForAnimation = random.randint(0, 2)
        step=0
        while notClosed:
            if ani == 10  or ani==-30:
             if step<=len(path)-2:
                step+=1
             animForMario=0

            if anit:
                ani += 0.5
                if ani == 10:
                    rndForAnimation = random.randint(0, 2)
                    anit = False
            elif not anit:
                ani -= 0.5
                if ani == -30:
                    rndForAnimation = random.randint(0, 2)
                    anit = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    notClosed = False

            # self.__screen.fill((146, 220, 231, 255))
            self.__wallpaper = pygame.transform.scale(self.__wallpaper, (self.__lenght, self.__height))
            self.__screen.blit(self.__wallpaper, (0, 0))

            tmpScale = self.__lenght // len(self.__map)
            self.__block = pygame.transform.scale(self.__block, (tmpScale, tmpScale))
            self.__mushroom = pygame.transform.scale(self.__mushroom, (tmpScale, tmpScale))
            self.__goomba = pygame.transform.scale(self.__goomba, (tmpScale, tmpScale))
            self.__goomba1 = pygame.transform.scale(self.__goomba1, (tmpScale, tmpScale))
            self.__goomba2 = pygame.transform.scale(self.__goomba2, (tmpScale, tmpScale))
            self.__lakitu = pygame.transform.scale(self.__lakitu, (tmpScale, tmpScale))
            self.__lakitu1 = pygame.transform.scale(self.__lakitu1, (tmpScale, tmpScale))
            self.__lakitu2 = pygame.transform.scale(self.__lakitu2, (tmpScale, tmpScale))
            self.__mario = pygame.transform.scale(self.__mario, (tmpScale, tmpScale))
            self.__mario2 = pygame.transform.scale(self.__mario2, (tmpScale, tmpScale))
            self.__jumpingMario = pygame.transform.scale(self.__jumpingMario, (tmpScale, tmpScale))
            self.__sittingMario = pygame.transform.scale(self.__sittingMario, (tmpScale, tmpScale))
            self.__winnerMario = pygame.transform.scale(self.__winnerMario, (tmpScale, tmpScale))
            self.__winner = pygame.transform.scale(self.__winner, (tmpScale*3, tmpScale*3))

            for i in range(0, len(self.__map)):

                xLoc = i * tmpScale
                yLoc = self.__height - tmpScale
                self.__screen.blit(self.__block, (xLoc, yLoc))
                if (self.__map[i] == "M"):
                    self.__screen.blit(self.__mushroom, (xLoc + 0.2 * ani, yLoc - tmpScale))
                elif (self.__map[i] == "G"):

                    if rndForAnimation == 0:
                        self.__screen.blit(self.__goomba1, (xLoc , yLoc - tmpScale +  0.6 * ani))
                    elif rndForAnimation == 1:
                        self.__screen.blit(self.__goomba2, (xLoc, yLoc - tmpScale + 0.6 * ani))
                    elif rndForAnimation == 2:

                        self.__screen.blit(self.__goomba, (xLoc, yLoc - tmpScale + 0.6 * ani))


                elif (self.__map[i] == "L"):
                    if rndForAnimation == 0:
                        self.__screen.blit(self.__lakitu, (xLoc + 0.4 * ani, yLoc - 2 * tmpScale + 0.3 * ani))
                    elif rndForAnimation == 1:
                        self.__screen.blit(self.__lakitu1, (xLoc + 0.4 * ani, yLoc - 2 * tmpScale + 0.3 * ani))
                    elif rndForAnimation == 2:
                        self.__screen.blit(self.__lakitu2, (xLoc + 0.4 * ani, yLoc - 2 * tmpScale + 0.3 * ani))

            # for i in range(0, len(path)):

            xLoc = step * tmpScale
            yLoc = self.__height - tmpScale
            animForMario +=tmpScale/80
            if step!=len(path)-1:
                if path[step] == 0:
                    if step+1!=len(path) and path[step+1]==1:
                         self.__screen.blit(self.__jumpingMario, (xLoc+tmpScale +abs(animForMario), yLoc - 1*tmpScale -abs(animForMario)))
                    elif step+1!=len(path) and path[step+1]==2:
                         self.__screen.blit(self.__sittingMario, (xLoc+tmpScale +abs(animForMario), yLoc - 1*tmpScale ))
                    else:
                        if anit:
                          self.__screen.blit(self.__mario, (xLoc +tmpScale+abs(animForMario), yLoc - 1*tmpScale  ))
                        else:
                            self.__screen.blit(self.__mario2, (xLoc + tmpScale + abs(animForMario), yLoc - 1 * tmpScale))

                elif path[step] == 1:
                    if step+1!=len(path) and path[step+1]==0:
                         self.__screen.blit(self.__jumpingMario, (xLoc+tmpScale +abs(animForMario), yLoc - 2*tmpScale +abs(animForMario)))

                    else:
                     self.__screen.blit(self.__jumpingMario, (xLoc+tmpScale+abs(animForMario), yLoc - 2 * tmpScale))

                elif path[step] == 2:
                    self.__screen.blit(self.__sittingMario, (xLoc+tmpScale+abs(animForMario), yLoc - 1 * tmpScale))
            else:
                self.__screen.blit(self.__winnerMario, (xLoc , yLoc - 1 * tmpScale +   ani))
                self.__screen.blit(self.__winner, (self.__lenght/2-tmpScale, self.__height/2-tmpScale - 1 * tmpScale +   ani))

            # self.mapUpdator()    TODO   # uncomment it
            pygame.display.update()

    def mapUpdator(self,step,path):
        #you have map and path                      and current step
                                   # self.__map                         step
                                    # path
        pass

