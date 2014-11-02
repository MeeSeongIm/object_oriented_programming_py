
# vectors 

class Vector:
    def __init__(self,x,y,z,w):
        self.x=x
        self.y=y
        self.z=z
        self.w=w
    def __str__(self):
        return "Vector(%d, %d, %d, %d)" % (self.x, self.y, self.z, self.w)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
    def __mult__(self, other):                                                                  # component-wise multiplication
        return Vector(self.x*other.x, self.y*other.y, self.z*other.z, self.w*other.w)
    def length(self):
        return ("%.2f" % (self.x**2 + self.y**2 + self.z**2 + self.w**2)**(0.5))
    def normalization(self):
        return("(%.2f, %.2f, %.2f, %.2f)" % (self.x/(self.x**2 + self.y**2 + self.z**2 + self.w**2)**(0.5),self.y/(self.x**2 + self.y**2 + self.z**2 + self.w**2)**(0.5),self.z/(self.x**2 + self.y**2 + self.z**2 + self.w**2)**(0.5),self.w/(self.x**2 + self.y**2 + self.z**2 + self.w**2)**(0.5)))
    def __dotProduct__(self, other):
        return self.x*other.x+self.y*other.y+self.z*other.z+self.w*other.w

# cross-product for a quadruple: use Gram-Schmidt algorithm. 

v1 = Vector(40,30,20,10)
v2 = Vector(10,20,30,40)
print(v1.__add__(v2))
print(v1.__mult__(v2))
print(v1.length())
print(v1.normalization())
print(v1.__dotProduct__(v2))





