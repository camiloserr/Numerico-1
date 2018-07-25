import math

def raiz():
    x = 2.58
    for i in range(5):
        y= 7/x
        y +=x
        y *= 0.5
        x = y

    return y

print( raiz() )
print( math.sqrt(7) )
error = raiz() - math.sqrt(7)
print (error)
