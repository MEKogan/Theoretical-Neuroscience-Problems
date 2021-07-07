import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import integrate


r_0 = 50 #Background firing rate, in Hz
dt = 10 #Minimum time interval, in ms
var_s = 10 #Variance of Gaussian white noise stimulus, in ms
T = 10000 #Length of trial, in ms
t = np.arange(0,T,dt) #Array of time values from 0 to T, in ms
tau = np.arange(0, T, dt) #Array of time values for tau, in ms
rate = [r_0] * T #Initializing array of rate values, in Hz

#Constructing a Gaussian white noise stimulus

stimulus = np.zeros(len(tau))
for i in range(len(tau)):
    stimulus[i] = random.gauss(0, np.sqrt(var_s/dt))


D = - np.cos(2*np.pi *(tau - .02) / .14) * np.exp(- tau / .06) #Linear Kernel, in Hz/ms

#Only need to calculate integral up to tau = 50 ms since D(tau > 50 ms) = 0


print(stimulus)





