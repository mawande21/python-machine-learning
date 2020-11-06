from tkinter import *
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title('Tkinter with Histogram')
root.geometry("600x600")
root.configure(background='red')


def graph():

    Nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
    Bins = np.array([0, 1, 2, 3])

    print("nums: ", Nums)
    print("bins: ", Bins)
    print("Result:", np.histogram(Nums, Bins))

    # labels on the x-axis
    # labeling and visuals

    plt.hist(Nums, bins=Bins, color='red')
    plt.title("Histogram of nums against bins.")
    plt.xlabel("Nums")
    plt.ylabel("Bins")
    plt.show()


my_button = Button(root, text='Show Graph', command=graph)
my_button.pack(pady=200)

root.mainloop()

