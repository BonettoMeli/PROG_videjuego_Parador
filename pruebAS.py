import sys
import pygame
pygame.init()
#------------creo la pantalla y le doy nombre----------------------------------------
pantalla = pygame.display.set_mode((1400,800))
pygame.display.set_caption("Videojuego ¨EL PARADOR¨")

#----------PANTALLA DE INICIO----------------------------------------------------------
imagen_inicio = pygame.image.load('visual/inicio.png')
imagen = pygame.transform.scale(imagen_inicio, (1400, 800))

boton_jugar = pygame.Rect(510, 470, 350, 60)

#---------------IMAGENES----------------------------------------------
carga = pygame.image.load('visual/explorando_dimen.png')
carga = pygame.transform.scale(carga, (1400, 800))

intro = pygame.image.load('visual/instrucciones.png')
intro = pygame.transform.scale(intro, (1400, 800))

boton_jugar2 = pygame.Rect(510, 760, 300, 60)

auto1 = pygame.image.load('visual/auto_parte1.png')
auto1 = pygame.transform.scale(auto1, (400, 800))
auto2 = pygame.image.load('visual/auto_parte2.png')
auto2 = pygame.transform.scale(auto2, (400, 800))
auto3 = pygame.image.load('visual/auto_parte3.png')
auto3 = pygame.transform.scale(auto3, (400, 800))



pantalla_actual = "inicio"
tiempo_carga = 0

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:

            # BOTÓN DEL MENÚ PRINCIPAL
            if pantalla_actual == "inicio":
                if boton_jugar.collidepoint(evento.pos):
                    pantalla_actual = "carga"
                    tiempo_carga = pygame.time.get_ticks()

            # BOTÓN DE LA PANTALLA DE INSTRUCCIONES
            elif pantalla_actual == "juego":
                if boton_jugar2.collidepoint(evento.pos):
                    pantalla_actual = "historia"
                    tiempo_historia = pygame.time.get_ticks()

    # ---------------- PANTALLAS ----------------

    if pantalla_actual == "inicio":
        pantalla.blit(imagen, (0, 0))

        mouse = pygame.mouse.get_pos()

        if boton_jugar.collidepoint(mouse):
            pygame.draw.rect(pantalla, (80, 80, 80), boton_jugar, 3)

    elif pantalla_actual == "carga":
        pantalla.blit(carga, (0, 0))

        if pygame.time.get_ticks() - tiempo_carga > 2000:
            pantalla_actual = "juego"

    elif pantalla_actual == "juego":
        pantalla.blit(intro, (0, 0))

        mouse = pygame.mouse.get_pos()

        if boton_jugar2.collidepoint(mouse):
            pygame.draw.rect(pantalla, (205, 170, 125), boton_jugar2, 3)

    elif pantalla_actual == "historia":

        tiempo = pygame.time.get_ticks() - tiempo_historia

        pantalla.blit(auto1, (0, 0))

        if tiempo > 1000:
            pantalla.blit(auto2, (400, 0))

        if tiempo > 2000:
            pantalla.blit(auto3, (800, 0))

    pygame.display.flip()