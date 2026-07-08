



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

#---------------IMAGENES----------------------------------------------
carga = pygame.image.load('visual/explorando_dimen.png')
carga = pygame.transform.scale(carga, (1400, 800))

intro = pygame.image.load('visual/instrucciones.png')
intro = pygame.transform.scale(intro, (1400, 800))

boton_jugar2 = pygame.Rect(600, 726, 220, 61)

carga2 = pygame.image.load('visual/carga2.png')
carga2 = pygame.transform.scale(carga2, (1400, 800))
#---------------------------------------------------------------------
n1 = pygame.image.load('visual/desde.png')
n2 = pygame.image.load('visual/unico.png')
n3 = pygame.image.load('visual/ruido.png')
n4 = pygame.image.load('visual/persiguen.png')
n5 = pygame.image.load('visual/importancia.png')
n6 = pygame.image.load('visual/noche1.png')
n7 = pygame.image.load('visual/algopaso.png')

n1 = pygame.transform.scale(n1, (1400, 800))
n2 = pygame.transform.scale(n2, (1400, 800))
n3 = pygame.transform.scale(n3, (1400, 800))
n4 = pygame.transform.scale(n4, (1400, 800))
n5 = pygame.transform.scale(n5, (1400, 800))
n6 = pygame.transform.scale(n6, (1400, 800))
n7 = pygame.transform.scale(n7, (1400, 800))
#-----------------------------------------------------------------------
auto1 = pygame.image.load('visual/auto_parte11.jpg')
auto2 = pygame.image.load('visual/auto_parte22.jpg')
auto3 = pygame.image.load('visual/auto_parte3.png')
auto1 = pygame.transform.scale(auto1, (490, 800))
auto2 = pygame.transform.scale(auto2, (490, 800))
auto3 = pygame.transform.scale(auto3, (480, 800))

boton1_historia = pygame.Rect(600, 726, 220, 61)
#------------------------------------------------------------------------
parte2 = pygame.image.load('visual/paro.png')
parte3 = pygame.image.load('visual/paro2.png')
parte2 = pygame.transform.scale(parte2, (490, 800))
parte3 = pygame.transform.scale(parte3, (925, 800))
#-------------------------------------------------------------------------
llegada1 = pygame.image.load('visual/llegada1.jpg')
llegada2 = pygame.image.load('visual/llegada2.jpg')
llegada3 = pygame.image.load('visual/llegada3.jpg')
llegada1 = pygame.transform.scale(llegada1, (490, 800))
llegada2 = pygame.transform.scale(llegada2, (470, 800))
llegada3 = pygame.transform.scale(llegada3, (490, 800))
#-------------------------------------------------------------------------
tren1 = pygame.image.load("visual/tren1.jpg")
tren2 = pygame.image.load("visual/tren2.jpg")
tren3 = pygame.image.load("visual/tren3.jpg")

tren1 = pygame.transform.scale(tren1, (490, 800))
tren2 = pygame.transform.scale(tren2, (490, 800))
tren3 = pygame.transform.scale(tren3, (490, 800))
#-------------------------------------------------------------------------
man = pygame.image.load("visual/tipo_sentado.jpeg")
charla1 = pygame.image.load("visual/charla1.jpg")
charla2 = pygame.image.load("visual/charla2.jpg")
charla3 = pygame.image.load("visual/charla3.jpg")
charla4 = pygame.image.load("visual/charla4.jpg")
charla5 = pygame.image.load("visual/charla5.jpeg")
charla6 = pygame.image.load("visual/charla6.jpeg")
charla7 = pygame.image.load("visual/charla7.PNG")
charla8 = pygame.image.load("visual/charla8.jpeg")
charla9 = pygame.image. load("visual/charla9.png")
charla10 = pygame.image.load("visual/charla10.jpeg")
charla11 = pygame.image.load("visual/charla11.jpeg")
maquinista1 = pygame.image.load("visual/maquinista1.jpg")
maquinista2 = pygame.image.load("visual/maquinista2.jpeg")


man = pygame.transform.scale(man,(1400, 800))
charla1 = pygame.transform.scale(charla1, (1400, 800))
charla2 = pygame.transform.scale(charla2, (1400, 800))
charla3 = pygame.transform.scale(charla3, (1400, 800))
charla4 = pygame.transform.scale(charla4, (1400, 800))
charla5 = pygame.transform.scale(charla5, (1400, 800))
charla6 = pygame.transform.scale(charla6, (1400, 800))
charla7 = pygame.transform.scale(charla7, (1400, 800))
charla8 = pygame.transform.scale(charla8, (1400, 800))
charla9 = pygame.transform.scale(charla9, (1400, 800))
charla10 = pygame.transform.scale(charla10, (1400, 800))
charla11 = pygame.transform.scale(charla11, (1400, 800))

