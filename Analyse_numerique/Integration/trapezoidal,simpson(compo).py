import numpy as np
def f(x):
  return np.exp(-(x**2))
def trap_comp(n,a,b):
  h=(b-a)/n
  I=0
  for i in range(0,n+1):
    x=a+i*h
    if(x==a or x==b):
      I+=f(x)
    else :
      I+=2*f(x)
  return I*(h/2)
def simp_comp(n,a,b):
  h=(b-a)/n
  I=0
  for i in range(0,n+1):
    x=a+i*h
    if(x==a or x==b):
      I+=f(x)
    else :
      if (i%2==0):
        I+=2*f(x)
      else :
        I+=4*f(x)
  return I*(h/3)
print("--Composite Trapezoidal Method--")
print(f"    n=4 :{trap_comp(4,0,1)}")
print(f"    n=6 :{trap_comp(6,0,1)}")
print("--Composite Simpson Method--")
print(f"    n=4 :{simp_comp(4,0,1)}")
print(f"    n=6 :{simp_comp(6,0,1)}")
