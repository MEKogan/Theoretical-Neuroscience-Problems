import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as int

k_inv = .5 # The inverse of the preferred spatial, in degrees
dx = .1 #Increment for x values
dy = .1 #Increment for y values
x = np.arange(-5, 5, dx) #Array of x coordinates, in degrees
y = np.arange(-5, 5, dy) #Array of y coordinates, in degrees


#Plot L_s as a function of K taking Phi = 0 and A = 50

K = np.arange(0,5,.1) #Array of stimulus spatial frequency values, in degrees
phi = 0 #Stimulus spatial orientation
A = 50 #Stimulus magnitude

#Spatial receptive field kernel with sig_x = sig_y = 1, phi = 0, and k_inv = .5 degrees
D_s, z = np.meshgrid(np.zeros(len(x)), np.zeros(len(y))) #Initializing spatial receptive field kernel as 2D array

for i in range(len(x)):
    for j in range(len(y)):
        D_s[i,j] =  1/(2 * np.pi) * np.exp( - x[i]**2 / 2 - y[j]**2 / 2) * np.cos(1/k_inv * x[i] - phi)

#L_s = integral dx dy D_s(x,y) * A * cos(K*x - phi)

L_int_x, m = np.meshgrid(np.zeros(len(y)), np.zeros(len(K))) #Creates array for integral values with respect to x
for i in range(len(K)):
    for j in range(len(y)):
        L_int_x[i,j] = int.simps(np.cos(K[i] * x)* D_s[:,j], x)

L_s = np.zeros(len(K))
for i in range(len(K)):
    L_s[i] = int.simps(L_int_x[i,:], y)

plt.plot(K, L_s,'o')
plt.xlabel('K (degrees)')
plt.ylabel(r'$L_s$')
plt.show()

#Plot L_s as a function of Phi taking 1/K = .5 and A = 50

Phi = np.arange(0, 2*np.pi, .1)
