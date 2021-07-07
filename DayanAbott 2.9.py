import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as int
from scipy.special import factorial

alpha = 66.67 #Gives inverse temporal development constant alpha, in s^-1
t = np.arange(0,10,.1)
tau = np.arange(0,10,.1)

#Compute and plot L_t for omega = 6*pi /s. Do not plot the negative part of L_t, cell cannot fire at negative rate.

omega = 6 * np.pi #Temporal frequency of 6*pi

D_t = alpha * np.exp(- alpha * tau) * ((alpha * tau) ** 5 / factorial(5) - (alpha * tau) ** 7 / factorial(7)) #Temporal Kernel of the cell

L_t = np.zeros(len(t))
for i in range(len(t)):
    L_t[i] = int.simps(D_t * np.cos(omega*(t[i] - tau)), tau)

print(L_t)
plt.plot(t,L_t,'o')
plt.xlabel('t (seconds)')
plt.ylabel(r'$L_t$')
plt.show()

#Compute and plot L_t^2 for omega = 6*pi /s