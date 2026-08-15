import sys
import pygame
from nivel1 import Nivel1
from Nivel3 import nivel3

class Juego:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.pantalla = pygame.display.set_mode((1400,800))
        pygame.display.set_caption("Videojuego: ¨EL PARADOR¨")
        self.pantalla_actual = "inicio"

        self.tiempo_cofre_abierto = 0

        #--------- ESTADOS DE LOS SONIDOS ------------------------------------------------
        self.sonido_n1 = False
        self.auto_paro_reproducido = False
        self.llegada1_son_reproduciendo = False
        self.llegada2_son_reproduciendo = False
        self.boleto1_son_reproduciendo = False
        self.charla1_son_reproduciendo = False
        self.charla2_son_reproduciendo = False
        self.charla3_son_reproduciendo = False
        self.charla4_son_reproduciendo = False
        self.charla5_son_reproduciendo = False
        self.charla6_son_reproduciendo = False
        self.charla7_son_reproduciendo = False
        self.charla8_son_reproduciendo = False
        self.charla9_son_reproduciendo = False
        self.charla10_son_reproduciendo = False
        self.charla11_son_reproduciendo = False
        self.gracias2_son_reproduciendo = False
        self.maquinista2_intro_son_reproduciendo = False
        self.maquinista_gracias1_son_reproduciendo = False
        self.maquinista_gracias2_son_reproduciendo = False
        self.viejo_intro2_son_reproduciendo = False
        self.viejo_libro_son_reproduciendo = False
        self.favela_reproduciendo = False

        self.fuente = pygame.font.SysFont("Times New Roman", 80)
        self.fuente_pequenia = pygame.font.SysFont("Times New Roman", 25)

        #---------------------------------------------------------
        self.imagenes = Imagenes()
        self.sonidos = Sonidos()
        self.inventario = Inventario()
        self.botones = Botones()

        self.nivel1 = Nivel1 (self.pantalla, self.imagenes, self.sonidos, self.botones)
        self.nivel3 = nivel3 (self.pantalla, self.imagenes, self.sonidos, self.botones)

    def obtener_pantalla(self):
        return self.pantalla
    
    def manejar_eventos(self):
        eventos = pygame.event.get()
        for evento in eventos:
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        return eventos

    def manejar_teclado(self, evento):
        if evento.type == pygame.KEYDOWN:

            if self.pantalla_actual == "cofre":
                if evento.key == pygame.K_BACKSPACE:
                    self.codigo_ingresado = self.codigo_ingresado[:-1]
                else:
                    self.codigo_ingresado += evento.unicode.upper()

                if self.codigo_ingresado == self.codigo_correcto:
                    self.tiempo_cofre_abierto = pygame.time.get_ticks()
                    self.pantalla_actual = "cofre_desbloqueando"

    def ejecutar(self):
        print("juego")

