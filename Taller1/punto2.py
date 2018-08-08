#punto 2

#calcula el volunmen, pasandole la longitud x del cuadrado,  el lado l de la lamina y el ancho a de la lamina
#le resto 1000 a la vol para que las respuestas queden sobre el eje x, asi puedo hacer la biseccion mas facil
def vol(x , l ,a):
    return x*((l-2*x)*(a-2*x)) -1000


def bisec( low , high ):
    x  = (low+high)/2
    y = vol(x , 24 , 32)
    if y > -10**(-8) and y <= 0:
        return x
    if vol(x , 24 , 32) * vol(low , 24 , 32) < 0:
        return bisec(low , x)

    elif vol(high , 24 , 32) * vol(x , 24 , 32) < 0:
        return bisec(x , high)
    else:
        return "error raro"

def tri(low , high):
    tamano = (high - low) / 3
    x1 = low + tamano
    x2 = low + 2*tamano

    #evalua la vol en la mitad
    y = vol ( (low + high )/2 , 24 , 32)
    if y > -10**(-8) and y <= 0:
        return ((low + high)/2)


    #si la vol cambia de signo en la primera particion, mando la recursion por ahi
    if( vol (low , 24 , 32) * vol (x1 , 24 , 32) < 0):
        return tri (low , x1)

    if (vol(x1 , 24 , 32) * vol(x2 , 24 , 32) < 0):
        return tri(x1, x2)

    if (vol(x2 , 24 , 32) * vol(high , 24 , 32) < 0):
        return tri(x2 , high)

    else:
        return "error inesperado"


min = float(input("ingrese el valor minimo: "))
max = float(input("ingrese el valor maximo: "))
print "con biseccion: "
print "x = ", bisec(min , max)
print "con triseccion: "
res = tri(min , max)
print "x = ", res

if vol(res , 24 , 32 ) <=0 and vol(res , 24 , 32 ) > -10**(-8):
    print "converge"
else:
    print "no converge ):" 
