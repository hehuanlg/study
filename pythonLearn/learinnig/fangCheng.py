import math
def quadratic(a,b,c):
    n = b**2 - 4*a*c
    if n < 0:
        return 'none'
    if n > 0:
        x1 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        return x1,x2
    else:
        x = -b/2*a
        return x
print('a*x^2+b*x+c=0')
a = input('输入a')
b = input('输入b')
c = input('输入c')
a = int(a)
b = int(b)
c = int(c)
print('结果：',quadratic(a,b,c))

