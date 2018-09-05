from sympy import*
from numpy import*
import numpy as np
import math
import matplotlib.pyplot as plot

def vand(x):
    n=len(x)
    d=zeros([n,n])
    for i in range(n):
        for j in range(n):
            d[i][j]=x[i]**(n-j-1)
    dt=1
    for i in range(n):
        for j in range(n):
            if j<i:
                dt=dt*(x[j]-x[i])
    c=linalg.cond(d,inf)
    return [d,dt,c]

def lagrange(x,y,u=None):
    n = len(x)
    t = Symbol('t')
    p = 0
    for i in range(n):
        L=1
        for j in range(n):
            if j!=i:
                L=L*(t-x[j])/(x[i]-x[j])
        p = p+y[i]*L
        p = expand(p)
    if u==None:
        return p
    else:
        r=p.subs(t,u)
        return r

x=[100,300,400,500]
f=[-160,-4.2,9,16.9]
[d,dt,c] = vand(x)
a = linalg.solve(d,f)
for i in range(len(a)):
    
print(a)

p = lagrange(x,f)
print(p)
r = lagrange(x,f,450)
print(r)
#plot.plot(x,y)
#plot.grid(true)
#plot.show()
