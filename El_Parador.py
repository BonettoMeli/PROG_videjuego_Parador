import sys
import pygame
pygame.init()
pygame.mixer.init()
#------------creo la pantalla y le doy nombre----------------------------------------
pantalla = pygame.display.set_mode((1400,800))
pygame.display.set_caption("Videojuego ¨EL PARADOR¨")
#-------------PANTALLA DE INICIO-----------------------------------------------------
imagen_inicio = pygame.image.load('visual/Inicio.png')
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
n5 = pygame.image.load('visual/importancia.jpeg')
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
charla5 = pygame.image.load("visual/charla5.jpg")
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

bolso = pygame.image.load("visual/bolso.png")
bolso = pygame.transform.scale(bolso, (150, 130))
#-------------------------------------------------------------------------
nivel1 = pygame.image.load("visual/Nivel1.jpeg")
nivel2 = pygame.image.load("visual/Nivel2.jpeg")
nivel3 = pygame.image.load("visual/Nivel3.jpeg")
nivel4 = pygame.image.load("visual/Nivel4.jpeg")

nivel1 = pygame.transform.scale(nivel1, (1400, 800))
nivel2 = pygame.transform.scale(nivel2, (1400, 800))
nivel3 = pygame.transform.scale(nivel3, (1400, 800))
nivel4 = pygame.transform.scale(nivel4, (1400, 800))
#-----------------NIVEL UNO-----------------------------------------------
interior = pygame.image.load("visual/vagon_vacio.jpeg")
interior = pygame.transform.scale(interior, (1400, 800))

jardin = pygame.image.load("visual/lenguas_muertas2.jpg")
invernadero = pygame.image.load("visual/invernadero_adentro.jpg")
cofre = pygame.image.load("visual/cofre_lengua1.jpeg")
cofre_abierto = pygame.image.load("visual/cofre_lengua2.jpeg")
cofre_zoom = pygame.image.load("visual/cofre_zoom2.jpeg")
afuera = pygame.image.load("visual/tren_lengua_abierto.png")
cofre_semilla = pygame.image.load("visual/cofre_semilla.jpeg")
cofre_vacio = pygame.image.load("visual/cofre_vacio.jpeg")
semilla_transp = pygame.image.load("visual/semilla_trasparente.png")
gracias1 = pygame.image.load("visual/gracias1.jpeg")

jardin = pygame.transform.scale(jardin, (1400, 800))
invernadero = pygame.transform.scale(invernadero, (1400, 800))
cofre = pygame.transform.scale(cofre, (1400, 800))
cofre_abierto = pygame.transform.scale(cofre_abierto, (1400, 800))
cofre_zoom = pygame.transform.scale(cofre_zoom, (1400, 800))
afuera = pygame.transform.scale(afuera, (1400, 800))
cofre_semilla = pygame.transform.scale(cofre_semilla, (1400, 800))
cofre_vacio = pygame.transform.scale(cofre_vacio, (1400, 800))
semilla_transp = pygame.transform.scale(semilla_transp, (100, 90))
gracias1 = pygame.transform.scale(gracias1, (1400, 800))

#HOJAS DEL INVERNADERO
hoja_A = pygame.image.load("visual/hoja_A.jpg")
hoja_M = pygame.image.load("visual/hoja_M.jpg")
hoja_T = pygame.image.load("visual/hoja_T.jpg")
hoja_V = pygame.image.load("visual/hoja_V.jpg")

hoja_A = pygame.transform.scale(hoja_A, (600, 400))
hoja_M = pygame.transform.scale(hoja_M, (600, 400))
hoja_T = pygame.transform.scale(hoja_T, (600, 400))
hoja_V = pygame.transform.scale(hoja_V, (600, 400))

maquinista_hablando = False
#-----------------BOTONES NIVEL UNO------------------------------
flecha_centro = pygame.Rect(750, 450, 100, 100)  #x-y-ancho-largo
flecha_centro2 = pygame.Rect(660, 380, 100, 180 )

flecha_derecha = pygame.Rect(1220, 280, 180, 220)
flecha_izquierda = pygame.Rect(30, 280, 100, 220)

flecha_abajo = pygame.Rect(820, 600, 120, 140) #dentro del invernadero
flecha_abajo2 = pygame.Rect(620, 430, 120, 140)

flecha_atras = pygame.Rect(610, 600, 120, 140)
flecha_cabina = pygame.Rect(600, 480, 120, 140)

flecha_cabina2 = pygame.Rect(680, 600, 120, 140) #abajo al medio

flecha_abajo_derecha = pygame.Rect(1240, 600, 140, 140)
flecha_centro_central = pygame.Rect(600, 300, 220, 300)
flecha_centro_central_peque = pygame.Rect(660, 420, 100, 100)

BAcertijo = pygame.Rect(890, 280, 150, 300)

flecha_centro_casa = pygame.Rect(950, 300, 150, 200)

#pygame.draw.rect(pantalla, (255, 0, 0), flecha_cabina2, 3) ----- para dibujar los botones
planta_A = pygame.Rect(500, 180, 220, 220)
planta_M = pygame.Rect(450, 330, 280, 180)
planta_T = pygame.Rect(680, 620, 180, 110)# x y ancho largo
planta_V = pygame.Rect(20, 150, 280, 280)

planta_ampliada = None
rueda1 = pygame.Rect(470, 230, 110, 190)
rueda2 = pygame.Rect(585, 230, 110, 190)
rueda3 = pygame.Rect(700, 230, 110, 190)
rueda4 = pygame.Rect(815, 230, 110, 190)


letras = ["A", "A", "A", "A"]

abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

fuente = pygame.font.SysFont("Times New Roman", 80)
fuente_pequenia = pygame.font.SysFont("Times New Roman", 25)

def siguiente_letra(letra):
    indice = abecedario.index(letra)
    return abecedario[(indice + 1) % len(abecedario)]
#-------------------- NIVEL 2 --------------------------------------------
tiempo_maquinista = 0
tiempo_gracias = 0
tiempo_intro2 = 0

afuera2 = pygame.image.load("visual/tren_archivo_afuera.jpg")
camino = pygame.image.load("visual/tres_caminos.jpeg")
libro = pygame.image.load("visual/libro_archivo.jpeg")
cabina2 = pygame.image.load("visual/cabina2.jpeg")
cabina2_hablando = pygame.image.load("visual/cabina2_hablando.jpeg")
vagon_archivo = pygame.image.load("visual/vagon_interior.jpeg")
puerta = pygame.image.load("visual/biblioteca_sumergido.jpeg")
puerta_zoom = pygame.image.load("visual/puerta_zoom.jpeg")
puerta_abierta1 = pygame.image.load("visual/puerta_abierta.png")
casa_afuera = pygame.image.load("visual/casa_afuera.jpeg")
casa_adentro = pygame.image.load("visual/casa_adentro.jpeg")
cofre_abierto2 = pygame.image.load("visual/cofre_abierto2.jpeg")
cofre_vacio2 = pygame.image.load("visual/cofre_vacio2.jpeg")
gracias2 = pygame.image.load("visual/gracias2.jpeg")
maquinista_fusible = pygame.image.load("visual/cabina2_hablando.jpeg")
intro_archivo = pygame.image.load("visual/intro_archivo.jpeg")

