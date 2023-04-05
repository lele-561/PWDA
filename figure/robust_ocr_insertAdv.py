import matplotlib.pyplot as plt
import numpy as np

dataset = 'CR'
plt.figure(figsize=(8, 5))
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.95, top=0.9, wspace=0.5, hspace=0.6)

score_type = 'F1'
plot_data_x = []
plot_data_y = []
y_ticks = []
x_ticks = []
if dataset == 'TREC-6':
    score_type = 'MCC'
    y_ticks = [0.6, 0.7, 0.8, 0.9, 1]
    x_ticks = [1000, 2000, 3000]
    plot_data_x = [100, 500, 2000, 3569]
    plot_data_y = [
        # ocr
        [
            # plot 1
            [
                [0.5889, 0.7802, 0.8054, 0.8079],
                [0.5762, 0.7676, 0.7819, 0.7609],
                [0.5696, 0.7584, 0.7785, 0.7777],
                [0.5604, 0.7643, 0.776, 0.7802],
                [0.5638, 0.7676, 0.7727, 0.7816],
            ],
            # plot 2
            [
                [0.6518, 0.7601, 0.7861, 0.8171],
                [0.6384, 0.7727, 0.7592, 0.7668],
                [0.6862, 0.7584, 0.7492, 0.7735],
                [0.6711, 0.7341, 0.7576, 0.7735],
                [0.5696, 0.7819, 0.7466, 0.7768],
            ],
            # plot 3
            [
                [0.7016, 0.7617, 0.8029, 0.8247],
                [0.6871, 0.7466, 0.7936, 0.781],
                [0.6695, 0.7374, 0.7517, 0.7609],
                [0.7047, 0.7802, 0.7617, 0.7592],
                [0.6971, 0.7324, 0.7849, 0.7787],
            ],
            # plot 4
            [
                [0.6938, 0.7424, 0.797, 0.8054],
                [0.6535, 0.7374, 0.7668, 0.7752],
                [0.7173, 0.7307, 0.7492, 0.7659],
                [0.7206, 0.7332, 0.7668, 0.7701],
                [0.7055, 0.7584, 0.7831, 0.7803],
            ],
            # plot 5
            [
                [0.672, 0.7508, 0.7903, 0.8171],
                [0.7064, 0.7534, 0.7676, 0.7735],
                [0.7055, 0.7458, 0.7534, 0.7601],
                [0.7072, 0.7383, 0.7559, 0.771],
                [0.7097, 0.7282, 0.7799, 0.7792],
            ],
        ],
        # insertAdv
        [
            # plot 1
            [
                [0.6352, 0.8526, 0.8904, 0.9208],
                [0.6823, 0.8455, 0.8819, 0.9009],
                [0.6696, 0.8584, 0.8985, 0.8977],
                [0.6604, 0.8643, 0.886, 0.8802],
                [0.6549, 0.8298, 0.8686, 0.8836],
            ],
            # plot 2
            [
                [0.7001, 0.8441, 0.9005, 0.9073],
                [0.6984, 0.8527, 0.8592, 0.8968],
                [0.7862, 0.8584, 0.8892, 0.9035],
                [0.7711, 0.8341, 0.8776, 0.8835],
                [0.7677, 0.8467, 0.8753, 0.8784],
            ],
            # plot 3
            [
                [0.7835, 0.8517, 0.8812, 0.909],
                [0.7871, 0.8466, 0.8936, 0.891],
                [0.7695, 0.8374, 0.8917, 0.8809],
                [0.8047, 0.8802, 0.8617, 0.8792],
                [0.7961, 0.8408, 0.8652, 0.8877],
            ],
            # plot 4
            [
                [0.786, 0.8374, 0.8854, 0.8972],
                [0.7535, 0.8374, 0.8668, 0.8952],
                [0.8173, 0.8307, 0.8792, 0.8959],
                [0.8206, 0.8332, 0.8668, 0.8901],
                [0.7742, 0.8703, 0.8866, 0.8934],
            ],
            # plot 5
            [
                [0.7641, 0.8298, 0.8829, 0.904],
                [0.8064, 0.8534, 0.8676, 0.8935],
                [0.8055, 0.8458, 0.8534, 0.9001],
                [0.8072, 0.8383, 0.8559, 0.881],
                [0.752, 0.8349, 0.8795, 0.8795],
            ],
        ]
    ]
