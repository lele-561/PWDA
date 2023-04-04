# 说明：2分类数据集，划分不同大小的训练集
import random
from random import shuffle


# 对比实验：全部方法
def generate_all_set(input_file, output_file, num_0_all, num_1_all, aug_num):
    with open(input_file, 'r', encoding='UTF-8') as f:
        sentences = f.readlines()
        counter = 0

        num_all = num_0_all + num_1_all
        num_0 = int(num_0_all / num_all * size)
        num_1 = int(num_1_all / num_all * size)
        if num_0 + num_1 != size:
            num_0 += size - num_0 - num_1
        print(num_0, num_1)
        sentence_group = []
        one_sentence = []
        for _ in sentences:
            if counter == 16:  # eda均为16条，普通为0，回译为1
                counter = 0
                one_sentence.append(_)
                sentence_group.append(one_sentence)
                one_sentence = []
                continue
            one_sentence.append(_)
            counter += 1
        sentence_0 = sentence_group[0:num_0_all]
        sentence_1 = sentence_group[num_0_all:]
        shuffle(sentence_0)
        shuffle(sentence_1)

        output_0 = sentence_0[:num_0]
        output_1 = sentence_1[:num_1]
        output_list = [output_0, output_1]

        to_be_write = []
        for output in output_list:
            for _ in output:
                # 普通执行
                # to_be_write.extend(_)
                # eda执行
                to_be_write.append(_[-1])  # 原句
                tmp_out = _[:16]  # 全部数据：eda为16，普通为 :
                shuffle(tmp_out)
                to_be_write.extend(tmp_out[:aug_num])
        shuffle(to_be_write)

    with open(output_file, 'w', encoding='UTF-8') as f_train:
        for _ in to_be_write:
            f_train.write(_)


# 消融实验：部分方法
def generate_ablation_set(input_file, output_file, num_0_all, num_1_all, aug_num, operation):
    with open(input_file, 'r', encoding='UTF-8') as f:
        sentences = f.readlines()
        counter = 0

        num_all = num_0_all + num_1_all
        num_0 = int(num_0_all / num_all * size)
        num_1 = int(num_1_all / num_all * size)
        if num_0 + num_1 != size:
            num_0 += size - num_0 - num_1
        print(num_0, num_1)
        sentence_group = []
        one_sentence = []
        for _ in sentences:
            if counter == 16:
                counter = 0
                one_sentence.append(_)
                sentence_group.append(one_sentence)
                one_sentence = []
                continue
            one_sentence.append(_)
            counter += 1
        sentence_0 = sentence_group[0:num_0_all]
        sentence_1 = sentence_group[num_0_all:]
        shuffle(sentence_0)
        shuffle(sentence_1)

        output_0 = sentence_0[:num_0]
        output_1 = sentence_1[:num_1]
        output_list = [output_0, output_1]

        to_be_write = []
        for output in output_list:
            for _ in output:
                # eda执行
                to_be_write.append(_[-1])  # 原句
                if operation == 'RP':
                    tmp_out = _[0:4]  # eda消融数据：随机预测0:4，随机插入4:8，随机交换8:12，随机删除12:16
                elif operation == 'RI':
                    tmp_out = _[4:8]
                elif operation == 'RS':
                    tmp_out = _[8:12]
                elif operation == 'RD':
                    tmp_out = _[12:16]
                shuffle(tmp_out)
                to_be_write.extend(tmp_out[:aug_num])
        shuffle(to_be_write)

    with open(output_file, 'w', encoding='UTF-8') as f_train:
        for _ in to_be_write:
            f_train.write(_)


if __name__ == '__main__':
    dataset = 'SST-2'
    origin_dir = '../../data/' + dataset + '/experiment'
    alphas = [0.1, 0.2, 0.3, 0.4, 0.5]
    aug_nums = [1, 2, 4, 8, 16]
    all_num = []
    sizes = []
    if dataset == 'CR':
        all_num = [510, 962]
        sizes = [100, 500, 1472]

    elif dataset == 'SST-2':
        all_num = [2641, 2843]
        sizes = [100, 500, 2000, 5484]

    random.seed(1)
    for alpha in alphas:
        for size in sizes:
            for aug_num in aug_nums:
                # 原数据
                # input_f = origin_dir + '/train.txt'
                # output_f = origin_dir + '/train/train-' + str(size) + '.txt'
                # 回译数据
                # input_f = origin_dir + '/backTran/backTran-train.txt'
                # output_f = origin_dir + '/backTran/backTran-train-' + str(size) + '.txt'
                # eda数据
                # input_f = origin_dir + '/eda-' + str(alpha) + '/eda-train-' + str(alpha) + '.txt'
                # output_f = origin_dir + '/eda-' + str(alpha) + '/eda-train-' + str(alpha) + '_' + str(size) + '_' + str(
                #     aug_num) + '.txt'
                # pwda数据
                input_f = origin_dir + '/pwda-' + str(alpha) + '/pwda-train-' + str(alpha) + '.txt'
                output_f = origin_dir + '/pwda-' + str(alpha) + '/pwda-train-' + str(alpha) + '_' + str(
                    size) + '_' + str(
                    aug_num) + '.txt'

                generate_all_set(input_f, output_f, all_num[0], all_num[1], aug_num)

                # 消融实验数据
                # operations = ['RP', 'RI', 'RS', 'RD']
                # for operation in operations:
                #     input_f = origin_dir + '/pwda-' + str(alpha) + '/pwda-train-' + str(alpha) + '.txt'
                #     output_f = origin_dir + '/pwda-' + str(alpha) + '/pwda-train-' + str(alpha) + '_' \
                #                + operation + '_' + str(size) + '_' + str(aug_num) + '.txt'
                #     generate_ablation_set(input_f, output_f, all_num[0], all_num[1], aug_num, operation)
