import sys
import pygame
pygame.init()
pygame.mixer.init()

from Clases_POO import Juego, Imagenes, Sonidos, Inventario, Boton, Botones

juego = Juego()
#imagenes = Imagenes()
#sonidos = Sonidos()
juego.ejecutar()
pantalla = juego.obtener_pantalla()
#botones  = Botones()


#-----------FUNCIONES FLECHAS-------------------------------------------------------------
def flecha_derecha_f(x, y):
    pygame.draw.polygon(pantalla,(255,255,255),
        [(x+40,y),(x,y-50),(x,y+50)])

def flecha_izquierda_f(x, y):
    pygame.draw.polygon(pantalla,(255,255,255),
        [(x-40,y),(x,y-50),(x,y+50)])

def flecha_arriba_f(x, y):
    pygame.draw.polygon(pantalla,(255,255,255),
        [(x,y-30),(x-40,y),(x+40,y)])

def flecha_abajo_f(x, y):
    pygame.draw.polygon(pantalla,(255,255,255),
        [(x,y+60),(x-50,y),(x+50,y)])

def flecha_abajo_pequena_f(x, y):
    pygame.draw.polygon(pantalla,(255,255,255),
        [(x,y+40),(x-50,y),(x+50,y)])

def flecha_abajo_derecha_f(x, y):
    pygame.draw.polygon(pantalla,(255,255,255),
        [(x,y-40),(x,y+40),(x+40,y)])

def flecha_arriba_grande_f(x, y):
    pygame.draw.polygon(pantalla,(255,255,255),
        [(x,y-60),(x-50,y),(x+50,y)])

def flecha_camino_izq_f(x, y):
    pygame.draw.polygon(pantalla,(255,255,255),
        [(x-50,y-40),(x+20,y-30),(x-20,y+10)])

def flecha_camino_med_f(x, y):
    pygame.draw.polygon(pantalla,(255,255,255),
        [(x+50,y-40),(x-40,y-10),(x+10,y+10)])

def flecha_camino_der_f(x, y):
    pygame.draw.polygon(pantalla,(255,255,255),
        [(x-30,y-20),(x+50,y-30),(x+10,y+30)])

def flecha_libro_der_f(x, y):
    pygame.draw.polygon(pantalla,(255,255,255),
        [(x+25, y), (x, y-30), (x, y+30)])

def flecha_libro_izq_f(x, y):
    pygame.draw.polygon(pantalla,(255,255,255),
        [(x-25, y), (x, y-30), (x, y+30)])

def cambiar_pantalla_si_toca(boton, destino, evento, sonido=None):
    global pantalla_actual #le dice a la funcion que quiere modificar la variable ya existente
    if boton.collidepoint(evento.pos):
        if sonido:
            sonido.play()
        pantalla_actual = destino
        return True #si toca el boton
    return False #si no toca el boton

#--------------INVENTARIO-------------------------------------------------
imagenes_objetos = {
    "semilla_objeto": juego.imagenes.semilla_transp, 
    "llave_objeto": juego.imagenes.llave_transp,
    "fusible_objeto": juego.imagenes.fusible_transp}

#----------INICIO DEL PROGRAMA-------------------------------------------------------------------------------
juego.pantalla_actual = "jardin" #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

num_encontrado = []
num_correcto = "7352"
num_ingresado = ""