elif dataset == 'SST-2':
    y_ticks = [0.6, 0.7, 0.8, 0.9, 1]
    x_ticks = [1000, 3000, 5000]
    plot_data_x = [100, 500, 2000, 5484]
    plot_data_y = [
        # ocr
        [
            # plot 1
            [
                [0.8033, 0.7904, 0.8093, 0.8257],
                [0.7543, 0.7619, 0.7995, 0.8284],
                [0.6857, 0.8008, 0.8043, 0.8278],
                [0.644, 0.7994, 0.8221, 0.8191],
                [0.698, 0.7848, 0.7971, 0.8119],
            ],
            # plot 2
            [
                [0.7567, 0.7557, 0.8129, 0.8365],
                [0.7804, 0.7845, 0.8137, 0.8151],
                [0.6181, 0.7935, 0.8049, 0.8275],
                [0.6907, 0.8045, 0.8108, 0.8057],
                [0.6745, 0.7946, 0.8241, 0.8247],
            ],
            # plot 3
            [
                [0.7626, 0.788, 0.8064, 0.81],
                [0.7475, 0.8115, 0.8158, 0.8077],
                [0.6775, 0.783, 0.8057, 0.8052],
                [0.748, 0.7945, 0.8231, 0.8091],
                [0.7282, 0.774, 0.8012, 0.8164],
            ],
            # plot 4
            [
                [0.7346, 0.7581, 0.7691, 0.8076],
                [0.7079, 0.7553, 0.7937, 0.8221],
                [0.7268, 0.7595, 0.7899, 0.8155],
                [0.7582, 0.8115, 0.8282, 0.812],
                [0.7211, 0.7932, 0.788, 0.8044],
            ],
            # plot 5
            [
                [0.8018, 0.7861, 0.7989, 0.8065],
                [0.7931, 0.7921, 0.7889, 0.8016],
                [0.7719, 0.7881, 0.8065, 0.8099],
                [0.788, 0.7906, 0.8097, 0.8091],
                [0.6995, 0.7829, 0.7856, 0.8103],
            ],
        ],
        # insertAdv
        [
            # plot 1
            [
                [0.8406, 0.864, 0.8726, 0.8824],
                [0.7813, 0.8665, 0.8651, 0.863],
                [0.8072, 0.8586, 0.8669, 0.8842],
                [0.7486, 0.8539, 0.8662, 0.8677],
                [0.728, 0.8425, 0.8617, 0.8798]
            ],
            # plot 2
            [
                [0.8359, 0.8575, 0.866, 0.885],
                [0.8046, 0.8506, 0.861, 0.8704],
                [0.6997, 0.8552, 0.8776, 0.8786],
                [0.8343, 0.8566, 0.8554, 0.8791],
                [0.7592, 0.8526, 0.8708, 0.8717]
            ],
            # plot 3
            [
                [0.8309, 0.8607, 0.8746, 0.8853],
                [0.8128, 0.8576, 0.8827, 0.8859],
                [0.7749, 0.8544, 0.8665, 0.8738],
                [0.8043, 0.8571, 0.882, 0.8696],
                [0.8139, 0.8626, 0.8759, 0.8795]
            ],
            # plot 4
            [
                [0.8275, 0.822, 0.8511, 0.872],
                [0.7794, 0.8328, 0.8672, 0.8641],
                [0.8059, 0.8341, 0.8767, 0.8797],
                [0.8172, 0.8304, 0.8686, 0.8796],
                [0.8135, 0.8389, 0.8599, 0.8764]
            ],
            # plot 5
            [
                [0.8337, 0.8446, 0.8653, 0.8716],
                [0.8571, 0.8235, 0.8654, 0.8711],
                [0.8519, 0.8311, 0.8486, 0.8729],
                [0.8609, 0.8557, 0.8621, 0.8672],
                [0.8268, 0.848, 0.8742, 0.8699]
            ],
        ]
    ]
