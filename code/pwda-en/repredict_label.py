import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification


def classify_TREC(input_f, output_f):
    device = torch.device("cuda")
    model = AutoModelForSequenceClassification.from_pretrained(
        r'D:\Transformers\models\distilbert-base-cased-trec-coarse').to(device)
    tokenizer = AutoTokenizer.from_pretrained(r'D:\Transformers\models\distilbert-base-cased-trec-coarse')

    with open(input_f, 'r', encoding='UTF-8') as in_f:
        lines = in_f.readlines()
    with open(output_f, 'w', encoding='UTF-8') as out_f:
        for line in lines:
            parts = line[:-1].split('\t')
            sentence = parts[0]
            inputs = tokenizer(sentence, return_tensors="pt").to(device)
            with torch.no_grad():
                logits = model(**inputs).logits
            predicted_class_id = logits.argmax().item()
            label = model.config.id2label[predicted_class_id]
            if label == 'DESC':
                out_f.write('0\n')
            elif label == 'ENTY':
                out_f.write('1\n')
            elif label == 'ABBR':
                out_f.write('2\n')
            elif label == 'HUM':
                out_f.write('3\n')
            elif label == 'LOC':
                out_f.write('4\n')
            elif label == 'NUM':
                out_f.write('5\n')


def classify_SST2(input_f, output_f):
    device = torch.device("cuda")
    tokenizer = DistilBertTokenizer.from_pretrained(
        r"D:\Transformers\models\distilbert-base-uncased-finetuned-sst-2-english")
    model = DistilBertForSequenceClassification.from_pretrained(
        r"D:\Transformers\models\distilbert-base-uncased-finetuned-sst-2-english").to(device)

    with open(input_f, 'r', encoding='UTF-8') as in_f:
        lines = in_f.readlines()
    with open(output_f, 'w', encoding='UTF-8') as out_f:
        for line in lines:
            parts = line[:-1].split('\t')
            sentence = parts[0]
            inputs = tokenizer(sentence, return_tensors="pt").to(device)
            with torch.no_grad():
                logits = model(**inputs).logits
            predicted_class_id = logits.argmax().item()
            label = model.config.id2label[predicted_class_id]
            if label == 'POSITIVE':
                out_f.write('1\n')
            else:
                out_f.write('0\n')


def calculateChange(origin_f, predict_f, correct_out_f):
    with open(origin_f, 'r', encoding='UTF-8') as orig_f:
        orig_lines = orig_f.readlines()
    with open(predict_f, 'r', encoding='UTF-8') as pred_f:
        pred_labels = pred_f.readlines()

    sentence_group = []
    label_group = []
    one_sentence = []
    one_label = []
    counter = 0
    for i in range(len(orig_lines)):
        if counter == 16:  # eda和pwda均为16条，普通为0，回译为1
            counter = 0
            one_sentence.append(orig_lines[i])
            one_label.append(pred_labels[i])
            sentence_group.append(one_sentence)
            label_group.append(one_label)
            one_sentence = []
            one_label = []
            continue
        one_sentence.append(orig_lines[i])
        one_label.append(pred_labels[i])
        counter += 1

    count_dif = 0
    for i in range(len(sentence_group)):
        parts = sentence_group[i][-1].strip().split('\t')
        orig_label = parts[1]
        pred_label = label_group[i][-1].strip()

        if pred_label == orig_label:  # 成功预测出原标签
            for j in range(len(sentence_group[i])):  # 修改每句话新预测出的标签
                orig_sentence = sentence_group[i][j][:-1].split('\t')[0]
                if sentence_group[i][j].strip().split('\t')[1] != label_group[i][j].strip():
                    count_dif += 1
                sentence_group[i][j] = orig_sentence + '\t' + label_group[i][j]
    print('change:', count_dif, '; all:', len(orig_lines))
    with open(correct_out_f, 'w', encoding='UTF-8') as out_f:
        for _ in sentence_group:
            for __ in _:
                out_f.write(__)


if __name__ == '__main__':
    dataset = 'SST-2'
    alpha = 0.5
    input_file = '../../data/' + dataset + '/experiment/pwda-noLC-' + str(alpha) + '/pwda-noLC-train-' + str(
        alpha) + '.txt'
    predict_output_file = '../../data/' + dataset + '/experiment/pwda-' + str(alpha) + '/predict-label.txt'
    correct_output_file = '../../data/' + dataset + '/experiment/pwda-' + str(alpha) + '/pwda-train-' + str(
        alpha) + '.txt'
    # 先预测
    if dataset == 'TREC-6':
        classify_TREC(input_file, predict_output_file)
    else:
        classify_SST2(input_file, predict_output_file)
    # 再计算改变的个数
    calculateChange(input_file, predict_output_file, correct_output_file)

# α	            数据集(%)
# 	    SST-2	CR	    TREC-6
# 0.1	3.94	4.96	9.41
# 0.2	6.16	6.81	12.19
# 0.3	8.71	9.51	16.04
# 0.4	11.51	11.74	20.97
# 0.5	14.77	14.07	25.88

# alpha=0.1
# SST-2 change: 3672 ; all: 93228
# CR change: 1242 ; all: 25024
# TREC-6 change: 5722 ; all: 60673

# alpha=0.2
# SST-2 change: 5743 ; all: 93228
# CR change: 1705 ; all: 25024
# TREC-6 change: 7397 ; all: 60673

# alpha=0.3
# SST-2 change: 8124 ; all: 93228
# CR change: 2380 ; all: 25024
# TREC-6 change: 9729 ; all: 60673

# alpha=0.4
# SST-2 change: 10733 ; all: 93228
# CR change: 2938 ; all: 25024
# TREC-6 change: 12722 ; all: 60673

# alpha=0.5
# SST-2 change: 13767 ; all: 93228
# CR change: 3520 ; all: 25024
# TREC-6 change: 15705 ; all: 60673
