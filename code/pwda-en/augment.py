from pwda import *
from split_phrase import *


def gen_pwda(in_file, out_file, alpha_rp, alpha_ri, alpha_rs, alpha_rd, num_aug):
    writer = open(out_file, 'w', encoding='UTF-8')
    lines = open(in_file, 'r', encoding='UTF-8').readlines()

    for i, line in enumerate(lines):
        parts = line[:-1].split('\t')
        label = parts[1].strip()
        sentence = parts[0].strip()
        print(sentence)
        # 1. 划分句子结构
        res_sent = split_to_phrase(sentence)  # 划分好的句子
        # 2. 根据增广句子数对生成的句子结构进行处理，多退少补
        # 生成的句子结构数>=要求增广的句子数：直接shuffle，再取相应数目送入4个方法
        # 生成的句子结构数<要求增广的句子数：从句子结构中随机选择填入，重复相差的次数，再将所有结构shuffle，送入4个方法
        num_aug_all = (int(num_aug / 4) + 1) * 4  # 每种方法增加句子的个数*4
        if len(res_sent) < num_aug_all:
            while len(res_sent) != num_aug_all:
                random_sent = res_sent[random.randint(0, len(res_sent) - 1)]
                res_sent.append(random_sent)
        shuffle(res_sent)
        res_sent = res_sent[:num_aug_all]

        aug_sentences = pwda(res_sent,
                             alpha_rp=alpha_rp, alpha_ri=alpha_ri, alpha_rs=alpha_rs, p_rd=alpha_rd,
                             num_aug=num_aug)
        for aug_sentence in aug_sentences:
            writer.write(aug_sentence.strip() + '\t' + label + '\n')
    writer.close()
    print("generated augmented sentences with pwda-en for " + in_file + " to " + out_file + " with num_aug=" + str(
        num_aug))


if __name__ == "__main__":
    dataset = 'SST-2'  # 英文数据集
    num_aug = 16  # 增广句子数
    alphas = [0.1, 0.2, 0.3, 0.4, 0.5]  # 修改率
    for alpha in alphas:
        input_file = '../../data/' + dataset + '/experiment/train/train.txt'
        output_file = '../../data/' + dataset + '/experiment/pwda-noLC-' + str(alpha) + '/pwda-noLC-train-' + str(
            alpha) + '.txt'
        gen_pwda(input_file, output_file, alpha_rp=alpha, alpha_ri=alpha, alpha_rs=alpha, alpha_rd=alpha,
                 num_aug=num_aug)