afuera2 = pygame.transform.scale(afuera2, (1400, 800))
camino = pygame.transform.scale(camino, (1400, 800))
libro = pygame.transform.scale(libro, (1400, 800))
cabina2 = pygame.transform.scale(cabina2, (1400, 800))
cabina2_hablando = pygame.transform.scale(cabina2_hablando, (1400, 800))
vagon_archivo = pygame.transform.scale(vagon_archivo, (1400, 800))
puerta = pygame.transform.scale(puerta, (1400, 800))
puerta_zoom = pygame.transform.scale(puerta_zoom, (1400, 800))
puerta_abierta1 = pygame.transform.scale(puerta_abierta1, (1400, 800))
casa_afuera = pygame.transform.scale(casa_afuera, (1400, 800))
casa_adentro = pygame.transform.scale(casa_adentro, (1400, 800))
cofre_abierto2 = pygame.transform.scale(cofre_abierto2, (1400, 800))
cofre_vacio2 = pygame.transform.scale(cofre_vacio2, (1400, 800))
gracias2 = pygame.transform.scale(gracias2, (1400, 800))
maquinista_fusible = pygame.transform.scale(maquinista_fusible, (1400,800))
intro_archivo = pygame.transform.scale(intro_archivo, (1400,800))

panel = pygame.image.load("visual/mueble_palancas.jpeg")
panel = pygame.transform.scale(panel, (1400, 800))
palanca_arriba = pygame.image.load("visual/P_arriba.png")
palanca_arriba = pygame.transform.scale(palanca_arriba,(270,350))
palanca_abajo = pygame.image.load("visual/P_abajo.png")
palanca_abajo = pygame.transform.scale(palanca_abajo,(250,350))

libro1 = pygame.image.load("visual/libro1.png")
libro1 = pygame.transform.scale(libro1, (900, 500))
libro2 = pygame.image.load("visual/libro2.png")
libro2 = pygame.transform.scale(libro2, (900, 500))
libro3 = pygame.image.load("visual/libro3.jpeg")
libro3 = pygame.transform.scale(libro3, (900, 500))
libro4 = pygame.image.load("visual/libro4.png")
libro4 = pygame.transform.scale(libro4, (900, 500))
libro5 = pygame.image.load("visual/libro5.png")
libro5 = pygame.transform.scale(libro5, (900, 500))

llave1 = pygame.image.load("visual/llave_abajo.jpeg")
llave1 = pygame.transform.scale(llave1, (1400,800))
llave2 = pygame.image.load("visual/sin_llave.jpeg")
llave2 = pygame.transform.scale(llave2, (1400,800))

llave_transp = pygame.image.load("visual/llave_transparente.png")
llave_transp = pygame.transform.scale(llave_transp, (100, 90))
fusible_transp = pygame.image.load("visual/fusible_transparente.png")
fusible_transp = pygame.transform.scale(fusible_transp, (100, 90))

inte_biblio = pygame.image.load("visual/interior_biblioteca.png")
inte_biblio = pygame.transform.scale(inte_biblio, (1400,800))
mapa = pygame.image.load("visual/sala_mapa.jpeg")
mapa = pygame.transform.scale(mapa, (1400,800))
cofre_archi = pygame.image.load("visual/cofre_archivo_cerrado.png")
cofre_archi = pygame.transform.scale(cofre_archi, (1400,800))

archivo2_viejo = pygame.image.load("visual/archivo2_viejo.jpeg")
archivo2_viejo = pygame.transform.scale(archivo2_viejo, (1400,800))

atras = pygame.Rect(620, 670, 120, 80)
B_libro = pygame.Rect(200, 300, 260, 250)
B_interior = pygame.Rect(620, 570, 120, 60)
BCentro_n2 = pygame.Rect(620, 670, 120, 80)
B_libro_atras = pygame.Rect(1220, 450, 120, 100)

Rect_libro = pygame.Rect(250,150,900,500)
B_flecha_libro_der = pygame.Rect(1050,500,80,100)
B_flecha_libro_izq = pygame.Rect(280,500,80,100)

camino1 = pygame.Rect(510, 540, 100, 100)
camino2 = pygame.Rect(750, 500, 100, 100)
camino3 = pygame.Rect(880, 550, 100, 100)

botonMaquinista = pygame.Rect(900, 300, 250, 380)

B_puerta = pygame.Rect(600, 320, 210, 380)
B_volver_puerta = pygame.Rect(650,700,100,100)
B_palancas = pygame.Rect(450, 450, 430, 220)
B_fusible = pygame.Rect(600, 400, 200, 200)

cofre_A = pygame.Rect(620, 300, 150, 100)
numeros = [0,0,0,0]

def siguiente_numero(numero):
    return (numero + 1) % 10

C_num1 = pygame.Rect(500,480,90,90)
C_num2 = pygame.Rect(620,480,90,90)
C_num3 = pygame.Rect(740,480,90,90)
C_num4 = pygame.Rect(850,480,90,90)

palancas = [False, False, False, False]
B_palanca1 = pygame.Rect(220,300,100,210)
B_palanca2 = pygame.Rect(500,300,100,210)
B_palanca3 = pygame.Rect(780,300,100,210)
B_palanca4 = pygame.Rect(1050,300,100,210)

B_llave = pygame.Rect(1050,300,100,200)

#--------------------SONIDOS--Y--MUSICA-----------------------------------
texto_gris = pygame.mixer.Sound("musica_sonido/1_texto_gris_audio.mpeg")
auto_paro_sonido0 = pygame.mixer.Sound("musica_sonido/y_eso.mpeg")
auto_paro_sonido = pygame.mixer.Sound("musica_sonido/2_ay_no_el_auto_se_paro.mpeg")
auto_paro_sonido2 = pygame.mixer.Sound("musica_sonido/3_bueno_por_suerte_hay_un_tren_cerca.mpeg")
llegada1_sonido = pygame.mixer.Sound("musica_sonido/4_por_fin_llegue_a_la_estacion.mpeg")
llegada2_sonido = pygame.mixer.Sound("musica_sonido/5_wow_que_rapido.mpeg")
boleto1_sonido = pygame.mixer.Sound("musica_sonido/6_este_tren_debe.mpeg")
charla1_sonido = pygame.mixer.Sound("musica_sonido/7_es_raro.mpeg")
charla2_sonido = pygame.mixer.Sound("musica_sonido/8_por_que_dice_eso.mpeg")
charla3_sonido = pygame.mixer.Sound("musica_sonido/9_debes_ser_nueva.mpeg")
charla4_sonido = pygame.mixer.Sound("musica_sonido/10_es_no_es_un_tren.mpeg")
charla5_sonido = pygame.mixer.Sound("musica_sonido/11_hoy_vamos_a_pasar.mpeg")
charla6_sonido = pygame.mixer.Sound("musica_sonido/12_y_cada_una_es_unica.mpeg")
charla7_sonido = pygame.mixer.Sound("musica_sonido/13_que_raro_el_tren.mpeg")
charla8_sonido = pygame.mixer.Sound("musica_sonido/14_rapido_ve_a_preguntarle.mpeg")
charla9_sonido = pygame.mixer.Sound("musica_sonido/17_sin_combustible_maquinista.mp3")
charla10_sonido = pygame.mixer.Sound("musica_sonido/15_el_maquinista_me_dijo.mpeg")
charla11_sonido = pygame.mixer.Sound("musica_sonido/16_claro_por_supuesto.mp3")

