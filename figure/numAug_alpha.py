import matplotlib.pyplot as plt
import numpy as np

dataset = 'CR'
plt.figure(figsize=(8, 5))
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.99, top=0.9, wspace=0.5, hspace=0.6)

score_type = 'F1'
plot_data_x = []
plot_data_y = []
y_ticks = []
x_ticks = []
if dataset == 'TREC-6':
    score_type = 'MCC'
    y_ticks = [0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1]
    x_ticks = [1000, 2000, 3000]
    plot_data_x = [100, 500, 2000, 3569]
    plot_data_y = [
        # plot 1
        [
            [0.693, 0.9211, 0.948, 0.953],
            [0.6659, 0.9186, 0.9413, 0.9513],
            [0.6822, 0.9086, 0.9438, 0.948],
            [0.6686, 0.9161, 0.943, 0.9488],
            [0.6661, 0.9086, 0.9362, 0.9465]
        ],
        # plot 2
        [
            [0.7617, 0.9186, 0.9438, 0.9597],
            [0.7768, 0.9102, 0.943, 0.9497],
            [0.7752, 0.922, 0.9371, 0.9413],
            [0.7727, 0.9211, 0.9438, 0.9522],
            [0.7122, 0.9262, 0.9388, 0.9437]
        ],
        # plot 3
        [
            [0.8498, 0.9203, 0.9497, 0.9572],
            [0.8381, 0.9237, 0.9455, 0.9572],
            [0.8238, 0.9228, 0.9455, 0.9564],
            [0.8297, 0.9237, 0.9396, 0.9471],
            [0.8062, 0.9245, 0.9446, 0.9387]
        ],
        # plot 4
        [
            [0.8641, 0.9295, 0.9547, 0.9522],
            [0.8297, 0.9228, 0.9463, 0.9522],
            [0.8289, 0.9228, 0.9471, 0.9547],
            [0.8809, 0.9186, 0.948, 0.9471],
            [0.8582, 0.9262, 0.9402, 0.9399]
        ],
        # plot 5
        [
            [0.8515, 0.9329, 0.9446, 0.9471],
            [0.8658, 0.9287, 0.9438, 0.9572],
            [0.8473, 0.9236, 0.9446, 0.943],
            [0.8977, 0.9295, 0.9446, 0.9471],
            [0.8599, 0.9253, 0.9398, 0.9404]
        ],
    ]
