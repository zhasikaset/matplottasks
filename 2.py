import matplotlib.pyplot as plt
import numpy as np
#you have to scale graph in order to get circle, by default it is a little bit squizzed

x10 = np.linspace(-10,10,10000)
y10 = np.array([(100-i*i)**(0.5)+10 for i in x10])
y20 = np.array([-(100-i*i)**(0.5)+10 for i in x10])

x50 = np.linspace(-50,50,100000)
y50 = np.array([(2500-i*i)**(0.5)+50 for i in x50])
y250 = np.array([-(2500-i*i)**(0.5)+50 for i in x50])

x100 = np.linspace(-100,100,100000)
y100 = np.array([(10000-i*i)**(0.5)+100 for i in x100])
y2100 = np.array([-(10000-i*i)**(0.5)+100 for i in x100])

plt.plot(x10,y10,color = 'black')
plt.plot(x10,y20,color = 'black')

plt.plot(x50,y50,color = 'black')
plt.plot(x50,y250,color = 'black')

plt.plot(x100,y100,color = 'black')
plt.plot(x100,y2100,color = 'black')

plt.grid(True)
plt.show()