class Inventario():
    def __init__(self):
        self.abierto = False
        self.objetos = []
        self.objeto_seleccionado = None
        self.boton_bolso = Boton(1220, 610, 130, 130)

        self.imagenes_objetos = {
            "semilla_objeto": "semilla_transp",
            "llave_objeto": "llave_transp",
            "fusible_objeto": "fusible_transp"}

        self.casillas = [
        Boton(520, 640, 60, 60), #casilla1
        Boton(590, 640, 60, 60), # '' 2
        Boton(655, 640, 60, 60), # '' 3
        Boton(720, 640, 60, 60), # '' 4
        Boton(790, 640, 60, 60), # '' 5
        Boton(860, 640, 60, 60), # '' 6
        ]


    def alternar(self):
        self.abierto = not self.abierto

    def seleccionar(self, posicion, casillas):
        if not self.abierto:
            return
        for i in range(len(casillas)):
            if casillas[i].collidepoint(posicion):
                if i<len(self.objetos):
                    if self.objeto_seleccionado == self.objetos[i]:
                        self.objeto_seleccionado = None
                    else:
                        self.objeto_seleccionado = self.objetos[i]

    def manejar_click(self, posicion, pantalla_actual, pantallas_ocultas):
        if self.boton_bolso.collidepoint(posicion) and pantalla_actual not in pantallas_ocultas:
            self.alternar()
        if self.abierto:
            self.seleccionar(posicion, self.casillas)


    def dibujar(self, pantalla, imagenes):
        pantalla.blit(imagenes.bolso, (1210, 610))
        if self.abierto:
            pantalla.blit(imagenes.inventario, (470, 500))

            for i in range(len(self.objetos)):
                nombre = self.objetos[i]
                if nombre == "semilla_objeto":
                    imagen = imagenes.semilla_transp
                elif nombre == "llave_objeto":
                    imagen = imagenes.llave_transp
                elif nombre == "fusible_objeto":
                    imagen = imagenes.fusible_transp

                imagen_centrada = imagen.get_rect(center=self.casillas[i].rect.center)
                pantalla.blit(imagen, imagen_centrada)

                if self.objetos[i] == self.objeto_seleccionado:pygame.draw.rect(pantalla,(255, 255, 0),self.casillas[i].rect,3)
class Boton():
    def __init__(self, x, y, ancho, alto):
        self.rect = pygame.Rect(x, y, ancho, alto)
    def collidepoint(self,pos):
        return self.rect.collidepoint(pos)
    def dibujar(self, pantalla, color=(255,0,0), grosor=2): #boton_jugar.dibujar(pantalla)
        pygame.draw.rect(pantalla, color, self.rect, grosor)

class Botones:
    def __init__ (self):
        #-----------------------BOTONES COMIENZO----------------------------------------------
        self.boton_jugar = Boton(510, 468, 350, 65)
        self.boton_jugar2 = Boton(600, 726, 220, 61)

        self.boton1_historia = Boton(600, 726, 220, 61)
        self.boton_cabina = Boton(600, 726, 220, 61)
        #-----------------BOTONES NIVEL UNO------------------------------
        self.flecha_centro = Boton(750, 450, 100, 100)  #x-y-ancho-largo
        self.flecha_centro2 = Boton(660, 380, 100, 180 )
        self.flecha_derecha = Boton(1220, 280, 180, 220)
        self.flecha_izquierda = Boton(30, 280, 100, 220)
        self.flecha_abajo = Boton(820, 600, 120, 140) #dentro del invernadero
        self.flecha_abajo2 = Boton(620, 430, 120, 140)
        self.flecha_atras = Boton(610, 600, 120, 140)
        self.flecha_cabina = Boton(600, 480, 120, 140)
        self.flecha_cabina2 = Boton(680, 600, 120, 140) #abajo al medio
        self.flecha_abajo_derecha = Boton(1240, 600, 140, 140)
        self.flecha_centro_central = Boton(600, 300, 220, 300)
        self.flecha_centro_central_peque = Boton(660, 420, 100, 100)
        self.flecha_centro_casa = Boton(950, 300, 150, 200)
        self.BAcertijo = Boton(890, 280, 150, 300)

        self.planta_A = Boton(500, 180, 220, 220)
        self.planta_M = Boton(450, 330, 280, 180)
        self.planta_T = Boton(680, 620, 180, 110)# x y ancho largo
        self.planta_V = Boton(20, 150, 280, 280)

        self.rueda1 = Boton(470, 230, 110, 190)
        self.rueda2 = Boton(585, 230, 110, 190)
        self.rueda3 = Boton(700, 230, 110, 190)
        self.rueda4 = Boton(815, 230, 110, 190)

        self.atras = Boton(620, 670, 120, 80)
        self.B_libro = Boton(200, 300, 260, 250)
        self.B_interior = Boton(620, 570, 120, 60)
        self.BCentro_n2 = Boton(620, 670, 120, 80)
        self.B_libro_atras = Boton(1220, 450, 120, 100)

        self.Rect_libro = Boton(250,150,900,500)
        self.B_flecha_libro_der = Boton(1050,500,80,100)
        self.B_flecha_libro_izq = Boton(280,500,80,100)

        self.camino1 = Boton(510, 540, 100, 100)
        self.camino2 = Boton(750, 500, 100, 100)
        self.camino3 = Boton(880, 550, 100, 100)

        self.botonMaquinista = Boton(900, 300, 250, 380)

        self.B_puerta = Boton(600, 320, 210, 380)
        self.B_volver_puerta = Boton(650,700,100,100)
        self.B_palancas = Boton(450, 450, 430, 220)
        self.B_fusible = Boton(600, 400, 200, 200)

        self.cofre_A = Boton(620, 300, 150, 100)

        self.C_num1 = Boton(500,480,90,90)
        self.C_num2 = Boton(620,480,90,90)
        self.C_num3 = Boton(740,480,90,90)
        self.C_num4 = Boton(850,480,90,90)

        self.B_palanca1 = Boton(220,300,100,210)
        self.B_palanca2 = Boton(500,300,100,210)
        self.B_palanca3 = Boton(780,300,100,210)
        self.B_palanca4 = Boton(1050,300,100,210)

        self.B_llave = Boton(1050,300,100,200)
        self.boton_viejo = Boton(950,350,200,300)

        #nivel 3
        self.B_camino = Boton(420,600,100,100)
        self.B_camino_flechas = Boton(890,520,100,100)
        self.B_camino1_ciudad = Boton(510,470,100,100)
        self.B_camino2_ciudad = Boton(660,440,100,60)
        self.B_camino3_ciudad = Boton(810,480,100,100)
        self.B_camino_medio = Boton(650,510,100,60)

        self.Boton_bolso = Boton(1220, 610, 130, 130)

