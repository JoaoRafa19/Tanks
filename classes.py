import pygame
from random import randint

class TankVerde:
    
    def __init__(self):
        
        self.tank = pygame.image.load("tankverde.png")
        self.rect = self.tank.get_rect()
        self.initialpos = [randint(0,680), randint(0,490)]
        self.rect.x, self.rect.y = self.initialpos[0], self.initialpos[1]
        self.direction = "UP"
        self.is_active = True
        
        self.tiros = []
        
    def move_esquerda(self):
        self.tank = pygame.image.load("tankverdeesquerda.png")
        self.rect = self.rect.move([-1,0])
        self.direction = "LEFT"
        
    def move_direita(self):
        self.tank = pygame.image.load("tankverdedireita.png")
        self.rect = self.rect.move([1,0])
        self.direction = "RIGHT"
        
        
    def move_cima(self):
        self.tank = pygame.image.load("tankverde.png")
        self.rect = self.rect.move([0,-1])
        self.direction = "UP"
        
    def move_baixo(self):
        self.tank = pygame.image.load("tankverdebaixo.png")
        self.rect = self.rect.move([0,1])
        self.direction = "DOWN"
        
    def atira(self):
        pygame.mixer.music.load("shoot.wav")
        pygame.mixer.music.play()
        newTiro = Tiro()
        newTiro.rect.x, newTiro.rect.y = self.rect.centerx, self.rect.centery
        newTiro.direction = self.direction
        self.tiros.append(newTiro) 
        
    
        
class Tiro:
    
    def __init__(self):
        self.tiro = pygame.image.load("tiro.png")
        self.rect = self.tiro.get_rect()
        self.direction = None
        self.velocidade = 4
        
        
        
    def move(self):
        if self.direction == "LEFT":
            self.rect = self.rect.move([-self.velocidade,0])
            
        elif self.direction == "RIGHT":
            self.rect = self.rect.move([self.velocidade,0])
            
        elif self.direction == "UP":
            self.rect = self.rect.move([0,-self.velocidade])
            
        elif self.direction == "DOWN":
            self.rect = self.rect.move([0,self.velocidade])
        
        
        
class TankLaranja:
    
    def __init__(self):
        
        self.tank = pygame.image.load("tanklaranja.png")
        self.rect = self.tank.get_rect()
        self.initialpos = [randint(10,680), randint(10,480)]
        self.rect.x, self.rect.y = self.initialpos[0], self.initialpos[1]
        self.direction = "UP"
        self.is_active = True
        
        self.tiros = []
        
    def move_esquerda(self):
        self.tank = pygame.image.load("tanklaranjaesquerda.png")
        self.rect = self.rect.move([-1,0])
        self.direction = "LEFT"
        
    def move_direita(self):
        self.tank = pygame.image.load("tanklaranjadireita.png")
        self.rect = self.rect.move([1,0])
        self.direction = "RIGHT"
        
        
    def move_cima(self):
        self.tank = pygame.image.load("tanklaranja.png")
        self.rect = self.rect.move([0,-1])
        self.direction = "UP"
        
    def move_baixo(self):
        self.tank = pygame.image.load("tanklaranjabaixo.png")
        self.rect = self.rect.move([0,1])
        self.direction = "DOWN"
        
    def atira(self):
        pygame.mixer.music.load("shoot.wav")
        pygame.mixer.music.play()
        newTiro = Tiro()
        newTiro.rect.x, newTiro.rect.y = self.rect.centerx, self.rect.centery
        newTiro.direction = self.direction
        self.tiros.append(newTiro) 
              
        
        
        
        
        
        
        