while True:
    eventos = juego.manejar_eventos()
    for evento in eventos:
        juego.manejar_teclado(evento)
        juego.manejar_mouse(evento)


    #----------------------------------------------------------------------------------------------------------  
    if juego.pantalla_actual == "inicio":
        pantalla.blit(juego.imagenes.inicio, (0, 0))
        mouse = pygame.mouse.get_pos()
        if juego.botones.boton_jugar.collidepoint(mouse):
            pygame.draw.rect(pantalla, (80, 80, 80), juego.botones.boton_jugar, 3)

    elif juego.pantalla_actual == "carga":
        pantalla.blit(juego.imagenes.carga, (0, 0))
        if pygame.time.get_ticks() - juego.tiempo_carga > 1000:
            juego.pantalla_actual = "juego"

    elif juego.pantalla_actual == "juego":
        pantalla.blit(juego.imagenes.intro, (0, 0))
        mouse = pygame.mouse.get_pos()
        if juego.botones.boton_jugar2.collidepoint(mouse):
            pygame.draw.rect(pantalla, (205, 170, 125), juego.botones.boton_jugar2, 4)

    elif juego.pantalla_actual == "historia":
        pantalla.fill((244, 228, 188)) 
        tiempo = pygame.time.get_ticks() - juego.tiempo_historia
        pantalla.blit(juego.imagenes.carga2, (0, 0))
        if tiempo > 2000:
            pantalla.blit(juego.imagenes.n1, (0, 0))
            if not sonido_n1:
                juego.sonidos.texto_gris.play()
                sonido_n1 = True
        if tiempo > 4000:
            pantalla.blit(juego.imagenes.n2, (0, 0))
        if tiempo > 6500:
            pantalla.blit(juego.imagenes.n3, (0, 0))
        if tiempo > 9500: 
            pantalla.blit(juego.imagenes.n4, (0, 0))
        if tiempo > 12500:
            pantalla.blit(juego.imagenes.n5, (0, 0))
        if tiempo > 16500:
            pantalla.blit(juego.imagenes.n6, (0, 0))
        if tiempo > 19200:
            pantalla.blit(juego.imagenes.n7, (0, 0))
            juego.pantalla_actual = "n7"

    elif juego.pantalla_actual == "comienzo":  
        juego.sonidos.texto_gris.stop()
        if not favela_reproduciendo:
            juego.sonidos.favela.play()
            favela_reproduciendo = True

        pantalla.fill((244, 228, 188))   
        tiempo = pygame.time.get_ticks() - juego.tiempo_comienzo
        pantalla.blit(juego.imagenes.auto1, (0, 0))

        if tiempo > 6000:
            juego.sonidos.favela.stop()
            pantalla.blit(juego.imagenes.auto2, (475, 0))
            juego.sonidos.interfe.play()

        if tiempo > 10000:
            pantalla.blit(juego.imagenes.auto3, (920, 0))
            juego.sonidos.interfe.stop()
            if not auto0_paro_reproducido:
                juego.sonidos.auto_paro_sonido0.play()
                auto0_paro_reproducido = True

            juego.sonidos.sin_arranque.play()
            juego.pantalla_actual = "auto3"

    elif juego.pantalla_actual == "auto_parado":
        juego.sonidos.auto_paro_sonido0.stop()
        pantalla.fill((244, 228, 188))
        tiempo = pygame.time.get_ticks() - juego.tiempo_auto_parado
        pantalla.blit(juego.imagenes.parte2, (0, 0))

        if not auto_paro_reproducido:
            juego.sonidos.auto_paro_sonido.play()
            auto_paro_reproducido = True

        if tiempo > 4000:
            juego.sonidos.auto_paro_sonido.stop()
            pantalla.blit(juego.imagenes.parte3, (475, 0))
            juego.sonidos.auto_paro_sonido2.play()
            juego.pantalla_actual = "parte3"
            juego.sonidos.sin_arranque.stop()

    elif juego.pantalla_actual == "llegada_estacion":
        juego.sonidos.auto_paro_sonido2.stop()
        pantalla.fill((244, 228, 188))  
        tiempo = pygame.time.get_ticks() - juego.tiempo_llegadaa

        if tiempo > 2000:
            pantalla.blit(juego.imagenes.llegada1, (0, 0))
            if not llegada1_son_reproduciendo:
                juego.sonidos.llegada1_sonido.play()
                llegada1_son_reproduciendo = True
        if tiempo > 6000:
            pantalla.blit(juego.imagenes.llegada2, (475, 0))
            juego.sonidos.ruido_tren.play()
            if not llegada2_son_reproduciendo:
                juego.sonidos.llegada2_sonido.play()
                llegada2_son_reproduciendo = True
        if tiempo > 10000:
            pantalla.blit(juego.imagenes.llegada3, (920, 0))
            juego.sonidos.ruido_tren.stop()
            juego.pantalla_actual = "llegada3"

    elif juego.pantalla_actual == "boleto":
        pantalla.fill((244, 228, 188))  
        tiempo = pygame.time.get_ticks() - juego.tiempo_boleto
        if tiempo > 1000:
            juego.sonidos.tren_humo.play()
            pantalla.blit(juego.imagenes.tren1, (0, 0))
        if tiempo > 3000:
            juego.sonidos.tren_humo.stop()
            pantalla.blit(juego.imagenes.tren2, (470, 0))
            if not boleto1_son_reproduciendo:
                juego.sonidos.boleto1_sonido.play()
                boleto1_son_reproduciendo = True
        if tiempo > 5000:
            pantalla.blit(juego.imagenes.tren3, (920, 0))
            juego.pantalla_actual = "tren3"
    
    elif juego.pantalla_actual == "charla":
        tiempo = pygame.time.get_ticks() - juego.tiempo_charla
        pantalla.blit(juego.imagenes.man, (0, 0))
        if tiempo > 2000:
            pantalla.fill((0, 0, 0))
        if tiempo > 2500:
            pantalla.blit(juego.imagenes.charla1, (0, 0))
            if not charla1_son_reproduciendo:
                juego.sonidos.charla1_sonido.play()
                charla1_son_reproduciendo = True
        if tiempo > 5000:
            juego.sonidos.charla1_sonido.stop()
            pantalla.blit(juego.imagenes.charla2, (0, 0))
            if not charla2_son_reproduciendo:
                juego.sonidos.charla2_sonido.play()
                charla2_son_reproduciendo = True
        if tiempo > 7000:
            juego.sonidos.charla2_sonido.stop()
            pantalla.blit(juego.imagenes.charla3, (0, 0))
            if not charla3_son_reproduciendo:
                juego.sonidos.charla3_sonido.play()
                charla3_son_reproduciendo = True
        if tiempo > 9500:
            juego.sonidos.charla3_sonido.stop()
            pantalla.blit(juego.imagenes.charla4, (0, 0))
            if not charla4_son_reproduciendo:
                juego.sonidos.charla4_sonido.play()
                charla4_son_reproduciendo = True
        if tiempo > 27000:
            juego.sonidos.charla4_sonido.stop()
            pantalla.blit(juego.imagenes.charla5, (0, 0))
            if not charla5_son_reproduciendo:
                juego.sonidos.charla5_sonido.play()
                charla5_son_reproduciendo = True
        if tiempo > 42000:
            juego.sonidos.charla5_sonido.stop()
            pantalla.blit(juego.imagenes.charla6, (0, 0))
            if not charla6_son_reproduciendo:
                juego.sonidos.charla6_sonido.play()#y cada una es unica
                charla6_son_reproduciendo = True
        if tiempo > 50000:
            juego.sonidos.charla6_sonido.stop()
            pantalla.blit(juego.imagenes.charla7, (0, 0)) 
            if not charla7_son_reproduciendo:
                juego.sonidos.charla7_sonido.play() #que raro el tren
                charla7_son_reproduciendo = True
        if tiempo > 53000:
            juego.sonidos.charla7_sonido.stop()
            pantalla.blit(juego.imagenes.charla8, (0, 0))
            if not charla8_son_reproduciendo:
                juego.sonidos.charla8_sonido.play()
                charla8_son_reproduciendo = True
        if tiempo > 57000:
            juego.sonidos.charla8_sonido.stop()
            pantalla.blit(juego.imagenes.maquinista1, (0, 0))
        if tiempo > 60000:
            pantalla.blit(juego.imagenes.maquinista2, (0, 0)) #9
            if not charla9_son_reproduciendo:
                juego.sonidos.charla9_sonido.play()
                charla9_son_reproduciendo = True
        if tiempo > 67000:
            pantalla.blit(juego.imagenes.charla10, (0, 0))
            if not charla10_son_reproduciendo:
                juego.sonidos.charla10_sonido.play()
                charla10_son_reproduciendo = True
        if tiempo > 77000:
            pantalla.blit(juego.imagenes.charla11, (0, 0))
            if not charla11_son_reproduciendo:
                juego.sonidos.charla11_sonido.play()
                charla11_son_reproduciendo = True

        if tiempo > 80000:
            pantalla.fill((0, 0, 0))
        if tiempo > 83000:
            pantalla.blit(juego.imagenes.nivel1, (0, 0))
        if tiempo > 86000:
            pantalla.blit(juego.imagenes.carga, (0, 0))
        if tiempo > 90000:
            juego.pantalla_actual = "afuera"

    elif juego.pantalla_actual == "n7":
        pantalla.blit(juego.imagenes.n7, (0,0))
        flecha_abajo_derecha_f(1340, 720)
    
    elif juego.pantalla_actual == "auto3":
        flecha_abajo_derecha_f(1340, 720)

    elif juego.pantalla_actual == "parte3":
        flecha_abajo_derecha_f(1340, 720)
    
    elif juego.pantalla_actual == "llegada3":
        flecha_abajo_derecha_f(1340, 720)

    elif juego.pantalla_actual == "tren3":
        flecha_abajo_derecha_f(1340, 720)
    #________________________________________ NIVEL 1 ___________________________________________________
    if juego.pantalla_actual in ["jardin", "afuera", "interior", "cofre",
        "cofre_zoom", "cofre_abierto", "semilla", "cofre_vacio", "invernadero", "cabina", "gracias"]:

        juego.dibujar()

    if juego.pantalla_actual == "jardin":
        flecha_derecha_f(1280, 400)
        flecha_arriba_f(820, 510)
        flecha_izquierda_f(120, 400)

    elif juego.pantalla_actual == "afuera":
        flecha_izquierda_f(120, 400)
        flecha_derecha_f(1280, 400)
        flecha_arriba_f(700, 560)
    
    elif juego.pantalla_actual == "interior":
        flecha_abajo_f(650,660)
        flecha_arriba_f(685,510)

    elif juego.pantalla_actual == "cofre":
        flecha_izquierda_f(120,400)
        flecha_derecha_f(1280,400)

    elif juego.pantalla_actual == "cofre_zoom":

        texto1 = juego.fuente.render(juego.letras[0], True, (0,0,0))
        pantalla.blit(texto1, (493,290))
        texto2 = juego.fuente.render(juego.letras[1], True, (0,0,0))
        pantalla.blit(texto2, (607,290))
        texto3 = juego.fuente.render(juego.letras[2], True, (0,0,0))
        pantalla.blit(texto3, (723,290))
        texto4 = juego.fuente.render(juego.letras[3], True, (0,0,0))
        pantalla.blit(texto4, (837,290))

        pygame.draw.rect(pantalla, (255,0,0), juego.botones.rueda1, 2)
        pygame.draw.rect(pantalla, (255,0,0), juego.botones.rueda2, 2)
        pygame.draw.rect(pantalla, (255,0,0), juego.botones.rueda3, 2)
        pygame.draw.rect(pantalla, (255,0,0), juego.botones.rueda4, 2)

        if "".join(juego.letras) == "AMTV": #mantener esto en el programa principal
            juego.tiempo_cofre_abierto = pygame.time.get_ticks()
            juego.pantalla_actual = "cofre_abierto"

    elif juego.pantalla_actual == "cofre_abierto":
        flecha_izquierda_f(120,400)
        flecha_derecha_f(1280,400)

        if pygame.time.get_ticks() - juego.tiempo_cofre_abierto > 1000:
                    juego.sonidos.cofre_efecto.play()
                    juego.pantalla_actual = "cofre_abierto"

    elif juego.pantalla_actual == "semilla":
        flecha_abajo_f(710,660)

    elif juego.pantalla_actual == "cofre_vacio":
        flecha_abajo_f(710,660)
        juego.sonidos.semilla_efecto.stop()

    elif juego.pantalla_actual == "invernadero":
        if juego.planta_ampliada == "A":
            pantalla.blit(juego.imagenes.hoja_A, (700,200))
        elif juego.planta_ampliada == "M":
            pantalla.blit(juego.imagenes.hoja_M, (700,200))
        elif juego.planta_ampliada == "T":
            pantalla.blit(juego.imagenes.hoja_T, (700,200))
        elif juego.planta_ampliada == "V":
            pantalla.blit(juego.imagenes.hoja_V, (700,200))

        flecha_abajo_f(900,660)

    elif juego.pantalla_actual == "cabina":
        if juego.maquinista_hablando:
            pantalla.blit(juego.imagenes.maquinista2, (0,0))
        else:
            pantalla.blit(juego.imagenes.maquinista1, (0,0))

        pygame.draw.rect(pantalla, (255,0,0), juego.botones.botonMaquinista, 2)
        flecha_abajo_f(710,660)
        if juego.maquinista_hablando:
            if pygame.time.get_ticks() - juego.tiempo_maquinista > 6000:
                juego.maquinista_hablando = False
                juego.charla9_son_reproduciendo = False

        flecha_abajo_f(710,660)

    elif juego.pantalla_actual == "gracias":
        pantalla.blit(juego.imagenes.gracias1,(0,0))
        tiempo = pygame.time.get_ticks() - juego.tiempo_gracias
        if tiempo < 100:
            if not juego.maquinista_gracias1_son_reproduciendo:
                juego.sonidos.maquinista_gracias1.play()
                juego.maquinista_gracias1_son_reproduciendo = True
        if tiempo > 5000:
            pantalla.fill((0, 0, 0))
        if tiempo > 7000:
            pantalla.blit(juego.imagenes.nivel2, (0, 0))
        if tiempo > 12000:
            pantalla.blit(juego.imagenes.carga, (0, 0))
        if tiempo > 14000:
            juego.pantalla_actual = "intro_archivo"
            tiempo_intro2 = pygame.time.get_ticks()
           
    #________________________________________ NIVEL 2 ___________________________________________________
    elif juego.pantalla_actual == "intro_archivo":
        tiempo = pygame.time.get_ticks() - tiempo_intro2
        if tiempo > 2000:
            pantalla.blit(juego.imagenes.intro_archivo, (0,0))
            if not juego.viejo_intro2_son_reproduciendo:
                juego.sonidos.viejo_intro2.play()
                juego.viejo_intro2_son_reproduciendo = True
            
        if tiempo > 8500:
            juego.sonidos.viejo_intro2.stop()
            juego.viejo_intro2_son_reproduciendo = False
            pantalla.blit(juego.imagenes.cabina2_hablando,(0,0))
            if not juego.maquinista2_intro_son_reproduciendo:
                juego.sonidos.maquinista2_intro.play()
                juego.maquinista2_intro_son_reproduciendo = True
            
        if tiempo > 14000:
            juego.sonidos.maquinista2_intro.stop()
            juego.maquinista2_intro_son_reproduciendo = False
            pantalla.fill((0, 0, 0))
        if tiempo > 15000:
            juego.pantalla_actual = "archivo"

    elif juego.pantalla_actual == "archivo":
        pantalla.blit(juego.imagenes.afuera2, (0, 0))
        flecha_arriba_f(680,610)
        flecha_abajo_f(680,680)

    elif juego.pantalla_actual == "caminos":
        pantalla.blit(juego.imagenes.camino, (0, 0))
        flecha_abajo_f(730,680)
        flecha_camino_izq_f(580,600)
        flecha_camino_med_f(800,570)
        flecha_camino_der_f(910,610)

    elif juego.pantalla_actual == "casa":
        pantalla.blit(juego.imagenes.casa_afuera, (0,0))
        flecha_izquierda_f(100, 400)
        flecha_arriba_f(1000, 450)

    elif juego.pantalla_actual == "casa2":
        if juego.panel_resuelto == False:
            pantalla.blit(juego.imagenes.casa_adentro, (0, 0))
            juego.LLL=False
        if juego.panel_resuelto == True:
            juego.LLL=True
            if juego.llave_recogida == True:
                pantalla.blit(juego.imagenes.llave2, (0,0))
                juego.LLL= False
            else:
                pantalla.blit(juego.imagenes.llave1, (0,0))
            
        flecha_izquierda_f(100, 400)

    elif juego.pantalla_actual == "panel":
        pantalla.blit(juego.imagenes.panel, (0,0))
        if juego.palancas[0]:
            pantalla.blit(juego.imagenes.palanca_arriba, (150,200))
        else:
            juego.pantalla.blit(juego.imagenes.palanca_abajo, (150, 280))
        if juego.palancas[1]:
            pantalla.blit(juego.imagenes.palanca_arriba, (420,200))
        else:
            pantalla.blit(juego.imagenes.palanca_abajo, (420, 280))
        if juego.palancas[2]:
            pantalla.blit(juego.imagenes.palanca_arriba, (700,200))
        else:
            pantalla.blit(juego.imagenes.palanca_abajo, (700, 280))
        if juego.palancas[3]:
            pantalla.blit(juego.imagenes.palanca_arriba, (970,200))
        else:
            pantalla.blit(juego.imagenes.palanca_abajo, (970, 280))
        if juego.palancas == [False, True, False, True]:
            juego.panel_resuelto = True 
            
        flecha_abajo_f(710,660)

    elif juego.pantalla_actual == "libro":
        pantalla.blit(juego.imagenes.libro, (0, 0))

        if juego.libro_abierto:
            sombra = pygame.Surface((1400,800))
            sombra.set_alpha(150)
            sombra.fill((0,0,0))
            pantalla.blit(sombra, (0,0))

            if juego.pagina_libro == 1:
                pantalla.blit(juego.imagenes.libro1, (250,150))
                flecha_libro_der_f(1080,550)
            elif juego.pagina_libro == 2:
                pantalla.blit(juego.imagenes.libro2, (250,150))
                flecha_libro_izq_f(320,550)
                flecha_libro_der_f(1080,550)
            elif juego.pagina_libro == 3:
                pantalla.blit(juego.imagenes.libro3, (250,150))
                flecha_libro_izq_f(320,550)
                flecha_libro_der_f(1080,550)
            elif juego.pagina_libro == 4:
                pantalla.blit(juego.imagenes.libro5, (250,150))
                flecha_libro_izq_f(320,550)
                flecha_libro_der_f(1080,550)
            elif juego.pagina_libro == 5:
                pantalla.blit(juego.imagenes.libro4, (250,150))
                flecha_libro_izq_f(320,550)

        flecha_abajo_derecha_f(1250,500)
        flecha_abajo_derecha_f(1250, 500)

    elif juego.pantalla_actual == "puerta_biblioteca":
        pantalla.blit(juego.imagenes.puerta, (0, 0))
        flecha_abajo_pequena_f(680, 690)
        flecha_arriba_f(680, 500)

    elif juego.pantalla_actual == "puerta":
        pantalla.blit(juego.imagenes.puerta_zoom, (0, 0))
        flecha_abajo_pequena_f(700, 710)

        if juego.Mensaje_ce:
            pygame.draw.rect(pantalla, (40,40,40), (1100,40,200,35))
            pygame.draw.rect(pantalla, (255,255,255), (1100,40,200,35), 2)  
            Cerrado = juego.fuente_pequenia.render("Cerrado", True, (255,255,255))
            juego.sonidos.efecto_Pcerrado.play()
            pantalla.blit(Cerrado, (1150,40))

            if pygame.time.get_ticks() - tiempo_cerrado > 2000:
                juego.Mensaje_ce = False

    elif juego.pantalla_actual == "puerta_abierta1":
        pantalla.blit(juego.imagenes.puerta_abierta1, (0,0))
        flecha_abajo_pequena_f(700, 710)

    elif juego.pantalla_actual == "puerta_interior":
        pantalla.blit(juego.imagenes.inte_biblio,(0,0))
        flecha_derecha_f(1280,400)
        flecha_abajo_pequena_f(700, 710)

    elif juego.pantalla_actual == "sala_mapa":
        pantalla.blit(juego.imagenes.mapa,(0,0))
        flecha_abajo_pequena_f(700, 710)

    elif juego.pantalla_actual == "cofre_cerrado_archivo":
        pantalla.blit(juego.imagenes.cofre_archi, (0,0))
        num1 = juego.fuente.render(str(juego.numeros[0]), True, (255,255,255))
        pantalla.blit(juego.num1, (530,480))
        num2 = juego.fuente.render(str(juego.numeros[1]), True, (255,255,255))
        pantalla.blit(juego.num2, (650,480))
        num3 = juego.fuente.render(str(juego.numeros[2]), True, (255,255,255))
        pantalla.blit(juego.num3, (770,480))
        num4 = juego.fuente.render(str(juego.numeros[3]), True, (255,255,255))
        pantalla.blit(juego.num4, (880,480))

        flecha_abajo_pequena_f(700, 710)

        if juego.numeros == [7,3,5,2]:
            juego.pantalla_actual = "cofre_abierto2"
            juego.sonidos.cofre_efecto.play()

    elif juego.pantalla_actual == "cofre_abierto2":
        if juego.fusible_recogido:
            pantalla.blit(juego.imagenes.cofre_vacio2, (0,0))
        else:
            pantalla.blit(juego.imagenes.cofre_abierto2, (0,0))
        flecha_abajo_pequena_f(700, 710)
             
    elif juego.pantalla_actual == "interior2":
        pantalla.blit(juego.imagenes.archivo2_viejo, (0,0))
        flecha_abajo_f(620,660)
        flecha_arriba_f(640,550)
        pygame.draw.rect(pantalla, (255,0,0), juego.botones.boton_viejo, 2)
    
    elif juego.pantalla_actual == "cabina2":
        if juego.sonidos.maquinista2_intro_son_reproduciendo:
            pantalla.blit(juego.imagenes.maquinista_fusible, (0,0))
            tiempo = pygame.time.get_ticks() - juego.tiempo_maquinista2
            if tiempo > 4000:
                juego.maquinista_intro_son_reproduciendo = False
                pantalla.blit(juego.imagenes.cabina2,(0,0))
        else:
            pantalla.blit(juego.imagenes.cabina2,(0,0))
                
        flecha_abajo_f(710,660)

    elif juego.pantalla_actual == "gracias2":
        pantalla.blit(juego.imagenes.gracias2,(0,0))
        tiempo = pygame.time.get_ticks() - juego.tiempo_gracias
        if tiempo < 100:
            if not juego.maquinista_gracias2_son_reproduciendo:
                juego.sonidos.maquinista_gracias2.play()
                juego.maquinista_gracias2_son_reproduciendo = True
    
        if tiempo > 5000:
            pantalla.fill((0, 0, 0))
        if tiempo > 7000:
            pantalla.blit(juego.imagenes.nivel3, (0, 0))
        if tiempo > 12000:
            pantalla.blit(juego.imagenes.carga, (0, 0))
        if tiempo > 14000:
            juego.pantalla_actual = "nivel3" 
#------------------------------------------------------------------------
    pantallas_ocultas = ["inicio", "carga", "juego", "historia", "n7", "comienzo", "auto3",
                        "auto_parado", "parte3", "llegada_estacion", "llegada3", "boleto", "tren3", "charla"]
    juego.inventario.dibujar(pantalla, juego.imagenes)
    
    pygame.display.flip()