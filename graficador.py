import numpy as np
import matplotlib.pyplot as plt
data =np.loadtxt("datos.dat")
t=data[:,0]
x=data[:,1]
y=data[:,2]

plt.figure(figsize=(5,10))
plt.subplot(2,1,1)
plt.plot(t,x)
plt.xlabel("Tiempo")
plt.ylabel("Posición x")
plt.subplot(2,1,2)
plt.plot(t,y)
plt.xlabel("Tiempo")
plt.ylabel("Posición y")
plt.savefig("BeltranSantiago_final_15.pdf")

