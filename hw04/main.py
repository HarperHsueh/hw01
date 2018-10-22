class Rectangle(object):
    def __init__(self,x,y):
        self.width=x
        self.height=y

    def area(self):
        return self.width*self.height

class Square(Rectangle):
    def __init__(self,z):
        self.width=z
        self.height=z

class Ellipse(object):
    def __init__(self,a,b):
        self.width=a
        self.height=b
        
    def area(self):
        return self.width*self.height*3.14

class Circle(Ellipse):
    def __init__(self,r):
        self.width=r
        self.height=r

def compute_area(shapes):
    return sum([m.area() for m in shapes])

shapes = [Ellipse(10, 20), Square(15), Circle(5),
          Rectangle(20, 15), Circle(5), Square(15),
          Ellipse(10, 20)]



total_area=compute_area(shapes)
print('total_area= ', total_area)
