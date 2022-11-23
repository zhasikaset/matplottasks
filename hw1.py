import matplotlib.pyplot as plt
import numpy as np

x,y=[],[]

for i in range(0,40,2):

    x.append(np.random.randint(i,i+2))
    y.append(np.random.randint(5,90))

plt.plot(x,y,marker="^",color="blue")
plt.title("Graph")
plt.xlabel('x axis')
plt.ylabel("y axis")
plt.legend('curve',loc = "upper right")
plt.grid(True)
plt.show()