sonido_n1 = False
auto_paro_reproducido = False
llegada1_son_reproduciendo = False
llegada2_son_reproduciendo = False
boleto1_son_reproduciendo = False
charla1_son_reproduciendo = False
charla2_son_reproduciendo = False
charla3_son_reproduciendo = False
charla4_son_reproduciendo = False
charla5_son_reproduciendo = False
charla6_son_reproduciendo = False
charla7_son_reproduciendo = False
charla8_son_reproduciendo = False
charla9_son_reproduciendo = False
charla10_son_reproduciendo = False
charla11_son_reproduciendo = False

gracias2_son_reproduciendo = False
maquinista2_intro_son_reproduciendo = False
gracias_maquinista2 = pygame.mixer.Sound("musica_sonido/gracias_maquinista2.mp3")
maquinista2_intro = pygame.mixer.Sound("musica_sonido/maquinista2_intro.mp3")


maquinista_gracias1_son_reproduciendo = False
maquinista_gracias2_son_reproduciendo = False
favela_reproduciendo = False

favela = pygame.mixer.Sound("musica_sonido/Favela.mp3")
favela.set_volume(0.7)

maquinista_gracias1 = pygame.mixer.Sound("musica_sonido/18_gracias_maquinista.mp3")
maquinista_gracias2 = pygame.mixer.Sound("musica_sonido/gracias_maquinista2.mp3")

chica_auto_paro2 = pygame.mixer.Sound("musica_sonido/chica_estacion_cerca.mp3")
interfe = pygame.mixer.Sound("musica_sonido/interferencia_efecto.mp3")
interfe.set_volume(0.1)

cofre_efecto = pygame.mixer.Sound("musica_sonido/cofre_abriendose.mp3")
semilla_efecto = pygame.mixer.Sound("musica_sonido/efecto_semilla.mp3")
semilla_efecto.set_volume(0.05)

botonson = pygame.mixer.Sound("musica_sonido/boton_efecto.mp3")
ruido_tren = pygame.mixer.Sound("musica_sonido/Bocina_tren.mp3")
ruido_tren.set_volume(0.3)

sin_arranque = pygame.mixer.Sound("musica_sonido/efecto_sin_arranque.mp3")
sin_arranque.set_volume(0.3)
tren_avanzando = pygame.mixer.Sound("musica_sonido/tren_avanzando.WAV")

acertijo1 = pygame.mixer.Sound("musica_sonido/acertijo_viejo.mp3")
acertijo1.set_volume(0.5)

cascada = pygame.mixer.Sound("musica_sonido/Cascadas_agua.mp3")
cascada.set_volume(0.05)

tren_humo = pygame.mixer.Sound("musica_sonido/tren_humo.mp3")
tren_humo.set_volume(0.1)

#-----------FUNCIONES FLECHAS-------------------------------------------------------------
def flecha_derecha_f(x, y):
    pygame.draw.polygon(
        pantalla,
        (255,255,255),
        [(x+40,y),(x,y-50),(x,y+50)]
    )

def flecha_izquierda_f(x, y):
    pygame.draw.polygon(
        pantalla,
        (255,255,255),
        [(x-40,y),(x,y-50),(x,y+50)]
    )

def flecha_arriba_f(x, y):
    pygame.draw.polygon(
        pantalla,
        (255,255,255),
        [(x,y-30),(x-40,y),(x+40,y)]
    )

def flecha_abajo_f(x, y):
    pygame.draw.polygon(
        pantalla,
        (255,255,255),
        [(x,y+60),(x-50,y),(x+50,y)]
    )

def flecha_abajo_pequena_f(x, y):
    pygame.draw.polygon(
        pantalla,
        (255,255,255),
        [(x,y+40),(x-50,y),(x+50,y)]
    )

def flecha_abajo_derecha_f(x, y):
    pygame.draw.polygon(
        pantalla,
        (255,255,255),
        [(x,y-40),(x,y+40),(x+40,y)]
    )

def flecha_arriba_grande_f(x, y):
    pygame.draw.polygon(
        pantalla,
        (255,255,255),
        [(x,y-60),(x-50,y),(x+50,y)]
    )

def flecha_camino_izq_f(x, y):
    pygame.draw.polygon(
        pantalla,
        (255,255,255),
        [(x-50,y-40),(x+20,y-30),(x-20,y+10)]
    )

def flecha_camino_med_f(x, y):
    pygame.draw.polygon(
        pantalla,
        (255,255,255),
        [(x+50,y-40),(x-40,y-10),(x+10,y+10)]
    )

def flecha_camino_der_f(x, y):
    pygame.draw.polygon(
        pantalla,
        (255,255,255),
        [(x-30,y-20),(x+50,y-30),(x+10,y+30)]
    )

def flecha_libro_der_f(x, y):
    pygame.draw.polygon(
        pantalla,
        (255,255,255),
        [(x+25, y), (x, y-30), (x, y+30)]
    )

def flecha_libro_izq_f(x, y):
    pygame.draw.polygon(
        pantalla,
        (255,255,255),
        [(x-25, y), (x, y-30), (x, y+30)]
    )

def inventario_f():
    pantalla.blit(bolso, (1210,610))
    if inventario_abierto:
        pantalla.blit(inventario, (470,500))

        for i in range(len(inventario_lista)):
            imagen = imagenes_objetos[inventario_lista[i]]
            imagen_centrada = imagen.get_rect(center=casillas[i].center)
            pantalla.blit(imagen, imagen_centrada) #muestra el objeto seleccionado centrado en la casilla

            if inventario_lista[i] == objeto_seleccionado:
                pygame.draw.rect(pantalla, (255,255,0), casillas[i], 3)

def cambiar_pantalla_si_toca(boton, destino, evento, sonido=None):
    global pantalla_actual #le dice a la funcion que quiere modificar la variable ya existente
    if boton.collidepoint(evento.pos):
        if sonido:
            sonido.play()
        pantalla_actual = destino
        return True #si toca el boton
    return False #si no toca el boton
