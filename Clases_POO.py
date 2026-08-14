import sys
import pygame

class Juego:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.pantalla = pygame.display.set_mode((1400,800))
        pygame.display.set_caption("Videojuego: ¨EL PARADOR¨")
        self.pantalla_actual = "inicio"

        self.pantallas_ocultas = ["inicio", "carga", "juego", "historia", "n7", "comienzo", "auto3",
                             "auto_parado", "parte3", "llegada_estacion", "llegada3", "boleto", "tren3", "charla"]

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

        #----------- INVENTARIO --------------------------------------------
        self.inventario_abierto = False
        self.tiempo_carga = 0
        self.tiempo_historia = 0

        #----------- NIVEL UNO -----------------------------------------------------------------------

        self.AAA = True  #Para que la imagen de cofre abierto se mantenga una vez que se abre el cofre
        self.BBB = True  #Para que la imagen de cofre vacio se mantenga una vez que se lleva la semilla

        self.letras = ["A", "A", "A", "A"]
        self.codigo_ingresado = ""
        self.codigo_correcto = "AMTV"
        self.abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.planta_ampliada = None
        self.fuente = pygame.font.SysFont("Times New Roman", 80)
        self.fuente_pequenia = pygame.font.SysFont("Times New Roman", 25)

        self.maquinista_hablando = False
        self.tiempo_cofre_abierto = 0
        self.tiempo_gracias = 0 
        self.tiempo_maquinista = 0

        #------------ NIVEL DOS ----------------------------------------------------------------------
        self.LLL=True
        self.libro_abierto = False
        self.pagina_libro = 1
        self.panel_resuelto = False
        self.llave_recogida = False
        self.puerta_abierta = False
        self.fusible_recogido = False
        self.maquinista_hablando2 = False
        

        self.Mensaje_ce = False
        self.tiempo_cerrado = 0

        self.num_encontrado = []
        self.num_correcto = "7352"
        self.num_ingresado = ""

        self.tiempo_maquinista2 = 0
        self.tiempo_gracias = 0
        self.tiempo_intro2 = 0

        self.numeros = [0,0,0,0]

        self.palancas = [False, False, False, False]

        #---------------------------------------------------------

        self.imagenes = Imagenes()
        self.sonidos = Sonidos()
        self.inventario = Inventario()
        self.botones = Botones()

    def siguiente_letra(self, letra):
        indice = self.abecedario.index(letra)
        return self.abecedario[(indice + 1) % len(self.abecedario)]

    def siguiente_numero(self, numero):
        return (numero + 1) % 10

    def obtener_pantalla(self):
        return self.pantalla
    
    def manejar_eventos(self):
        eventos = pygame.event.get()
        for evento in eventos:
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        return eventos
    
    def cambiar_pantalla_si_toca(self, boton, destino, evento, sonido=None):
        if boton.collidepoint(evento.pos):
            if sonido:
                sonido.play()
            self.pantalla_actual = destino
            return True
        return False


    def dibujar(self):

        #------------- NIVEL UNO ---------------------------------------
        if self.pantalla_actual == "jardin":
            self.pantalla.blit(self.imagenes.jardin, (0, 0))
            self.flecha_derecha_f(1280, 400)
            self.flecha_arriba_f(820, 510)
            self.flecha_izquierda_f(120, 400)

        elif self.pantalla_actual == "afuera":
            self.pantalla.blit(self.imagenes.afuera, (0,0))
            self.flecha_izquierda_f(120, 400)
            self.flecha_derecha_f(1280, 400)
            self.flecha_arriba_f(700, 560)

        elif self.pantalla_actual == "interior":
            self.pantalla.blit(self.imagenes.interior, (0,0))
            self.flecha_abajo_f(650,660)
            self.flecha_arriba_f(685,510)

        elif self.pantalla_actual == "cofre":
            self.pantalla.blit(self.imagenes.cofre, (0,0))
            self.flecha_izquierda_f(120,400)
            self.flecha_derecha_f(1280,400)

        elif self.pantalla_actual == "cofre_zoom":
            self.pantalla.blit(self.imagenes.cofre_zoom, (0,0))
            self.flecha_abajo_f(710,660)

            texto1 = self.fuente.render(self.letras[0], True, (0,0,0))
            self.pantalla.blit(texto1, (493,290))
            texto2 = self.fuente.render(self.letras[1], True, (0,0,0))
            self.pantalla.blit(texto2, (607,290))
            texto3 = self.fuente.render(self.letras[2], True, (0,0,0))
            self.pantalla.blit(texto3, (723,290))
            texto4 = self.fuente.render(self.letras[3], True, (0,0,0))
            self.pantalla.blit(texto4, (837,290))

            pygame.draw.rect(self.pantalla, (255,0,0), self.botones.rueda1, 2)
            pygame.draw.rect(self.pantalla, (255,0,0), self.botones.rueda2, 2)
            pygame.draw.rect(self.pantalla, (255,0,0), self.botones.rueda3, 2)
            pygame.draw.rect(self.pantalla, (255,0,0), self.botones.rueda4, 2)

        elif self.pantalla_actual == "cofre_abierto":
            self.pantalla.blit(self.imagenes.cofre_abierto, (0,0))
            self.flecha_izquierda_f(120,400)
            self.flecha_derecha_f(1280,400)

        elif self.pantalla_actual == "invernadero":
            self.pantalla.blit(self.imagenes.invernadero, (0,0))
            if self.planta_ampliada == "A":
                self.pantalla.blit(self.imagenes.hoja_A, (700,200))
            elif self.planta_ampliada == "M":
                self.pantalla.blit(self.imagenes.hoja_M, (700,200))
            elif self.planta_ampliada == "T":
                self.pantalla.blit(self.imagenes.hoja_T, (700,200))
            elif self.planta_ampliada == "V":
                self.pantalla.blit(self.imagenes.hoja_V, (700,200))
            
            self.flecha_abajo_f(900,660)
            

        elif self.pantalla_actual == "semilla":
            self.flecha_abajo_f(710,660)

        elif self.pantalla_actual == "cofre_vacio":
            self.flecha_abajo_f(710,660)

        elif self.pantalla_actual == "cabina":
            if self.maquinista_hablando:
                self.pantalla.blit(self.imagenes.maquinista2, (0,0))
            else:
                self.pantalla.blit(self.imagenes.maquinista1, (0,0))
            pygame.draw.rect(self.pantalla, (255,0,0), self.botones.botonMaquinista, 2)
            self.flecha_abajo_f(710,660)

        elif self.pantalla_actual == "gracias":
            tiempo = pygame.time.get_ticks() - self.tiempo_gracias
            if tiempo < 5000:
                self.pantalla.blit(self.imagenes.gracias1, (0,0))
            elif tiempo < 12000:
                self.pantalla.blit(self.imagenes.gracias2, (0,0))
            else:
                self.pantalla.blit(self.imagenes.gracias3, (0,0))

        #-----------NIVEL DOS ----------------------------------------------------------



    #-----------FUNCIONES FLECHAS-------------------------------------------------------------
    def flecha_derecha_f(self,x, y):
        pygame.draw.polygon(self.pantalla,(255,255,255),
            [(x+40,y),(x,y-50),(x,y+50)])

    def flecha_izquierda_f(self,x, y):
        pygame.draw.polygon(self.pantalla,(255,255,255),
            [(x-40,y),(x,y-50),(x,y+50)])

    def flecha_arriba_f(self,x, y):
        pygame.draw.polygon(self.pantalla,(255,255,255),
            [(x,y-30),(x-40,y),(x+40,y)])

    def flecha_abajo_f(self,x, y):
        pygame.draw.polygon(self.pantalla,(255,255,255),
            [(x,y+60),(x-50,y),(x+50,y)])

    def flecha_abajo_pequena_f(self,x, y):
        pygame.draw.polygon(self.pantalla,(255,255,255),
            [(x,y+40),(x-50,y),(x+50,y)])

    def flecha_abajo_derecha_f(self,x, y):
        pygame.draw.polygon(self.pantalla,(255,255,255),
            [(x,y-40),(x,y+40),(x+40,y)])

    def flecha_arriba_grande_f(self,x, y):
        pygame.draw.polygon(self.pantalla,(255,255,255),
            [(x,y-60),(x-50,y),(x+50,y)])

    def flecha_camino_izq_f(self,x, y):
        pygame.draw.polygon(self.pantalla,(255,255,255),
            [(x-50,y-40),(x+20,y-30),(x-20,y+10)])

    def flecha_camino_med_f(self,x, y):
        pygame.draw.polygon(self.pantalla,(255,255,255),
            [(x+50,y-40),(x-40,y-10),(x+10,y+10)])

    def flecha_camino_der_f(self,x, y):
        pygame.draw.polygon(self.pantalla,(255,255,255),
            [(x-30,y-20),(x+50,y-30),(x+10,y+30)])

    def flecha_libro_der_f(self,x, y):
        pygame.draw.polygon(self.pantalla,(255,255,255),
            [(x+25, y), (x, y-30), (x, y+30)])

    def flecha_libro_izq_f(self,x, y):
        pygame.draw.polygon(self.pantalla,(255,255,255),
            [(x-25, y), (x, y-30), (x, y+30)])
        

    def tiempos_de_pantalla(self):
        # ---------------- COFRE ZOOM ----------------
        if "".join(self.letras) == "AMTV": #mantener esto en el programa principal
                    self.tiempo_cofre_abierto = pygame.time.get_ticks()
                    self.pantalla_actual = "cofre_abierto"
        # ---------------- COFRE ---------------------
        if self.pantalla_actual == "cofre_desbloqueando":
            if pygame.time.get_ticks() - self.tiempo_cofre_abierto > 1000:
                self.sonidos.cofre_efecto.play()
                self.pantalla_actual = "cofre_abierto"
        # ---------------- COFRE ABIERTO ---------------------
        if pygame.time.get_ticks() - self.tiempo_cofre_abierto > 1000:
            self.sonidos.cofre_efecto.play()
            self.pantalla_actual = "cofre_abierto"
        # ---------------- CABINA ---------------------
        if self.maquinista_hablando:
            if pygame.time.get_ticks() - self.tiempo_maquinista > 6000:
                self.maquinista_hablando = False
                self.charla9_son_reproduciendo = False
        # ---------------- GRACIAS -------------------
        if self.pantalla_actual == "gracias":
            tiempo = pygame.time.get_ticks() - self.tiempo_gracias
            if tiempo < 100:
                if not self.maquinista_gracias1_son_reproduciendo:
                    self.sonidos.maquinista_gracias1.play()
                    self.maquinista_gracias1_son_reproduciendo = True

            elif tiempo > 5000 and not self.maquinista_gracias2_son_reproduciendo:
                self.sonidos.maquinista_gracias2.play()
                self.maquinista_gracias2_son_reproduciendo = True

            elif tiempo > 14000:
                self.pantalla_actual = "intro_archivo"
                self.tiempo_intro2 = pygame.time.get_ticks()



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

    def manejar_mouse(self, evento):
        if evento.type != pygame.MOUSEBUTTONDOWN:
            return
        self.inventario.manejar_click(
        evento.pos,
        self.pantalla_actual,
        self.pantallas_ocultas
        )

        if self.pantalla_actual == "inicio":  # BOTÓN DEL MENÚ PRINCIPAL
            self.cambiar_pantalla_si_toca(
                self.botones.boton_jugar,
                "carga",
                evento,
                self.sonidos.botonson
            )
            self.tiempo_carga = pygame.time.get_ticks()

        elif self.pantalla_actual == "juego":  # BOTÓN DE INSTRUCCIONES
            self.cambiar_pantalla_si_toca(
                self.botones.boton_jugar2,
                "historia",
                evento,
                self.sonidos.botonson
            )
            self.tiempo_historia = pygame.time.get_ticks()

        #--------- NIVEL UNO --------------------------------------------------------
        elif self.pantalla_actual == "jardin":
            self.cambiar_pantalla_si_toca(self.botones.flecha_centro, "invernadero", evento)
            self.cambiar_pantalla_si_toca(self.botones.flecha_izquierda, "afuera", evento)
            if self.botones.flecha_derecha.collidepoint(evento.pos):
                if self.AAA:
                    self.pantalla_actual = "cofre"
                else:
                    self.pantalla_actual = "cofre_abierto"

        elif self.pantalla_actual == "invernadero":
            if self.planta_ampliada is not None:
                self.planta_ampliada = None

            if self.botones.planta_A.collidepoint(evento.pos):
                self.planta_ampliada = "A"

            elif self.botones.planta_M.collidepoint(evento.pos):
                self.planta_ampliada = "M"

            elif self.botones.planta_T.collidepoint(evento.pos):
                self.planta_ampliada = "T"

            elif self.botones.planta_V.collidepoint(evento.pos):
                self.planta_ampliada = "V"
                    
            elif self.botones.flecha_abajo.collidepoint(evento.pos):
                self.pantalla_actual = "jardin"


        elif self.pantalla_actual == "cofre":
            if self.botones.BAcertijo.collidepoint(evento.pos):
                self.sonidos.acertijo1.play()

            elif self.cambiar_pantalla_si_toca(self.botones.flecha_izquierda,"jardin",evento):
                self.sonidos.acertijo1.stop()

            elif self.cambiar_pantalla_si_toca(self.botones.flecha_derecha,"afuera",evento):
                self.sonidos.acertijo1.stop()

            self.cambiar_pantalla_si_toca(self.botones.flecha_centro_central,"cofre_zoom",evento)

        elif self.pantalla_actual == "cofre_abierto":
            self.cambiar_pantalla_si_toca(self.botones.flecha_izquierda,"jardin",evento)
            self.cambiar_pantalla_si_toca(self.botones.flecha_derecha,"afuera",evento)
                
            if self.botones.flecha_centro_central.collidepoint(evento.pos):
                if self.BBB == True:
                    self.sonidos.semilla_efecto.play()
                    self.pantalla_actual = "semilla"
                else:
                    self.pantalla_actual = "cofre_vacio"
        
        elif self.pantalla_actual == "cofre_zoom":
            if self.botones.flecha_cabina2.collidepoint(evento.pos):
                if self.AAA == True:
                    self.pantalla_actual = "cofre"
                else:
                    self.pantalla_actual = "cofre_abierto"
            if self.botones.rueda1.collidepoint(evento.pos):
                self.letras[0] = self.siguiente_letra(self.letras[0])

            elif self.botones.rueda2.collidepoint(evento.pos):
                 self.letras[1] = self.siguiente_letra(self.letras[1])

            elif self.botones.rueda3.collidepoint(evento.pos):
                self.letras[2] = self.siguiente_letra(self.letras[2])

            elif self.botones.rueda4.collidepoint(evento.pos):
                self.letras[3] = self.siguiente_letra(self.letras[3])

        elif self.pantalla_actual == "semilla":
            if self.cambiar_pantalla_si_toca(self.botones.flecha_cabina2,"cofre_abierto",evento):
                self.AAA = False
            if self.cambiar_pantalla_si_toca(self.botones.flecha_centro_central_peque,"cofre_vacio",evento): #si selecciona la semilla...
                self.inventario.objetos.append("semilla_objeto")
                print(self.inventario.objetos)
                self.BBB = False

        elif self.pantalla_actual == "cofre_vacio":
            if self.cambiar_pantalla_si_toca(self.botones.flecha_cabina2,"cofre_abierto",evento):
                self.AAA = False

        elif self.pantalla_actual == "afuera":
            self.sonidos.cascada.play()
            if self.botones.flecha_izquierda.collidepoint(evento.pos):
                if self.AAA == True:
                    self.pantalla_actual = "cofre"
                else:
                    self.pantalla_actual = "cofre_abierto"
            self.cambiar_pantalla_si_toca(self.botones.flecha_derecha,"jardin",evento)
            self.cambiar_pantalla_si_toca(self.botones.flecha_centro2,"interior",evento)

        elif self.pantalla_actual == "interior":
            self.cambiar_pantalla_si_toca(self.botones.flecha_atras,"afuera",evento)
            self.cambiar_pantalla_si_toca(self.botones.flecha_cabina,"cabina",evento)

        elif self.pantalla_actual == "cabina":
            if self.botones.botonMaquinista.collidepoint(evento.pos):
                if self.inventario.objeto_seleccionado == "semilla_objeto":
                    self.inventario.objetos.remove("semilla_objeto")
                    self.inventario.objeto_seleccionado = None
                    self.pantalla_actual = "gracias"
                    self.tiempo_gracias = pygame.time.get_ticks()
                else:
                    if not self.charla9_son_reproduciendo:
                        self.sonidos.charla9_sonido.play()
                        self.charla9_son_reproduciendo = True
                        self.maquinista_hablando = True
                        self.tiempo_maquinista = pygame.time.get_ticks()

            if self.cambiar_pantalla_si_toca(self.botones.flecha_cabina2,"interior",evento):
                self.sonidos.charla9_sonido.stop()
                self.charla9_son_reproduciendo = False
                self.maquinista_hablando = False     



    #----------- NIVEL DOS -----------------------------------------------------
        elif self.pantalla_actual == "archivo":
            self.cambiar_pantalla_si_toca(self.botones.BCentro_n2,"caminos",evento)
            self.cambiar_pantalla_si_toca(self.botones.B_interior,"interior2",evento)
            self.viejo_libro_son_reproduciendo = False
    
        elif self.pantalla_actual == "caminos":
            self.cambiar_pantalla_si_toca(self.botones.camino1,"libro",evento)
            self.cambiar_pantalla_si_toca(self.botones.atras,"archivo",evento)
            self.cambiar_pantalla_si_toca(self.botones.camino2,"puerta_biblioteca",evento)
            self.cambiar_pantalla_si_toca(self.botones.camino3,"casa",evento)
    
        elif self.pantalla_actual == "casa":
            self.cambiar_pantalla_si_toca(self.botones.flecha_izquierda,"caminos",evento)
            self.cambiar_pantalla_si_toca(self.botones.flecha_centro_casa,"casa2",evento)
    
        elif self.pantalla_actual == "casa2":
            self.cambiar_pantalla_si_toca(self.botones.flecha_izquierda,"casa",evento)
            self.cambiar_pantalla_si_toca(self.botones.B_palancas,"panel",evento)
            if self.LLL == True:
                self.sonidos.sistema_poleas.play()
                if self.botones.B_llave.collidepoint(evento.pos):
                    self.llave_recogida=True
                    self.inventario.objetos.append("llave_objeto")
                    print(self.inventario.objetos)
                    self.LLL=False
    
        elif self.pantalla_actual == "puerta_biblioteca":
            self.cambiar_pantalla_si_toca(self.botones.atras,"caminos",evento)
            self.cambiar_pantalla_si_toca(self.botones.flecha_centro_central_peque,"puerta",evento)
    
        elif self.pantalla_actual == "libro":
            if self.botones.B_libro.collidepoint(evento.pos):
                self.libro_abierto = True
    
            elif self.botones.B_flecha_libro_der.collidepoint(evento.pos):
                if self.pagina_libro < 5:
                    self.pagina_libro += 1
                    self.sonidos.efecto_hoja.play()
            elif self.botones.B_flecha_libro_izq.collidepoint(evento.pos):
                if self.pagina_libro > 1:
                    self.pagina_libro -= 1
                    self.sonidos.efecto_hoja.play()
    
            elif self.botones.B_libro_atras.collidepoint(evento.pos):
                self.libro_abierto = False
                self.pagina_libro = 1
                self.pantalla_actual = "caminos"
            elif not self.botones.Rect_libro.collidepoint(evento.pos):
                self.libro_abierto = False
    
        elif self.pantalla_actual == "panel":
            if self.botones.B_palanca1.collidepoint(evento.pos):
                self.palancas[0] = not self.palancas[0]
                self.sonidos.efecto_palanca.play()
            elif self.botones.B_palanca2.collidepoint(evento.pos):
                self.palancas[1] = not self.palancas[1]
                self.sonidos.efecto_palanca.play()
            elif self.botones.B_palanca3.collidepoint(evento.pos):
                self.palancas[2] = not self.palancas[2]
                self.sonidos.efecto_palanca.play()
            elif self.botones.B_palanca4.collidepoint(evento.pos):
                self.palancas[3] = not self.palancas[3]
                self.sonidos.efecto_palanca.play()
            self.cambiar_pantalla_si_toca(self.botones.flecha_cabina2,"casa2",evento)
    
    
        elif self.pantalla_actual == "puerta":
            self.cambiar_pantalla_si_toca(self.botones.atras, "puerta_biblioteca", evento)
    
            if self.botones.B_puerta.collidepoint(evento.pos):
                if self.puerta_abierta:
                    self.pantalla_actual = "puerta_abierta1"
                elif self.inventario.objeto_seleccionado == "llave_objeto":
                    self.inventario.objetos.remove("llave_objeto")
                    self.inventario.objeto_seleccionado = None
                    self.puerta_abierta = True
                    self.pantalla_actual = "puerta_abierta1"
                    self.sonidos.efecto_Pabierta.play()
                else:
                    self.Mensaje_ce = True
                    self.tiempo_cerrado = pygame.time.get_ticks()
    
        elif self.pantalla_actual == "puerta_abierta1":
            self.cambiar_pantalla_si_toca(self.botones.atras,"puerta_biblioteca",evento)
            self.cambiar_pantalla_si_toca(self.botones.B_puerta,"puerta_interior",evento)
    
        elif self.pantalla_actual == "puerta_interior":
            self.cambiar_pantalla_si_toca(self.botones.flecha_derecha,"sala_mapa",evento)
            self.cambiar_pantalla_si_toca(self.botones.B_volver_puerta,"puerta",evento)
            self.cambiar_pantalla_si_toca(self.botones.cofre_A,"cofre_cerrado_archivo",evento)
    
        elif self.pantalla_actual == "cofre_cerrado_archivo":
            self.cambiar_pantalla_si_toca(self.botones.B_volver_puerta,"puerta_interior",evento)
            if self.botones.C_num1.collidepoint(evento.pos):
                self.numeros[0] = self.siguiente_numero(self.numeros[0])
    
            elif self.botones.C_num2.collidepoint(evento.pos):
                self.numeros[1] = self.siguiente_numero(self.numeros[1])
    
            elif self.botones.C_num3.collidepoint(evento.pos):
                self.numeros[2] = self.siguiente_numero(self.numeros[2])
    
            elif self.botones.C_num4.collidepoint(evento.pos):
                self.numeros[3] = self.siguiente_numero(self.numeros[3])
    
        elif self.pantalla_actual == "cofre_abierto2":
            self.cambiar_pantalla_si_toca(self.botones.B_volver_puerta , "puerta_interior", evento)
            
            if self.botones.B_fusible.collidepoint(evento.pos):
                if not self.fusible_recogido:
                    self.fusible_recogido = True
                    self.inventario.objetos.append("fusible_objeto")
                    print(self.inventario.objetos)
    
        elif self.pantalla_actual == "sala_mapa":
            self.cambiar_pantalla_si_toca(self.botones.B_volver_puerta,"puerta_interior",evento)
    
        elif self.pantalla_actual == "interior2":
            self.cambiar_pantalla_si_toca(self.botones.flecha_atras,"archivo",evento) 
            self.cambiar_pantalla_si_toca(self.botones.flecha_cabina,"cabina2",evento)               
            if self.botones.boton_viejo.collidepoint(evento.pos):
                if not self.viejo_libro_son_reproduciendo:
                    self.sonidos.viejo_libro.play()
                    self.viejo_libro_son_reproduciendo = True
                else:
                    self.viejo_libro_son_reproduciendo = False
            if not self.pantalla_actual == "interior2":
                self.sonidos.viejo_libro.stop()
    
        elif self.pantalla_actual == "cabina2":
            if self.cambiar_pantalla_si_toca(self.botones.flecha_cabina2,"interior2",evento):
                self.sonidos.maquinista2_intro.stop()
                self.sonidos.viejo_libro.stop()
            if self.botones.botonMaquinista.collidepoint(evento.pos):
    
                if self.inventario.objeto_seleccionado == "fusible_objeto":
                    self.inventario.objetos.remove("fusible_objeto")
                    self.inventario.objeto_seleccionado = None
                    self.pantalla_actual = "gracias2"
                    self.tiempo_gracias = pygame.time.get_ticks()
                else:
                    if not self.maquinista2_intro_son_reproduciendo:
                        self.sonidos.maquinista2_intro.play()
                        self.maquinista2_intro_son_reproduciendo = True
                        self.tiempo_maquinista2 = pygame.time.get_ticks()
    
            if self.cambiar_pantalla_si_toca(self.botones.flecha_cabina2,"interior2",evento):
                self.sonidos.maquinista2_intro.stop()
                self.maquinista2_intro_son_reproduciendo = False
                self.maquinista_hablando2 = False  


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