class Imagenes():
    def cargar(self, ruta, ancho, alto):
        imagen = pygame.image.load(ruta)
        return pygame.transform.scale(imagen, (ancho, alto))

    def __init__(self):
        #------- INVENTARIO ------------------------------------------------------
        self.bolso = self.cargar("visual/bolso.png",150,130)
        self.inventario = self.cargar("visual/inventario.png",500,400)

        #-------- CARGA DE NIVELES -----------------------------------------------
        self.nivel1 = self.cargar("visual/Nivel1.jpeg",1400,800)
        self.nivel2 = self.cargar("visual/Nivel2.jpeg",1400,800)
        self.nivel3 = self.cargar("visual/Nivel3.jpeg",1400,800)
        self.nivel4 = self.cargar("visual/Nivel4.jpeg",1400,800)

        #---------- IMAGENES DE CARGA GENERAL ------------------------------------
        self.inicio = self.cargar('visual/Inicio.png',1400,800)
        self.carga = self.cargar('visual/explorando_dimen.png',1400,800)
        self.intro = self.cargar('visual/instrucciones.png',1400,800)
        self.carga2 = self.cargar('visual/carga2.png',1400,800)

        #---------- HISTORIA -----------------------------------------------------
        self.n1 = self.cargar('visual/desde.png',1400,800)
        self.n2 = self.cargar('visual/unico.png',1400,800)
        self.n3 = self.cargar('visual/ruido.png',1400,800)
        self.n4 = self.cargar('visual/persiguen.png',1400,800)
        self.n5 = self.cargar('visual/importancia.jpeg',1400,800)
        self.n6 = self.cargar('visual/noche1.png',1400,800)
        self.n7 = self.cargar('visual/algopaso.png',1400,800)
        self.auto1 = self.cargar('visual/auto_parte11.jpg',490,800)
        self.auto2 = self.cargar('visual/auto_parte22.jpg',490,800)
        self.auto3 = self.cargar('visual/auto_parte3.png',480,800) 
        self.parte2 = self.cargar('visual/paro.png',490,800)
        self.parte3 = self.cargar('visual/paro2.png',925,800)
        self.llegada1 = self.cargar('visual/llegada1.jpg',490,800)
        self.llegada2 = self.cargar('visual/llegada2.jpg',470,800)
        self.llegada3 = self.cargar('visual/llegada3.jpg',490,800)
        self.tren1 = self.cargar("visual/tren1.jpg",490,800)
        self.tren2 = self.cargar("visual/tren2.jpg",490,800)
        self.tren3 = self.cargar("visual/tren3.jpg",490,800)
        self.man = self.cargar("visual/tipo_sentado.jpeg",1400,800)
        self.charla1 = self.cargar("visual/charla1.jpg",1400,800)
        self.charla2 = self.cargar("visual/charla2.jpg",1400,800)
        self.charla3 = self.cargar("visual/charla3.jpg",1400,800)
        self.charla4 = self.cargar("visual/charla4.jpg",1400,800)
        self.charla5 = self.cargar("visual/charla5.jpg",1400,800)
        self.charla6 = self.cargar("visual/charla6.jpeg",1400,800)
        self.charla7 = self.cargar("visual/charla7.PNG",1400,800)
        self.charla8 = self.cargar("visual/charla8.jpeg",1400,800)
        self.charla9 = self.cargar("visual/charla9.png",1400,800)
        self.charla10 = self.cargar("visual/charla10.jpeg",1400,800)
        self.charla11 = self.cargar("visual/charla11.jpeg",1400,800)
        self.maquinista1 = self.cargar("visual/maquinista1.jpg",1400,800)
        self.maquinista2 = self.cargar("visual/maquinista2.jpeg",1400,800)

        #-------------- OBJETOS QUE CONSIGUE EL USUARIO ------------------------------
        self.semilla_transp = self.cargar("visual/semilla_trasparente.png",100,90)
        self.fusible_transp = self.cargar("visual/fusible_transparente.png",100,90)
        self.llave_transp = self.cargar("visual/llave_transparente.png",100,90)

        #---------------- NIVEL UNO --------------------------------------------------------------------------
        self.interior = self.cargar("visual/vagon_vacio.jpeg",1400,800)

        self.jardin = self.cargar("visual/lenguas_muertas2.jpg",1400,800)
        self.invernadero = self.cargar("visual/invernadero_adentro.jpg",1400,800)
        self.cofre = self.cargar("visual/cofre_lengua1.jpeg",1400,800)
        self.cofre_abierto = self.cargar("visual/cofre_lengua2.jpeg",1400,800)
        self.cofre_zoom = self.cargar("visual/cofre_zoom2.jpeg",1400,800)
        self.afuera = self.cargar("visual/tren_lengua_abierto.png",1400,800)
        self.cofre_semilla = self.cargar("visual/cofre_semilla.jpeg",1400,800)
        self.cofre_vacio = self.cargar("visual/cofre_vacio.jpeg",1400,800)
        self.gracias1 = self.cargar("visual/gracias1.jpeg",1400,800)

        #HOJAS DEL INVERNADERO
        self.hoja_A = self.cargar("visual/hoja_A.jpg",600,400)
        self.hoja_M = self.cargar("visual/hoja_M.jpg",600,400)
        self.hoja_T = self.cargar("visual/hoja_T.jpg",600,400)
        self.hoja_V = self.cargar("visual/hoja_V.jpg",600,400)

        #---------------- NIVEL DOS -------------------------------------------------------------------------
        self.camino = self.cargar("visual/tres_caminos.jpeg",1400,800)

        #LIBRO
        self.libro = self.cargar("visual/libro_archivo.jpeg",1400,800)
        self.libro1 = self.cargar("visual/libro1.png",900,500)
        self.libro2 = self.cargar("visual/libro2.png",900,500)
        self.libro3 = self.cargar("visual/libro3.jpeg",900,500)
        self.libro4 = self.cargar("visual/libro4.png",900,500)
        self.libro5 = self.cargar("visual/libro5.png",900,500)

        #TREN
        self.intro_archivo = self.cargar("visual/intro_archivo.jpeg",1400,800)
        self.afuera2 = self.cargar("visual/tren_archivo_afuera.jpg",1400,800)
        self.cabina2 = self.cargar("visual/cabina2.jpeg",1400,800)
        self.cabina2_hablando = self.cargar("visual/cabina2_hablando.jpeg",1400,800)
        self.vagon_archivo = self.cargar("visual/vagon_interior.jpeg",1400,800)
        self.gracias2 = self.cargar("visual/gracias2.jpeg",1400,800)
        self.maquinista_fusible = self.cargar("visual/cabina2_hablando.jpeg",1400,800)
        self.archivo2_viejo = self.cargar("visual/archivo2_viejo.jpeg",1400,800)

        #BIBLIOTECA
        self.puerta = self.cargar("visual/biblioteca_sumergido.jpeg",1400,800)
        self.puerta_zoom = self.cargar("visual/puerta_zoom.jpeg",1400,800)
        self.puerta_abierta1 = self.cargar("visual/puerta_abierta.png",1400,800)
        self.cofre_abierto2 = self.cargar("visual/cofre_abierto2.jpeg",1400,800)
        self.cofre_vacio2 = self.cargar("visual/cofre_vacio2.jpeg",1400,800)
        self.inte_biblio = self.cargar("visual/interior_biblioteca.png",1400,800)
        self.mapa = self.cargar("visual/sala_mapa.jpeg",1400,800)
        self.cofre_archi = self.cargar("visual/cofre_archivo_cerrado.png",1400,800)

        #CASA LLAVE
        self.casa_afuera = self.cargar("visual/casa_afuera.jpeg",1400,800)
        self.casa_adentro = self.cargar("visual/casa_adentro.jpeg",1400,800)
        self.panel = self.cargar("visual/mueble_palancas.jpeg",1400,800)
        self.palanca_arriba = self.cargar("visual/P_arriba.png",270,350)
        self.palanca_abajo = self.cargar("visual/P_abajo.png",250,350)
        self.llave1 = self.cargar("visual/llave_abajo.jpeg",1400,800)
        self.llave2 = self.cargar("visual/sin_llave.jpeg",1400,800)

        #---------------- NIVEL TRES -------------------------------------------------------------------------
        self.ciudad_invertida = self.cargar("visual/ciudad_invertida.jpeg",1400,800)
        #CAMINOS
        self.flechas_ciudad_invertida = self.cargar("visual/flechas_ciudad_invertida.jpeg",1400,800)
        self.camino1 = self.cargar("visual/camino1_ciudad_invertida.jpeg",1400,800)
        self.camino2 = self.cargar("visual/camino2_ciudad_invertida.jpeg",1400,800)
        self.camino3 = self.cargar("visual/camino3_ciudad_invertida.jpeg",1400,800)
        self.camino4 = self.cargar("visual/camino4_ciudad_invertida.jpeg",1400,800)
        self.camino5 = self.cargar("visual/camino5_ciudad_invertida.jpeg",1400,800)


