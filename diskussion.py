import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat
from uncertainties import unumpy as unp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv
g = ufloat(0.5, 0.021)
s = ufloat(0.4079, 0.0022)
p = ufloat(0.442, 0.024)
print( "relG = ",0.021 / 0.500 )
print("relS =", 0.0022/0.4079  )
print( "relP = ", 0.024 / 0.442 )

print("abw. G und S = ", (g-s)/s)
print("abw. P und S = ", (p-s)/s)
print("abw. G und P = ", (g-p)/p)