import math

class Circulo():
    # defino consta de clase
    PI = 3.1416

    def __init__(self,r: float):
        self.radio = r

    def area(self)-> float:
        """Retorna el área del circulo"""
        return self.PI * ( math.pow(self.radio,2))

if __name__ == '__main__':
    circle = Circulo(5)
    print(circle.area())