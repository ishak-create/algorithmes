import numpy as np
import matplotlib.pyplot as plt
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

# points d'interpolations :
x_en=np.array([-1,0,1]) 
y_en=np.array([1,2,7])
# on teste la fonction interpolante par des points dans [-2,2]
x=np.linspace(-2,2,200) 
y=interp_newton(x_en,y_en,x)
plt.plot(x,y)
plt.plot(x_en,y_en,'o')
plt.title('interpolation de newton')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
