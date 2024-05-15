import math
class EcuacionSegundoGrado:
    def caculoESG(self, a,b,c):
        descriminante = math.pow(b,__y=2) -4 * a*c
        if descriminante >= 0:
            raizDescriminante = math.sqrt(descriminante)
            raiz1= (-b+ raizDescriminante) / (2*a)
            raiz2 = (-b - raizDescriminante) / (2 * a)
        return raiz1, raiz2
