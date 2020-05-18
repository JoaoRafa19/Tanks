import pygame
from random import randint


def renderCenario(screen, cenario):
    for i in cenario.muros:
        for j in i.parede:
            screen.blit(Muro().muro,j.rect)
        

class Muro:
    
    def __init__(self):
        self.muro = pygame.image.load("muro.png")
        self.rect = self.muro.get_rect()
        
    
        
class Parede:
    def __init__(self):
        self.orientacao  = randint(1,2)
        self.parede = []
        self.nummuros = randint(5,20)
        self.posicao_inicial = randint(50,680),randint(20,450)
        if self.orientacao == 1:
            for i in range(self.nummuros):
                muro = Muro()
                muro.rect.centerx = self.posicao_inicial[0]
                muro.rect.centery = self.posicao_inicial[1]+(10*i)
                self.parede.append(muro)
                
                
        if self.orientacao == 2:
            for i in range(self.nummuros):
                muro = Muro()
                muro.rect.centery = self.posicao_inicial[1]
                muro.rect.centerx = self.posicao_inicial[0]+(10*i)
                self.parede.append(muro)
                
            
            
         
       
class Cenario:
    
    def __init__(self):
        self.num_paredes = randint(10,15)
        self.muros= []
        
        for i in range(self.num_paredes):
            self.muros.append(Parede())
        
        
        
        
        
        
        
  