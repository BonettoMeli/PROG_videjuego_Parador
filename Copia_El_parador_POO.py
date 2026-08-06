import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("EL PARADOR")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)

# Control de FPS
reloj = pygame.time.Clock()

# Variables del juego
estado_actual = "MENU"
inventario = []

# Carga de recursos (imágenes, sonidos) simulada para la estructura
# sonido_agua = pygame.mixer.Sound("efecto_agua.mp3")
# sonido_palanca = pygame.mixer.Sound("efecto_palanca.mp3")

def dibujar_menu():
    pantalla.fill(NEGRO)
    fuente = pygame.font.SysFont("Arial", 40)
    texto_titulo = fuente.render("EL PARADOR", True, BLANCO)
    texto_instruccion = fuente.render("Presiona ESPACIO para comenzar", True, GRIS)
    
    pantalla.blit(texto_titulo, (ANCHO // 2 - texto_titulo.get_width() // 2, ALTO // 3))
    pantalla.blit(texto_instruccion, (ANCHO // 2 - texto_instruccion.get_width() // 2, ALTO // 2))

def dibujar_nivel_1():
    pantalla.fill((30, 30, 50))
    fuente = pygame.font.SysFont("Arial", 24)
    texto = fuente.render("Nivel 1: El Tren - Resuelve la avería", True, BLANCO)
    pantalla.blit(texto, (50, 50))

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if evento.type == pygame.KEYDOWN:
            if estado_actual == "MENU" and evento.key == pygame.K_SPACE:
                estado_actual = "NIVEL_1"
            elif estado_actual == "NIVEL_1" and evento.key == pygame.K_ESCAPE:
                estado_actual = "MENU"

    # Lógica de pantallas
    if estado_actual == "MENU":
        dibujar_menu()
    elif estado_actual == "NIVEL_1":
        dibujar_nivel_1()

    pygame.display.flip()
    reloj.tick(60)