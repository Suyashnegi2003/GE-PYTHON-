import math
def func():
    print('table of sin in the range of 0-10 with increament of 0.2')
    for x in range(0,10):
        print(math.sin(x))
        x=x+0.2
    print()
    print('table of cos')
   
    for x in range(0,10):
        print(math.cos(x))
        x=x+0.2
    print()
    print('table of tan')
    
    for x in range(0,10):
        print(math.tan(x))
        x=x+0.2
    print()
func()
