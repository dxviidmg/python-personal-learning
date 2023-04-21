class Circulo:

    def __str__(self) -> str:
        return 'soy un circulo'

class Triangulo:
    def __str__(self) -> str:
        return 'soy un triangulo'


class FactoryShapes:
    def create_object(self, type):
        if type == 1:
            return Circulo()
        elif type == 2:
            return Triangulo()
        else:
            ValueError('type unknown')

factory_shapes = FactoryShapes()

t = factory_shapes.create_object(1)
print(t.__str__())

