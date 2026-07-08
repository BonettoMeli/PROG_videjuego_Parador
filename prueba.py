import sys
import pygame
pygame.init()
pygame.mixer.init()

#------------creo la pantalla y le doy nombre----------------------------------------
pantalla = pygame.display.set_mode((1400,800))
pygame.display.set_caption("Videojuego ¨EL PARADOR¨")

#-------------PANTALLA DE INICIO-----------------------------------------------------
imagen_inicio = pygame.image.load('visual/inicio.png')
imagen = pygame.transform.scale(imagen_inicio, (1400, 800))

boton_jugar = pygame.Rect(510, 468, 350, 65)
