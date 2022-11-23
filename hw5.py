import matplotlib.pyplot as plt
import numpy as np
from math import *

countries = ["India","Germany","Australia","South Korea","US","UK"]
density = [27.7,16.5,9.2,4.5,18.5,24.6]
output = []
for i in range(len(countries)):
    txt = "For "+countries[i]+" is "+str(density[i])+"%"
    output.append(txt)

plt.pie(density,labels = countries,explode = [0,0,0,0,0.2,0],shadow=True,startangle=150)
plt.title("Population density index")
plt.legend(output)
plt.show()

