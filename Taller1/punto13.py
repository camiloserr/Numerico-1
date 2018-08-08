import math

MIN = -10**(-7)
MAX = 10**(-7)

def f( x , n , k):
    return ((x**k) - n)

def bisec( low , high , n , k):
    x  = float((low+high)/2)
    y = float(f(x , n , k))
    if y > MIN and y < MAX:
        return x
    if y * float(f(low , n , k)) < 0:
        return bisec(low , x ,  n,  k)

    elif float(f(high , n , k)) * y < 0:
        return bisec(x , high , n , k)
    else:
        return "error raro"


print("Para hallar la k-esima raiz de n:")
n = input("n: ")
k = input("k: ")
print bisec(0 , n , n , k)
