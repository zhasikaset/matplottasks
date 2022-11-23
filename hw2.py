import matplotlib.pyplot as plt
import numpy as np

x,y=[],[]
for i in range(1,30):
    x.append(np.random.uniform(i/50-0.05,i/50+0.05))
    y.append(np.random.uniform(x[i-1]+0.03,x[i-1]-0.03))
x0 = np.linspace(x[0],x[-1],100)
y0 = np.array([y[0]+(y[0]-y[-1])*(i-x[0])/(x[0]-x[-1]) for i in x0])
for i in range(len(x)):
    plt.plot(x[i],y[i],marker="o",color = 'blue')
plt.plot(x0,y0,color='red')
plt.title("Best fit line using regression method")
plt.xlabel('x axis')
plt.ylabel("y axis")
plt.grid(True)
plt.show()