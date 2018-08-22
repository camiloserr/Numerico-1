from pylab import*
import math

#Parcial 1, Análisis numérico. Realizado por: Daniel Mendoza.
#Ejercicio 1b
def Suma(a,n):
    result = 0
    for i in range(n):
        for j in range(n):
            result += a[i][j]

    return result;


a = []
n = int(input("Ingrese el tamaño de la matriz cuadrada A: ") )
valores_complejidad = []
while(n != 0):
    a.clear()
    valores_complejidad.append(n*n)
    print("Ingrese la matriz A")
    for i in range(n):
        aux = []
        for j in range(n):
            mensaje = "A(" + str(i) + " , " + str(j) + ") = "
            k = int(input(mensaje) )
            aux.append(k)

        a.append(aux)
    suma = Suma(a,n)
    print("La suma de la matriz A [", n, "] es: ", suma)
    n = int(input("Ingrese el tamaño de la matriz cuadrada A (0 para terminar): ") )

print("La complejidad del algorítmo es O(n*n)")
for i in range(len(valores_complejidad)):
    print("Para la matriz ", i+1 ,", la complejidad es de O(", valores_complejidad[i],")")


#Ejercicio 2c

x = []
x.append(-1.3)
x.append(0)
for i in range(1,10):
    r = x[i] - (math.log(x[i]+2))*((x[i]*x[i-1])/(math.sin(x[i])-math.sin(x[i-1])))

#Ejercicio 3g
def seidel(a,b,x,w):

    r = int(input("numero de iteraciones: "))
    for it in range(r):
        nn = len(x)
        for i in range(nn):
            s=0
            for j in range(nn):
                if i!=j:
                    s = s+a[i][j]*x[j]
            x[i] = w*(b[i]-s)/a[i][i]

    return x


# 3x-y-z=-1
# -x+3y+1=3
# 2x+y+4z=7

#a = [[3, -1, -1], [-1, 3, 1], [2, 1, 4]]
#b = [1, 3, 7]

#valores iniciales
#x = [0, 0, 0]

a = []
b = []

#valores iniciales
x = []

n = int(input("ingrese el numero de filas de la matriz A: ") )
m = int(input("ingrese el numero de columnas de la matriz A: ") )

mensaje = ""

print("Ingrese la matriz A")
for i in range(n):
    aux = []
    for j in range(m):
        mensaje = "A(" + str(i) + " , " + str(j) + ") = "
        k = int(input(mensaje) )
        aux.append(k)

    a.append(aux)


for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j] ," ", end=" ")
    print(" ")



print ("Ingrese el vector solucion de la matriz")
b.clear()
for i in range(n):
    mensaje = "B(" + str(i) + ") = "
    k = int(input(mensaje) )
    b.append(k)


print ("Ingrese los valores iniciales de Xn")

for i in range(n):
    mensaje = "X(" + str(i) + ") = "
    k = int(input(mensaje) )
    x.append(k)
w = float(input("Ingrese el valor de relajación w: "))
flag = True
if(m > n):
    print("Infinitas soluciones.")
elif(n == m):
    y = seidel(a,b,x,w)
else:
    y = seidel(temp,b,x,w)
    for i in range(len(x)+1,n):
        result = 0
        for j in range(m):
            result += a[i][j]*y[j]

        if(result != b[i]):
            flag = False
if(flag):
    for i in  range (len(y)):
        print("x",i," = " ,y[i])
else:
    print("No tiene solucion.")
