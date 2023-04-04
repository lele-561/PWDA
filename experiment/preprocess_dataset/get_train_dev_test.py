import os
import random
from random import shuffle

random.seed(1)
# 每次生成训练集、验证集、测试集时需要修改的地方
dataset = 'TREC-6'
origin_dir = '../../data/' + dataset
fraction = 1

train = []
dev = []
test = []

train_file = origin_dir + '/experiment/train/train.txt'
dev_file = origin_dir + '/experiment/test/dev.txt'
test_file = origin_dir + '/experiment/test/test.txt'

for root, dirs, files in os.walk(origin_dir + '/origin'):
    for file in files:
        # 获取文件路径
        train_list = []
        dev_list = []
        test_list = []
        file_path = os.path.join(root, file)
        with open(file_path, 'r', encoding='UTF-8') as f:
            lines = f.readlines()
            len_f = len(lines)
            shuffle(lines)
            train_list.extend(lines[:int(len_f * 0.6)])
            dev_list.extend(lines[int(len_f * 0.6):int(len_f * 0.8)])
            test_list.extend(lines[int(len_f * 0.8):])
            # 按训练集占比划分
            train.extend(train_list[:int(len(train_list) * fraction)])
            dev.extend(dev_list[: max(1, int(len(dev_list) * fraction))])
            test.extend(test_list[:max(1, int(len(test_list) * fraction))])

with open(train_file, 'w', encoding='UTF-8') as f_train:
    for _ in train:
        f_train.write(_)
with open(dev_file, 'w', encoding='UTF-8') as f_dev:
    shuffle(dev)
    for _ in dev:
        f_dev.write(_)
with open(test_file, 'w', encoding='UTF-8') as f_test:
    shuffle(test)
    for _ in test:
        f_test.write(_)
