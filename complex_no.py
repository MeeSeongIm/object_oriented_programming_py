

from numpy import arctan

class ComplexNumbers(object):
    def __init__(self, real, imag):
        self.r = real
        self.i = imag     

    def squared(self):
        self.squared_r = (self.r)**2 -(self.i)**2
        self.squared_i = 2*(self.r)*(self.i)
        print("The square of %s+%si is %s+%si." % (self.r, self.i, self.squared_r, self.squared_i))

def addition(x,y,z,w):
    print("The sum of %s + %si and %s + %si is %s+%si." % (x,y,z,w, x+z, y+w))
    return (x+z, y+w)
        
def multiplication(x,y,z,w):
    print("The product of %s + %si and %s + %si is %s+%si." % (x,y,z,w, x*z-y*w, y*z+x*w) )

complex_no = ComplexNumbers(5,7)
print(complex_no.r)
print(complex_no.i)
complex_no.squared()
print(complex_no.squared_r)
print(complex_no.squared_i)

unit_no = ComplexNumbers(1,1)
print(unit_no.r)
unit_no.squared()

print(addition(complex_no.r, complex_no.i, unit_no.r, unit_no.i))
print(multiplication(complex_no.r, complex_no.i, unit_no.r, unit_no.i))

# convert a complex number to radians.

def radians(x,y):
    if x >0:
        print("%s+ %si in polar coordinates is %se^(%si)." % (x,y,x**2 + y**2, arctan(y/x))) 
    if x <0:
        print("%s+ %si in polar coordinates is %se^(%si)." % (x,y,x**2 + y**2, arctan(y/x)+pi))
    if x == 0 and y >0:
        print("%s+ %si in polar coordinates is %se^(%si)." % (x,y,x**2 + y**2, pi/2)) 
    if x == 0 and y <0:
        print("%s+ %si in polar coordinates is %se^(%si)." % (x,y,x**2 + y**2, 3*pi/2)) 
 
print(radians(unit_no.r, unit_no.i))



