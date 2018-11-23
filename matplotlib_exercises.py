#Exercises in matplotlib
import numpy as np
import matplotlib.pyplot as plt

#Exercise 1: Getting started with Matplotlib
#1:
plt.figure(1)
plt.plot(range(10))
plt.show()

#2:
Time = range(7)
CO2 = [250, 265, 272, 260, 300, 320, 389]
plt.figure(2)
plt.plot(Time, CO2)
plt.plot(Time, CO2, "b--")
plt.xlabel("Time (Decade)")
plt.ylabel("CO2 (ppm)")
plt.title("CO2 concentration")
plt.show()


#3 - combined with exercise 2:
Time = range(7)
CO2 = [250, 265, 272, 260, 300, 320, 389]
Temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
#plt.figure(3)
fig, ax1 = plt.subplots()
ax1.plot(Time, CO2, "b--")
ax1.set_ylabel("CO2 (ppm)")
ax1.set_xlabel("Time")
ax2 = ax1.twinx()
ax2.plot(Time, Temp, "r--")
ax2.set_ylabel("Temp (degC)")
plt.title("CO2 concentration and temperature")
plt.show()
