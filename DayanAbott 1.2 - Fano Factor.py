import numpy as np
import scipy as sp
import matplotlib as mp

n = 10 #Number of trials
T = 10 #Length of trial, in s
dt = .001 #minimum time step, in s
t_j, t_p = np.meshgrid(np.arange(0,T,dt), np.arange(n)) #time steps of dt from 0 to T in meshgrid form, in s
rate,y = np.meshgrid(np.zeros(len(t_j[0,:])+1), np.arange(n)) #Initializing r(t) array
r_0 = 100 #Value r(t) exponentially recovers to, in Hz
rate[:,0] = r_0 #Sets first element of each row in rate to r_0
tau_ref = 10 #Refractory recovery rate, in s
random, x = np.meshgrid(np.zeros(len(t_j[0,:])), np.arange(n)) #Array of random numbers between 0 and 1
spkt = [] #Initializing array for list of spike times
tau, z = np.meshgrid(np.zeros(len(t_j[0,:])+1), np.arange(n)) #Initializing array to track times between spikes

for j in range(n):
    for i in range(len(t_j[0,:])):
        random[j,i] = np.random.rand(1)

for j in range(n):
    spkt.append([])
    for i in range(len(t_j[0,:])):
        # If r(t) = 0, time since spike is incremented and r(t) begins to exponentially rise
        if  rate[j,i] == 0:
            tau[j,i+1] = tau[j,i] + dt
            rate[j,i+1] = r_0 * (1 - np.exp(-tau[j,i+1]) / tau_ref)
        # If spike occurs, r(t) is set to 0 and exponentially approaches r_0
        elif random[j,i] < rate[j,i] * dt:
            tau[j,i] = 0
            rate[j,i+1] = 0
            spkt[j].append(t_j[j,i])
        # If r(t) = r_0 and spike does not occur, time is incremented and r(t) = r_0
        elif rate[j,i] == r_0:
            tau[j,i+1] = tau[j,i] + dt
            rate[j,i+1] = rate[j,i]
        # If r(t) != 0 and != r_0 and spike does not occur, time is incremented and r(t) exponentially approaches r_0
        else:
            tau[j,i+1] = tau[j,i] + dt
            rate[j,i+1] = r_0 * (1 - np.exp(-tau[j,i + 1] / tau_ref))

interspike = []
for j in range(n):
    interspike.append([])
    for i in range(len(spkt[j][:])-1):
        interspike[j].append(spkt[j][i+1] - spkt[j][i])

#Check array values
print(t_j)
print(interspike)



#Compute the Fano Factor

 #Mean of the spike counts across all trials
var = np.zeros(n) #Variance of the interspike intervals for each trial
spikes = np.zeros(n)
for j in range(n):
        spikes[j] = np.mean(len(spkt[j][:]))
        mean = np.mean(spikes)
        var[j] = np.var(spkt[j][:])
        var_spk = np.average(var)

Fano = var_spk/mean
print(Fano)
