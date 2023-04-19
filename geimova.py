import pygame, sys, time, os, subprocess

# Inicializar pygame
pygame.init()

def start_game():
    pass

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir dimensiones de la pantalla
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Fondo de pantalla
fondo_pant = pygame.image.load('img/Background/1.png').convert()
fondo_pant = pygame.transform.scale(fondo_pant, (SCREEN_WIDTH, SCREEN_HEIGHT))



#Titulo del juego
pygame.display.set_caption("LANCELOT")

# Definir fuente
font = pygame.font.Font("fonts/BitfalsFont.otf", 36)

# Cargar música del menú
class LoadingScreen:
    def __init__(self):
        self.progress = 0
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render("Cargando...", True, WHITE)
        self.text_rect = self.text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
                        
    def update(self):
        self.progress += 1
        pygame.draw.rect(screen, WHITE, [150, 400, self.progress, 50])    
        screen.blit(self.text, self.text_rect)
        pygame.display.update()


# Definir opciones del menú
options = [""]
selected_option = 0

# Bucle principal del juego
while True:
     # Dibujar el fondo
    screen.blit(fondo_pant, (0, 0))
    
    #Dibujo del titulo
    title = font.render("Reiniciar juego", True, ( 155, 255, 213 ))
    title_rect = title.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/8))
    screen.blit(title, title_rect)
    
    # Dibujar las opciones del menú
    for i in range(len(options)):
        text = font.render(options[i], True, BLACK)
        if i == selected_option:
            text = font.render(options[i], True, (255, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + i*50))
        screen.blit(text, text_rect)

    # Actualizar pantalla
    pygame.display.flip()
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(options)
                effect_sound.play()
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(options)
                effect_sound = pygame.mixer.Sound("music/selection.mp3")
                effect_sound.play()
            elif event.key == pygame.K_RETURN:
                if selected_option == 0:
                    effect_sound = pygame.mixer.Sound("music/selected.mp3")
                    effect_sound.play()        
                    # Crear la pantalla de carga
                    screen.fill(BLACK)
                    pygame.mixer.music.stop()
                    pygame.display.flip()
                    loading_screen = LoadingScreen()
                    # Bucle principal del juego
                    loading = True
                    while loading:
                        # Manejar eventos
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                loading = False

                        # Actualizar la pantalla de carga
                        loading_screen.update()
                        
                        # Simular carga de recursos
                        time.sleep(0.01)
                        if loading_screen.progress >= 500:
                            loading = False
                            start_game()
                    # ... Código del menú ... 
                    # Abrir el archivo Lancelot.py
                    pygame.quit()
                    subprocess.call(["python", "game.py"])
        elif selected_option == 1:
        # Cargar la imagen del manual
         manual_image = pygame.image.load('img/manual.png').convert()
         manual_image_rect = manual_image.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        # Mostrar la imagen en la pantalla
         screen.blit(manual_image, manual_image_rect)
         pygame.display.update()

        # Esperar a que el usuario presione cualquier tecla
         waiting = True
         while waiting:
             for event in pygame.event.get():
                 if event.type == pygame.KEYDOWN:
                     waiting = False
                     break
        # ... Código del menú ...
                 elif selected_option == 2:
                  pygame.quit()
                  sys.exit()
                    
    
   