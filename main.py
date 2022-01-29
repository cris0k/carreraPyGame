import pygame
import sys

class Game():
    
    corredores = []
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((640, 480)) #tamaño de la pantalla
        pygame.display.set_caption("CARRERA DE BICHOS")
        self.backround = pygame.image.load("images/background.png")#metemos la imagen del fondo desde un directorio previamente creado
        
        self.runner = pygame.image.load("images/turtle.png")
        
    def competir(self):
        
        x = 0
        hayGanador = False
        
        while True:
            #comprobacion de los eventos
            for event in pygame.event.get(): # procesamos todos los eventos(entradas de teclado, de mando...)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #refrescamos/renderizar la pangtalla        
            self.__screen.blit(self.backround, (0,0)) # .blit pinta el backround + coordenada
            self.__screen.blit(self.runner,(x,240))
            pygame.display.flip() #refresca la pantalla
            
            x += 3
            if x >= 250:
                hayGanador = True
                
        pygame.quit()
        sys.exit()
            
        
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()
    