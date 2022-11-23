import matplotlib.pyplot as plt
import numpy as np
from math import *

countries = ["India","Germany","Australia","South Korea","US","UK"]
density = [27.7,16.5,9.2,4.5,18.5,24.6]

plt.pie(density,explode = [0,0,0,0,0.2,0],labels = countries,shadow=True,startangle=150,autopct='%.1f%%')
plt.title("Population Density Index")
plt.show()

