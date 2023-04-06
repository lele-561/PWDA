import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(5, 2))
plt.subplots_adjust(left=0.13, bottom=0.25, right=0.8, top=0.9, wspace=0.4, hspace=0.6)

y_ticks = [-2, 0, 2, 4, 6, 8, 10, 12]
x_ticks = [1, 2, 4, 8, 16]
plot_data_x = [1, 2, 4, 8, 16]
plot_data_y = [
    # plot 1
    [
        [3.29, 6.08, 8.62, 9.9, 11.02],
        [2.42, 2.78, 2.8, 2.76, 2.63],
        [0.91, 1.12, 1.5, 1.39, 1.49],
        [1.37, 1.46, 1.38, 1, 0.82]
    ],
    # plot 2
    [
        [1.29, 3.78, 6.98, 6.04, 8.32],
        [1.73, 1.14, 1.02, -0.1, -0.68],
        [2.31, 1.77, 2.39, 1.49, 1.24],
        [1.13, 0.77, 0.61, 0.56, -0.22]
    ]
]

# plot 1:
x = np.array(plot_data_x)
y1 = np.array(plot_data_y[0][0])
y2 = np.array(plot_data_y[0][1])
y3 = np.array(plot_data_y[0][2])
y4 = np.array(plot_data_y[0][3])
plt.subplot(1, 2, 1)
plt.plot(x, y1, label='100', marker='o')
plt.plot(x, y2, label='500', marker='^')
plt.plot(x, y3, label='2000', marker='s')
plt.plot(x, y4, label='all', marker='p')
plt.title('Before Attack', fontsize=10)
plt.xlabel('$n_{aug}$')
plt.ylabel('Performance gain (%)')
plt.xticks(x_ticks)
plt.yticks(y_ticks)

# plot 2:
x = np.array(plot_data_x)
y1 = np.array(plot_data_y[1][0])
y2 = np.array(plot_data_y[1][1])
y3 = np.array(plot_data_y[1][2])
y4 = np.array(plot_data_y[1][3])
plt.subplot(1, 2, 2)
plt.plot(x, y1, label='100', marker='o')
plt.plot(x, y2, label='500', marker='^')
plt.plot(x, y3, label='2000', marker='s')
plt.plot(x, y4, label='all', marker='p')
plt.title('After Attack', fontsize=10)
plt.xlabel('$n_{aug}$')
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.legend(title='data size', loc=0, bbox_to_anchor=(1, 1))

plt.show()
