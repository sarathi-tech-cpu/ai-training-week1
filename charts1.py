import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 40]
y2 = [5, 15, 20, 25, 35]
categories = ['A', 'B', 'C', 'D']
values = [15, 30, 45, 10]

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, y1, marker='o', color='blue')
axs[0, 0].set_title('Line Chart')

axs[0, 1].bar(categories, values, color='green')
axs[0, 1].set_title('Bar Chart')

axs[1, 0].scatter(x, y2, color='red')
axs[1, 0].set_title('Scatter Plot')

axs[1, 1].barh(categories, values, color='orange')
axs[1, 1].set_title('Horizontal Bar Chart')

plt.tight_layout()
plt.savefig('charts_output.png')
plt.show()