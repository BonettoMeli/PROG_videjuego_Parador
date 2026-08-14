import sys
import pygame
pygame.init()
pygame.mixer.init()

from Clases_POO import Juego, Imagenes, Sonidos, Inventario, Boton, Botones

juego = Juego()
imagenes = Imagenes()
sonidos = Sonidos()
inventario = Inventario()
juego.ejecutar()
pantalla = juego.obtener_pantalla()
botones  = Botones()

#-------------------- NIVEL 1 --------------------------------------------
fuente = pygame.font.SysFont("Times New Roman", 80)
fuente_pequenia = pygame.font.SysFont("Times New Roman", 25)

#-------------------- NIVEL 2 --------------------------------------------
tiempo_maquinista = 0
tiempo_gracias = 0
tiempo_intro2 = 0

numeros = [0,0,0,0]
def siguiente_numero(numero):
    return (numero + 1) % 10

palancas = [False, False, False, False]
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
    "semilla_objeto": imagenes.semilla_transp, 
    "llave_objeto": imagenes.llave_transp,
    "fusible_objeto": imagenes.fusible_transp}

#----------INICIO DEL PROGRAMA-------------------------------------------------------------------------------
pantalla_actual = "jardin" #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
tiempo_carga = 0
tiempo_historia = 0

num_encontrado = []
num_correcto = "7352"
num_ingresado = ""

inventario_abierto = False

libro_abierto = False
pagina_libro = 1
panel_resuelto = False
llave_recogida = False
puerta_abierta = False
fusible_recogido = False

Mensaje_ce = False
tiempo_cerrado = 0

