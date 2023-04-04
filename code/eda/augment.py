from eda import *


# generate more data with standard augmentation
def gen_eda(in_file, out_file, alpha_sr, alpha_ri, alpha_rs, alpha_rd, num_aug):
    writer = open(out_file, 'w', encoding='UTF-8')
    lines = open(in_file, 'r', encoding='UTF-8').readlines()

    for i, line in enumerate(lines):
        parts = line[:-1].split('\t')
        label = parts[1]
        sentence = parts[0]
        aug_sentences = eda(sentence, alpha_sr=alpha_sr, alpha_ri=alpha_ri, alpha_rs=alpha_rs, p_rd=alpha_rd,
                            num_aug=num_aug)
        for aug_sentence in aug_sentences:
            writer.write(aug_sentence.strip() + '\t' + label + '\n')
    writer.close()
    print("generated augmented sentences with eda for " + in_file + " to " + out_file + " with num_aug=" + str(num_aug))


if __name__ == "__main__":
    # how much to replace each word by synonyms
    alpha_sr = 0.1  # default
    # how much to insert new words that are synonyms
    alpha_ri = 0.1  # default
    # how much to swap words
    alpha_rs = 0.1  # default
    # how much to delete words
    alpha_rd = 0.1  # default
    # number of augmented sentences to generate per original sentence
    num_aug = 16  # default 默认生成句子数
    dataset = 'TREC-6'

    input_file = '../../data/' + dataset + '/experiment/train.txt'
    output_file = '../../data/' + dataset + '/experiment/eda-train-0.1.txt'
    gen_eda(input_file, output_file,
            alpha_sr=alpha_sr, alpha_ri=alpha_ri, alpha_rs=alpha_rs, alpha_rd=alpha_rd, num_aug=num_aug)
