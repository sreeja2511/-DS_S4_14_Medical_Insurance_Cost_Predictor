import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 9, 16])
ax.set_title('Sales Data')
ax.set_xlabel('Months')
ax.set_ylabel('Revenue')
plt.show()