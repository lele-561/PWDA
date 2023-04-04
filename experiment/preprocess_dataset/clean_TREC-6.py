from utils import *

class_name_to_num = {'DESC': 0, 'ENTY': 1, 'ABBR': 2, 'HUM': 3, 'LOC': 4, 'NUM': 5}


def clean(input_files):
    writer_DESC = open('../../data/TREC-6/origin/DESC.txt', 'w')
    writer_ENTY = open('../../data/TREC-6/origin/ENTY.txt', 'w')
    writer_ABBR = open('../../data/TREC-6/origin/ABBR.txt', 'w')
    writer_HUM = open('../../data/TREC-6/origin/HUM.txt', 'w')
    writer_LOC = open('../../data/TREC-6/origin/LOC.txt', 'w')
    writer_NUM = open('../../data/TREC-6/origin/NUM.txt', 'w')

    for _ in input_files:
        lines = open(_, 'r').readlines()
        for line in lines:
            parts = line[:-1].split(' ')
            tag = parts[0].split(':')[0]
            class_num = class_name_to_num[tag]
            sentence = get_only_chars(' '.join(parts[1:])).strip()
            print(tag, class_num, sentence)
            output_line = sentence + '\t' + str(class_num)
            if tag == 'DESC':
                writer_DESC.write(output_line + '\n')
            elif tag == 'ENTY':
                writer_ENTY.write(output_line + '\n')
            elif tag == 'ABBR':
                writer_ABBR.write(output_line + '\n')
            elif tag == 'HUM':
                writer_HUM.write(output_line + '\n')
            elif tag == 'LOC':
                writer_LOC.write(output_line + '\n')
            else:
                writer_NUM.write(output_line + '\n')
    writer_DESC.close()
    writer_ENTY.close()
    writer_ABBR.close()
    writer_HUM.close()
    writer_LOC.close()
    writer_NUM.close()


if __name__ == "__main__":
    clean(['../../experiment/TREC-6/raw/train_5452.txt', '../../experiment/TREC-6/raw/test_500.txt'])
