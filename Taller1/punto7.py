import math
def f( vec, punto ):
    return math.sqrt((vec[0] - punto[0])**2 + (vec[1] - punto[1])**2 + (vec[2] - punto[2])**2 )

def df( vec , punto ):
    return 0.5 * (math.sqrt((vec[0] - punto[0])**2 + (vec[1] - punto[1])**2 + (vec[2] - punto[2])**2 )**-1) * (2*(vec[0] - punto[0])
     + 2*(vec[1] - punto[1]) + 2*(vec[2] - punto[2]))
def ddf( vec , punto ):
    return 0.25 * (math.sqrt((vec[0] - punto[0])**2 + (vec[1] - punto[1])**2 + (vec[2] - punto[2])**2 )**-(3/2)) * (2*(vec[0] - punto[0])
     + 2*(vec[1] - punto[1]) + 2*(vec[2] - punto[2]))**2

def newton (v , p , t):
    h = df(v,p)/ddf(v,p)
    x = 2*math.cos(t)
    y = math.sin(t)
    z = 0
    r = 1
    while math.fabs(t) >= 10**-4:
        h = float(df(v,p)/ddf(v,p))
        t = t - h
        print (r)
    return t

t = float(input("Valor inicial de t: "))
x = 2*math.cos(t)
y = math.sin(t)
z = 0
vector = []
vector.append(x)
vector.append(y)
vector.append(z)
punto = [2,1,0]
t = newton( vector , punto , t )
