import numpy as np
import matplotlib.pyplot as plt

#fonction :
def f(x):
    return np.sin(x)

def f_prime(x):
    return np.cos(x)

#interpolation lagrange :
def lagrange(x_en,x,k):
  n=len(x_en)
  L=1
  for i in range(0,n):
   if(i!=k):
      L*=(x-x_en[i])/(x_en[k]-x_en[i])
  return L

def interp_lagrange(x_en,y_en,x) :
  p=0
  n=len(x_en)
  for i in range(0,n):
     p+=lagrange(x_en,x,i)*y_en[i]
  return p

#interpolation newton :

#fonction récursive pour calculer les différences dérivées 
def coef_newton(x_en,y_en,min_,max_):
  if(min_==max_) :
    return y_en[min_]
  else :
    return (coef_newton(x_en,y_en,min_+1,max_)-coef_newton(x_en,y_en,min_,max_-1))/(x_en[max_]-x_en[min_])
#fonction qui calcule le polynome de newton
def interp_newton(x_en,y_en,x):
   n=len(x_en)
   p=y_en[0]
   for i in range(1,n):
     m=1
     for j in range(0,i):
       m*=x-x_en[j]
     p+=coef_newton(x_en,y_en,0,i)*m
   return p

#interpolation hermite :
def H_(x_en,x,k):
 return (x-x_en[k])*(lagrange(x_en,x,k)**2)

def derivee(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2*h)

def H(x_en,x,k):
    L = lagrange(x_en, x, k)
    L_prime = derivee(
        lambda t: lagrange(x_en, t, k),
        x_en[k]
    )   
    return (1 - 2*(x - x_en[k])*L_prime) * L**2

def interp_hermite(x_en,y_en,y_prime,x):
  p=0
  n=len(x_en)
  for k in range(0,n):
    p+=y_en[k]*H(x_en,x,k)+y_prime[k]*H_(x_en,x,k)
  return p

# points d'interpolations :
x_en=np.array([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
y_en = f(x_en)
y_prime=f_prime(x_en)
# on teste la fonction interpolante par des points dans [-2,2]
x = np.linspace(-np.pi, np.pi, 100)
# Fonction originale
y_original = f(x)
#polynomes d'interpolations
y1=interp_lagrange(x_en,y_en,x)
y2=interp_newton(x_en,y_en,x)
y3=interp_hermite(x_en,y_en,y_prime,x)
#tracage
plt.figure(figsize=(10,6))
plt.plot(x, y_original, 'b-', label='Fonction originale')
plt.plot(x, y2, 'y', label='Interpolation newton')
plt.plot(x, y1, 'k--', label='Interpolation lagrange')
plt.plot(x, y3, 'r--', label='Interpolation Hermite')
plt.plot(x_en, y_en, 'o', label='Points d interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.title("fonction originale / Hermite / Newton")
plt.grid()
plt.legend()
plt.show()
