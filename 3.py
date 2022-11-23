import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(2,4,1000)
y1 = np.array([(1-(i-3)**2)**(0.5)+4 for i in x1])
y12 = np.array([-(1-(i-3)**2)**(0.5)+4 for i in x1])

x2 = np.linspace(1.5,4.5,2000)
y2 = np.array([(1.5**2-(i-3)**2)**(0.5)+4 for i in x2])
y22 = np.array([-(1.5**2-(i-3)**2)**(0.5)+4 for i in x2])

x3 = np.linspace(1,5,3000)
y3 = np.array([(4-(i-3)**2)**(0.5)+4 for i in x3])
y32 = np.array([-(4-(i-3)**2)**(0.5)+4 for i in x3])

x4 = np.linspace(6,8,1000)
y4 = np.array([(1-(i-7)**2)**(0.5)+4 for i in x4])
y42 = np.array([-(1-(i-7)**2)**(0.5)+4 for i in x4])

x5 = np.linspace(5.5,8.5,2000)
y5 = np.array([(2.25-(i-7)**2)**(0.5)+4 for i in x5])
y52 = np.array([-(2.25-(i-7)**2)**(0.5)+4 for i in x5])

x6 = np.linspace(5,9,3000)
y6 = np.array([(4-(i-7)**2)**(0.5)+4 for i in x6])
y62 = np.array([-(4-(i-7)**2)**(0.5)+4 for i in x6])

liney = np.linspace(0,8,100)
linex = np.array([5 for i in range(100)])

plt.plot(x1,y1,color = 'black')
plt.plot(x1,y12,color = 'black')

plt.plot(x2,y2,color = 'yellow')
plt.plot(x2,y22,color = 'yellow')

plt.plot(x3,y3,color = 'green')
plt.plot(x3,y32,color = 'green')

plt.plot(x4,y4,color = 'black')
plt.plot(x4,y42,color = 'black')

plt.plot(x5,y5,color = 'yellow')
plt.plot(x5,y52,color = 'yellow')

plt.plot(x6,y6,color = 'green')
plt.plot(x6,y62,color = 'green')

plt.plot(linex,liney,color = 'green')

plt.xlim(0,10)
plt.ylim(0,8)

plt.grid(True)
plt.show()