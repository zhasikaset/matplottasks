import matplotlib.pyplot as plt
import numpy as np
import random

plt.subplot(221)
nums = np.random.randint(750,1000)
x = np.array([round(np.random.uniform(0.05,0.99), 2) for i in range(nums)])
y = np.array([(np.random.randint(10,9999)) for i in range(nums)])
plt.title("Spring")
plt.scatter(x,y,color = "green",s = 7, marker = "o",alpha = 0.8)
plt.suptitle("Bike rentals at different temperatures by season")

plt.subplot(222)
nums = np.random.randint(750,1000)
x = np.array([round(np.random.uniform(0.05,0.99), 2) for i in range(nums)])
y = np.array([(np.random.randint(10,9999)) for i in range(nums)])
plt.title("Summer")
plt.scatter(x,y,color = "yellow",s = 7, marker = "o",alpha = 0.8)

plt.subplot(223)
nums = np.random.randint(750,1000)
x = np.array([round(np.random.uniform(0.05,0.99), 2) for i in range(nums)])
y = np.array([(np.random.randint(10,9999)) for i in range(nums)])
plt.title("Fall")
plt.scatter(x,y,color = "red",s = 7, marker = "o",alpha = 0.8)

plt.subplot(224)
nums = np.random.randint(750,1000)
x = np.array([round(np.random.uniform(0.05,0.99), 2) for i in range(nums)])
y = np.array([(np.random.randint(10,9999)) for i in range(nums)])
plt.title("Winter")
plt.scatter(x,y,color = "cyan",s = 7, marker = "o",alpha = 0.8)

plt.show()