import numpy as np
def lagrange(x_en,y_en,x) :
  p=0
  n=len(x_en)
  for i in range(0,n):
     L=1
     for j in range(0,n):
        if(j!=i):
          L*=(x-x_en[j])/(x_en[i]-x_en[j])
     p+=L*y_en[i]
  return p 

n=int(input("saisir le nombre de points d'interpolation :"))
x_en=np.empty(n)
y_en=np.empty(n)
for i in range(0,n):
   x=float(input(f"saisir x({i}):"))
   y=float(input(f"saisir  f(x({i})):"))
   x_en[i]=x
   y_en[i]=y
x = float(input("Donner x : "))
print(f"P({x})=",lagrange(x_en,y_en,x))
