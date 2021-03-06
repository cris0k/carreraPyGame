import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("images/termo1.png")
        
    def convertir(self, grados, toUnidad):
        resultado = 0
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
            
        return "{:10.2f}".format(resultado)
        
class Selector():
    __tipoUnidad = None
    
    def __init__(self,unidad = 'C'):
        self.__customes = []
        self.__customes.append(pygame.image.load("images/posiF.png"))
        self.__customes.append(pygame.image.load("images/posiC.png"))
        
        self.__tipoUnidad = unidad
        
    def custome(self):
        if self.__tipoUnidad == 'F':
            return self.__customes[0]
        else:
            return self.__customes[1]
        
    def change(self):
        if self.__tipoUnidad =='F':
            self.__tipoUnidad = 'C'
        else:
            self.__tipoUnidad = 'F'
            
    def unidad(self):
        return self.__tipoUnidad

class NumberInput():
    __value = 0
    __strValue = ""
    __position = [0,0]
    __size = [0,0]
    __pointsCount = 0
    
    def __init__(self, value=0):
        self.__font = pygame.font.SysFont("Arial", 24)
        self.value(value)
        
    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) < 10 or (event.unicode == '.' and self.__pointsCount == 0): # contolamos la cantidad de numeros que metemos
                self.__strValue += event.unicode # para que vaya añadiendo los numeros que le añadamos
                self.value(self.__strValue) # actualiza el numero que metamos
                if event.unicode == '.':
                    self.__pointsCount += 1
            elif event.key == K_BACKSPACE: # para que podamos borrar la entrada
                if self.__strValue[-1] =='.':
                    self.__pointsCount -= 1
                self.__strValue = self.__strValue[:-1] # -1 porque borramos desde atras
                self.value(self.__strValue)
        
    def render(self):  
        textBlock = self.__font.render(self.__strValue, True, (74,74,74)) #texto del input
        rect = textBlock.get_rect() #rectangulo grafico donde ira el valor
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        
        return (rect, textBlock)
    
    def value(self, val = None): # nos aseguramos que lo que entra es un numero entero
        
        if val == None:
            return self.__value
        else:
            val = str(val)
            print(val, "cadena")
            try:
                self.__value = float(val)
                self.__strValue = val
                if '.' in self.__strValue:
                    self.__pointsCount = 1
                else:
                    self.__pointsCount = 0   
            except:
                pass
    
    def width(self,val= None):
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                pass
            
    def height(self,val= None):
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass
            
    def size(self,val=None):
        if val == None:
            return self.__size
        else:
            try:
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass
            
    def posX(self,val= None):
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass
            
    def posY(self,val= None):
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass
            
    def pos(self,val=None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass
    

class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290,415))
        pygame.display.set_caption("Termomentro")
        
        
        self.termometro = Termometro()
        self.entrada = NumberInput("Monchu")
        self.entrada.pos((106,58)) #coordenadas del rectangulo
        self.entrada.size((133,28)) #tamaño del rectangulo
        
        self.selector = Selector()
        
        
    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def start(self): #coontrol de eventos
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                    
                self.entrada.on_event(event) # esto comprobara que se han pulsado las teclas adecuadas y con la info dada va a modificar Value
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir(grados, nuevaUnidad)
                    self.entrada.value(temperatura)
                
            #pintamos el fondo de pantalla
            self.__screen.fill((244,236,203))
         
            
            #pintamos el termometro en su posicion
            self.__screen.blit(self.termometro.custome,(50,34))
            
            #pintamos el cuadro de texto
            text = self.entrada.render() #obtenemos rectangulo blanco y foto texto y lo asignamos a text
            pygame.draw.rect(self.__screen,(255,255,255), text[0]) #creamos el rectangulo blanco con sus datos(posicion y tamaño)
            self.__screen.blit(text[1],self.entrada.pos()) #pintamos la foto del texto (text[1])
            
            #pintamos el selector F-C
            self.__screen.blit(self.selector.custome(), (112,153))
            
            pygame.display.flip()
        
if __name__ == '__main__':
    pygame.font.init()
    app = mainApp()
    app.start()