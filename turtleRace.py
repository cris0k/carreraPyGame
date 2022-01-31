import pygame, sys
import random

class Runner():
    __customes = ('turtle', 'fish', 'prawn', 'moray', 'octopus')
    
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0, 4) #crea 4 personajes aleatorios de los png dados
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.position = [x,y]
        self.name = ""
        
    def avanzar(self):
        self.position[0] += random.randint(1,6)
        

class Game():
    runners = [] #lista de corredores
    __posY =(160,200,240,280) #posicion de corredores
    __names = ('Tommy', 'Jerry', 'Bunny', 'Speedy')
    __startLine = -5
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        for i in range(4):
            theRunner = Runner(self.__startLine, self.__posY[i]) # esto es para que posicione cada runner segun la coordenada indicada, en orden
            theRunner.name = self.__names[i]
            self.runners.append(theRunner) #lo añadimos a la lista de runners
        
        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            
            for activeRunner in self.runners:
                activeRunner.avanzar()
                
                if activeRunner.position[0] >= self.__finishLine:
                    print("{} ha ganado".format(activeRunner.name))
                    gameOver = True
            
            self.__screen.blit(self.__background, (0,0))
            
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position) #esto ultimo hace que la posicion de la tortuga este donde le digamos
            
            pygame.display.flip()
            
        while True:
            for event in pygame.event.get(): # para que cuando termine la carrera, no se cierre y espere a que cerremos
                if event.type == pygame.QUIT:
                    pygame.quit()#control de salida
                    sys.exit()
    
    

if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.competir()