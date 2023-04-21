from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Circulo(Forma):
    def area(self):
        print('area circulo')

    def perimetro(self):
        print('perimetro circulo')


class Cuadrado(Forma):
    def area(self):
        print('area Cuadrado')

    def perimetro(self):
        print('perimetro Cuadrado')



#c = Circulo()
#print(c.area())
#print(c.perimetro())

for e in [Circulo(), Cuadrado()]:
    print(e.area(), e.perimetro())