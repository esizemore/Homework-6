#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 14:45:36 2017

@author: elizabethsizemore
"""

from math import sin
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

#given information
l=.12 #arm length (m)
g=9.8 #gravity (m/s^2)
initial_t=0.0 #initial time seconds
final_t= 20.0 #stop time seconds
N=1000#number of steps
h=(final_t-initial_t)/N #step size conditions

def f(r,t):
    theta= r[0]
    omega=r[1]
    ddttheta=omega
    ddtomega=-(g/l)*sin(theta*np.pi/180)
    return np.array ([ddttheta*180/np.pi, ddtomega], float)
    
tpoints=arange(initial_t, final_t, h)
xpoints =[]
r=(-175, 0.0)


#Use 4th order runga kutta
for t in tpoints:
    xpoints.append(r[0])
    k1=h*f(r, t)
    k2= h*f(r+ 0.5*k1, t+0.5*h)
    k3=h*f(r + 0.5*k2, t+0.5*h)
    k4=h*f(r+k3, t+h)
    r+= (k1+2*k2+2*k3+k4)/6


plt.plot (tpoints, xpoints)
plt.xlabel('Time (seconds)')
plt.ylabel('Angle (degrees)')
plt.title('Function of Pendulum Angle vs time')






















