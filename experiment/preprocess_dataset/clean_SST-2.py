from utils import *


def get_label(decimal):
    if 0 <= decimal <= 0.2:
        return 0
    elif 0.2 < decimal <= 0.4:
        return 1
    elif 0.4 < decimal <= 0.6:
        return 2
    elif 0.6 < decimal <= 0.8:
        return 3
    elif 0.8 < decimal <= 1:
        return 4
    else:
        return -1


def get_label_binary(decimal):
    if 0 <= decimal <= 0.4:
        return 0
    elif 0.6 < decimal <= 1:
        return 1
    else:
        return -1


def get_split(split_num):
    if split_num == 1 or split_num == 3:
        return 'train'
    elif split_num == 2:
        return 'test'


if __name__ == "__main__":
    data_path = '../../data/SST-2/raw/datasetSentences.txt'
    labels_path = '../../data/SST-2/raw/sentiment_labels.txt'
    split_path = '../../data/SST-2/raw/datasetSplit.txt'
    dictionary_path = '../../data/SST-2/raw/dictionary.txt'

    sentence_lines = open(data_path, 'r').readlines()
    labels_lines = open(labels_path, 'r').readlines()
    split_lines = open(split_path, 'r').readlines()
    dictionary_lines = open(dictionary_path, 'r').readlines()

    print(len(sentence_lines))
    print(len(split_lines))
    print(len(labels_lines))
    print(len(dictionary_lines))

    # create dictionary for id to label
    id_to_label = {}
    for line in labels_lines[1:]:
        parts = line[:-1].split("|")
        _id = parts[0]
        score = float(parts[1])
        label = get_label_binary(score)

        id_to_label[_id] = label

    print(len(id_to_label), "id to labels read in")

    # create dictionary for phrase to label
    phrase_to_label = {}
    for line in dictionary_lines:
        parts = line[:-1].split("|")
        phrase = parts[0]
        _id = parts[1]
        label = id_to_label[_id]

        phrase_to_label[phrase] = label

    print(len(phrase_to_label), "phrase to id read in")

    # create id to split
    id_to_split = {}
    for line in split_lines[1:]:
        parts = line[:-1].split(",")
        _id = parts[0]
        split_num = float(parts[1])
        split = get_split(split_num)
        id_to_split[_id] = split

    print(len(id_to_split), "id to split read in")

    writer_neg = open('../../data/SST-2/origin/negative.txt', 'w')
    writer_pos = open('../../data/SST-2/origin/positive.txt', 'w')

    # create sentence to split and label
    for sentence_line in sentence_lines[1:]:
        parts = sentence_line[:-1].split('\t')
        _id = parts[0]
        sentence = get_only_chars(parts[1])
        split = id_to_split[_id]

        if parts[1] in phrase_to_label:
            label = phrase_to_label[parts[1]]
            if label in {0, 1}:
                if label == 0:
                    writer_neg.write(sentence.strip() + '\t' + str(label) + '\n')
                else:
                    writer_pos.write(sentence.strip() + '\t' + str(label) + '\n')
    writer_neg.close()
    writer_pos.close()
