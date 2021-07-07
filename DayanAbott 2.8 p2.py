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


#Compute and plot L_1**2 + L_2**2 as a function of Phi
K_inv = .5
A = 5
Phi = np.arange(0, 2*np.pi, .1)


#Spatial Field Kernels D_1 and D_2 for a complex cell
Ds_1, z1 = np.meshgrid(np.zeros(len(x)), np.zeros(len(y)))
Ds_2, z2 = np.meshgrid(np.zeros(len(x)), np.zeros(len(y)))
for i in range(len(x)):
    for j in range(len(y)):
        Ds_1[i,j] = 1/(2*np.pi * sig_x * sig_y) * np.exp(-x[i]**2 /(2*sig_x**2) - y[j]**2/(2*sig_y**2)) * np.cos(1/k_inv * x[i] - phi_1)
        Ds_2[i, j] = 1 / (2 * np.pi * sig_x * sig_y) * np.exp(
            -x[i] ** 2 / (2 * sig_x ** 2) - y[j] ** 2 / (2 * sig_y ** 2)) * np.cos(1 / k_inv * x[i] - phi_2)



#Integral of L_1 and L_2 in the x-direction
L_1x, z3 = np.meshgrid(np.zeros(len(y)), np.zeros(len(Phi)))
L_2x, z4 = np.meshgrid(np.zeros(len(y)), np.zeros(len(Phi)))
for i in range(len(Phi)):
    for j in range(len(y)):
        L_1x[i,j] = int.simps(Ds_1[:,j] * A * np.cos(1/K_inv * x * np.cos(Theta) + 1/K_inv * y[j] * np.sin(Theta) - Phi[i]) , x)
        L_2x[i, j] = int.simps(Ds_2[:, j] * A * np.cos(1/K_inv * x * np.cos(Theta) + 1/K_inv * y[j] * np.sin(Theta) - Phi[i]), x)

L_1 = np.zeros(len(Phi))
L_2 = np.zeros(len(Phi))
L_s = np.zeros(len(Phi))
for i in range(len(Phi)):
    L_1[i] = int.simps(L_1x[i,:], y)
    L_2[i] = int.simps(L_2x[i, :], y)
    L_s[i] = L_1[i]**2 + L_2[i]**2

#Plot of L_s versus Phi. Maximum is at Phi = n*pi, where n = 0, 1, 2, 3 ... , corresponding to the spatial phase selectivity of the complex cell.
plt.plot(Phi, L_s,'o')
plt.xlabel('Phi (degrees)')
plt.ylabel(r'$L_s$')
plt.show()
