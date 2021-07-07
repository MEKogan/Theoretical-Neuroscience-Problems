import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

n = 10 #Number of trials
T = 10 #Length of trial, in s
dt = .001 #minimum time step, in s
t_j, t_p = np.meshgrid(np.arange(0,T,dt), np.arange(n)) #time steps of dt from 0 to T in meshgrid form, in s
rate,y = np.meshgrid(np.zeros(len(t_j[0,:])+1), np.arange(n)) #Initializing r(t) array
r_0 = 100 #Value r(t) exponentially recovers to, in Hz
rate[:,0] = r_0 #Sets first element of each row in rate to r_0
tau_ref = 10 #Refractory recovery rate, in s
random, x = np.meshgrid(np.zeros(len(t_j[0,:])), np.arange(n)) #Array of random numbers between 0 and 1
spkt_const = [] #Initializing array for list of spike times for Poisson Generator with constant rate
spkt_ref = [] #Initializing array for list of spike times for Poisson Generator with refractory period
spkt_var = [] #Initializing array for list of spike times for Poisson Generator with variable firing rate
tau, z = np.meshgrid(np.zeros(len(t_j[0,:])+1), np.arange(n)) #Initializing array to track times between spikes

#Initializing 2D array of random numbers
for j in range(n):
    for i in range(len(t_j[0,:])):
        random[j,i] = np.random.rand(1)

#Poisson Spike Generator with constant rate of 100 Hz

for j in range(n):
    spkt_const.append([])
    for i in range(len(t_j[0,:])):
        if random[j,i] < r_0 * dt:
            spkt_const[j].append(t_j[j,i])

plt.acorr(spkt_const[0][:], maxlags = 100)
plt.show()

#Poisson Spike Generator with refractory period

for j in range(n):
    spkt_ref.append([])
    for i in range(len(t_j[0,:])):
        # If r(t) = 0, time since spike is incremented and r(t) begins to exponentially rise
        if  rate[j,i] == 0:
            tau[j,i+1] = tau[j,i] + dt
            rate[j,i+1] = r_0 * (1 - np.exp(-tau[j,i+1]) / tau_ref)
        # If spike occurs, r(t) is set to 0 and exponentially approaches r_0
        elif random[j,i] < rate[j,i] * dt:
            tau[j,i] = 0
            rate[j,i+1] = 0
            spkt_ref[j].append(t_j[j,i])
        # If r(t) = r_0 and spike does not occur, time is incremented and r(t) = r_0
        elif rate[j,i] == r_0:
            tau[j,i+1] = tau[j,i] + dt
            rate[j,i+1] = rate[j,i]
        # If r(t) != 0 and != r_0 and spike does not occur, time is incremented and r(t) exponentially approaches r_0
        else:
            tau[j,i+1] = tau[j,i] + dt
            rate[j,i+1] = r_0 * (1 - np.exp(-tau[j,i + 1] / tau_ref))

plt.acorr(spkt_ref[0][:], maxlags = 10)
plt.show()

#Poisson Spike Generator with variable firing rate

#Calculating variable rate(t) = 100 * (1 + cos(2 * pi * t / 300)
rate_var, k = np.meshgrid(np.zeros(len(t_j[0,:])), np.arange(n))
for j in range(n):
    for i in range(len(t_j[0,:])):
        rate_var[j,i] =  100 * (1 + np.cos(2 * np.pi * t_j[j,i])/300)

#Calculating spike times for variable rate
for j in range(n):
    spkt_var.append([])
    for i in range(len(t_j[0,:])):
        if random[j,i] < rate_var[j,i] * dt:
            spkt_var[j].append(t_j[j,i])

plt.acorr(spkt_var[0][:], maxlags = 10)
plt.show()