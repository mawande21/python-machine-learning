import matplotlib.pyplot as plt



test_scores = [12,99,65,85,42]

test_names = ['Andy', 'Martin', 'Zahara', 'Vuyo', 'Ziyaad']

#labels on the x-axis
x_pos = [i for i, _ in enumerate(test_names)]

#labeling and visuals
plt.bar(x_pos, test_scores, color='red')

plt.xlabel("Test Names")

plt.ylabel("Marks")

plt.title("Python marks for 5 students")

plt.xticks(x_pos, test_names)

plt.show()

