import numpy as np
import matplotlib.pyplot as plt
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

x=np.linspace(-2,2,200)
x_en=np.array([-1,0,1])
y_en=np.array([1,2,7])
y=lagrange(x_en,y_en,x)
plt.plot(x,y)
plt.plot(x_en,y_en,'o')
plt.title('interpolation de Lagrange')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
