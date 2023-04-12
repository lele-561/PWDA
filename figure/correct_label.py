import matplotlib.pyplot as plt
import numpy as np

dataset = 'TREC-6'
plt.figure(figsize=(5, 2))
plt.subplots_adjust(left=0.13, bottom=0.25, right=0.8, top=0.9, wspace=0.4, hspace=0.6)
score_type = 'F1'
model_type = 'XLNet'
plot_data_x = []
plot_data_y = []
y_ticks = []
x_ticks = []
if dataset == 'TREC-6':
    score_type = 'MCC'
    model_type = 'RoBERTa'
    y_ticks = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    x_ticks = [1000, 3000]
    plot_data_x = [100, 500, 2000, 3569]
    plot_data_y = [
        # plot 1
        [
            [-0.34, 1.44, 0.03, 0.44],
            [-0.2, -0.35, -0.83, -0.6],
            [0.92, 1.21, 0.27, -1.24],
            [1.6, 0.68, 0.19, 0.32],
            [2.13, 2.18, 0.2, -0.5]
        ],
        # plot 2
        [
            [4.62, 1.51, 1.18, 0.33],
            [2.26, 2.35, 0.34, 1.09],
            [2.35, 1.59, 1.51, 2.6],
            [4.87, 4.2, 2.94, 1.93],
            [3.1, 4.62, 2.6, 2.09]
        ]
    ]
elif dataset == 'SST-2':
    y_ticks = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    x_ticks = [1000, 3000, 5000]
    plot_data_x = [100, 500, 2000, 5484]
    plot_data_y = [
        # plot 1
        [
            [0.28, 2.66, -0.05, 0.46],
            [0.46, -0.34, -0.34, -0.24],
            [-2.22, 1.62, -0.17, -1.34],
            [0.59, 1.38, 0.9, 0.7],
            [3.73, 2.06, 1.54, 0.09]
        ],
        # plot 2
        [
            [0.52, 1.17, 1.43, 1.87],
            [1.13, 2, 2.18, 3.3],
            [1, 2.53, 1.43, 1.3],
            [1.14, 4.1, 3.59, 1.45],
            [3.88, 4.85, 3.85, 1.24],
        ]
    ]
elif dataset == 'CR':
    y_ticks = [-3, -2, -1, 0, 1, 2, 3]
    x_ticks = [500, 1000]
    plot_data_x = [100, 500, 1472]
    plot_data_y = [
        [
            # plot 1
            [0.06, 0.77, 2.37],
            [0.4, 0.77, 2.9],
            [0.69, 1.3, 2.66],
            [-0.28, 0.52, 2.02],
            [0.28, 1.41, -0.84]
        ],
        # plot 2
        [
            [1.07, 0.42, 0.08],
            [-0.16, 2.06, 1.22],
            [-0.5, 1.51, 0.86],
            [1.25, 2.28, -0.45],
            [1.68, 2.08, 1.51]
        ],
    ]

# plot 1:
x = np.array(plot_data_x)
y1 = np.array(plot_data_y[0][0])
y2 = np.array(plot_data_y[0][1])
y3 = np.array(plot_data_y[0][2])
y4 = np.array(plot_data_y[0][3])
y5 = np.array(plot_data_y[0][4])
plt.subplot(1, 2, 1)
plt.plot(x, y1, label='1', marker='o')
plt.plot(x, y2, label='2', marker='^')
plt.plot(x, y3, label='4', marker='s')
plt.plot(x, y4, label='8', marker='p')
plt.plot(x, y5, label='16', marker='*')
plt.title('CNN', fontsize=10)
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
plt.subplot(1, 2, 2)
plt.plot(x, y1, label='1', marker='o')
plt.plot(x, y2, label='2', marker='^')
plt.plot(x, y3, label='4', marker='s')
plt.plot(x, y4, label='8', marker='p')
plt.plot(x, y5, label='16', marker='*')
plt.title(model_type, fontsize=10)
plt.xlabel('data size')
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.legend(title='$n_{aug}$', loc=0, bbox_to_anchor=(1, 1))

plt.show()
