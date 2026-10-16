import numpy as np
def m_(i,k,a):
  return a[i,k]/a[k,k] 
a=np.array([[1,2,1],[2,3,1],[5,6,9]],dtype=float)
b=np.array([-1,0,20],dtype=float)
x=np.array([0,0,0],dtype=float)
n=3
test=1

for k in range(0,n-1):
  for l in range(k+1,n):
    if(a[l,k]>a[k,k]):
     a[[k,l]]=a[[l,k]]
     b[[k,l]]=b[[l,k]]
  if (a[k,k]==0) :
    for i in range(k+1,n):
      if(a[i,k]!=0):
        a[[k,i]]=a[[i,k]]
        b[[k,i]]=b[[i,k]]
        break
      if(i==n-1 and a[n-1,k]==0):
        test=0
  if(test==0) : 
    break
  for i in range(k+1,n):
    m=m_(i,k,a)
    for j in range(k,n):
      a[i,j]-=m*a[k,j]
    b[i]-=m*b[k]
if(test!=0):
  x[n-1]=b[n-1]/a[n-1,n-1]
  for i in range(n-2,-1,-1):
    x[i]=(1/a[i,i])*(b[i]-np.dot(a[i, i + 1:n], x[i + 1:n]))
  print(x)
else :
  print("ce systeme n'a pas de solution")
