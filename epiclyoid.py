import matplotlib.pyplot as plt
from matplotlib import animation
from math import *
import cmath as math2
import numpy as np
import sys
import parser

reps = 1

print("0. Exit ")
print("1. Input integer value ")
print("2. Input fraction numbers ")
print("3. Input root number  ")
print("4. Input Euler's number")
opt = int(raw_input("Choice : "))

if opt == 0:
    sys.exit(0)
if opt == 1:
    R = int(raw_input(" R = "))
    r = int(raw_input(" r = "))
    reps = int(raw_input("Number of repetitions = "))
if opt == 2:
    r = int(raw_input(" r = "))
    print ("R = n/d")
    n = float(raw_input("n = "))
    d = float(raw_input("d = "))
    reps = int(raw_input("Number of repetitions = "))

    R = float(n/d)
if opt == 3:
    r = int(raw_input(" r = "))
    R = sqrt(float(raw_input(" R = ")))
    reps = int(raw_input("Number of repetitions = "))
if opt == 4:
    r = int(raw_input(" r = "))
    print ("1. e + x ")
    print ("2. e - x ")
    print ("3. e * x ")
    print ("4. e / x ")
    op = int(raw_input("Choice : "))
    if op == 1:
        R = float(math2.e + (int(raw_input("e +  "))))
    if op == 2:
        R = float(math2.e - (int(raw_input("e -  "))))
    if op == 3:
        R = float(math2.e * (int(raw_input("e *  "))))
    if op ==4:
        R = float(math2.e / (int(raw_input("e /  "))))
    reps = int(raw_input("Number of repetitions = "))



circumference = reps * 360
x_points = []
y_points = []


print " Epicycloid"
for s in range(0,circumference):
    x = (R + r) * cos(radians(s)) - r * cos(radians(((R + r)/r)*s))
    y = (R + r) * sin(radians(s)) - r * sin(radians(((R + r)/r)*s))
    x_points.append(x)
    y_points.append(y)



raza = plt.Line2D((0, 0), (0, 0), linewidth=1, color="k")
circler = plt.Circle((0, 0), r, color='r', fill=False)
circleR = plt.Circle((0, 0), R, color='r', fill=False)
punct = plt.Circle((0, 0), float(float(r)/10), color="r")
fig, ax = plt.subplots()
ax.set_xlim(-2*(R + r),2*(R + r))
ax.set_ylim(-2*(R + r),2*(R + r))
trace, = ax.plot([], [], color="b")
ax.add_artist(circleR)
ax.add_artist(raza)
ax.add_artist(punct)
ax.add_artist(circler)
ax.add_artist(trace)



def init():
    circler.center = (0, 0)
    punct.center = (0, 0)
    ax.add_patch(circler)
    ax.add_patch(punct)
    return circler, punct,

def animate(i):
    x = (r +  R) * np.cos(np.radians(i))
    y = (r + R) * np.sin(np.radians(i))
    x2 = x_points[i]
    y2 = y_points[i]
    raza.set_data((x, x2), (y , y2))
    circler.center = (x, y)
    punct.center = (x2, y2)
    trace.set_data((x_points[:i], y_points[:i]))
    return circler, punct, raza, trace,

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=circumference,
                               interval=20,
                               blit=True)

plt.grid()
plt.plot(x_points, y_points, alpha=0)
plt.show()




