from numpy import*
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
x=[35,45,55,65,75]
f=[35,48,70,40,22]
[d,dt,c] = vand(x)
a = linalg.solve(d,f)
print(a)
