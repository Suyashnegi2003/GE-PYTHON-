
class rectangle():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    def perimeter(self):
        print('destructor call!!')
x=int(input('enter length:'))
y=int(input('enter breadth:'))
a=rectangle(x,y)
print('area of rectangle is:',a.area())
print('perimeter of rectangle is:',a.perimeter())
