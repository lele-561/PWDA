import matplotlib.pyplot as plt
import numpy as np

dataset = 'CR'
plt.figure(figsize=(9, 2))
plt.subplots_adjust(left=0.08, bottom=0.25, right=0.9, top=0.9, wspace=0.3, hspace=0.6)

score_type = 'F1'
plot_data_x = []
plot_data_y = []
y_ticks = []
x_ticks = []
if dataset == 'TREC-6':
    score_type = 'MCC'
    y_ticks = [0, 4, 8, 12, 16]
    x_ticks = [1000, 3000]
    plot_data_x = [100, 500, 2000, 3569]
    plot_data_y = [
        # plot 1
        [
            [14.18, 4.03, 2.12, 1.6],
            [13.96, 3.52, 2.07, 1.59],
            [10.24, 3.75, 1.93, 1.59],
            [13.71, 3.63, 1.79, 1.54],
            [10.88, 2.55, 1.85, 1.76]

        ],
        # plot 2
        [
            [15.05, 3.1, 2.41, 1.18],
            [12.39, 3.44, 2.43, 1.88],
            [11.6, 3.44, 2.4, 1.84],
            [12.33, 3.47, 2.38, 1.62],
            [13.73, 3.61, 2.49, 1.85]

        ],
        # plot 3
        [
            [10.85, 3.63, 2.04, 1.49],
            [8.66, 3.58, 1.96, 1.65],
            [11.94, 3.41, 2.4, 1.48],
            [4.31, 3.1, 2.07, 1.31],
            [6.92, 2.97, 2.21, 1.34]
        ],
        # plot 4
        [
            [12.56, 3.36, 1.96, 1.58],
            [8.05, 2.52, 1.99, 1.32],
            [6.57, 3.66, 1.62, 1.51],
            [5.54, 2.93, 1.56, 1.37],
            [5.13, 3.24, 1.62, 1.42]
        ],
    ]
elif dataset == 'SST-2':
    y_ticks = [-3, -2, -1, 0, 1, 2, 3]
    x_ticks = [1000, 3000, 5000]
    plot_data_x = [100, 500, 2000, 5484]
    plot_data_y = [
        # plot 1
        [
            [1.76, 2.2, 0.53, 0.56],
            [0.2, 0.9, 0.31, 0.52],
            [-0.9, 0.65, 1.12, 0.59],
            [-3.05, 0.67, 0.5, 0.63],
            [-3.9, 0.23, -0.23, 0.66]
        ],
        # plot 2
        [
            [1.82, 1.29, 0.58, 0.59],
            [0.19, 0.53, 0.39, 0.58],
            [-0.81, 0.4, 0.61, 0.47],
            [-2.79, 0.93, 0.81, 0.72],
            [-3.13, -0.72, -0.09, 1.09]
        ],
        # plot 3
        [
            [1.85, 0.79, 0.26, 0.48],
            [0.34, 0.95, 0.35, 0.33],
            [-1.45, 1.07, 0.34, 0.43],
            [-3.96, -0.3, -0.57, 0.36],
            [-3.36, -0.75, -0.68, 0.42]
        ],
        # plot 4
        [
            [0.1, 1.06, 0.11, 0.71],
            [-0.28, 0.24, 0.24, 0.55],
            [-2.74, 0.93, 0.15, 0.46],
            [-3.08, 0.74, -0.38, 0.9],
            [-3.66, -0.35, -1.17, 0.68]
        ],
        # plot 5
        [
            [0.9198, 0.935, 0.9288, 0.9211],
            [0.8781, 0.8825, 0.9126, 0.9104],
            [0.8638, 0.8933, 0.8966, 0.9191],
            [0.8795, 0.8914, 0.9011, 0.9132],
            [0.8784, 0.889, 0.9122, 0.9106]
        ],
    ]
