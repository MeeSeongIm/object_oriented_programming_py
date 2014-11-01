
class Shapes:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[" "]* width for i in list(range(height))]

    def setpixel(self, row, col):
        self.data[row][col] = "*"
        
    def getpixel(self, row, col):
        return self.data[row][col]
    
    def display(self):
        print("\n".join(["".join(row) for row in self.data]))

 
width = 80
height = 20
frame = Shapes(width,height)
for i in list(range(width)):
    frame.setpixel(0,i)
    frame.setpixel(height-1,i)

for i in list(range(height)):
    frame.setpixel(i,0)
    frame.setpixel(i,width-1)

for i in list(range(height)):
    frame.setpixel(-i,i)
    frame.setpixel(-i,2*i)
    frame.setpixel(-i,3*i)
    frame.setpixel(-i,4*i)
 
frame.display()

