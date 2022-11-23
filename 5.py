import matplotlib.pyplot as plt
import numpy as np

coffee,tea,water = np.random.randint(100,150),np.random.randint(100,150),np.random.randint(100,150)

coffeex = np.array([round(np.random.uniform(-0.2,1.4), 4) for i in range(coffee)])
coffeey = np.array([round(np.random.uniform(-0.2,1.2), 4) for i in range(coffee)])

teax = np.array([round(np.random.uniform(-0.2,1.4), 4) for i in range(tea)])
teay = np.array([round(np.random.uniform(-0.2,1.2), 4) for i in range(tea)])

waterx = np.array([round(np.random.uniform(-0.2,1.4), 4) for i in range(water)])
watery = np.array([round(np.random.uniform(-0.2,1.2), 4) for i in range(water)])

plt.scatter(coffeex,coffeey,color='black',s=3)
plt.scatter(teax,teay,color="green",s=3)
plt.scatter(waterx,watery,color="blue",s=3)
plt.legend(["coffee", "tea","water"],loc ="lower right")
plt.show()
