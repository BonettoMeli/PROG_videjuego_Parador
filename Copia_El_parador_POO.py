import sys
import pygame
pygame.init()
pygame.mixer.init()

from clase_imagenes import Imagenes_Juego

#------------creo la pantalla y le doy nombre----------------------------------------
pantalla = pygame.display.set_mode((1400,800))
pygame.display.set_caption("Videojuego ¨EL PARADOR¨")
#-------------PANTALLA DE INICIO-----------------------------------------------------


imagen_inicio = Imagenes_Juego("visual/Inicio.png", 1400, 800)

boton_jugar = pygame.Rect(510, 468, 350, 65)
#---------------IMAGENES----------------------------------------------
carga = pygame.image.load('visual/explorando_dimen.png')
carga = pygame.transform.scale(carga, (1400, 800))

intro = pygame.image.load('visual/instrucciones.png')
intro = pygame.transform.scale(intro, (1400, 800))

boton_jugar2 = pygame.Rect(600, 726, 220, 61)

carga2 = pygame.image.load('visual/carga2.png')
carga2 = pygame.transform.scale(carga2, (1400, 800))
#---------------------------------------------------------------------
pantalla_actual = "inicio"

while True:
    if pantalla_actual == "inicio":
        pantalla.blit(imagen_inicio.obtener(), (0, 0))
        mouse = pygame.mouse.get_pos()
        if boton_jugar.collidepoint(mouse):
            pygame.draw.rect(pantalla, (80, 80, 80), boton_jugar, 3)