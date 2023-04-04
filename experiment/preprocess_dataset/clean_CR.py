# 0 = neg, 1 = pos
from utils import *


def retrieve_reviews(line):
    reviews = set()
    chars = list(line)
    for i, char in enumerate(chars):
        if char == '[':
            if chars[i + 1] == '-':
                reviews.add(0)
            elif chars[i + 1] == '+':
                reviews.add(1)

    reviews = list(reviews)
    if len(reviews) == 2:
        return -2
    elif len(reviews) == 1:
        return reviews[0]
    else:
        return -1


def clean_files(input_files, output_files):
    writer_neg = open(output_files[0], 'w', encoding='utf-8')
    writer_pos = open(output_files[1], 'w', encoding='utf-8')
    negative_lines = []
    positive_lines = []
    for input_file in input_files:
        print(input_file)
        input_lines = open(input_file, 'r', encoding='utf-8').readlines()
        counter = 0
        bad_counter = 0
        for line in input_lines:
            if line[0] == '#':
                continue
            review = retrieve_reviews(line)
            if review in {0, 1}:
                print(line)
                right_pos = line.rfind('#')
                line = line[right_pos + 1:]
                print(line)
                good_line = get_only_chars(re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", line))
                output_line = good_line.strip() + '\t' + str(review) + '\n'
                if review == 0:
                    negative_lines.append(output_line)
                else:
                    positive_lines.append(output_line)
                counter += 1
            elif review == -2:
                bad_counter += 1
        print(input_file, counter, bad_counter)

    for _ in negative_lines:
        writer_neg.write(_)
    for _ in positive_lines:
        writer_pos.write(_)
    writer_neg.close()
    writer_pos.close()


if __name__ == '__main__':
    input_files = ['Canon_G3.txt', 'Computer.txt', 'DVD.txt', 'Nikon_4300.txt', 'Nokia_6610.txt', 'Router.txt',
                   'Speaker.txt', 'Zen_Xtra.txt']
    input_files = ['../../data/CR/raw/' + f for f in input_files]
    output_files = ['../../data/CR/origin/negative.txt', '../../data/CR/origin/positive.txt']
    clean_files(input_files, output_files)
