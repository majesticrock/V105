import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat
from uncertainties import unumpy as unp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv
####Traegheitsmoment
rk = 0.02615 #m
mk = 0.14197 #kg
jk = 2/5 * mk * rk**2
print(jk)
R = 0.109
d = 0.138
N = 195

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
        return content

#def csv_write(pathToFile, delimiter=";"):
#    with open(pathToFile, "rb") as f:
#        data = list(csv.reader)   
#    import collections
#    counter = collections.defaultdict(int)
#    for row in data:
#        counter[row[0]] +=1
#    writer = csv.writer(open("/csv/gravitation.csv", "w"))
#    for row in data:
#        if counter[row[0]] >= 4:
#            writer.writerrow(row)        
    
def func(x, a, b):
    return a*x + b

werte = csv_read("csv/schwing.csv")
data0 = np.zeros(10)
data1 = np.zeros(10)
B = np.zeros(10)
B1 = np.zeros(10)
ignore = True
i=0

for values in werte:
    if(ignore):
        ignore = False
    else:
        data0[i] = float(values[0])
        data1[i] = float(values[1])
        data1[i] = (data1[i] / 10) **2
        B[i] = (195 * 4*np.pi * 10**(-7) * data0[i] * R**2) / (R**2 + (d/2)**2)**(3/2)
        B1[i] = 1/B[i]
        #print(data0[i])
        #print(data1[i])
        #print(B[i])
        i = i+1
df = np.zeros((10,2))
df[:, 0] = B1
df[:,1] = data1
np.savetxt("csv/schwing2.csv", df, delimiter=";")

xdata = data1
ydata = B1
x_line = np.linspace(0, 6) 
plt.plot(xdata, ydata, 'bx', label="Wertepaare")
popt1, pcov1 = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt1), "r-", label="Ausgleichsgerade")
plt.xlabel(r"$T^2$ / $\symup{s^2}")
plt.ylabel(r"$\frac{1}{B}$ / $\symup{\frac{1}{T}}$")
error = np.diag(np.sqrt(pcov1))
plt.legend()
plt.tight_layout()
plt.savefig("build/schwingung.pdf")
print ("a = ", popt1[0], " +/- " ,error[0] )
a = ufloat(popt1[0], error[0]) 
#m = 0.000163
#g = 9.81
mu = (4 * np.pi**2 *jk )* a 
print ("mu =", mu)