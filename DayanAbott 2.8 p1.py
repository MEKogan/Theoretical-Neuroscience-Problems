import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as int

sig_x = 1 #Variance in x, in degrees
sig_y = 1 #Variance in y, in degrees
k_inv = .5 #Inverse of the preferred spatial frequency of the cell, in degrees
phi_1 = 0 #Preferred spatial phase of L_1, in radians
phi_2 = - np.pi/2 #Preferred spatial phase of L_2, in radians
Theta = 0 #Stimulus orientation, in radians
x = np.arange(-5,5,.1) #Array of x values from -1 to 1, in degrees
y = np.arange(-5,5,.1) #Array of y values from -1 to 1, in degrees


#Compute and plot L_1**2 + L_2**2 as a function of K

Phi = 0 #Stimulus spatial phase, in radians
A = 5 #Kernel magnitude
K = np.arange(0,5,.1) #Array of stimulus spatial frequencies to be plotted against from 0 to 5, in inverse degrees

#Spatial Field Kernels D_1 and D_2 for a complex cell
Ds_1, z1 = np.meshgrid(np.zeros(len(x)), np.zeros(len(y)))
Ds_2, z2 = np.meshgrid(np.zeros(len(x)), np.zeros(len(y)))
for i in range(len(x)):
    for j in range(len(y)):
        Ds_1[i,j] = 1/(2*np.pi * sig_x * sig_y) * np.exp(-x[i]**2 /(2*sig_x**2) - y[j]**2/(2*sig_y**2)) * np.cos(1/k_inv * x[i] - phi_1)
        Ds_2[i, j] = 1 / (2 * np.pi * sig_x * sig_y) * np.exp(
            -x[i] ** 2 / (2 * sig_x ** 2) - y[j] ** 2 / (2 * sig_y ** 2)) * np.cos(1 / k_inv * x[i] - phi_2)


#Integral of L_1 and L_2 in the x-direction
L_1x, z3 = np.meshgrid(np.zeros(len(y)), np.zeros(len(K)))
L_2x, z4 = np.meshgrid(np.zeros(len(y)), np.zeros(len(K)))
for i in range(len(K)):
    for j in range(len(y)):
        L_1x[i,j] = int.simps(Ds_1[:,j] * A * np.cos(K[i] * x * np.cos(Theta) + K[i] * y[j] * np.sin(Theta) - Phi) , x)
        L_2x[i, j] = int.simps(Ds_2[:, j] * A * np.cos(K[i] * x * np.cos(Theta) + K[i] * y[j] * np.sin(Theta) - Phi), x)

#Integrals of L_1 and L_2 in the y-direction
L_1 = np.array(np.zeros(len(K)))
L_2 = np.array(np.zeros(len(K)))
L_s = np.array(np.zeros(len(K)))
for i in range(len(K)):
    L_1[i] = int.simps(L_1x[i,:], y)
    L_2[i] = int.simps(L_2x[i, :], y)
    L_s[i] = L_1[i]**2 + L_2[i]**2

#Plot of L_s versus K. Maximum is at K = 2, corresponding to the spatial frequency selectivity of the cell.
plt.plot(K, L_s,'o')
plt.xlabel('K (degrees)')
plt.ylabel(r'$L_s$')
plt.show()

print(K[np.max(L_s[:])])






