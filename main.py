import pygame
import classes
import obstaculos

pygame.init()


size = [700,500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TANKS")
clock = pygame.time.Clock()

Tank1 = classes.TankVerde()
Tank2 = classes.TankLaranja()


game = True

def Draw():
    
    screen.fill([45,45,45])
    
    if Tank1.is_active:
        screen.blit(Tank1.tank, Tank1.rect)
    for i in range(len(Tank1.tiros)):
        screen.blit(Tank1.tiros[i].tiro, Tank1.tiros[i].rect)
        
    if Tank2.is_active:
        screen.blit(Tank2.tank, Tank2.rect)
        
    for i in range(len(Tank2.tiros)):
        screen.blit(Tank2.tiros[i].tiro, Tank2.tiros[i].rect)  
    
def verifica_vitoria(tank1,tank2,screen):
    if not tank1.is_active:
        
        font = pygame.font.SysFont(None,40)
        text = font.render("VITORIA DO LARANJA", True, [255,255,255],[45,45,45])
        
        textRect = text.get_rect()
        textRect.centerx , textRect.centery = size[0]/2,size[1]/2
        screen.blit(text, textRect)
    elif not tank2.is_active:
        
        font = pygame.font.SysFont(None,40)
        text = font.render("VITORIA DO VERDE", True, [255,255,255],[45,45,45])
        textRect = text.get_rect()
        textRect.centerx , textRect.centery = size[0]/2,size[1]/2
        screen.blit(text, textRect)
    if not tank1.is_active or not tank2.is_active:
        reinicio_font = pygame.font.SysFont(None, 30)
        reinicio = reinicio_font.render("Pressione 'r' para uma nova partida 'Esc' para sair",True, [255,255,255],[45,45,45])
        reiniciorect = reinicio.get_rect()
        reiniciorect.centerx, reiniciorect.centery = size[0]/2,size[1]/2+40
        screen.blit(reinicio,reiniciorect)


#cenario
cenario = obstaculos.Cenario()



while game:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            import sys
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RCTRL:
                if Tank1.is_active:
                    Tank1.atira()
                
            if event.key == pygame.K_SPACE:
                if Tank2.is_active:
                    Tank2.atira()
        
    #move tank1
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        Tank1.move_esquerda()
    elif pressed_keys[pygame.K_UP]:
        Tank1.move_cima()
        
    elif pressed_keys[pygame.K_DOWN]:
        Tank1.move_baixo()
    elif pressed_keys[pygame.K_RIGHT]:
        Tank1.move_direita()
        
    #move tank2
    if pressed_keys[pygame.K_w]:
        Tank2.move_cima()
    elif pressed_keys[pygame.K_s]:
        Tank2.move_baixo()
    elif pressed_keys[pygame.K_d]:
        Tank2.move_direita()
    elif pressed_keys[pygame.K_a]:
        Tank2.move_esquerda()
        
    #move tiros
    for tiro in Tank1.tiros:
        tiro.move()
        
    for tiro in Tank2.tiros:
        tiro.move()  
    
    
    #retira os tiros que ja sairam da tela
    for tiro in Tank1.tiros:
        if tiro.rect.x <= 0:
            Tank1.tiros.remove(tiro)
        elif tiro.rect.x >= 700:
            Tank1.tiros.remove(tiro)
        elif tiro.rect.y <= 0:
            Tank1.tiros.remove(tiro)
        elif tiro.rect.y >= 500:
            Tank1.tiros.remove(tiro)
            
    #um tanque mata o outro
    for tiro in Tank1.tiros:
        if Tank2.is_active:
            if pygame.Rect.colliderect(tiro.rect,Tank2.rect):
                pygame.mixer.music.load("Explosion.wav")
                pygame.mixer.music.play()
                Tank2.is_active = False
            
    for tiro in Tank2.tiros:
        if Tank1.is_active:
            if pygame.Rect.colliderect(tiro.rect, Tank1.rect):
                pygame.mixer.music.load("Explosion.wav")
                pygame.mixer.music.play()
                Tank1.is_active = False
            
    #reinicia o jogo
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_r]:
        from random import randint
        cenario = obstaculos.Cenario()
        Tank1 = classes.TankVerde()
        Tank2 = classes.TankLaranja()
    
    #colisao com a parede
    for muro in cenario.muros:
        for paredinha in muro.parede:
            if pygame.Rect.colliderect(Tank1.rect, paredinha.rect):
                if Tank1.rect.centerx < paredinha.rect.centerx and Tank1.rect.centery in range(paredinha.rect.top, paredinha.rect.bottom):
                    Tank1.rect.centerx -= 2
                if Tank1.rect.centerx > paredinha.rect.centerx and Tank1.rect.centery in range(paredinha.rect.top, paredinha.rect.bottom):
                    Tank1.rect.centerx += 2
                if Tank1.rect.centery < paredinha.rect.centery and Tank1.rect.centerx in range(paredinha.rect.left, paredinha.rect.right):
                    Tank1.rect.centery -= 2
                if Tank1.rect.centery > paredinha.rect.centery and Tank1.rect.centerx in range(paredinha.rect.left, paredinha.rect.right):
                    Tank1.rect.centery += 2
                    
            if pygame.Rect.colliderect(Tank2.rect, paredinha.rect):
                if Tank2.rect.centerx < paredinha.rect.centerx and Tank2.rect.centery in range(paredinha.rect.top, paredinha.rect.bottom):
                    Tank2.rect.centerx -= 2
                if Tank2.rect.centerx > paredinha.rect.centerx and Tank2.rect.centery in range(paredinha.rect.top, paredinha.rect.bottom):
                    Tank2.rect.centerx += 2
                if Tank2.rect.centery < paredinha.rect.centery and Tank2.rect.centerx in range(paredinha.rect.left, paredinha.rect.right):
                    Tank2.rect.centery -= 2
                if Tank2.rect.centery > paredinha.rect.centery and Tank2.rect.centerx in range(paredinha.rect.left, paredinha.rect.right):
                    Tank2.rect.centery += 2
                    
                    
    #colisao com os tiros nas paredes
    for tiro in Tank1.tiros:
        for parede in cenario.muros:
            for muro in parede.parede:
                if pygame.Rect.colliderect(tiro.rect, muro.rect):
                    try:
                        Tank1.tiros.remove(tiro)
                    except:
                        Tank1.tiros = []
                    # parede.parede.remove(muro)
    for tiro in Tank2.tiros:
        for parede in cenario.muros:
            for muro in parede.parede:
                if pygame.Rect.colliderect(tiro.rect, muro.rect):
                    try:
                        Tank2.tiros.remove(tiro)
                    except:
                        Tank2.tiros = []
                    # parede.parede.remove(muro)
                                              
    Draw() 
    obstaculos.renderCenario(screen,cenario)      
    verifica_vitoria(Tank1,Tank2,screen)
    clock.tick(60)
    pygame.display.update()