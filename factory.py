from abc import abstractmethod
from Interface import implements, Interface

class Shape(Interface):
    @abstractmethod
    def draw() -> object:
        pass
    

class Circle(implements(Shape)):
    def draw() -> Shape:
        print('Circle is created')


class Rectangle(implements(Shape)):
    def draw() -> Shape:
        print('Rectangle is created')


class Triangle(implements(Shape)):
    def draw() -> Shape:
        print('Triangle is created')


class AnotherShape(implements(Shape)):
    def draw() -> Shape:
        print('Another shape is created')
        

class Factory:
    '''makeing objects according to value entered'''
    def __init__(self, shape:str) -> None:
        self.shape = shape

        self.shapes = {            
            'circle':Circle,
            'rectangle':Rectangle,
            'triangle':Triangle,
        }

    def CreateShape(self) -> Shape:
        '''method from type Shape'''

        '''if value not found in dict, call another object'''        
        return self.shapes.get(self.shape, AnotherShape)


if __name__=='__main__':

    shape = Factory('Circle'.casefold())
    created = shape.CreateShape()
    created.draw()