elif dataset == 'SST-2':
    y_ticks = [0.80, 0.85, 0.90, 0.95, 1]
    x_ticks = [1000, 3000, 5000]
    plot_data_x = [100, 500, 2000, 5484]
    plot_data_y = [
        # plot 1
        [
            [0.9092, 0.9109, 0.9017, 0.9125],
            [0.8629, 0.8837, 0.9058, 0.9008],
            [0.8585, 0.8776, 0.8971, 0.9161],
            [0.8793, 0.8806, 0.904, 0.9209],
            [0.8728, 0.8925, 0.8901, 0.9109]
        ],
        # plot 2
        [
            [0.9095, 0.9117, 0.9156, 0.9202],
            [0.8844, 0.8851, 0.9054, 0.9175],
            [0.8642, 0.8892, 0.906, 0.9157],
            [0.8519, 0.8829, 0.893, 0.918],
            [0.8369, 0.8899, 0.906, 0.9132]
        ],
        # plot 3
        [
            [0.9177, 0.9185, 0.9099, 0.9205],
            [0.8545, 0.8866, 0.9154, 0.9165],
            [0.8588, 0.8848, 0.9108, 0.9173],
            [0.8276, 0.8871, 0.9115, 0.9038],
            [0.8417, 0.8997, 0.8981, 0.9167]
        ],
        # plot 4
        [
            [0.9061, 0.9249, 0.911, 0.9056],
            [0.843, 0.8805, 0.8996, 0.9184],
            [0.8543, 0.8897, 0.9055, 0.9116],
            [0.8474, 0.8834, 0.9052, 0.9111],
            [0.868, 0.8844, 0.9014, 0.9088]
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
    y_ticks = [0.85, 0.90, 0.95, 1]
    x_ticks = [500, 1000]
    plot_data_x = [100, 500, 1472]
    plot_data_y = [
        # plot 1
        [
            [0.9051, 0.9527, 0.9646],
            [0.9025, 0.9558, 0.9615],
            [0.8877, 0.9587, 0.9584],
            [0.8815, 0.9531, 0.9634],
            [0.8677, 0.9511, 0.9628]
        ],
        # plot 2
        [
            [0.9201, 0.9737, 0.9647],
            [0.8616, 0.9659, 0.9599],
            [0.8737, 0.9488, 0.96],
            [0.9104, 0.9459, 0.9568],
            [0.9107, 0.9515, 0.9601]
        ],
        # plot 3
        [
            [0.8995, 0.9556, 0.9687],
            [0.9118, 0.9541, 0.9583],
            [0.9194, 0.9518, 0.9588],
            [0.8937, 0.9547, 0.9521],
            [0.9206, 0.9388, 0.9515]
        ],
        # plot 4
        [
            [0.9335, 0.9881, 0.9508],
            [0.9323, 0.9509, 0.9569],
            [0.9264, 0.9412, 0.9448],
            [0.8902, 0.9356, 0.9531],
            [0.9319, 0.9414, 0.9569]
        ],
        # plot 5
        [
            [0.9325, 0.9492, 0.9595],
            [0.902, 0.9329, 0.9475],
            [0.9274, 0.9436, 0.9344],
            [0.9346, 0.9333, 0.9457],
            [0.9256, 0.9313, 0.9408]
        ],
    ]

# plot 1:
x = np.array(plot_data_x)
y1 = np.array(plot_data_y[0][0])
y2 = np.array(plot_data_y[0][1])
y3 = np.array(plot_data_y[0][2])
y4 = np.array(plot_data_y[0][3])
y5 = np.array(plot_data_y[0][4])
plt.subplot(2, 3, 1)
plt.plot(x, y1, label='0.1', marker='o')
plt.plot(x, y2, label='0.2', marker='^')
plt.plot(x, y3, label='0.3', marker='s')
plt.plot(x, y4, label='0.4', marker='p')
plt.plot(x, y5, label='0.5', marker='*')
plt.title('$n_{aug}$ = 1', fontsize=10)
plt.xlabel('data size')
plt.ylabel(score_type + ' score')
plt.xticks(x_ticks)
plt.yticks(y_ticks)

# plot 2:
x = np.array(plot_data_x)
y1 = np.array(plot_data_y[1][0])
y2 = np.array(plot_data_y[1][1])
y3 = np.array(plot_data_y[1][2])
y4 = np.array(plot_data_y[1][3])
y5 = np.array(plot_data_y[1][4])
plt.subplot(2, 3, 2)
plt.plot(x, y1, label='0.1', marker='o')
plt.plot(x, y2, label='0.2', marker='^')
plt.plot(x, y3, label='0.3', marker='s')
plt.plot(x, y4, label='0.4', marker='p')
plt.plot(x, y5, label='0.5', marker='*')
plt.title('$n_{aug}$ = 2', fontsize=10)
plt.xlabel('data size')
plt.ylabel(score_type + ' score')
plt.xticks(x_ticks)
plt.yticks(y_ticks)

# plot 3:
x = np.array(plot_data_x)
y1 = np.array(plot_data_y[2][0])
y2 = np.array(plot_data_y[2][1])
y3 = np.array(plot_data_y[2][2])
y4 = np.array(plot_data_y[2][3])
y5 = np.array(plot_data_y[2][4])
plt.subplot(2, 3, 3)
plt.plot(x, y1, label='0.1', marker='o')
plt.plot(x, y2, label='0.2', marker='^')
plt.plot(x, y3, label='0.3', marker='s')
plt.plot(x, y4, label='0.4', marker='p')
plt.plot(x, y5, label='0.5', marker='*')
plt.title('$n_{aug}$ = 4', fontsize=10)
plt.xlabel('data size')
plt.ylabel(score_type + ' score')
plt.xticks(x_ticks)
plt.yticks(y_ticks)

# plot 4:
x = np.array(plot_data_x)
y1 = np.array(plot_data_y[3][0])
y2 = np.array(plot_data_y[3][1])
y3 = np.array(plot_data_y[3][2])
y4 = np.array(plot_data_y[3][3])
y5 = np.array(plot_data_y[3][4])
plt.subplot(2, 3, 4)
plt.plot(x, y1, label='0.1', marker='o')
plt.plot(x, y2, label='0.2', marker='^')
plt.plot(x, y3, label='0.3', marker='s')
plt.plot(x, y4, label='0.4', marker='p')
plt.plot(x, y5, label='0.5', marker='*')
plt.title('$n_{aug}$ = 8', fontsize=10)
plt.xlabel('data size')
plt.ylabel(score_type + ' score')
plt.xticks(x_ticks)
plt.yticks(y_ticks)

# plot 5:
x = np.array(plot_data_x)
y1 = np.array(plot_data_y[4][0])
y2 = np.array(plot_data_y[4][1])
y3 = np.array(plot_data_y[4][2])
y4 = np.array(plot_data_y[4][3])
y5 = np.array(plot_data_y[4][4])
plt.subplot(2, 3, 5)
plt.plot(x, y1, label='0.1', marker='o')
plt.plot(x, y2, label='0.2', marker='^')
plt.plot(x, y3, label='0.3', marker='s')
plt.plot(x, y4, label='0.4', marker='p')
plt.plot(x, y5, label='0.5', marker='*')
plt.title('$n_{aug}$ = 16', fontsize=10)
plt.xlabel('data size')
plt.ylabel(score_type + ' score')
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.legend(title='α', loc=0, bbox_to_anchor=(1, 1))

plt.show()
