#11 -1b- 7 - 13 - 2 - 4 o 5 - 6 - 15
import math
def horner(p, n, x, ans):
    y = p[0]
    d = 0
    for i in range( 1 , n ):
        d = y + x * d
        y = x * y + p[i]

    ans.append(y)
    ans.append(d)

def evalp(p, n, x):
    s = 0
    for i in range(n):
        s = s + p[i] * x**(n - i - 1)
    return s
def evald(p, n, x):
    s = 0
    for i in range(n):
        s = s + p[i] * (n - i - 1) * x**(n - i - 2)
    return s

n = 1 + int (input("Grado del polinomio: "))
print ( "Ingrese lo valores del polinomio: " )
#polinomio = [7, 6, -6, 0, 3, -4]
poli = []
for i in range(n):
    v = float (input())
    poli.append( v )
#n = len(polinomio)
for i in range(n):
    print (poli[i])
x = float (input( "Ingrese el valor de x0: " ))
ans = []
horner(poli, n, x, ans)
print ("P(x0): ", ans[0])
print ("Q(x0): ", ans[1])
print ("Número de operaciones: ", 2*(n-1))

print ( evalp(poli  , n, x))
print ( evald(poli  , n , x))