elif dataset == 'CR':
    y_ticks = [0.7, 0.8, 0.9, 1]
    x_ticks = [500, 1000]
    plot_data_x = [100, 500, 1472]
    plot_data_y = [
        # ocr
        [
            # plot 1
            [
                [0.8397, 0.8766, 0.8986],
                [0.8452, 0.8548, 0.878],
                [0.7858, 0.8948, 0.8342],
                [0.8396, 0.892, 0.8834],
                [0.8028, 0.8834, 0.8642],
            ],
            # plot 2
            [
                [0.8082, 0.885, 0.8764],
                [0.7796, 0.8519, 0.8456],
                [0.8292, 0.846, 0.8485],
                [0.8592, 0.8435, 0.8839],
                [0.8247, 0.8868, 0.8486],
            ],
            # plot 3
            [
                [0.8382, 0.8441, 0.8825],
                [0.853, 0.8442, 0.8633],
                [0.8612, 0.8609, 0.8795],
                [0.8193, 0.8612, 0.8728],
                [0.8363, 0.8377, 0.8636],
            ],
            # plot 4
            [
                [0.7965, 0.8632, 0.8776],
                [0.7731, 0.8442, 0.8832],
                [0.7856, 0.8519, 0.8489],
                [0.7902, 0.8398, 0.8835],
                [0.8061, 0.8521, 0.8723],
            ],
            # plot 5
            [
                [0.8049, 0.8625, 0.8416],
                [0.8354, 0.7396, 0.8659],
                [0.8308, 0.7949, 0.8581],
                [0.8666, 0.8581, 0.8567],
                [0.765, 0.8028, 0.7986],
            ],
        ],
        # insertAdv
        [
            # plot 1
            [
                [0.8942, 0.9272, 0.9431],
                [0.8963, 0.9239, 0.9345],
                [0.7802, 0.9358, 0.9231],
                [0.8132, 0.9128, 0.9305],
                [0.8447, 0.9291, 0.9378]
            ],
            # plot 2
            [
                [0.8136, 0.9388, 0.9394],
                [0.8346, 0.9212, 0.9292],
                [0.8476, 0.9122, 0.9336],
                [0.8687, 0.9134, 0.9088],
                [0.8816, 0.9172, 0.9182]
            ],
            # plot 3
            [
                [0.8671, 0.9333, 0.9416],
                [0.8758, 0.9246, 0.9286],
                [0.8808, 0.9113, 0.9082],
                [0.8795, 0.9384, 0.915],
                [0.8896, 0.9134, 0.9032]
            ],
            # plot 4
            [
                [0.9017, 0.9159, 0.928],
                [0.8629, 0.9293, 0.9116],
                [0.8743, 0.9129, 0.906],
                [0.7845, 0.9241, 0.9063],
                [0.9115, 0.9121, 0.9191]
            ],
            # plot 5
            [
                [0.8943, 0.9088, 0.9262],
                [0.8881, 0.9011, 0.8928],
                [0.8851, 0.899, 0.9016],
                [0.904, 0.901, 0.9138],
                [0.9091, 0.8893, 0.9005]
            ],
        ]
    ]

# plot 1:
x = np.array(plot_data_x)
y1_ocr = np.array(plot_data_y[0][0][0])
y2_ocr = np.array(plot_data_y[0][0][1])
y3_ocr = np.array(plot_data_y[0][0][2])
y4_ocr = np.array(plot_data_y[0][0][3])
y5_ocr = np.array(plot_data_y[0][0][4])
y1_adv = np.array(plot_data_y[1][0][0])
y2_adv = np.array(plot_data_y[1][0][1])
y3_adv = np.array(plot_data_y[1][0][2])
y4_adv = np.array(plot_data_y[1][0][3])
y5_adv = np.array(plot_data_y[1][0][4])
plt.subplot(2, 3, 1)
plt.plot(x, y1_ocr, label='0.1-OCR', marker='o')
plt.plot(x, y2_ocr, label='0.2-OCR', marker='^')
plt.plot(x, y3_ocr, label='0.3-OCR', marker='s')
plt.plot(x, y4_ocr, label='0.4-OCR', marker='p')
plt.plot(x, y5_ocr, label='0.5-OCR', marker='*')
plt.plot(x, y1_adv, label='0.1-InsertAdv', linestyle='dashed', marker='o')
plt.plot(x, y2_adv, label='0.2-InsertAdv', linestyle='dashed', marker='^')
plt.plot(x, y3_adv, label='0.3-InsertAdv', linestyle='dashed', marker='s')
plt.plot(x, y4_adv, label='0.4-InsertAdv', linestyle='dashed', marker='p')
plt.plot(x, y5_adv, label='0.5-InsertAdv', linestyle='dashed', marker='*')
plt.title('$n_{aug}$ = 1', fontsize=10)
plt.xlabel('data size')
plt.ylabel(score_type + ' score')
plt.xticks(x_ticks)
plt.yticks(y_ticks)

