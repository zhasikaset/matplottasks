import matplotlib.pyplot as plt
import numpy as np
import random


days = ['Mon','Tue',"Wed","Thu","Fri","Sat","Sun"]

colors = ['blue','green',"red","cyan","yellow","magenta","black"]

data = [random.randint(10,100) for i in range(7)]

plt.bar(days,data,color = colors)

plt.show()