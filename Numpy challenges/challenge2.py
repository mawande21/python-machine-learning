import matplotlib.pyplot as plt
import numpy as np


nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])

bins = np.array([0, 1, 2, 3])

plt.hist(nums, bins, color='yellow')

plt.xlabel("Nums")

plt.ylabel("Bins")

plt.title("Histogram of Nums against Bins")



plt.show()