# plot 2:
x = np.array(plot_data_x)
y1_ocr = np.array(plot_data_y[0][1][0])
y2_ocr = np.array(plot_data_y[0][1][1])
y3_ocr = np.array(plot_data_y[0][1][2])
y4_ocr = np.array(plot_data_y[0][1][3])
y5_ocr = np.array(plot_data_y[0][1][4])
y1_adv = np.array(plot_data_y[1][1][0])
y2_adv = np.array(plot_data_y[1][1][1])
y3_adv = np.array(plot_data_y[1][1][2])
y4_adv = np.array(plot_data_y[1][1][3])
y5_adv = np.array(plot_data_y[1][1][4])
plt.subplot(2, 3, 2)
plt.plot(x, y1_ocr, label='0.1-OCR', marker='o')
plt.plot(x, y2_ocr, label='0.2-OCR', marker='^')
plt.plot(x, y3_ocr, label='0.3-OCR', marker='s')
plt.plot(x, y4_ocr, label='0.4-OCR', marker='p')
plt.plot(x, y5_ocr, label='0.5-OCR', marker='*')
plt.plot(x, y1_adv, label='0.1-InsertAdv', linestyle='dashed', marker='o')
plt.plot(x, y2_adv, label='0.2-InsertAdv', linestyle='dashed', marker='^')
plt.plot(x, y3_adv, label='0.3-InsertAdv', linestyle='dashed', marker='s')
plt.plot(x, y4_adv, label='0.4-InsertAdv', linestyle='dashed', marker='p')
plt.plot(x, y5_adv, label='0.5-InsertAdv', linestyle='dashed', marker='*')
plt.title('$n_{aug}$ = 2', fontsize=10)
plt.xlabel('data size')
plt.ylabel(score_type + ' score')
plt.xticks(x_ticks)
plt.yticks(y_ticks)

# plot 3:
x = np.array(plot_data_x)
y1_ocr = np.array(plot_data_y[0][2][0])
y2_ocr = np.array(plot_data_y[0][2][1])
y3_ocr = np.array(plot_data_y[0][2][2])
y4_ocr = np.array(plot_data_y[0][2][3])
y5_ocr = np.array(plot_data_y[0][2][4])
y1_adv = np.array(plot_data_y[1][2][0])
y2_adv = np.array(plot_data_y[1][2][1])
y3_adv = np.array(plot_data_y[1][2][2])
y4_adv = np.array(plot_data_y[1][2][3])
y5_adv = np.array(plot_data_y[1][2][4])
plt.subplot(2, 3, 3)
plt.plot(x, y1_ocr, label='0.1-OCR', marker='o')
plt.plot(x, y2_ocr, label='0.2-OCR', marker='^')
plt.plot(x, y3_ocr, label='0.3-OCR', marker='s')
plt.plot(x, y4_ocr, label='0.4-OCR', marker='p')
plt.plot(x, y5_ocr, label='0.5-OCR', marker='*')
plt.plot(x, y1_adv, label='0.1-InsertAdv', linestyle='dashed', marker='o')
plt.plot(x, y2_adv, label='0.2-InsertAdv', linestyle='dashed', marker='^')
plt.plot(x, y3_adv, label='0.3-InsertAdv', linestyle='dashed', marker='s')
plt.plot(x, y4_adv, label='0.4-InsertAdv', linestyle='dashed', marker='p')
plt.plot(x, y5_adv, label='0.5-InsertAdv', linestyle='dashed', marker='*')
plt.title('$n_{aug}$ = 4', fontsize=10)
plt.xlabel('data size')
plt.ylabel(score_type + ' score')
plt.xticks(x_ticks)
plt.yticks(y_ticks)

