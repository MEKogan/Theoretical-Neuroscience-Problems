import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

n = 20 #Number of elements in tau_ref
T = 10 #Length of trial, in s
dt = .001 #minimum time step, in s
t_j, t_p = np.meshgrid(np.arange(0,T,dt), np.arange(n)) #time steps of dt from 0 to T in meshgrid form, in s
rate,y = np.meshgrid(np.zeros(len(t_j[0,:])+1), np.arange(n)) #Initializing r(t) array
r_0 = 100 #Value r(t) exponentially recovers to, in Hz
rate[:,0] = r_0 #Sets first element of each row in rate to r_0
tau_ref = np.arange(1,21,20/n) #Refractory recovery rate array from 1 to 20 in steps of 1, in ms
random, x = np.meshgrid(np.zeros(len(t_j[0,:])), np.arange(n)) #Initializing meshgrid of random numbers between 0 and 1
spkt = [] #Initializing array for list of spike times
tau, z = np.meshgrid(np.zeros(len(t_j[0,:])+1), np.arange(n)) #Initializing array to track times between spikes

#Filling random meshgrid with random elements
for j in range(n):
    for i in range(len(t_j[0,:])):
        random[j,i] = np.random.rand(1)

for j in range(len(tau_ref)):
    spkt.append([])
    for i in range(len(t_j[0,:])):
        # If r(t) = 0, time since spike is incremented and r(t) begins to exponentially rise
        if  rate[j,i] == 0:
            tau[j,i+1] = tau[j,i] + dt
            rate[j,i+1] = r_0 * (1 - np.exp(-tau[j,i+1]) / tau_ref[j])
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
            rate[j,i+1] = r_0 * (1 - np.exp(-tau[j,i + 1] / tau_ref[j]))

interspike = []
for j in range(n):
    interspike.append([])
    for i in range(len(spkt[j][:])-1):
        interspike[j].append(spkt[j][i+1] - spkt[j][i])

#Check array values
print(tau_ref)
print(len(tau_ref))
print(len(spkt))



#Plot coefficient of variation as a function of tau_ref over range 1 ms to 20 ms inclusive

mean = np.zeros(n) #Mean of the interspike intervals for each tau_ref
sd = np.zeros(n) #Standard deviation of the interspike intervals for each tau_ref
C_v = np.zeros(n) #Coefficient of variation for each tau_ref
for j in range(n):
        mean[j] = np.mean(interspike[j][:])
        sd[j] = np.std(interspike[j][:])
        C_v[j] = sd[j] / mean[j]

print(C_v)

plt.plot(tau_ref, C_v)
plt.title(r"$C_v$ Plotted Against $\tau_{ref}$")
plt.xlabel(r'$\tau_{ref}$ (ms)')
plt.ylabel(r'$C_v$')
plt.show()


#Plot interspike interval histograms for a few different values of tau_ref in this range



#For tau_ref = 1 ms
plt.hist(interspike[0][:], weights = np.ones(len(interspike[0][:]))/len(interspike[0][:]))
plt.title(r"$tau_{ref} = 1$ ms")
plt.show()

# For tau_ref = 5 ms
plt.hist(interspike[4][:], weights = np.ones(len(interspike[4][:]))/len(interspike[0][:]))
plt.title(r"$tau_{ref} = 5$ ms")
plt.show()

#For tau_ref = 7 ms
plt.hist(interspike[6][:], weights = np.ones(len(interspike[6][:]))/len(interspike[0][:]))
plt.title(r"$tau_{ref} = 7$ ms")
plt.show()

#For tau_ref = 8 ms
plt.hist(interspike[7][:], weights = np.ones(len(interspike[7][:]))/len(interspike[0][:]))
plt.title(r"$tau_{ref} = 8$ ms")
plt.show()

#For tau_ref = 11 ms
plt.hist(interspike[10][:], weights = np.ones(len(interspike[10][:]))/len(interspike[0][:]))
plt.title(r"$tau_{ref} = 11$ ms")
plt.show()

#For tau_ref = 16 ms
plt.hist(interspike[15][:], weights = np.ones(len(interspike[15][:]))/len(interspike[0][:]))
plt.title(r"$tau_{ref} = 16$ ms")
plt.show()

#For tau_ref = 20 ms
plt.hist(interspike[19][:], weights = np.ones(len(interspike[19][:]))/len(interspike[0][:]))
plt.title(r"$tau_{ref} = 20$ ms")
plt.show()