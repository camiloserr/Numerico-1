#Taller de busqueda de raices por funciones: Bisección, Trisección y Cuatrisección; con opción de hacer una función general
#Realizado por: Daniel Andrés Mendoza Pérez

import math


#Función bisección para encontrar la raíz de un función en un intervalo entre low y high
def bisec( low, high ):
    x = ( low + high ) / 2
    #y = (math.e ** -x) + x - 2
    y=f(x)
    #print ( x )
    if( y < 10**-8 and y > -10**-8):
        return x
    if( ( f( low ) * f( x ) ) < 0 ):
        return bisec( low , x )
    else:
        return bisec( x , high )

#Función trisección para encontrar la raíz de una función en un intervalo entre low y high
def trisec(low , high):
    spc = ( high - low ) / 3 #tamaño de la partición
    x1 = low + spc
    x2 = low + ( 2 * spc )
    #x1 y x2 son los puntos que limitan las particiones del intervalo
    x = ( low + high ) / 2
    y = f(x)
    if( y < 10**-8 and y > -10**-8):
        return x
    if( ( f( low ) * f ( x1 ) ) < 0 ):
        return trisec( low , x1 )
    elif( ( f( x1 ) * f ( x2 ) ) < 0 ):
        return trisec( x1 , x2 )
    else:
        return trisec( x2 , high)

#Función cuatrisección para encontrar la raíz de una función en un intervalo entre low y high
def cuatrisec(low, high):
    spc = ( high - low ) / 4 #tamaño de la partición
    x1 = low + spc
    x2 = low + ( 2 * spc )
    x3 = low + ( 3 * spc )
    #x1, x2  y x3 son los puntos que limitan las particiones del intervalo
    x = ( low + high ) / 2
    y = f(x)
    if( y < 10**-8 and y > -10**-8):
        return x
    if( ( f( low ) * f ( x1 ) ) < 0 ):
        return cuatrisec( low , x1 )
    elif( ( f( x1 ) * f ( x2 ) ) < 0 ):
        return cuatrisec( x1 , x2 )
    elif( ( f( x2 ) * f ( x3 ) ) < 0 ):
        return cuatrisec( x2 , x3)
    else:
        return cuatrisec( x3 , high )

#Función para encontrar la raíz de una función en un intervalo entre low y high, dado un número n de particiones
def generalsec(low, high, n):
    x = ( high + low ) / 2
    y = f(x)
    #Caso base y condicional para fin de la recursión
    if( y < 10**-8 and y > -10**-8):
        return x

    spc = ( high - low ) / n #tamaño de la partición
    for i in range(n):
        x1 = low + ( i * spc)
        x2 = low + ( ( i + 1 ) * spc )
        if( ( f( x1 ) * f ( x2 ) ) < 0 ):
            return generalsec( x1 , x2 , n )



def f(x):
    return (math.e ** -x) + x - 2



print ("Bisección: ", bisec(0, 100) )
print ("Trisección: ", trisec(0, 100) )
print ("Cuatrisección: ", cuatrisec(0, 100) )
print ("Generalsección: ", generalsec(0, 100, 4) )