# plot 4:
x = np.array(plot_data_x)
y1_ocr = np.array(plot_data_y[0][3][0])
y2_ocr = np.array(plot_data_y[0][3][1])
y3_ocr = np.array(plot_data_y[0][3][2])
y4_ocr = np.array(plot_data_y[0][3][3])
y5_ocr = np.array(plot_data_y[0][3][4])
y1_adv = np.array(plot_data_y[1][3][0])
y2_adv = np.array(plot_data_y[1][3][1])
y3_adv = np.array(plot_data_y[1][3][2])
y4_adv = np.array(plot_data_y[1][3][3])
y5_adv = np.array(plot_data_y[1][3][4])
plt.subplot(2, 3, 4)
plt.plot(x, y1_ocr, label='0.1-OCR', marker='o')
plt.plot(x, y2_ocr, label='0.2-OCR', marker='^')
plt.plot(x, y3_ocr, label='0.3-OCR', marker='s')
plt.plot(x, y4_ocr, label='0.4-OCR', marker='p')
plt.plot(x, y5_ocr, label='0.5-OCR', marker='*')
plt.plot(x, y1_adv, label='0.1-InsertAdv', linestyle='dashed', marker='o')
plt.plot(x, y2_adv, label='0.2-InsertAdv', linestyle='dashed', marker='^')
plt.plot(x, y3_adv, label='0.3-InsertAdv', linestyle='dashed', marker='s')
plt.plot(x, y4_adv, label='0.4-InsertAdv', linestyle='dashed', marker='p')
plt.plot(x, y5_adv, label='0.5-InsertAdv', linestyle='dashed', marker='*')
plt.title('$n_{aug}$ = 8', fontsize=10)
plt.xlabel('data size')
plt.ylabel(score_type + ' score')
plt.xticks(x_ticks)
plt.yticks(y_ticks)

# plot 5:
x = np.array(plot_data_x)
y1_ocr = np.array(plot_data_y[0][4][0])
y2_ocr = np.array(plot_data_y[0][4][1])
y3_ocr = np.array(plot_data_y[0][4][2])
y4_ocr = np.array(plot_data_y[0][4][3])
y5_ocr = np.array(plot_data_y[0][4][4])
y1_adv = np.array(plot_data_y[1][4][0])
y2_adv = np.array(plot_data_y[1][4][1])
y3_adv = np.array(plot_data_y[1][4][2])
y4_adv = np.array(plot_data_y[1][4][3])
y5_adv = np.array(plot_data_y[1][4][4])
plt.subplot(2, 3, 5)
plt.plot(x, y1_ocr, label='0.1-OCR', marker='o')
plt.plot(x, y2_ocr, label='0.2-OCR', marker='^')
plt.plot(x, y3_ocr, label='0.3-OCR', marker='s')
plt.plot(x, y4_ocr, label='0.4-OCR', marker='p')
plt.plot(x, y5_ocr, label='0.5-OCR', marker='*')
plt.plot(x, y1_adv, label='0.1-InsertAdv', linestyle='dashed', marker='o')
plt.plot(x, y2_adv, label='0.2-InsertAdv', linestyle='dashed', marker='^')
plt.plot(x, y3_adv, label='0.3-InsertAdv', linestyle='dashed', marker='s')
plt.plot(x, y4_adv, label='0.4-InsertAdv', linestyle='dashed', marker='p')
plt.plot(x, y5_adv, label='0.5-InsertAdv', linestyle='dashed', marker='*')
plt.title('$n_{aug}$ = 16', fontsize=10)
plt.xlabel('data size')
plt.ylabel(score_type + ' score')
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.legend(ncol=2, title='α', loc=0, bbox_to_anchor=(1, 1))

plt.show()
