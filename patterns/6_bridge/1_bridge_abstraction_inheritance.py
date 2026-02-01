from abc import ABC, abstractmethod

# Abstraction
class Shape(ABC):
    def __init__(self, radius):
        self.radius = radius

    @abstractmethod
    def render_circle(self):pass
    
    # @abstractmethod
    # def render_square(self):pass

class Cartesian(Shape):
    def __init__(self, radius):
        super().__init__(radius)

    def render_circle(self):
        print(f"Drawing circle at radius {self.radius} in pixel format")

class Raster(Shape):
    def __init__(self, radius):
        super().__init__(radius)

    def render_circle(self):
        print(f"Drawing circle at radius {self.radius} in line format")

# Bridge
class Draw:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):pass
    def resize(self):pass


# Inheritance
class Circle(Draw):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer(self.radius).render_circle()

    def resize(self, factor):
        self.radius *= factor



# circle = Circle(Raster, 10)
circle = Circle(Cartesian, 10)
circle.draw()
circle.resize(2)
circle.draw()
circle.resize(0.5)
circle.draw()

