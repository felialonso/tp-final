import pygame, random 

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.mixer.init() #Esto es para el sonido 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter") #Para darle titulo a la ventana 
clock = pygame.time.Clock() #Controlar nuestro frames por segundos 


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"SPACE INVADERS\assets\player.png").convert()
        self.image.set_colorkey(WHITE)#Esta funcion se encarga de remover el fondo negro de la imagen
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0 

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed() # Muestra el estado de las teclas q se presionaron
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    
    def shoot(self):
        bala = Bala(self.rect.centerx, self.rect.top)
        all_sprites.add(bala)
        balas.add(bala) 


class Enemigos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\falon\OneDrive\Escritorio\LAB Y PROGRAMACION\SPACE INVADERS\assets\green.png").convert()
        self.image.set_colorkey(WHITE) #Esta funcion se encarga de remover el fondo negro de la imagen
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40) #Esto hace q le de el efecto de q este bajando 
        self.speedy = random.randrange(1, 10) #Esto es para q vayan saliendo con diferentes velocidades
        self.speedx = random.randrange(-5, 5)


    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 25:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40) 
            self.speedy = random.randrange(1, 10)




class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\falon\OneDrive\Escritorio\LAB Y PROGRAMACION\SPACE INVADERS\assets\BALA.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect() 
        self.rect.y = y  
        self.rect.centerx = x #Centrar el objeto de manera facil
        self.speedy = -10 #Se le pone negativo por q va desde abajo y necesit ir creciendo

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0: #Esto hace q elimine cualquier objeto de la lista cuando ya sale de la ventana
            self.kill()



#Cargar el fondo
background = pygame.image.load(r"C:\Users\falon\OneDrive\Escritorio\LAB Y PROGRAMACION\SPACE INVADERS\assets\fondo.jpg").convert()

all_sprites = pygame.sprite.Group()
enemigo_sprites = pygame.sprite.Group()
balas = pygame.sprite.Group()

player = Player()
all_sprites.add(player) #Aca se agrega al jugador a la lista

for i in range(8):
    enemigo = Enemigos()
    all_sprites.add(enemigo)
    enemigo_sprites.add(enemigo)

running = True 
while running:
    clock.tick(45)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:#Si la tecla espacio se apreta dispara la bala
            if event.key == pygame.K_SPACE:
                player.shoot()


    
    all_sprites.update()

    hits =  pygame.sprite.spritecollide(player, enemigo_sprites, True) #Esto es la colicion
    if hits:
        running = False

    screen.blit(background, [0, 0])

    all_sprites.draw(screen)

    pygame.display.flip()
pygame.quit()