#--------------INVENTARIO-------------------------------------------------
Boton_bolso = pygame.Rect(1220, 610, 130, 130)
inventario = pygame.image.load("visual/inventario.png")
inventario = pygame.transform.scale(inventario, (500, 400))

inventario_lista = []
objeto_seleccionado = None
imagenes_objetos = {
    "semilla_objeto": semilla_transp, 
    "llave_objeto":llave_transp,
    "fusible_objeto":fusible_transp
}

casillas = [
    pygame.Rect(520, 640, 60, 60), #casilla1
    pygame.Rect(590, 640, 60, 60), # '' 2
    pygame.Rect(655, 640, 60, 60), # '' 3
    pygame.Rect(720, 640, 60, 60), # '' 4
    pygame.Rect(790, 640, 60, 60), # '' 5
    pygame.Rect(860, 640, 60, 60), # '' 6
]

#----------INICIO DEL PROGRAMA-------------------------------------------------------------------------------
pantalla_actual = "gracias" #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
tiempo_carga = 0
tiempo_historia = 0

codigo_encontrado = []
codigo_correcto = "AMTV"
codigo_ingresado = ""

num_encontrado = []
num_correcto = "7352"
num_ingresado = ""

AAA = True  #Para que la imagen de cofre abierto se mantenga una vez que se abre el cofre
BBB = True  #Para que la imagen de cofre vacio se mantenga una vez que se lleva la semilla
inventario_abierto = False
auto0_paro_reproducido = False
libro_abierto = False
pagina_libro = 1

panel_resuelto = False
llave_recogida = False
puerta_abierta = False
fusible_recogido = False