elif dataset == 'CR':
    y_ticks = [-2, 0, 2, 4, 6, 8]
    x_ticks = [500, 1000]
    plot_data_x = [100, 500, 1472]
    plot_data_y = [
        # plot 1
        [
            [7.07, 3.09, 0.95],
            [5.09, 2.47, 0.79],
            [2.44, 2.08, 1.01],
            [5.52, 2.51, 1.06],
            [1.55, 2.59, 1.07]
        ],
        # plot 2
        [
            [5.13, 2.53, 0.83],
            [2.55, 3.15, 1.11],
            [4.17, 2.53, 1],
            [1.88, 2.22, 0.78],
            [1.32, 2.51, 0.81]
        ],
        # plot 3
        [
            [3.9, 1.97, 0.98],
            [3.49, 2.85, 0.68],
            [-0.19, 2.66, 0.66],
            [-0.97, 2.54, 0.32],
            [-1.37, 2.35, 0.8]
        ],
        # plot 4
        [
            [2.92, 3.11, 0.95],
            [2.45, 3.14, 0.85],
            [-1, 2.97, 0.95],
            [-0.32, 2.52, 1.04],
            [-0.7, 2.23, 0.63]
        ],
    ]

# plot 1:
x = np.array(plot_data_x)
y1 = np.array(plot_data_y[0][0])
y2 = np.array(plot_data_y[0][1])
y3 = np.array(plot_data_y[0][2])
y4 = np.array(plot_data_y[0][3])
y5 = np.array(plot_data_y[0][4])
plt.subplot(1, 4, 1)
plt.plot(x, y1, label='0.1', marker='o')
plt.plot(x, y2, label='0.2', marker='^')
plt.plot(x, y3, label='0.3', marker='s')
plt.plot(x, y4, label='0.4', marker='p')
plt.plot(x, y5, label='0.5', marker='*')
plt.title('Random Prediction', fontsize=10)
plt.xlabel('data size')
plt.ylabel(score_type + ' score gain (%)')
plt.xticks(x_ticks)
plt.yticks(y_ticks)

# plot 2:
x = np.array(plot_data_x)
y1 = np.array(plot_data_y[1][0])
y2 = np.array(plot_data_y[1][1])
y3 = np.array(plot_data_y[1][2])
y4 = np.array(plot_data_y[1][3])
y5 = np.array(plot_data_y[1][4])
plt.subplot(1, 4, 2)
plt.plot(x, y1, label='0.1', marker='o')
plt.plot(x, y2, label='0.2', marker='^')
plt.plot(x, y3, label='0.3', marker='s')
plt.plot(x, y4, label='0.4', marker='p')
plt.plot(x, y5, label='0.5', marker='*')
plt.title('Random Insertion', fontsize=10)
plt.xlabel('data size')
plt.xticks(x_ticks)
plt.yticks(y_ticks)

# plot 3:
x = np.array(plot_data_x)
y1 = np.array(plot_data_y[2][0])
y2 = np.array(plot_data_y[2][1])
y3 = np.array(plot_data_y[2][2])
y4 = np.array(plot_data_y[2][3])
y5 = np.array(plot_data_y[2][4])
plt.subplot(1, 4, 3)
plt.plot(x, y1, label='0.1', marker='o')
plt.plot(x, y2, label='0.2', marker='^')
plt.plot(x, y3, label='0.3', marker='s')
plt.plot(x, y4, label='0.4', marker='p')
plt.plot(x, y5, label='0.5', marker='*')
plt.title('Random Swap', fontsize=10)
plt.xlabel('data size')
plt.xticks(x_ticks)
plt.yticks(y_ticks)

# plot 4:
x = np.array(plot_data_x)
y1 = np.array(plot_data_y[3][0])
y2 = np.array(plot_data_y[3][1])
y3 = np.array(plot_data_y[3][2])
y4 = np.array(plot_data_y[3][3])
y5 = np.array(plot_data_y[3][4])
plt.subplot(1, 4, 4)
plt.plot(x, y1, label='0.1', marker='o')
plt.plot(x, y2, label='0.2', marker='^')
plt.plot(x, y3, label='0.3', marker='s')
plt.plot(x, y4, label='0.4', marker='p')
plt.plot(x, y5, label='0.5', marker='*')
plt.title('Random Deletion', fontsize=10)
plt.xlabel('data size')
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.legend(title='α', loc=0, bbox_to_anchor=(1, 1))

plt.show()
