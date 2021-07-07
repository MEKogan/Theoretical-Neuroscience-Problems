import numpy as np
import scipy as sp
import matplotlib as mp

rate = 100 #constant rate, in Hz
T = 10 #Length of trial, in s
dt = .001 #minimum time step, in s

# Homogenous Poisson Process

t = np.arange(0, T, dt) #time steps of dt from 0 to T, in s

spkt = t[np.random.rand(len(t)) < rate * dt]  #List of spikes times

interspike = [0] * (len(spkt))
for i in range(len(spkt)-1):
    interspike[i] = spkt[i+1] - spkt[i] #Interspike interval, in s

# Calculating Coefficient of Variation and Fano factor

sigma_n_sq = rate * T #Variance of spike count
n_average = len(spkt) #Average number of spikes

variance_tau = np.var(interspike) #Variance of interspike interval
sigma_tau = np.sqrt(variance_tau) #Standard deviation of interspike interval
tau_average = np.average(interspike) #Average of interspike interval
C_v = sigma_tau / tau_average #Coefficient of variation of interspike interval

print(sigma_tau)
print(tau_average)
print(C_v)