maquinista1 = pygame.transform.scale(maquinista1, (1400, 800))
maquinista2 = pygame.transform.scale(maquinista2, (1400, 800))

boton_cabina = pygame.Rect(600, 726, 220, 61)

interior = pygame.image.load("visual/vagon_vacio.jpeg")
interior = pygame.transform.scale(interior, (1400, 800))

#-----------------NIVEL UNO-----------------------------------------------
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

#HOJAS DEL INVERNADERO
hoja_A = pygame.image.load("visual/hoja_A.jpg")
hoja_M = pygame.image.load("visual/hoja_M.jpg")
hoja_T = pygame.image.load("visual/hoja_T.jpg")
hoja_V = pygame.image.load("visual/hoja_V.jpg")

hoja_A = pygame.transform.scale(hoja_A, (500, 500))
hoja_M = pygame.transform.scale(hoja_M, (500, 500))
hoja_T = pygame.transform.scale(hoja_T, (500, 500))
hoja_V = pygame.transform.scale(hoja_V, (500, 500))

#-----------------BOTONES NIVEL UNO------------------------------

flecha_centro = pygame.Rect(750, 450, 100, 100)
flecha_centro2 = pygame.Rect(660, 380, 100, 180 )

flecha_derecha = pygame.Rect(1220, 280, 180, 220)

flecha_izquierda = pygame.Rect(0, 280, 100, 220)

flecha_abajo = pygame.Rect(820, 600, 120, 140)
flecha_abajo2 = pygame.Rect(620, 430, 120, 140)

flecha_atras = pygame.Rect(610, 600, 120, 140)
flecha_cabina = pygame.Rect(600, 480, 120, 140)

flecha_cabina2 = pygame.Rect(680, 600, 120, 140)


planta_A = pygame.Rect(500, 180, 220, 220)
planta_M = pygame.Rect(450, 330, 280, 180)
planta_T = pygame.Rect(500, 550, 320, 150)
planta_V = pygame.Rect(20, 150, 280, 280)

planta_ampliada = None

#zoom_cofre = pygame.rect()

#--------------------SONIDOS--Y--MUSICA-----------------------------------
#pygame.mixer.music.load("musica_sonido/nueve.mp3")
#pygame.mixer.music.play()

chica_auto_paro2 = pygame.mixer.Sound("musica_sonido/chica_estacion_cerca.mp3")

interfe = pygame.mixer.Sound("musica_sonido/interferencia_efecto.mp3")
botonson = pygame.mixer.Sound("musica_sonido/boton_efecto.mp3")
ruido_tren = pygame.mixer.Sound("musica_sonido/Bocina_tren.mp3")

sin_arranque = pygame.mixer.Sound("musica_sonido/efecto_sin_arranque.mp3")
tren_avanzando = pygame.mixer.Sound("musica_sonido/tren_avanzando.WAV")
#-------------------------------------------------------------------------