class Sonidos():
    def cargar(self, ruta, volumen=1):
        sonido = pygame.mixer.Sound(ruta)
        sonido.set_volume(volumen)
        return sonido

    def __init__(self):
        #----------EFECTOS------------------------------------------------------
        self.botonson = self.cargar("musica_sonido/boton_efecto.mp3")
        #del tren
        self.ruido_tren = self.cargar("musica_sonido/Bocina_tren.mp3",0.3)
        self.tren_humo = self.cargar("musica_sonido/tren_humo.mp3",0.1)
        self.tren_avanzando = self.cargar("musica_sonido/tren_avanzando.WAV")
        #
        self.cofre_efecto = self.cargar("musica_sonido/cofre_abriendose.mp3")
        self.semilla_efecto = self.cargar("musica_sonido/efecto_semilla.mp3",0.5)
        #-------------HISTORIA--------------------------------------------------------------------------------
        self.texto_gris = self.cargar("musica_sonido/1_texto_gris_audio.mpeg")
        self.auto_paro_sonido0 = self.cargar("musica_sonido/y_eso.mpeg")
        self.auto_paro_sonido = self.cargar("musica_sonido/2_ay_no_el_auto_se_paro.mpeg")
        self.auto_paro_sonido2 = self.cargar("musica_sonido/3_bueno_por_suerte_hay_un_tren_cerca.mpeg")
        self.llegada1_sonido = self.cargar("musica_sonido/4_por_fin_llegue_a_la_estacion.mpeg")
        self.llegada2_sonido = self.cargar("musica_sonido/5_wow_que_rapido.mpeg")
        self.boleto1_sonido = self.cargar("musica_sonido/6_este_tren_debe.mpeg")
        self.charla1_sonido = self.cargar("musica_sonido/7_es_raro.mpeg")
        self.charla2_sonido = self.cargar("musica_sonido/8_por_que_dice_eso.mpeg")
        self.charla3_sonido = self.cargar("musica_sonido/9_debes_ser_nueva.mpeg")
        self.charla4_sonido = self.cargar("musica_sonido/10_es_no_es_un_tren.mpeg")
        self.charla5_sonido = self.cargar("musica_sonido/11_hoy_vamos_a_pasar.mpeg")
        self.charla6_sonido = self.cargar("musica_sonido/12_y_cada_una_es_unica.mpeg")
        self.charla7_sonido = self.cargar("musica_sonido/13_que_raro_el_tren.mpeg")
        self.charla8_sonido = self.cargar("musica_sonido/14_rapido_ve_a_preguntarle.mpeg")
        self.charla9_sonido = self.cargar("musica_sonido/17_sin_combustible_maquinista.mp3")
        self.charla10_sonido = self.cargar("musica_sonido/15_el_maquinista_me_dijo.mpeg")
        self.charla11_sonido = self.cargar("musica_sonido/16_claro_por_supuesto.mp3")
        self.chica_auto_paro2 = self.cargar("musica_sonido/chica_estacion_cerca.mp3")
        self.interfe = self.cargar("musica_sonido/interferencia_efecto.mp3",0.1)
        self.sin_arranque = self.cargar("musica_sonido/efecto_sin_arranque.mp3",0.3)

        self.favela = self.cargar("musica_sonido/Favela.mp3",0.7)
        #------------- dentro del TREN --------------------------------------------------------------------
        self.gracias_maquinista2 = self.cargar("musica_sonido/gracias_maquinista2.mp3")
        self.maquinista2_intro = self.cargar("musica_sonido/maquinista2_intro.mp3")
        self.viejo_intro2 = self.cargar("musica_sonido/voz_viejo_intro2.mp3")
        self.viejo_libro = self.cargar("musica_sonido/viejo_molesto3.mp3")
        self.maquinista_gracias1 = self.cargar("musica_sonido/18_gracias_maquinista.mp3")
        self.maquinista_gracias2 = self.cargar("musica_sonido/gracias_maquinista2.mp3")

        #------------- NIVEL UNO -----------------------------------------------------------
        self.cascada = self.cargar("musica_sonido/Cascadas_agua.mp3",0.5)
        self.acertijo1 = self.cargar("musica_sonido/acertijo_viejo.mp3",0.5)
        #------------- NIVEL DOS -----------------------------------------------------------
        self.efecto_palanca = self.cargar("musica_sonido/efecto_palanca.mp3")
        self.sistema_poleas = self.cargar("musica_sonido/sistema_poleas.mp3")
        self.efecto_hoja = self.cargar("musica_sonido/pagina_libro.mp3")
        self.efecto_Pcerrado = self.cargar("musica_sonido/puerta_cerrada.mp3")
        self.efecto_Pabierta = self.cargar("musica_sonido/puerta_abierta.mp3")