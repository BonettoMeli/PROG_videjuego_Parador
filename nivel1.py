import sys
import pygame
pygame.init()
pygame.mixer.init()

#------------creo la pantalla y le doy nombre----------------------------------------
pantalla = pygame.display.set_mode((1400,800))
pygame.display.set_caption("Videojuego ¨EL PARADOR¨")



jardin = pygame.image.load("visual/lenguas_muertas2.jpg")
invernadero = pygame.image.load("visual/invernadero_adentro.jpg")
cofre = pygame.image.load("visual/cofre_lengua1.jpg")
cofre_abierto = pygame.image.load("visual/cofre_lengua2.jpg")
afuera = pygame.image.load("visual/tren_lengua_abierto.jpeg")

jardin = pygame.transform.scale(jardin, (1400, 800))
invernadero = pygame.transform.scale(invernadero, (1400, 800))
cofre = pygame.transform.scale(cofre, (1400, 800))
cofre_abierto = pygame.transform.scale(cofre_abierto, (1400, 800))
afuera = pygame.transform.scale(afuera, (1400, 800))

flecha_centro = pygame.Rect(620, 250, 140, 220)
flecha_centro2 = pygame.Rect(620, 250, 140, 220)

flecha_derecha = pygame.Rect(1220, 280, 180, 220)

flecha_izquierda = pygame.Rect(0, 280, 180, 220)

flecha_abajo = pygame.Rect(620, 430, 120, 140)

flecha_abajo2 = pygame.Rect(620, 430, 120, 140)

pantalla_actual = "inicio"
tiempo_carga = 0
tiempo_historia = 0

codigo_encontrado = []
codigo_correcto = "AMTV"
codigo_ingresado = ""

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if evento.type == pygame.KEYDOWN:

            if pantalla_actual == "cofre":

                if evento.key == pygame.K_BACKSPACE:
                    codigo_ingresado = codigo_ingresado[:-1]

                else:
                    codigo_ingresado += evento.unicode.upper()
                
                if codigo_ingresado == codigo_correcto:
                    pantalla_actual = "cofre_abierto"

        

            if pantalla_actual == "jardin":

                if flecha_centro.collidepoint(evento.pos):
                    pantalla_actual = "invernadero"
                
                elif flecha_derecha.collidepoint(evento.pos):
                    pantalla_actual = "cofre"

            elif pantalla_actual == "invernadero":
                
                if flecha_abajo.collidepoint(evento.pos):
                    pantalla_actual = "jardin"

            elif pantalla_actual == "cofre":

                if flecha_izquierda.collidepoint(evento.pos):
                    pantalla_actual = "jardin"

            elif pantalla_actual == "afuera":
                if flecha_abajo2.collidepoint(evento.pos):
                    pantalla_actual = "jardin"
                elif flecha_centro2.collideponit(evento.pos):
                    pantalla_actual = "tren_dentro"