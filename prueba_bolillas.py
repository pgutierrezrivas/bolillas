import pygame as pg
from class_bolilla import *

pg.init()

anchoPantalla = 800
altoPantalla = 600

pantallaPrincipal = pg.display.set_mode( (anchoPantalla, altoPantalla) )
pg.display.set_caption("Bolillas Rebotando")

gameOver = False

#idea inicial: creo 20 variables bolas y sus caracteristicas particulares más una lista para recogerlas a todas.
    #bola1 = Bolilla(400, 300, (192, 57, 43), 20, 20, 0.5, 0.5, True)
    #bola2 = Bolilla(200, 150, (255, 240, 51), 50, 50, 0.5, 0.5, False)
    #listBolas = [bola1, bola2, bola3, bolaa4, ..., bola20]
    #bola1.mueveBola = self.mueveBola aqui el parametro self del metodo mueveBola hace referencia a la instancia/objeto(bola1) que llama a dicho metodo.

#idea para no repetir tanto codigo al crear las bolas con una lista más el uso de la libreria random(aleatorio):
listBolas = [] #creamos lista a cero.
for i in range(20): #creamos 20 bolas añadimos a la lista vacia con append:
    #lista.append(clase.funcion(parametros)):
    listBolas.append(Bolilla.bolaAleatoria(600, 400, i)) #aqui el metodo bolaAleatoria no tiene el parametro self ya que no lo llamamos a traves de un objeto sino de la clase(Bolilla).

while not gameOver:

    for eventos in pg.event.get(): #captura todos los eventos/objetos de pygame en forma de lista y los podemos recorrer
        print(eventos)
        if eventos.type == pg.QUIT:
            gameOver = True

    pantallaPrincipal.fill( (52, 152, 219) )#asignar (en tuplas) un color rgb a la pantalla.

    for bola in listBolas: #para cada bola creada hacemos que se muevan con la funcion mueveBola:
        bola.mueveBola(anchoPantalla, 0, altoPantalla, 0)

        #unos seran rectangulos y otros circulos y por tanto debemos crear dos opciones:
        if bola.esCirculo:
            pg.draw.circle(pantallaPrincipal, bola.color, (bola.posicionX, bola.posicionY), bola.ancho, 0) #esto dibuja circulos.
        else:
            pg.draw.rect(pantallaPrincipal, bola.color, (bola.posicionX, bola.posicionY, bola.ancho, bola.alto)) #esto dibuja rectangulos.

    pg.display.flip()#activa todo lo que hemos hecho en la pantalla por lo que las cosas que pongamos tienen que escribirse antes de este comando para que se ejecuten.

pg.quit() #para que termine de mostrar
