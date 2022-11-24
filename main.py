import pygame as pg

#inicializar todos los modulos de pygame
#pantallas,sonidos,teclados, etc
pg.init()

#creamos una pantalla o surface
pantalla_principal = pg.display.set_mode( (800,600) )#ventana y tamaño (en tuplas) ventana
pg.display.set_caption("Bolillas Rebotando")#titulo de la ventana


game_over = False

x1=400 #creamos un contador para que se pueda mover en el eje x y en el y
y1=300
vx1=1
vy1=1

x2=400 
y2=300
vx2=1
vy2=1

while not game_over:

    for eventos in pg.event.get(): #captura todos los eventos/objetos de pygame en forma de lista y los podemos recorrer
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill( (52, 152, 219) )#asignar (en tuplas) un color a la pantalla
    
    x += vx
    y += vy
    if x >= 800 or x==0:#llega a los limites en x
        vx *= -1 #se pone el asterisco para cambiar el simbolo del -1 cuando llegue a los limites
    if y >= 600 or y==0:#llega a los limites en y
        vy *= -1

    pg.draw.rect(pantalla_principal, (192, 57, 43), (x,y, 20,20))#metodo para dibujar un rectangulo introduciendo: sourface, color en rgb, posicion del centro del objeto ancho y largo + tamaño del rectangulo ancho y largo
    pg.display.flip()#activa todo en la pantalla por lo que las cosas que pongamos tienen que escribirse antes de este comando para que se ejecuten.




pg.quit() #para que termine de mostrar