Mensaje_ce = False
tiempo_cerrado = 0

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
                    tiempo_cofre_abierto = pygame.time.get_ticks()
                    pantalla_actual = "cofre_desbloqueando"      

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if Boton_bolso.collidepoint(evento.pos) and pantalla_actual not in pantallas_ocultas:
                inventario_abierto = not inventario_abierto
            if inventario_abierto:
                for i in range(len(casillas)):
                    if casillas[i].collidepoint(evento.pos):
                        if i < len(inventario_lista):
                            if objeto_seleccionado == inventario_lista[i]:
                                objeto_seleccionado = None      # Se deselecciona
                            else:
                                objeto_seleccionado = inventario_lista[i]   # Se selecciona


            if pantalla_actual == "inicio": # BOTÓN DEL MENÚ PRINCIPAL
                cambiar_pantalla_si_toca(boton_jugar,"carga",evento,botonson)
                tiempo_carga = pygame.time.get_ticks()

            elif pantalla_actual == "juego": # BOTÓN DE LA PANTALLA DE INSTRUCCIONES
                cambiar_pantalla_si_toca(boton_jugar2,"historia",evento,botonson)
                tiempo_historia = pygame.time.get_ticks()
            
            elif pantalla_actual == "n7":
                cambiar_pantalla_si_toca(flecha_abajo_derecha,"comienzo",evento)
                tiempo_comienzo = pygame.time.get_ticks()
            
            elif pantalla_actual == "auto3":
                cambiar_pantalla_si_toca(flecha_abajo_derecha,"auto_parado",evento)
                tiempo_auto_parado = pygame.time.get_ticks()
            
            elif pantalla_actual == "parte3":
                cambiar_pantalla_si_toca(flecha_abajo_derecha,"llegada_estacion",evento)
                tiempo_llegadaa = pygame.time.get_ticks()

            elif pantalla_actual == "llegada3":
                cambiar_pantalla_si_toca(flecha_abajo_derecha,"boleto",evento)
                tiempo_boleto = pygame.time.get_ticks()

            elif pantalla_actual == "tren3":
                cambiar_pantalla_si_toca(flecha_abajo_derecha,"charla",evento)
                tiempo_charla = pygame.time.get_ticks()

            #-----------------------------nivel 1-------------------------------------------------------
            elif pantalla_actual == "jardin":
                cambiar_pantalla_si_toca(flecha_centro, "invernadero", evento)
                cambiar_pantalla_si_toca(flecha_izquierda, "afuera", evento)
                if flecha_derecha.collidepoint(evento.pos):
                    if AAA:
                        pantalla_actual = "cofre"
                    else:
                        pantalla_actual = "cofre_abierto"

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
                if BAcertijo.collidepoint(evento.pos):
                    acertijo1.play()

                elif cambiar_pantalla_si_toca(flecha_izquierda,"jardin",evento):
                    acertijo1.stop()

                elif cambiar_pantalla_si_toca(flecha_derecha,"afuera",evento):
                    acertijo1.stop()

                cambiar_pantalla_si_toca(flecha_centro_central,"cofre_zoom",evento)

            elif pantalla_actual == "cofre_abierto":
                cambiar_pantalla_si_toca(flecha_izquierda,"jardin",evento)
                cambiar_pantalla_si_toca(flecha_derecha,"afuera",evento)
                
                if flecha_centro_central.collidepoint(evento.pos):
                    if BBB == True:
                        semilla_efecto.play()
                        pantalla_actual = "semilla"
                    else:
                        pantalla_actual = "cofre_vacio"
            
            elif pantalla_actual == "cofre_zoom":
                if flecha_cabina2.collidepoint(evento.pos):
                    if AAA == True:
                        pantalla_actual = "cofre"
                    else:
                        pantalla_actual = "cofre_abierto"

                if rueda1.collidepoint(evento.pos):
                        letras[0] = siguiente_letra(letras[0])

                elif rueda2.collidepoint(evento.pos):
                        letras[1] = siguiente_letra(letras[1])

                elif rueda3.collidepoint(evento.pos):
                        letras[2] = siguiente_letra(letras[2])

                elif rueda4.collidepoint(evento.pos):
                        letras[3] = siguiente_letra(letras[3])

            elif pantalla_actual == "semilla":
                if cambiar_pantalla_si_toca(flecha_cabina2,"cofre_abierto",evento):
                    AAA = False
                if cambiar_pantalla_si_toca(flecha_centro_central_peque,"cofre_vacio",evento): #si selecciona la semilla...
                    inventario_lista.append("semilla_objeto")
                    BBB = False

            elif pantalla_actual == "cofre_vacio":
                if cambiar_pantalla_si_toca(flecha_cabina2,"cofre_abierto",evento):
                    AAA = False

            elif pantalla_actual == "afuera":
                cascada.play()
                if flecha_izquierda.collidepoint(evento.pos):
                    if AAA == True:
                        pantalla_actual = "cofre"
                    else:
                        pantalla_actual = "cofre_abierto"
                cambiar_pantalla_si_toca(flecha_derecha,"jardin",evento)
                cambiar_pantalla_si_toca(flecha_centro2,"interior",evento)

            elif pantalla_actual == "interior":
                cambiar_pantalla_si_toca(flecha_atras,"afuera",evento)
                cambiar_pantalla_si_toca(flecha_cabina,"cabina",evento)

            elif pantalla_actual == "cabina":
                if botonMaquinista.collidepoint(evento.pos):
                    if objeto_seleccionado == "semilla_objeto":
                        inventario_lista.remove("semilla_objeto")
                        objeto_seleccionado = None
                        pantalla_actual = "gracias"
                        tiempo_gracias = pygame.time.get_ticks()
                    else:
                        if not charla9_son_reproduciendo:
                            charla9_sonido.play()
                            charla9_son_reproduciendo = True
                            maquinista_hablando = True
                            tiempo_maquinista = pygame.time.get_ticks()

                if cambiar_pantalla_si_toca(flecha_cabina2,"interior",evento):
                    charla9_sonido.stop()
                    charla9_son_reproduciendo = False
                    maquinista_hablando = False

                #------------------------------- NIVEL 2 (flechas y botones)-----------------------------------------------
            elif pantalla_actual == "archivo":
                cambiar_pantalla_si_toca(BCentro_n2,"caminos",evento)
                cambiar_pantalla_si_toca(B_interior,"interior2",evento)

            elif pantalla_actual == "caminos":
                cambiar_pantalla_si_toca(camino1,"libro",evento)
                cambiar_pantalla_si_toca(atras,"archivo",evento)
                cambiar_pantalla_si_toca(camino2,"puerta_biblioteca",evento)
                cambiar_pantalla_si_toca(camino3,"casa",evento)

            elif pantalla_actual == "casa":
                cambiar_pantalla_si_toca(flecha_izquierda,"caminos",evento)
                cambiar_pantalla_si_toca(flecha_centro_casa,"casa2",evento)

            elif pantalla_actual == "casa2":
                cambiar_pantalla_si_toca(flecha_izquierda,"casa",evento)
                cambiar_pantalla_si_toca(B_palancas,"panel",evento)
                if LLL == True:
                    if B_llave.collidepoint(evento.pos):
                        llave_recogida=True
                        inventario_lista.append("llave_objeto")
                        LLL=False

            elif pantalla_actual == "puerta_biblioteca":
                cambiar_pantalla_si_toca(atras,"caminos",evento)
                cambiar_pantalla_si_toca(flecha_centro_central_peque,"puerta",evento)

            elif pantalla_actual == "libro":
                if B_libro.collidepoint(evento.pos):
                    libro_abierto = True

                elif B_flecha_libro_der.collidepoint(evento.pos):
                    if pagina_libro < 5:
                        pagina_libro += 1
                elif B_flecha_libro_izq.collidepoint(evento.pos):
                    if pagina_libro > 1:
                        pagina_libro -= 1

                elif B_libro_atras.collidepoint(evento.pos):
                    libro_abierto = False
                    pagina_libro = 1
                    pantalla_actual = "caminos"
                elif not Rect_libro.collidepoint(evento.pos):
                    libro_abierto = False

            elif pantalla_actual == "panel":
                if B_palanca1.collidepoint(evento.pos):
                    palancas[0] = not palancas[0]
                elif B_palanca2.collidepoint(evento.pos):
                    palancas[1] = not palancas[1]
                elif B_palanca3.collidepoint(evento.pos):
                    palancas[2] = not palancas[2]
                elif B_palanca4.collidepoint(evento.pos):
                    palancas[3] = not palancas[3]
                cambiar_pantalla_si_toca(flecha_cabina2,"casa2",evento)


            elif pantalla_actual == "puerta":
                cambiar_pantalla_si_toca(atras, "puerta_biblioteca", evento)

                if B_puerta.collidepoint(evento.pos):
                    if puerta_abierta:
                        pantalla_actual = "puerta_abierta1"
                    elif objeto_seleccionado == "llave_objeto":
                        inventario_lista.remove("llave_objeto")
                        objeto_seleccionado = None
                        puerta_abierta = True
                        pantalla_actual = "puerta_abierta1"
                    else:
                        Mensaje_ce = True
                        tiempo_cerrado = pygame.time.get_ticks()

            elif pantalla_actual == "puerta_abierta1":
                cambiar_pantalla_si_toca(atras,"puerta_biblioteca",evento)
                cambiar_pantalla_si_toca(B_puerta,"puerta_interior",evento)

            elif pantalla_actual == "puerta_interior":
                cambiar_pantalla_si_toca(flecha_derecha,"sala_mapa",evento)
                cambiar_pantalla_si_toca(B_volver_puerta,"puerta",evento)
                cambiar_pantalla_si_toca(cofre_A,"cofre_cerrado_archivo",evento)

            elif pantalla_actual == "cofre_cerrado_archivo":
                cambiar_pantalla_si_toca(B_volver_puerta,"puerta_interior",evento)
                if C_num1.collidepoint(evento.pos):
                    numeros[0] = siguiente_numero(numeros[0])

                elif C_num2.collidepoint(evento.pos):
                    numeros[1] = siguiente_numero(numeros[1])

                elif C_num3.collidepoint(evento.pos):
                    numeros[2] = siguiente_numero(numeros[2])

                elif C_num4.collidepoint(evento.pos):
                    numeros[3] = siguiente_numero(numeros[3])

            elif pantalla_actual == "cofre_abierto2":
                cambiar_pantalla_si_toca(B_volver_puerta , "puerta_interior", evento)
        
                if B_fusible.collidepoint(evento.pos):
                    if not fusible_recogido:
                        fusible_recogido = True
                        inventario_lista.append("fusible_objeto")
                        

            elif pantalla_actual == "sala_mapa":
                cambiar_pantalla_si_toca(B_volver_puerta,"puerta_interior",evento)

            elif pantalla_actual == "interior2":
                cambiar_pantalla_si_toca(flecha_atras,"archivo",evento) 
                cambiar_pantalla_si_toca(flecha_cabina,"cabina2",evento)

            elif pantalla_actual == "cabina2":
                if cambiar_pantalla_si_toca(flecha_cabina2,"interior2",evento):
                    maquinista2_intro.stop()
                if botonMaquinista.collidepoint(evento.pos):

                    if objeto_seleccionado == "fusible_objeto":
                        inventario_lista.remove("fusible_objeto")
                        objeto_seleccionado = None
                        pantalla_actual = "gracias2"
                        tiempo_gracias = pygame.time.get_ticks()
                    else:
                        if not maquinista2_intro_son_reproduciendo:
                            maquinista2_intro.play()
                            maquinista2_intro_son_reproduciendo = True
                            tiempo_maquinista2 = pygame.time.get_ticks()

                if cambiar_pantalla_si_toca(flecha_cabina2,"interior2",evento):
                    maquinista2_intro.stop()
                    maquinista2_intro_son_reproduciendo = False
                    maquinista_hablando2 = False
    #----------------------------------------------------------------------------------------------------------        
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
            if not sonido_n1:
                texto_gris.play()
                sonido_n1 = True
        if tiempo > 4000:
            pantalla.blit(n2, (0, 0))
        if tiempo > 6500:
            pantalla.blit(n3, (0, 0))
        if tiempo > 9500: 
            pantalla.blit(n4, (0, 0))
        if tiempo > 12500:
            pantalla.blit(n5, (0, 0))
        if tiempo > 16500:
            pantalla.blit(n6, (0, 0))
        if tiempo > 19200:
            pantalla.blit(n7, (0, 0))
            pantalla_actual = "n7"

    elif pantalla_actual == "comienzo":  
        texto_gris.stop()
        if not favela_reproduciendo:
            favela.play()
            favela_reproduciendo = True

        pantalla.fill((244, 228, 188))   
        tiempo = pygame.time.get_ticks() - tiempo_comienzo
        pantalla.blit(auto1, (0, 0))

        if tiempo > 6000:
            favela.stop()
            pantalla.blit(auto2, (475, 0))
            interfe.play()

        if tiempo > 10000:
            pantalla.blit(auto3, (920, 0))
            interfe.stop()
            if not auto0_paro_reproducido:
                auto_paro_sonido0.play()
                auto0_paro_reproducido = True

            sin_arranque.play()
            pantalla_actual = "auto3"

    elif pantalla_actual == "auto_parado":
        auto_paro_sonido0.stop()
        pantalla.fill((244, 228, 188))
        tiempo = pygame.time.get_ticks() - tiempo_auto_parado
        pantalla.blit(parte2, (0, 0))

        if not auto_paro_reproducido:
            auto_paro_sonido.play()
            auto_paro_reproducido = True

        if tiempo > 4000:
            auto_paro_sonido.stop()
            pantalla.blit(parte3, (475, 0))
            auto_paro_sonido2.play()
            pantalla_actual = "parte3"
            sin_arranque.stop()

    elif pantalla_actual == "llegada_estacion":
        auto_paro_sonido2.stop()
        pantalla.fill((244, 228, 188))  
        tiempo = pygame.time.get_ticks() - tiempo_llegadaa

        if tiempo > 2000:
            pantalla.blit(llegada1, (0, 0))
            if not llegada1_son_reproduciendo:
                llegada1_sonido.play()
                llegada1_son_reproduciendo = True
        if tiempo > 6000:
            pantalla.blit(llegada2, (475, 0))
            ruido_tren.play()
            if not llegada2_son_reproduciendo:
                llegada2_sonido.play()
                llegada2_son_reproduciendo = True
        if tiempo > 10000:
            pantalla.blit(llegada3, (920, 0))
            ruido_tren.stop()
            pantalla_actual = "llegada3"

    elif pantalla_actual == "boleto":
        pantalla.fill((244, 228, 188))  
        tiempo = pygame.time.get_ticks() - tiempo_boleto
        if tiempo > 1000:
            tren_humo.play()
            pantalla.blit(tren1, (0, 0))
        if tiempo > 3000:
            tren_humo.stop()
            pantalla.blit(tren2, (470, 0))
            if not boleto1_son_reproduciendo:
                boleto1_sonido.play()
                boleto1_son_reproduciendo = True
        if tiempo > 5000:
            pantalla.blit(tren3, (920, 0))
            pantalla_actual = "tren3"
    
    elif pantalla_actual == "charla":
        tiempo = pygame.time.get_ticks() - tiempo_charla
        pantalla.blit(man, (0, 0))
        if tiempo > 2000:
            pantalla.fill((0, 0, 0))
        if tiempo > 2500:
            pantalla.blit(charla1, (0, 0))
            if not charla1_son_reproduciendo:
                charla1_sonido.play()
                charla1_son_reproduciendo = True
        if tiempo > 5000:
            charla1_sonido.stop()
            pantalla.blit(charla2, (0, 0))
            if not charla2_son_reproduciendo:
                charla2_sonido.play()
                charla2_son_reproduciendo = True
        if tiempo > 7000:
            charla2_sonido.stop()
            pantalla.blit(charla3, (0, 0))
            if not charla3_son_reproduciendo:
                charla3_sonido.play()
                charla3_son_reproduciendo = True
        if tiempo > 9500:
            charla3_sonido.stop()
            pantalla.blit(charla4, (0, 0))
            if not charla4_son_reproduciendo:
                charla4_sonido.play()
                charla4_son_reproduciendo = True
        if tiempo > 27000:
            charla4_sonido.stop()
            pantalla.blit(charla5, (0, 0))
            if not charla5_son_reproduciendo:
                charla5_sonido.play()
                charla5_son_reproduciendo = True
        if tiempo > 42000:
            charla5_sonido.stop()
            pantalla.blit(charla6, (0, 0))
            if not charla6_son_reproduciendo:
                charla6_sonido.play()#y cada una es unica
                charla6_son_reproduciendo = True
        if tiempo > 50000:
            charla6_sonido.stop()
            pantalla.blit(charla7, (0, 0)) 
            if not charla7_son_reproduciendo:
                charla7_sonido.play() #que raro el tren
                charla7_son_reproduciendo = True
        if tiempo > 53000:
            charla7_sonido.stop()
            pantalla.blit(charla8, (0, 0))
            if not charla8_son_reproduciendo:
                charla8_sonido.play()
                charla8_son_reproduciendo = True
        if tiempo > 57000:
            charla8_sonido.stop()
            pantalla.blit(maquinista1, (0, 0))
        if tiempo > 60000:
            pantalla.blit(maquinista2, (0, 0)) #9
            if not charla9_son_reproduciendo:
                charla9_sonido.play()
                charla9_son_reproduciendo = True
        if tiempo > 67000:
            pantalla.blit(charla10, (0, 0))
            if not charla10_son_reproduciendo:
                charla10_sonido.play()
                charla10_son_reproduciendo = True
        if tiempo > 77000:
            pantalla.blit(charla11, (0, 0))
            if not charla11_son_reproduciendo:
                charla11_sonido.play()
                charla11_son_reproduciendo = True

        if tiempo > 80000:
            pantalla.fill((0, 0, 0))
        if tiempo > 83000:
            pantalla.blit(nivel1, (0, 0))
        if tiempo > 86000:
            pantalla.blit(carga, (0, 0))
        if tiempo > 90000:
            pantalla_actual = "afuera"

    #________________________________________ NIVEL 1 ___________________________________________________
    elif pantalla_actual == "n7":
        pantalla.blit(n7, (0,0))
        flecha_abajo_derecha_f(1340, 720)
    
    elif pantalla_actual == "auto3":
        flecha_abajo_derecha_f(1340, 720)

    elif pantalla_actual == "parte3":
        flecha_abajo_derecha_f(1340, 720)
    
    elif pantalla_actual == "llegada3":
        flecha_abajo_derecha_f(1340, 720)

    elif pantalla_actual == "tren3":
        flecha_abajo_derecha_f(1340, 720)
    
    elif pantalla_actual == "jardin":
        pantalla.blit(jardin, (0,0))
        flecha_derecha_f(1280, 400)
        flecha_arriba_f(820, 510)
        flecha_izquierda_f(120, 400)

    elif pantalla_actual == "afuera":
        pantalla.blit(afuera, (0,0))
        flecha_izquierda_f(120, 400)
        flecha_derecha_f(1280, 400)
        flecha_arriba_f(700, 560)
    
    elif pantalla_actual == "interior":
        pantalla.blit(interior, (0,0))
        flecha_abajo_f(650,660)
        flecha_arriba_f(685,510)

    elif pantalla_actual == "cofre":
        pantalla.blit(cofre, (0,0))
        #pygame.draw.rect(pantalla, (255,0,0), BAcertijo, 2)

        flecha_izquierda_f(120,400)
        flecha_derecha_f(1280,400)

    elif pantalla_actual == "cofre_desbloqueando":
        pantalla.blit(cofre_zoom, (0,0))

        if pygame.time.get_ticks() - tiempo_cofre_abierto > 1000:
            cofre_efecto.play()
            pantalla_actual = "cofre_abierto"

    elif pantalla_actual == "cofre_zoom":
        pantalla.blit(cofre_zoom, (0,0))
        flecha_abajo_f(710,660)

        texto1 = fuente.render(letras[0], True, (0,0,0))
        pantalla.blit(texto1, (493,290))
        texto2 = fuente.render(letras[1], True, (0,0,0))
        pantalla.blit(texto2, (607,290))
        texto3 = fuente.render(letras[2], True, (0,0,0))
        pantalla.blit(texto3, (723,290))
        texto4 = fuente.render(letras[3], True, (0,0,0))
        pantalla.blit(texto4, (837,290))

        pygame.draw.rect(pantalla, (255,0,0), rueda1, 2)
        pygame.draw.rect(pantalla, (255,0,0), rueda2, 2)
        pygame.draw.rect(pantalla, (255,0,0), rueda3, 2)
        pygame.draw.rect(pantalla, (255,0,0), rueda4, 2)

        if "".join(letras) == "AMTV":
            tiempo_cofre_abierto = pygame.time.get_ticks()
            pantalla_actual = "cofre_desbloqueando"

    elif pantalla_actual == "cofre_abierto":
        pantalla.blit(cofre_abierto, (0, 0))

        flecha_izquierda_f(120,400)
        flecha_derecha_f(1280,400)

    elif pantalla_actual == "semilla":
        pantalla.blit(cofre_semilla, (0, 0)) 
        flecha_abajo_f(710,660)

    elif pantalla_actual == "cofre_vacio":
        pantalla.blit(cofre_vacio, (0, 0))
        flecha_abajo_f(710,660)
        semilla_efecto.stop()

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

        flecha_abajo_f(900,660)

    elif pantalla_actual == "cabina":
        if maquinista_hablando:
            pantalla.blit(maquinista2, (0,0))
        else:
            pantalla.blit(maquinista1, (0,0))

        pygame.draw.rect(pantalla, (255,0,0), botonMaquinista, 2)
        flecha_abajo_f(710,660)
        if maquinista_hablando:
            if pygame.time.get_ticks() - tiempo_maquinista > 6000:
                maquinista_hablando = False
                charla9_son_reproduciendo = False

        flecha_abajo_f(710,660)

    elif pantalla_actual == "gracias":
        pantalla.blit(gracias1,(0,0))
        tiempo = pygame.time.get_ticks() - tiempo_gracias
        if tiempo < 100:
            if not maquinista_gracias1_son_reproduciendo:
                maquinista_gracias1.play()
                maquinista_gracias1_son_reproduciendo = True

        if tiempo > 5000:
            pantalla.fill((0, 0, 0))
        if tiempo > 7000:
            pantalla.blit(nivel2, (0, 0))
        if tiempo > 12000:
            pantalla.blit(carga, (0, 0))
        if tiempo > 14000:
            pantalla_actual = "intro_archivo"
            tiempo_intro2 = pygame.time.get_ticks()
        
    #________________________________________ NIVEL 2 ___________________________________________________
    elif pantalla_actual == "intro_archivo":
        tiempo = pygame.time.get_ticks() - tiempo_intro2
        if tiempo < 3000:
            pantalla.blit(intro_archivo, (0,0))
        if tiempo < 5000:
            pantalla.blit(cabina2_hablando, (0,0))
            pantalla_actual = "archivo"


    
    elif pantalla_actual == "archivo":
        pantalla.blit(afuera2, (0, 0))
        flecha_arriba_f(680,610)
        flecha_abajo_f(680,680)
        #pygame.draw.rect(pantalla, (255,0,0), B_interior, 2)
        #pygame.draw.rect(pantalla, (255,0,0), Boton_bolso, 2)

    elif pantalla_actual == "caminos":
        pantalla.blit(camino, (0, 0))
        flecha_abajo_f(730,680)
        flecha_camino_izq_f(580,600)
        flecha_camino_med_f(800,570)
        flecha_camino_der_f(910,610)
        #pygame.draw.rect(pantalla, (255,0,0), camino1, 2)
        #pygame.draw.rect(pantalla, (255,0,0), camino2, 2)
        #pygame.draw.rect(pantalla, (255,0,0), camino3, 2)

    elif pantalla_actual == "casa":
        pantalla.blit(casa_afuera, (0,0))
        flecha_izquierda_f(100, 400)
        flecha_arriba_f(1000, 450)
        #pygame.draw.rect(pantalla, (255,0,0), flecha_centro_casa, 2)
        #pygame.draw.rect(pantalla, (255,0,0), flecha_izquierda, 2)

    elif pantalla_actual == "casa2":
        if panel_resuelto == False:
            pantalla.blit(casa_adentro, (0, 0))
            LLL=False
        if panel_resuelto == True:
            LLL=True
            if llave_recogida == True:
                pantalla.blit(llave2, (0,0))
                LLL= False
            else:
                pantalla.blit(llave1, (0,0))
            #pygame.draw.rect(pantalla, (255,0,0), B_llave, 2)      
        flecha_izquierda_f(100, 400)

    elif pantalla_actual == "panel":
        pantalla.blit(panel, (0,0))
        if palancas[0]:
            pantalla.blit(palanca_arriba, (150,200))
        else:
            pantalla.blit(palanca_abajo, (150, 280))
        if palancas[1]:
            pantalla.blit(palanca_arriba, (420,200))
        else:
            pantalla.blit(palanca_abajo, (420, 280))
        if palancas[2]:
            pantalla.blit(palanca_arriba, (700,200))
        else:
            pantalla.blit(palanca_abajo, (700, 280))
        if palancas[3]:
            pantalla.blit(palanca_arriba, (970,200))
        else:
            pantalla.blit(palanca_abajo, (970, 280))

        if palancas == [False, True, False, True]:
            panel_resuelto = True 
            
        flecha_abajo_f(710,660)
        #pygame.draw.rect(pantalla, (255,0,0), B_palanca1, 2)
        #pygame.draw.rect(pantalla, (255,0,0), B_palanca2, 2)
        #pygame.draw.rect(pantalla, (255,0,0), B_palanca3, 2)
        #pygame.draw.rect(pantalla, (255,0,0), B_palanca4, 2)

    elif pantalla_actual == "libro":
        pantalla.blit(libro, (0, 0))

        if libro_abierto:
            sombra = pygame.Surface((1400,800))
            sombra.set_alpha(150)
            sombra.fill((0,0,0))
            pantalla.blit(sombra, (0,0))

            if pagina_libro == 1:
                pantalla.blit(libro1, (250,150))
                flecha_libro_der_f(1080,550)
            elif pagina_libro == 2:
                pantalla.blit(libro2, (250,150))
                flecha_libro_izq_f(320,550)
                flecha_libro_der_f(1080,550)
            elif pagina_libro == 3:
                pantalla.blit(libro3, (250,150))
                flecha_libro_izq_f(320,550)
                flecha_libro_der_f(1080,550)
            elif pagina_libro == 4:
                pantalla.blit(libro5, (250,150))
                flecha_libro_izq_f(320,550)
                flecha_libro_der_f(1080,550)
            elif pagina_libro == 5:
                pantalla.blit(libro4, (250,150))
                flecha_libro_izq_f(320,550)

        flecha_abajo_derecha_f(1250,500)
        flecha_abajo_derecha_f(1250, 500)

    elif pantalla_actual == "puerta_biblioteca":
        pantalla.blit(puerta, (0, 0))
        flecha_abajo_pequena_f(680, 690)
        flecha_arriba_f(680, 500)
        #pygame.draw.rect(pantalla, (255,0,0), atras, 2)
        #pygame.draw.rect(pantalla, (255,0,0), flecha_centro_central_peque, 2)

    elif pantalla_actual == "puerta":
        pantalla.blit(puerta_zoom, (0, 0))
        flecha_abajo_pequena_f(700, 710)

        if Mensaje_ce:
            pygame.draw.rect(pantalla, (40,40,40), (1100,40,200,35))
            pygame.draw.rect(pantalla, (255,255,255), (1100,40,200,35), 2)  
            Cerrado = fuente_pequenia.render("Cerrado", True, (255,255,255))
            pantalla.blit(Cerrado, (1150,40))

            if pygame.time.get_ticks() - tiempo_cerrado > 2000:
                Mensaje_ce = False
        #pygame.draw.rect(pantalla, (255,0,0), B_volver_puerta, 2)
        #pygame.draw.rect(pantalla, (255,0,0), B_puerta, 2)

    elif pantalla_actual == "puerta_abierta1":
        pantalla.blit(puerta_abierta1, (0,0))
        flecha_abajo_pequena_f(700, 710)
        #pygame.draw.rect(pantalla, (255,0,0), B_puerta, 2)
        #pygame.draw.rect(pantalla, (255,0,0), atras, 2)


    elif pantalla_actual == "puerta_interior":
        pantalla.blit(inte_biblio,(0,0))
        flecha_derecha_f(1280,400)
        flecha_abajo_pequena_f(700, 710)

        #pygame.draw.rect(pantalla, (255,0,0), B_volver_puerta, 2)
        #pygame.draw.rect(pantalla, (255,0,0), flecha_derecha, 2)
        #pygame.draw.rect(pantalla, (255,0,0), cofre_A, 2)

    elif pantalla_actual == "sala_mapa":
        pantalla.blit(mapa,(0,0))
        flecha_abajo_pequena_f(700, 710)

    elif pantalla_actual == "cofre_cerrado_archivo":
        pantalla.blit(cofre_archi, (0,0))
        num1 = fuente.render(str(numeros[0]), True, (255,255,255))
        pantalla.blit(num1, (530,480))
        num2 = fuente.render(str(numeros[1]), True, (255,255,255))
        pantalla.blit(num2, (650,480))
        num3 = fuente.render(str(numeros[2]), True, (255,255,255))
        pantalla.blit(num3, (770,480))
        num4 = fuente.render(str(numeros[3]), True, (255,255,255))
        pantalla.blit(num4, (880,480))

        flecha_abajo_pequena_f(700, 710)
        #pygame.draw.rect(pantalla, (255,0,0), C_num1, 2)
        #pygame.draw.rect(pantalla, (255,0,0), C_num2, 2)
        #pygame.draw.rect(pantalla, (255,0,0), C_num3, 2)
        #pygame.draw.rect(pantalla, (255,0,0), C_num4, 2)

        if numeros == [7,3,5,2]:
            pantalla_actual = "cofre_abierto2"

    elif pantalla_actual == "cofre_abierto2":
        if fusible_recogido:
            pantalla.blit(cofre_vacio2, (0,0))
        else:
            pantalla.blit(cofre_abierto2, (0,0))
        flecha_abajo_pequena_f(700, 710)
        #pygame.draw.rect(pantalla, (255,0,0), B_fusible, 2)
             
    elif pantalla_actual == "interior2":
        pantalla.blit(archivo2_viejo, (0,0))
        flecha_abajo_f(620,660)
        flecha_arriba_f(640,550)
    
    elif pantalla_actual == "cabina2":
        if maquinista2_intro_son_reproduciendo:
            pantalla.blit(maquinista_fusible, (0,0))
            tiempo = pygame.time.get_ticks() - tiempo_maquinista2
            if tiempo > 4000:
                maquinista_intro_son_reproduciendo = False
                pantalla.blit(cabina2,(0,0))
        else:
            pantalla.blit(cabina2,(0,0))
                
        flecha_abajo_f(710,660)

    elif pantalla_actual == "gracias2":
        pantalla.blit(gracias2,(0,0))
        tiempo = pygame.time.get_ticks() - tiempo_gracias
        if tiempo < 100:
            if not maquinista_gracias2_son_reproduciendo:
                maquinista_gracias1.play()
                maquinista_gracias2_son_reproduciendo = True
    
        if tiempo > 5000:
            pantalla.fill((0, 0, 0))
        if tiempo > 7000:
            pantalla.blit(nivel3, (0, 0))
        if tiempo > 12000:
            pantalla.blit(carga, (0, 0))
        if tiempo > 14000:
            pantalla_actual = "nivel3" 

#------------------------------------------------------------------------
    pantallas_ocultas = ["inicio", "carga", "juego", "historia",
                        "n7", "comienzo", "auto3", "auto_parado", 
                        "parte3", "llegada_estacion", "llegada3", 
                        "boleto", "tren3", "charla"]

    if pantalla_actual not in pantallas_ocultas:
        inventario_f()

    pygame.display.flip()


# FALTA SEGUNDO NIVEL:
# intro
# dar fusble al maquinista
# que de las gracias
# musica y sonido
# cerrar nivel y pasar al tres