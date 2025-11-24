from math import sin, cos

class Point:

    def __init__(self):
        self.x = None
        self.y = None

    def __str__(self):
        return f"x={self.x}\ny={self.y}"


    @staticmethod
    def cartesion_point(x, y):
        p = Point()
        p.x = x
        p.y = y
        return p

    @staticmethod
    def polar_point(rho, theta):
        p = Point()
        p.x = rho*cos(theta)
        p.y = rho*sin(theta)
        return p
    

    def add_cordinates(self):
        return self.x + self.y
 
if __name__ == "__main__":
    p1 = Point.cartesion_point(x=2, y=4)
    print(p1)
    co = p1.add_cordinates()
    print(co)
    p2 = Point.polar_point(5, 6)
    print(p2)