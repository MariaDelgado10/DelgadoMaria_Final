import numpy as np

import matplotlib.pylab as plt

data=np.genfromtxt("punto15.dat")


plt.figure()
plt.plot(data[:,1], data[:,2])
plt.xlabel("x")
plt.ylabel("y")
plt.title("coordenadas")
plt.savefig("punto15.pdf")
