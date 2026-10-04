import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def f_prime(x):
    return np.cos(x)

def lagrange(x_en,x,k):
  n=len(x_en)
  L=1
  for i in range(0,n):
   if(i!=k):
      L*=(x-x_en[i])/(x_en[k]-x_en[i])
  return L

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

def inter_hermite(x_en,y_en,y_prime,x):
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
x = np.linspace(-np.pi, np.pi, 500)
# Fonction originale
y_original = f(x)
y=inter_hermite(x_en,y_en,y_prime,x)
plt.figure(figsize=(10,10))
plt.plot(x, y_original, 'b-', label='Fonction originale')
plt.plot(x, y, 'r--', label='Interpolation Hermite')
plt.plot(x_en, y_en, 'o', label='Points d interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Comparaison : fonction originale / Hermite")
plt.grid()
plt.legend()

plt.show()
