import random

class Bolilla():
    #defino el constructor del objeto Bolilla y sus atributos
    def __init__(self, posX, posY, color, alto, ancho, vx, vy, esCirculo):
        #self.atributo = parametro
        self.posicionX = posX
        self.posicionY = posY
        self.color = color
        self.alto = alto
        self.ancho = ancho
        self.velocidadX = vx
        self.velocidadY = vy
        self.esCirculo = esCirculo

    #defino un metodo para mover la bola y que rebote cuando llegue a los limites del eje x e y.
    #def metodo(parametro1, param2, ...):
    def mueveBola(self, maxPosicionX, minPosicionX, maxPosicionY, minPosicionY):
        self.posicionX += self.velocidadX
        self.posicionY += self.velocidadY

        #creamos esta condicion para que si la figura geometrica es un circulo, este se tope con el minimo de la pantalla (centro del circulo+anchocirculo).
        #si es un rectangulo el centro de este es la esquina superior izquierda y no es necesario.
        if self.esCirculo:
            minPosicionX += self.ancho
            minPosicionY += self.ancho

        #restamos el ancho de la figura geometrica a la posicion maxima que pueda tener para que no se salga de la pantalla. Y no lo hacemos del minimo ya que el punto 0 de la figura es la esquina superior izquierda.
        if self.posicionX >= (maxPosicionX - self.ancho) or self.posicionX <= minPosicionX: #minPosicion <= que 0 ya que si ponemos velocidades tales como 0.3 (0.2-0.3 sale negativo y no = 0 por lo que sigue trayectoria recta y no rebota)
            self.velocidadX *= -1

        if self.posicionY >= (maxPosicionY - self.alto) or self.posicionY <= minPosicionY:
            self.velocidadY *= -1
    
    #creo funcion bolaAleatoria y no le pongo el parametro self ya que la funcion no depende de una instancia/objeto de la clase Bolilla:
    def bolaAleatoria(maxPosBolaX, maxPosBolaY, i):
        #(15+i como minimo de posX y posY para que el centro del circulo no empiece en el 0 de la pantalla.
        return Bolilla(random.randrange(15+i, maxPosBolaX), random.randrange(15+i, maxPosBolaY),
            (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)),
            15+i, 15+i, 
            0.3, 0.3, 
            random.choice([True, False]))
            #random.choice para elegir entre dos elementos de una secuencia.
            #random.random() > 0.5 esta opcion permite darle mayor probabilidad a una opcion.