while True:
    eventos = juego.manejar_eventos()
    for evento in eventos:
        juego.manejar_teclado(evento)

        if evento.type == pygame.MOUSEBUTTONDOWN:
            inventario.manejar_click(evento.pos, pantalla_actual, pantallas_ocultas)

            if pantalla_actual == "inicio": # BOTÓN DEL MENÚ PRINCIPAL
                cambiar_pantalla_si_toca(botones.boton_jugar,"carga",evento,sonidos.botonson)
                tiempo_carga = pygame.time.get_ticks()

            elif pantalla_actual == "juego": # BOTÓN DE LA PANTALLA DE INSTRUCCIONES
                cambiar_pantalla_si_toca(botones.boton_jugar2,"historia",evento,sonidos.botonson)
                tiempo_historia = pygame.time.get_ticks()
            
            elif pantalla_actual == "n7":
                cambiar_pantalla_si_toca(botones.flecha_abajo_derecha,"comienzo",evento)
                tiempo_comienzo = pygame.time.get_ticks()
            
            elif pantalla_actual == "auto3":
                cambiar_pantalla_si_toca(botones.flecha_abajo_derecha,"auto_parado",evento)
                tiempo_auto_parado = pygame.time.get_ticks()
            
            elif pantalla_actual == "parte3":
                cambiar_pantalla_si_toca(botones.flecha_abajo_derecha,"llegada_estacion",evento)
                tiempo_llegadaa = pygame.time.get_ticks()

            elif pantalla_actual == "llegada3":
                cambiar_pantalla_si_toca(botones.flecha_abajo_derecha,"boleto",evento)
                tiempo_boleto = pygame.time.get_ticks()

            elif pantalla_actual == "tren3":
                cambiar_pantalla_si_toca(botones.flecha_abajo_derecha,"charla",evento)
                tiempo_charla = pygame.time.get_ticks()

            #-----------------------------nivel 1-------------------------------------------------------
            elif pantalla_actual == "jardin":
                cambiar_pantalla_si_toca(botones.flecha_centro, "invernadero", evento)
                cambiar_pantalla_si_toca(botones.flecha_izquierda, "afuera", evento)
                if botones.flecha_derecha.collidepoint(evento.pos):
                    if juego.nivel1.AAA:
                        pantalla_actual = "cofre"
                    else:
                        pantalla_actual = "cofre_abierto"

            elif pantalla_actual == "invernadero":
                if juego.nivel1.planta_ampliada is not None:
                    juego.nivel1.planta_ampliada = None

                if botones.planta_A.collidepoint(evento.pos):
                    juego.nivel1.planta_ampliada = "A"

                elif botones.planta_M.collidepoint(evento.pos):
                    juego.nivel1.planta_ampliada = "M"

                elif botones.planta_T.collidepoint(evento.pos):
                    juego.nivel1.planta_ampliada = "T"

                elif botones.planta_V.collidepoint(evento.pos):
                    juego.nivel1.planta_ampliada = "V"
                    
                elif botones.flecha_abajo.collidepoint(evento.pos):
                    pantalla_actual = "jardin"


            elif pantalla_actual == "cofre":
                if botones.BAcertijo.collidepoint(evento.pos):
                    juego.sonidos.acertijo1.play()

                elif cambiar_pantalla_si_toca(botones.flecha_izquierda,"jardin",evento):
                    juego.sonidos.acertijo1.stop()

                elif cambiar_pantalla_si_toca(botones.flecha_derecha,"afuera",evento):
                    juego.sonidos.acertijo1.stop()

                cambiar_pantalla_si_toca(botones.flecha_centro_central,"cofre_zoom",evento)

            elif pantalla_actual == "cofre_abierto":
                cambiar_pantalla_si_toca(botones.flecha_izquierda,"jardin",evento)
                cambiar_pantalla_si_toca(botones.flecha_derecha,"afuera",evento)
                
                if botones.flecha_centro_central.collidepoint(evento.pos):
                    if juego.nivel1.BBB == True:
                        juego.sonidos.semilla_efecto.play()
                        pantalla_actual = "semilla"
                    else:
                        pantalla_actual = "cofre_vacio"
            
            elif pantalla_actual == "cofre_zoom":
                if botones.flecha_cabina2.collidepoint(evento.pos):
                    if juego.nivel1.AAA == True:
                        pantalla_actual = "cofre"
                    else:
                        pantalla_actual = "cofre_abierto"

                if botones.rueda1.collidepoint(evento.pos):
                        juego.nivel1.letras[0] = juego.nivel1.siguiente_letra(juego.nivel1.letras[0])

                elif botones.rueda2.collidepoint(evento.pos):
                        juego.nivel1.letras[1] = juego.nivel1.siguiente_letra(juego.nivel1.letras[1])

                elif botones.rueda3.collidepoint(evento.pos):
                        juego.nivel1.letras[2] = juego.nivel1.siguiente_letra(juego.nivel1.letras[2])

                elif botones.rueda4.collidepoint(evento.pos):
                        juego.nivel1.letras[3] = juego.nivel1.siguiente_letra(juego.nivel1.letras[3])

            elif pantalla_actual == "semilla":
                if cambiar_pantalla_si_toca(botones.flecha_cabina2,"cofre_abierto",evento):
                    juego.nivel1.AAA = False
                if cambiar_pantalla_si_toca(botones.flecha_centro_central_peque,"cofre_vacio",evento): #si selecciona la semilla...
                    inventario.objetos.append("semilla_objeto")
                    print(inventario.objetos)
                    juego.nivel1.BBB = False

            elif pantalla_actual == "cofre_vacio":
                if cambiar_pantalla_si_toca(botones.flecha_cabina2,"cofre_abierto",evento):
                    juego.nivel1.AAA = False

            elif pantalla_actual == "afuera":
                juego.sonidos.cascada.play()
                if botones.flecha_izquierda.collidepoint(evento.pos):
                    if juego.nivel1.AAA == True:
                        pantalla_actual = "cofre"
                    else:
                        pantalla_actual = "cofre_abierto"
                cambiar_pantalla_si_toca(botones.flecha_derecha,"jardin",evento)
                cambiar_pantalla_si_toca(botones.flecha_centro2,"interior",evento)

            elif pantalla_actual == "interior":
                cambiar_pantalla_si_toca(botones.flecha_atras,"afuera",evento)
                cambiar_pantalla_si_toca(botones.flecha_cabina,"cabina",evento)

            elif pantalla_actual == "cabina":
                if botones.botonMaquinista.collidepoint(evento.pos):
                    if inventario.objeto_seleccionado == "semilla_objeto":
                        inventario.objetos.remove("semilla_objeto")
                        inventario.objeto_seleccionado = None
                        pantalla_actual = "gracias"
                        juego.nivel1.tiempo_gracias = pygame.time.get_ticks()
                    else:
                        if not juego.charla9_son_reproduciendo:
                            juego.sonidos.charla9_sonido.play()
                            charla9_son_reproduciendo = True
                            juego.nivel1.maquinista_hablando = True
                            tiempo_maquinista = pygame.time.get_ticks()

                if cambiar_pantalla_si_toca(botones.flecha_cabina2,"interior",evento):
                    juego.sonidos.charla9_sonido.stop()
                    juego.charla9_son_reproduciendo = False
                    juego.nivel1.maquinista_hablando = False

                #------------------------------- NIVEL 2 (flechas y botones)-----------------------------------------------
            elif pantalla_actual == "archivo":
                cambiar_pantalla_si_toca(botones.BCentro_n2,"caminos",evento)
                cambiar_pantalla_si_toca(botones.B_interior,"interior2",evento)
                viejo_libro_son_reproduciendo = False

            elif pantalla_actual == "caminos":
                cambiar_pantalla_si_toca(botones.camino1,"libro",evento)
                cambiar_pantalla_si_toca(botones.atras,"archivo",evento)
                cambiar_pantalla_si_toca(botones.camino2,"puerta_biblioteca",evento)
                cambiar_pantalla_si_toca(botones.camino3,"casa",evento)

            elif pantalla_actual == "casa":
                cambiar_pantalla_si_toca(botones.flecha_izquierda,"caminos",evento)
                cambiar_pantalla_si_toca(botones.flecha_centro_casa,"casa2",evento)

            elif pantalla_actual == "casa2":
                cambiar_pantalla_si_toca(botones.flecha_izquierda,"casa",evento)
                cambiar_pantalla_si_toca(botones.B_palancas,"panel",evento)
                if LLL == True:
                    juego.sonidos.sistema_poleas.play()
                    if botones.B_llave.collidepoint(evento.pos):
                        llave_recogida=True
                        inventario.objetos.append("llave_objeto")
                        print(inventario.objetos)
                        LLL=False

            elif pantalla_actual == "puerta_biblioteca":
                cambiar_pantalla_si_toca(botones.atras,"caminos",evento)
                cambiar_pantalla_si_toca(botones.flecha_centro_central_peque,"puerta",evento)

            elif pantalla_actual == "libro":
                if botones.B_libro.collidepoint(evento.pos):
                    libro_abierto = True

                elif botones.B_flecha_libro_der.collidepoint(evento.pos):
                    if pagina_libro < 5:
                        pagina_libro += 1
                        juego.sonidos.efecto_hoja.play()
                elif botones.B_flecha_libro_izq.collidepoint(evento.pos):
                    if pagina_libro > 1:
                        pagina_libro -= 1
                        juego.sonidos.efecto_hoja.play()

                elif botones.B_libro_atras.collidepoint(evento.pos):
                    libro_abierto = False
                    pagina_libro = 1
                    pantalla_actual = "caminos"
                elif not botones.Rect_libro.collidepoint(evento.pos):
                    libro_abierto = False

            elif pantalla_actual == "panel":
                if botones.B_palanca1.collidepoint(evento.pos):
                    palancas[0] = not palancas[0]
                    juego.sonidos.efecto_palanca.play()
                elif botones.B_palanca2.collidepoint(evento.pos):
                    palancas[1] = not palancas[1]
                    juego.sonidos.efecto_palanca.play()
                elif botones.B_palanca3.collidepoint(evento.pos):
                    palancas[2] = not palancas[2]
                    juego.sonidos.efecto_palanca.play()
                elif botones.B_palanca4.collidepoint(evento.pos):
                    palancas[3] = not palancas[3]
                    juego.sonidos.efecto_palanca.play()
                cambiar_pantalla_si_toca(botones.flecha_cabina2,"casa2",evento)


            elif pantalla_actual == "puerta":
                cambiar_pantalla_si_toca(botones.atras, "puerta_biblioteca", evento)

                if botones.B_puerta.collidepoint(evento.pos):
                    if puerta_abierta:
                        pantalla_actual = "puerta_abierta1"
                    elif inventario.objeto_seleccionado == "llave_objeto":
                        inventario.objetos.remove("llave_objeto")
                        inventario.objeto_seleccionado = None
                        puerta_abierta = True
                        pantalla_actual = "puerta_abierta1"
                        juego.sonidos.efecto_Pabierta.play()
                    else:
                        Mensaje_ce = True
                        tiempo_cerrado = pygame.time.get_ticks()

            elif pantalla_actual == "puerta_abierta1":
                cambiar_pantalla_si_toca(botones.atras,"puerta_biblioteca",evento)
                cambiar_pantalla_si_toca(botones.B_puerta,"puerta_interior",evento)

            elif pantalla_actual == "puerta_interior":
                cambiar_pantalla_si_toca(botones.flecha_derecha,"sala_mapa",evento)
                cambiar_pantalla_si_toca(botones.B_volver_puerta,"puerta",evento)
                cambiar_pantalla_si_toca(botones.cofre_A,"cofre_cerrado_archivo",evento)

            elif pantalla_actual == "cofre_cerrado_archivo":
                cambiar_pantalla_si_toca(botones.B_volver_puerta,"puerta_interior",evento)
                if botones.C_num1.collidepoint(evento.pos):
                    numeros[0] = siguiente_numero(numeros[0])

                elif botones.C_num2.collidepoint(evento.pos):
                    numeros[1] = siguiente_numero(numeros[1])

                elif botones.C_num3.collidepoint(evento.pos):
                    numeros[2] = siguiente_numero(numeros[2])

                elif botones.C_num4.collidepoint(evento.pos):
                    numeros[3] = siguiente_numero(numeros[3])

            elif pantalla_actual == "cofre_abierto2":
                cambiar_pantalla_si_toca(botones.B_volver_puerta , "puerta_interior", evento)
        
                if botones.B_fusible.collidepoint(evento.pos):
                    if not fusible_recogido:
                        fusible_recogido = True
                        inventario.objetos.append("fusible_objeto")
                        print(inventario.objetos)

            elif pantalla_actual == "sala_mapa":
                cambiar_pantalla_si_toca(botones.B_volver_puerta,"puerta_interior",evento)

            elif pantalla_actual == "interior2":
                cambiar_pantalla_si_toca(botones.flecha_atras,"archivo",evento) 
                cambiar_pantalla_si_toca(botones.flecha_cabina,"cabina2",evento)               
                if botones.boton_viejo.collidepoint(evento.pos):
                    if not viejo_libro_son_reproduciendo:
                        juego.sonidos.viejo_libro.play()
                        viejo_libro_son_reproduciendo = True
                    else:
                        viejo_libro_son_reproduciendo = False
                if not pantalla_actual == "interior2":
                    juego.sonidos.viejo_libro.stop()

            elif pantalla_actual == "cabina2":
                if cambiar_pantalla_si_toca(botones.flecha_cabina2,"interior2",evento):
                    juego.sonidos.maquinista2_intro.stop()
                    juego.sonidos.viejo_libro.stop()
                if botones.botonMaquinista.collidepoint(evento.pos):

                    if inventario.objeto_seleccionado == "fusible_objeto":
                        inventario.objetos.remove("fusible_objeto")
                        inventario.objeto_seleccionado = None
                        pantalla_actual = "gracias2"
                        juego.nivel1.tiempo_gracias = pygame.time.get_ticks()
                    else:
                        if not maquinista2_intro_son_reproduciendo:
                            juego.sonidos.maquinista2_intro.play()
                            maquinista2_intro_son_reproduciendo = True
                            tiempo_maquinista2 = pygame.time.get_ticks()

                if cambiar_pantalla_si_toca(botones.flecha_cabina2,"interior2",evento):
                    juego.sonidos.maquinista2_intro.stop()
                    maquinista2_intro_son_reproduciendo = False
                    juego.maquinista_hablando2 = False
    #----------------------------------------------------------------------------------------------------------  
    if pantalla_actual == "inicio":
        pantalla.blit(imagenes.inicio, (0, 0))
        mouse = pygame.mouse.get_pos()
        if botones.boton_jugar.collidepoint(mouse):
            pygame.draw.rect(pantalla, (80, 80, 80), botones.boton_jugar, 3)

    elif pantalla_actual == "carga":
        pantalla.blit(imagenes.carga, (0, 0))
        if pygame.time.get_ticks() - tiempo_carga > 1000:
            pantalla_actual = "juego"

    elif pantalla_actual == "juego":
        pantalla.blit(imagenes.intro, (0, 0))
        mouse = pygame.mouse.get_pos()
        if botones.boton_jugar2.collidepoint(mouse):
            pygame.draw.rect(pantalla, (205, 170, 125), botones.boton_jugar2, 4)

    elif pantalla_actual == "historia":
        pantalla.fill((244, 228, 188)) 
        tiempo = pygame.time.get_ticks() - tiempo_historia
        pantalla.blit(imagenes.carga2, (0, 0))
        if tiempo > 2000:
            pantalla.blit(imagenes.n1, (0, 0))
            if not sonido_n1:
                juego.sonidos.texto_gris.play()
                sonido_n1 = True
        if tiempo > 4000:
            pantalla.blit(imagenes.n2, (0, 0))
        if tiempo > 6500:
            pantalla.blit(imagenes.n3, (0, 0))
        if tiempo > 9500: 
            pantalla.blit(imagenes.n4, (0, 0))
        if tiempo > 12500:
            pantalla.blit(imagenes.n5, (0, 0))
        if tiempo > 16500:
            pantalla.blit(imagenes.n6, (0, 0))
        if tiempo > 19200:
            pantalla.blit(imagenes.n7, (0, 0))
            pantalla_actual = "n7"

    elif pantalla_actual == "comienzo":  
        juego.sonidos.texto_gris.stop()
        if not favela_reproduciendo:
            juego.sonidos.favela.play()
            favela_reproduciendo = True

        pantalla.fill((244, 228, 188))   
        tiempo = pygame.time.get_ticks() - tiempo_comienzo
        pantalla.blit(imagenes.auto1, (0, 0))

        if tiempo > 6000:
            juego.sonidos.favela.stop()
            pantalla.blit(imagenes.auto2, (475, 0))
            juego.sonidos.interfe.play()

        if tiempo > 10000:
            pantalla.blit(imagenes.auto3, (920, 0))
            juego.sonidos.interfe.stop()
            if not auto0_paro_reproducido:
                juego.sonidos.auto_paro_sonido0.play()
                auto0_paro_reproducido = True

            juego.sonidos.sin_arranque.play()
            pantalla_actual = "auto3"

    elif pantalla_actual == "auto_parado":
        juego.sonidos.auto_paro_sonido0.stop()
        pantalla.fill((244, 228, 188))
        tiempo = pygame.time.get_ticks() - tiempo_auto_parado
        pantalla.blit(imagenes.parte2, (0, 0))

        if not auto_paro_reproducido:
            juego.sonidos.auto_paro_sonido.play()
            auto_paro_reproducido = True

        if tiempo > 4000:
            juego.sonidos.auto_paro_sonido.stop()
            pantalla.blit(imagenes.parte3, (475, 0))
            juego.sonidos.auto_paro_sonido2.play()
            pantalla_actual = "parte3"
            juego.sonidos.sin_arranque.stop()

    elif pantalla_actual == "llegada_estacion":
        juego.sonidos.auto_paro_sonido2.stop()
        pantalla.fill((244, 228, 188))  
        tiempo = pygame.time.get_ticks() - tiempo_llegadaa

        if tiempo > 2000:
            pantalla.blit(imagenes.llegada1, (0, 0))
            if not llegada1_son_reproduciendo:
                juego.sonidos.llegada1_sonido.play()
                llegada1_son_reproduciendo = True
        if tiempo > 6000:
            pantalla.blit(imagenes.llegada2, (475, 0))
            juego.sonidos.ruido_tren.play()
            if not llegada2_son_reproduciendo:
                juego.sonidos.llegada2_sonido.play()
                llegada2_son_reproduciendo = True
        if tiempo > 10000:
            pantalla.blit(imagenes.llegada3, (920, 0))
            juego.sonidos.ruido_tren.stop()
            pantalla_actual = "llegada3"

    elif pantalla_actual == "boleto":
        pantalla.fill((244, 228, 188))  
        tiempo = pygame.time.get_ticks() - tiempo_boleto
        if tiempo > 1000:
            juego.sonidos.tren_humo.play()
            pantalla.blit(imagenes.tren1, (0, 0))
        if tiempo > 3000:
            juego.sonidos.tren_humo.stop()
            pantalla.blit(imagenes.tren2, (470, 0))
            if not boleto1_son_reproduciendo:
                juego.sonidos.boleto1_sonido.play()
                boleto1_son_reproduciendo = True
        if tiempo > 5000:
            pantalla.blit(imagenes.tren3, (920, 0))
            pantalla_actual = "tren3"
    
    elif pantalla_actual == "charla":
        tiempo = pygame.time.get_ticks() - tiempo_charla
        pantalla.blit(imagenes.man, (0, 0))
        if tiempo > 2000:
            pantalla.fill((0, 0, 0))
        if tiempo > 2500:
            pantalla.blit(imagenes.charla1, (0, 0))
            if not charla1_son_reproduciendo:
                juego.sonidos.charla1_sonido.play()
                charla1_son_reproduciendo = True
        if tiempo > 5000:
            juego.sonidos.charla1_sonido.stop()
            pantalla.blit(imagenes.charla2, (0, 0))
            if not charla2_son_reproduciendo:
                juego.sonidos.charla2_sonido.play()
                charla2_son_reproduciendo = True
        if tiempo > 7000:
            juego.sonidos.charla2_sonido.stop()
            pantalla.blit(imagenes.charla3, (0, 0))
            if not charla3_son_reproduciendo:
                juego.sonidos.charla3_sonido.play()
                charla3_son_reproduciendo = True
        if tiempo > 9500:
            juego.sonidos.charla3_sonido.stop()
            pantalla.blit(imagenes.charla4, (0, 0))
            if not charla4_son_reproduciendo:
                juego.sonidos.charla4_sonido.play()
                charla4_son_reproduciendo = True
        if tiempo > 27000:
            juego.sonidos.charla4_sonido.stop()
            pantalla.blit(imagenes.charla5, (0, 0))
            if not charla5_son_reproduciendo:
                juego.sonidos.charla5_sonido.play()
                charla5_son_reproduciendo = True
        if tiempo > 42000:
            juego.sonidos.charla5_sonido.stop()
            pantalla.blit(imagenes.charla6, (0, 0))
            if not charla6_son_reproduciendo:
                juego.sonidos.charla6_sonido.play()#y cada una es unica
                charla6_son_reproduciendo = True
        if tiempo > 50000:
            juego.sonidos.charla6_sonido.stop()
            pantalla.blit(imagenes.charla7, (0, 0)) 
            if not charla7_son_reproduciendo:
                juego.sonidos.charla7_sonido.play() #que raro el tren
                charla7_son_reproduciendo = True
        if tiempo > 53000:
            juego.sonidos.charla7_sonido.stop()
            pantalla.blit(imagenes.charla8, (0, 0))
            if not charla8_son_reproduciendo:
                juego.sonidos.charla8_sonido.play()
                charla8_son_reproduciendo = True
        if tiempo > 57000:
            juego.sonidos.charla8_sonido.stop()
            pantalla.blit(imagenes.maquinista1, (0, 0))
        if tiempo > 60000:
            pantalla.blit(imagenes.maquinista2, (0, 0)) #9
            if not charla9_son_reproduciendo:
                juego.sonidos.charla9_sonido.play()
                charla9_son_reproduciendo = True
        if tiempo > 67000:
            pantalla.blit(imagenes.charla10, (0, 0))
            if not charla10_son_reproduciendo:
                juego.sonidos.charla10_sonido.play()
                charla10_son_reproduciendo = True
        if tiempo > 77000:
            pantalla.blit(imagenes.charla11, (0, 0))
            if not charla11_son_reproduciendo:
                juego.sonidos.charla11_sonido.play()
                charla11_son_reproduciendo = True

        if tiempo > 80000:
            pantalla.fill((0, 0, 0))
        if tiempo > 83000:
            pantalla.blit(imagenes.nivel1, (0, 0))
        if tiempo > 86000:
            pantalla.blit(imagenes.carga, (0, 0))
        if tiempo > 90000:
            pantalla_actual = "afuera"

    elif pantalla_actual == "n7":
        pantalla.blit(imagenes.n7, (0,0))
        flecha_abajo_derecha_f(1340, 720)
    
    elif pantalla_actual == "auto3":
        flecha_abajo_derecha_f(1340, 720)

    elif pantalla_actual == "parte3":
        flecha_abajo_derecha_f(1340, 720)
    
    elif pantalla_actual == "llegada3":
        flecha_abajo_derecha_f(1340, 720)

    elif pantalla_actual == "tren3":
        flecha_abajo_derecha_f(1340, 720)
    #________________________________________ NIVEL 1 ___________________________________________________
    if pantalla_actual in ["jardin", "afuera", "interior", "cofre",
        "cofre_zoom", "cofre_abierto", "semilla", "cofre_vacio", "invernadero", "cabina", "gracias"]:

        juego.nivel1.dibujar(pantalla_actual)

    if pantalla_actual == "jardin":
        flecha_derecha_f(1280, 400)
        flecha_arriba_f(820, 510)
        flecha_izquierda_f(120, 400)

    elif pantalla_actual == "afuera":
        flecha_izquierda_f(120, 400)
        flecha_derecha_f(1280, 400)
        flecha_arriba_f(700, 560)
    
    elif pantalla_actual == "interior":
        flecha_abajo_f(650,660)
        flecha_arriba_f(685,510)

    elif pantalla_actual == "cofre":
        flecha_izquierda_f(120,400)
        flecha_derecha_f(1280,400)

    elif pantalla_actual == "cofre_zoom":
        flecha_abajo_f(710,660)

        texto1 = fuente.render(juego.nivel1.letras[0], True, (0,0,0))
        pantalla.blit(texto1, (493,290))
        texto2 = fuente.render(juego.nivel1.letras[1], True, (0,0,0))
        pantalla.blit(texto2, (607,290))
        texto3 = fuente.render(juego.nivel1.letras[2], True, (0,0,0))
        pantalla.blit(texto3, (723,290))
        texto4 = fuente.render(juego.nivel1.letras[3], True, (0,0,0))
        pantalla.blit(texto4, (837,290))

        pygame.draw.rect(pantalla, (255,0,0), botones.rueda1, 2)
        pygame.draw.rect(pantalla, (255,0,0), botones.rueda2, 2)
        pygame.draw.rect(pantalla, (255,0,0), botones.rueda3, 2)
        pygame.draw.rect(pantalla, (255,0,0), botones.rueda4, 2)

        if "".join(juego.nivel1.letras) == "AMTV":
            juego.nivel1.tiempo_cofre_abierto = pygame.time.get_ticks()
            pantalla_actual = "cofre_abierto"

    elif pantalla_actual == "cofre_abierto":
        flecha_izquierda_f(120,400)
        flecha_derecha_f(1280,400)

        if pygame.time.get_ticks() - juego.nivel1.tiempo_cofre_abierto > 1000:
                    juego.sonidos.cofre_efecto.play()
                    pantalla_actual = "cofre_abierto"

    elif pantalla_actual == "semilla":
        flecha_abajo_f(710,660)

    elif pantalla_actual == "cofre_vacio":
        flecha_abajo_f(710,660)
        juego.sonidos.semilla_efecto.stop()

    elif pantalla_actual == "invernadero":
        if juego.nivel1.planta_ampliada == "A":
            pantalla.blit(imagenes.hoja_A, (700,200))
        elif juego.nivel1.planta_ampliada == "M":
            pantalla.blit(imagenes.hoja_M, (700,200))
        elif juego.nivel1.planta_ampliada == "T":
            pantalla.blit(imagenes.hoja_T, (700,200))
        elif juego.nivel1.planta_ampliada == "V":
            pantalla.blit(imagenes.hoja_V, (700,200))

        flecha_abajo_f(900,660)

    elif pantalla_actual == "cabina":
        if juego.nivel1.maquinista_hablando:
            pantalla.blit(imagenes.maquinista2, (0,0))
        else:
            pantalla.blit(imagenes.maquinista1, (0,0))

        pygame.draw.rect(pantalla, (255,0,0), botones.botonMaquinista, 2)
        flecha_abajo_f(710,660)
        if juego.nivel1.maquinista_hablando:
            if pygame.time.get_ticks() - juego.nivel1.tiempo_maquinista > 6000:
                juego.maquinista_hablando = False
                juego.charla9_son_reproduciendo = False

        flecha_abajo_f(710,660)

    elif pantalla_actual == "gracias":
        pantalla.blit(imagenes.gracias1,(0,0))
        tiempo = pygame.time.get_ticks() - juego.nivel1.tiempo_gracias
        if tiempo < 100:
            if not juego.maquinista_gracias1_son_reproduciendo:
                juego.sonidos.maquinista_gracias1.play()
                juego.maquinista_gracias1_son_reproduciendo = True

        if tiempo > 5000:
            pantalla.fill((0, 0, 0))
        if tiempo > 7000:
            pantalla.blit(imagenes.nivel2, (0, 0))
        if tiempo > 12000:
            pantalla.blit(imagenes.carga, (0, 0))
        if tiempo > 14000:
            pantalla_actual = "intro_archivo"
            tiempo_intro2 = pygame.time.get_ticks()
           
    #________________________________________ NIVEL 2 ___________________________________________________
    elif pantalla_actual == "intro_archivo":
        tiempo = pygame.time.get_ticks() - tiempo_intro2
        if tiempo > 2000:
            pantalla.blit(imagenes.intro_archivo, (0,0))
            if not juego.viejo_intro2_son_reproduciendo:
                juego.sonidos.viejo_intro2.play()
                juego.viejo_intro2_son_reproduciendo = True
            
        if tiempo > 8500:
            juego.sonidos.viejo_intro2.stop()
            viejo_intro2_son_reproduciendo = False
            pantalla.blit(imagenes.cabina2_hablando,(0,0))
            if not juego.maquinista2_intro_son_reproduciendo:
                juego.sonidos.maquinista2_intro.play()
                juego.maquinista2_intro_son_reproduciendo = True
            
        if tiempo > 14000:
            juego.sonidos.maquinista2_intro.stop()
            juego.maquinista2_intro_son_reproduciendo = False
            pantalla.fill((0, 0, 0))
        if tiempo > 15000:
            pantalla_actual = "archivo"

    elif pantalla_actual == "archivo":
        pantalla.blit(imagenes.afuera2, (0, 0))
        flecha_arriba_f(680,610)
        flecha_abajo_f(680,680)

    elif pantalla_actual == "caminos":
        pantalla.blit(imagenes.camino, (0, 0))
        flecha_abajo_f(730,680)
        flecha_camino_izq_f(580,600)
        flecha_camino_med_f(800,570)
        flecha_camino_der_f(910,610)

    elif pantalla_actual == "casa":
        pantalla.blit(imagenes.casa_afuera, (0,0))
        flecha_izquierda_f(100, 400)
        flecha_arriba_f(1000, 450)

    elif pantalla_actual == "casa2":
        if panel_resuelto == False:
            pantalla.blit(imagenes.casa_adentro, (0, 0))
            LLL=False
        if panel_resuelto == True:
            LLL=True
            if llave_recogida == True:
                pantalla.blit(imagenes.llave2, (0,0))
                LLL= False
            else:
                pantalla.blit(imagenes.llave1, (0,0))
            
        flecha_izquierda_f(100, 400)

    elif pantalla_actual == "panel":
        pantalla.blit(imagenes.panel, (0,0))
        if palancas[0]:
            pantalla.blit(imagenes.palanca_arriba, (150,200))
        else:
            pantalla.blit(imagenes.palanca_abajo, (150, 280))
        if palancas[1]:
            pantalla.blit(imagenes.palanca_arriba, (420,200))
        else:
            pantalla.blit(imagenes.palanca_abajo, (420, 280))
        if palancas[2]:
            pantalla.blit(imagenes.palanca_arriba, (700,200))
        else:
            pantalla.blit(imagenes.palanca_abajo, (700, 280))
        if palancas[3]:
            pantalla.blit(imagenes.palanca_arriba, (970,200))
        else:
            pantalla.blit(imagenes.palanca_abajo, (970, 280))

        if palancas == [False, True, False, True]:
            panel_resuelto = True 
            
        flecha_abajo_f(710,660)

    elif pantalla_actual == "libro":
        pantalla.blit(imagenes.libro, (0, 0))

        if libro_abierto:
            sombra = pygame.Surface((1400,800))
            sombra.set_alpha(150)
            sombra.fill((0,0,0))
            pantalla.blit(sombra, (0,0))

            if pagina_libro == 1:
                pantalla.blit(imagenes.libro1, (250,150))
                flecha_libro_der_f(1080,550)
            elif pagina_libro == 2:
                pantalla.blit(imagenes.libro2, (250,150))
                flecha_libro_izq_f(320,550)
                flecha_libro_der_f(1080,550)
            elif pagina_libro == 3:
                pantalla.blit(imagenes.libro3, (250,150))
                flecha_libro_izq_f(320,550)
                flecha_libro_der_f(1080,550)
            elif pagina_libro == 4:
                pantalla.blit(imagenes.libro5, (250,150))
                flecha_libro_izq_f(320,550)
                flecha_libro_der_f(1080,550)
            elif pagina_libro == 5:
                pantalla.blit(imagenes.libro4, (250,150))
                flecha_libro_izq_f(320,550)

        flecha_abajo_derecha_f(1250,500)
        flecha_abajo_derecha_f(1250, 500)

    elif pantalla_actual == "puerta_biblioteca":
        pantalla.blit(imagenes.puerta, (0, 0))
        flecha_abajo_pequena_f(680, 690)
        flecha_arriba_f(680, 500)

    elif pantalla_actual == "puerta":
        pantalla.blit(imagenes.puerta_zoom, (0, 0))
        flecha_abajo_pequena_f(700, 710)

        if Mensaje_ce:
            pygame.draw.rect(pantalla, (40,40,40), (1100,40,200,35))
            pygame.draw.rect(pantalla, (255,255,255), (1100,40,200,35), 2)  
            Cerrado = fuente_pequenia.render("Cerrado", True, (255,255,255))
            juego.sonidos.efecto_Pcerrado.play()
            pantalla.blit(Cerrado, (1150,40))

            if pygame.time.get_ticks() - tiempo_cerrado > 2000:
                Mensaje_ce = False

    elif pantalla_actual == "puerta_abierta1":
        pantalla.blit(imagenes.puerta_abierta1, (0,0))
        flecha_abajo_pequena_f(700, 710)

    elif pantalla_actual == "puerta_interior":
        pantalla.blit(imagenes.inte_biblio,(0,0))
        flecha_derecha_f(1280,400)
        flecha_abajo_pequena_f(700, 710)

    elif pantalla_actual == "sala_mapa":
        pantalla.blit(imagenes.mapa,(0,0))
        flecha_abajo_pequena_f(700, 710)

    elif pantalla_actual == "cofre_cerrado_archivo":
        pantalla.blit(imagenes.cofre_archi, (0,0))
        num1 = fuente.render(str(numeros[0]), True, (255,255,255))
        pantalla.blit(num1, (530,480))
        num2 = fuente.render(str(numeros[1]), True, (255,255,255))
        pantalla.blit(num2, (650,480))
        num3 = fuente.render(str(numeros[2]), True, (255,255,255))
        pantalla.blit(num3, (770,480))
        num4 = fuente.render(str(numeros[3]), True, (255,255,255))
        pantalla.blit(num4, (880,480))

        flecha_abajo_pequena_f(700, 710)

        if numeros == [7,3,5,2]:
            pantalla_actual = "cofre_abierto2"
            juego.sonidos.cofre_efecto.play()

    elif pantalla_actual == "cofre_abierto2":
        if fusible_recogido:
            pantalla.blit(imagenes.cofre_vacio2, (0,0))
        else:
            pantalla.blit(imagenes.cofre_abierto2, (0,0))
        flecha_abajo_pequena_f(700, 710)
             
    elif pantalla_actual == "interior2":
        pantalla.blit(imagenes.archivo2_viejo, (0,0))
        flecha_abajo_f(620,660)
        flecha_arriba_f(640,550)
        pygame.draw.rect(pantalla, (255,0,0), botones.boton_viejo, 2)
    
    elif pantalla_actual == "cabina2":
        if sonidos.maquinista2_intro_son_reproduciendo:
            pantalla.blit(imagenes.maquinista_fusible, (0,0))
            tiempo = pygame.time.get_ticks() - tiempo_maquinista2
            if tiempo > 4000:
                maquinista_intro_son_reproduciendo = False
                pantalla.blit(imagenes.cabina2,(0,0))
        else:
            pantalla.blit(imagenes.cabina2,(0,0))
                
        flecha_abajo_f(710,660)

    elif pantalla_actual == "gracias2":
        pantalla.blit(imagenes.gracias2,(0,0))
        tiempo = pygame.time.get_ticks() - juego.nivel1.tiempo_gracias
        if tiempo < 100:
            if not maquinista_gracias2_son_reproduciendo:
                juego.sonidos.maquinista_gracias2.play()
                maquinista_gracias2_son_reproduciendo = True
    
        if tiempo > 5000:
            pantalla.fill((0, 0, 0))
        if tiempo > 7000:
            pantalla.blit(imagenes.nivel3, (0, 0))
        if tiempo > 12000:
            pantalla.blit(imagenes.carga, (0, 0))
        if tiempo > 14000:
            pantalla_actual = "nivel3" 
#------------------------------------------------------------------------
    pantallas_ocultas = ["inicio", "carga", "juego", "historia", "n7", "comienzo", "auto3",
                        "auto_parado", "parte3", "llegada_estacion", "llegada3", "boleto", "tren3", "charla"]
    inventario.dibujar(pantalla, juego.imagenes)
    
    pygame.display.flip()