pantalla_actual = "jardin" #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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


        if evento.type == pygame.MOUSEBUTTONDOWN:
            
            if pantalla_actual == "inicio": # BOTÓN DEL MENÚ PRINCIPAL
                if boton_jugar.collidepoint(evento.pos):
                    botonson.play()
                    pantalla_actual = "carga"
                    tiempo_carga = pygame.time.get_ticks()

            elif pantalla_actual == "juego": # BOTÓN DE LA PANTALLA DE INSTRUCCIONES
                if boton_jugar2.collidepoint(evento.pos):
                    botonson.play()
                    pantalla_actual = "historia"
                    tiempo_historia = pygame.time.get_ticks()
            
            elif pantalla_actual == "jardin":

                if flecha_centro.collidepoint(evento.pos):
                    pantalla_actual = "invernadero"
                
                elif flecha_derecha.collidepoint(evento.pos):
                    pantalla_actual = "cofre"

                elif flecha_izquierda.collidepoint(evento.pos):
                    pantalla_actual = "afuera"

            elif pantalla_actual == "invernadero":
                if planta_ampliada is not None:
                    planta_ampliada = None

                if planta_A.collidepoint(evento.pos):
                    planta_ampliada = "A"

                elif planta_M.collidepoint(evento.pos):
                    planta_ampliada = "M"

                elif planta_T.collidepoint(evento.pos):
                    planta_ampliada = "T"

                elif planta_V.collidepoint(evento.pos):
                    planta_ampliada = "V"
                    
                elif flecha_abajo.collidepoint(evento.pos):
                    pantalla_actual = "jardin"


            elif pantalla_actual == "cofre":

                if flecha_izquierda.collidepoint(evento.pos):
                    pantalla_actual = "jardin"
                else:
                    pantalla_actual = "afuera"

            elif pantalla_actual == "afuera":

                if flecha_izquierda.collidepoint(evento.pos):
                    pantalla_actual = "cofre"

                elif flecha_derecha.collidepoint(evento.pos):
                    pantalla_actual = "jardin"

                elif flecha_centro2.collidepoint(evento.pos):
                    pantalla_actual = "interior"

            elif pantalla_actual == "interior":
                if flecha_atras.collidepoint(evento.pos):
                    pantalla_actual = "afuera"

                elif flecha_cabina.collidepoint(evento.pos):
                    pantalla_actual = "cavina"

            elif pantalla_actual == "cavina":
                if flecha_cabina2.collidepoint(evento.pos):
                    pantalla_actual = "interior"


            
    if pantalla_actual == "inicio":
        pantalla.blit(imagen, (0, 0))
        mouse = pygame.mouse.get_pos()

        if boton_jugar.collidepoint(mouse):
            pygame.draw.rect(pantalla, (80, 80, 80), boton_jugar, 3)

    elif pantalla_actual == "carga":
        pantalla.blit(carga, (0, 0))

        if pygame.time.get_ticks() - tiempo_carga > 1000:
            pantalla_actual = "juego"

    elif pantalla_actual == "juego":
        pantalla.blit(intro, (0, 0))
        mouse = pygame.mouse.get_pos()

        if boton_jugar2.collidepoint(mouse):
            pygame.draw.rect(pantalla, (205, 170, 125), boton_jugar2, 4)

    elif pantalla_actual == "historia":
        pantalla.fill((244, 228, 188)) 
        tiempo = pygame.time.get_ticks() - tiempo_historia

        pantalla.blit(carga2, (0, 0))
        if tiempo > 2000:
            pantalla.blit(n1, (0, 0))
        if tiempo > 4000:
            pantalla.blit(n2, (0, 0))
        if tiempo > 6000:
            pantalla.blit(n3, (0, 0))
        if tiempo > 8000: 
            pantalla.blit(n4, (0, 0))
        if tiempo > 10000:
            pantalla.blit(n5, (0, 0))
        if tiempo > 12000:
            pantalla.blit(n6, (0, 0))
        if tiempo > 14000:
            pantalla.blit(n7, (0, 0))

        if tiempo > 16000:
            pantalla_actual = "comienzo"
            tiempo_comienzo = pygame.time.get_ticks()



    elif pantalla_actual == "comienzo":  
        pantalla.fill((244, 228, 188))   
        tiempo = pygame.time.get_ticks() - tiempo_comienzo


        pantalla.blit(auto1, (0, 0))

        if tiempo > 4000:
            pantalla.blit(auto2, (475, 0))
            #interfe.play()

        if tiempo > 8000:
            pantalla.blit(auto3, (920, 0))
            #interfe.stop()

            sin_arranque.play()
        if tiempo > 12000:
            pantalla_actual = "auto_parado"
            tiempo_auto_parado = pygame.time.get_ticks()
            

    elif pantalla_actual == "auto_parado":
        pantalla.fill((244, 228, 188))   
        tiempo = pygame.time.get_ticks() - tiempo_auto_parado

        pantalla.blit(parte2, (0, 0))
        sin_arranque.stop()
        if tiempo > 3000:
            pantalla.blit(parte3, (475, 0))
            #chica_auto_paro2.play()

        if tiempo > 8500:
            pantalla_actual = "llegada_estacion"
            tiempo_llegadaa = pygame.time.get_ticks()


    elif pantalla_actual == "llegada_estacion":
        pantalla.fill((244, 228, 188))  
        tiempo = pygame.time.get_ticks() - tiempo_llegadaa

        if tiempo > 2000:
            pantalla.blit(llegada1, (0, 0))
        if tiempo > 6000:
            pantalla.blit(llegada2, (475, 0))
            #ruido_tren.play()
        if tiempo > 10000:
            pantalla.blit(llegada3, (920, 0))
            #ruido_tren.stop()

        if tiempo > 14000:
            pantalla_actual = "boleto"
            tiempo_boleto = pygame.time.get_ticks()

    elif pantalla_actual == "boleto":
        pantalla.fill((244, 228, 188))  
        tiempo = pygame.time.get_ticks() - tiempo_boleto

        pantalla.blit(tren1, (0, 0))
        if tiempo > 2000:
            pantalla.blit(tren2, (470, 0))
        if tiempo > 4000:
            pantalla.blit(tren3, (920, 0))
        if tiempo > 6000:
            pantalla_actual = "charla"
            tiempo_charla = pygame.time.get_ticks()
    
    elif pantalla_actual == "charla":
        tiempo = pygame.time.get_ticks() - tiempo_charla

        pantalla.blit(man, (0, 0))
        if tiempo > 2000:
            pantalla.fill((0, 0, 0))
        if tiempo > 2500:
            pantalla.blit(charla1, (0, 0))
        if tiempo > 4500:
            pantalla.blit(charla2, (0, 0))
        if tiempo > 6500:
            pantalla.blit(charla3, (0, 0))
        if tiempo > 8500:
            pantalla.blit(charla4, (0, 0))
        if tiempo > 10500:
            pantalla.blit(charla5, (0, 0))
        if tiempo > 12500:
            pantalla.blit(charla6, (0, 0))
        if tiempo > 14500:
            pantalla.blit(charla7, (0, 0))
        if tiempo > 16500:
            pantalla.blit(charla8, (0, 0))
        if tiempo > 18500:
            pantalla.blit(maquinista1, (0, 0))
        if tiempo > 20500:
            pantalla.blit(maquinista2, (0, 0))
        if tiempo > 22500:
            pantalla.blit(charla10, (0, 0))
        if tiempo > 25000:
            pantalla.blit(charla11)
        if tiempo > 26500:
            pantalla_actual = "afuera"
        

    #lista=[charla6,"inicio_juego"]
            
    elif pantalla_actual == "jardin":
        pantalla.blit(jardin, (0,0))

        # Flecha al cofre
        pygame.draw.polygon(
            pantalla,
            (255,255,255),
            [(1320,400),(1280,350),(1280,450)]
        )

        # Flecha al invernadero
        pygame.draw.polygon(
            pantalla,
            (255,255,255),
            [(820,470),(780,510),(860,510)]
        )

        #flecha hacia el tren
        pygame.draw.polygon(
            pantalla,
            (255,255,255),
            [(80,400),(120,350),(120,450)]
        )

    elif pantalla_actual == "afuera":
        pantalla.blit(afuera, (0,0))

        pygame.draw.polygon(
            pantalla,
            (255,255,255),
            [(80,400),(120,350),(120,450)]
        )

        pygame.draw.polygon(
            pantalla,
            (255,255,255),
            [(1320,400),(1280,350),(1280,450)]
        )

        pygame.draw.polygon(
            pantalla,
            (255,255,255),
            [(700,530),(660,560),(740,560)]
        )
    
    elif pantalla_actual == "interior":
        pantalla.blit(interior, (0,0))

        pygame.draw.polygon(
            pantalla,
            (255,255,255,255),
            [(650,720),(600,660),(700,660)]
        )

        pygame.draw.polygon(
            pantalla,
            (255,255,255),
            [(685,480),(650,510),(710,510)]
        )

    elif pantalla_actual == "cofre":
        pantalla.blit(cofre, (0,0))

        pygame.draw.polygon(
            pantalla,
            (255,255,255),
            [(80,400),(120,350),(120,450)]
        )

        pygame.draw.polygon(
            pantalla,
            (255,255,255),
            [(1320,400),(1280,350),(1280,450)]
        )
    
    elif pantalla_actual == "invernadero":
        pantalla.blit(invernadero, (0,0))

        if planta_ampliada == "A":
            pantalla.blit(hoja_A, (700,200))

        elif planta_ampliada == "M":
            pantalla.blit(hoja_M, (700,200))

        elif planta_ampliada == "T":
            pantalla.blit(hoja_T, (700,200))

        elif planta_ampliada == "V":
            pantalla.blit(hoja_V, (700,200))


        pygame.draw.polygon(
            pantalla,
            (255,255,255,255),
            [(900,720),(850,660),(950,660)]
        )
    
    elif pantalla_actual == "cavina":
        pantalla.blit(maquinista1, (0,0))

        pygame.draw.polygon(
            pantalla,
            (255,255,255,255),
            [(710,720),(660,660),(760,660)]
        )


    pygame.display.flip()