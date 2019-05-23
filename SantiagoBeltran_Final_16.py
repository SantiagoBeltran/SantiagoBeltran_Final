import numpy as np

x = np.array([4.0,10.0,12.0,80.0,50.0,40.0])
y = np.array([ 100.0,5.0,80.0,50.0,50.0,200.0])
t= np.array([73.0, 28.0, 59.0, 52.0, 39.0, 137.0])
sigma_t = np.ones(len(t))

def model(x,a, b,c):
    return (x-a)/b+c

def loglikelihood(x, t, sigma_t,a, b, c):
    d = t -  model(x,a, b, c)
    d = d/sigma_t
    d = -0.5 * np.sum(d**2)
    return d

N = 50000
lista_a = [np.random.random()]
lista_b = [np.random.random()]
lista_c = [np.random.random()]
lista_a1 = [np.random.random()]
lista_b1 = [np.random.random()]
lista_c1 = [np.random.random()]


for i in range(1,N):
    print(i)
    propuesta_a  = lista_a[i-1] + np.random.random()
    propuesta_c  = lista_c[i-1] + np.random.random()
    propuesta_b  = lista_b[i-1] + np.random.random()
    propuesta_a1  = lista_b[i-1] + np.random.random()
    propuesta_c1  = lista_c1[i-1] + np.random.random()
    propuesta_b1  = lista_b1[i-1] + np.random.random()

    logposterior_viejo = loglikelihood(x, t, sigma_t,  lista_a[i-1],lista_b[i-1], lista_c[i-1]) 
    logposterior_nuevo = loglikelihood(x, t, sigma_t,  propuesta_a,propuesta_b, propuesta_c) 
    logposterior_viejo1 = loglikelihood(y, t, sigma_t,  lista_a1[i-1],lista_b1[i-1], lista_c1[i-1]) 
    logposterior_nuevo1 = loglikelihood(y, t, sigma_t,  propuesta_a1,propuesta_b1, propuesta_c1) 

    r = min(1,np.exp(logposterior_nuevo-logposterior_viejo))
    r1 = min(1,np.exp(logposterior_nuevo1-logposterior_viejo1))
    
    alpha = np.random.random()
    if(alpha<r):
        lista_a.append(propuesta_a)
        lista_b.append(propuesta_b)
        lista_c.append(propuesta_c)
    else:
        lista_a.append(lista_a[i-1])
        lista_b.append(lista_b[i-1])
        lista_c.append(lista_c[i-1])
        
    if(alpha<r1):
        lista_a1.append(propuesta_a1)
        lista_b1.append(propuesta_b1)
        lista_c1.append(propuesta_c1)
    else:
        lista_a1.append(lista_a1[i-1])
        lista_b1.append(lista_b1[i-1])
        lista_c1.append(lista_c1[i-1])    

lista_a = np.array(lista_a)        
lista_b = np.array(lista_b)
lista_c = np.array(lista_c)

lista_a1 = np.array(lista_a1)
lista_b1 = np.array(lista_b1)
lista_c1 = np.array(lista_c1)

a=np.mean(lista_a)
b=np.mean(lista_b)
c=np.mean(lista_c)
a1=np.mean(lista_a1)
b1=np.mean(lista_b1)
c1=np.mean(lista_c1)

vs=np.sqrt(b**2+b1**2)
da=np.std(lista_a)
db=np.std(lista_b)
dc=np.std(lista_c)
da1=np.std(lista_a1)
db1=np.std(lista_b1)
dc1=np.std(lista_c1)
dvs=np.sqrt((db/b)**2+(db1/b)**2)
print("Coordenada x: {} +/- {} \n".format(a,da))
print("Coordenada y: {} +/- {} \n".format(a1,da1))
print("Tiempo lanzamiento: {} +/- {} \n".format(c1,dc1))
print("Velocidad del sonido: {} +/- {} \n".format(vs,dvs))