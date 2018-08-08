import math

def f(x):
    #poli = [2,3,0,-1]

    return x**3 - 4*(x**2) + 3*x -6

def muller(a , b , c):
    #numero maximo de iteraciones
    MAX = 100000
    res = 0
    for i in range(MAX):
        f1 = f(a)
        f2 = f(b)
        f3 = f(c)
        d1 = f1 - f3
        d2 = f2 - f3
        h1 = a - c
        h2  = b-c
        a0 = f3
        a1 = ((d2*h1**2)-(d1*h2**2)) / ((h1*h2) * (h1-h2))
        a2 = (((d1*h2) - (d2*h1))/((h1*h2) * (h1-h2)))
        x = ((-2*a0) / (a1 + math.fabs(math.sqrt(a1*a1-4*a0*a2))))
        y = ((-2*a0) / (a1-math.fabs(math.sqrt(a1*a1-4*a0*a2))))
        if x >= y:
            res = x + c
        else:
            res = y + c
        m = res*100
        n = c*100
        m = math.floor(m)
        n = math.floor(n)
        if m == n:
            return res
            break
        a = b
        b = c
        c = res

    print "error"

a= input("ingrese los valores de la semilla: ")
b = input()
c = input()
print muller(a,b,c)
