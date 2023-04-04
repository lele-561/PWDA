import random
import re
from random import shuffle

# 预测连续位置
import torch
from transformers import BartForConditionalGeneration
from transformers import BartTokenizer

device = torch.device("cuda")
model = BartForConditionalGeneration.from_pretrained(r"D:\Transformers\models\bart-large",
                                                     forced_bos_token_id=0).to(device)
tokenizer = BartTokenizer.from_pretrained(r"D:\Transformers\models\bart-large")


def BART_prediction(sentences):
    res = []
    for _ in sentences:
        batch = tokenizer(_, return_tensors="pt")
        batch.to(device)
        generated_ids = model.generate(batch["input_ids"], max_length=50)  # 设定一下maxlength否则报错
        res.extend(tokenizer.batch_decode(generated_ids, skip_special_tokens=True))
    return res


random.seed(1)  # 都给设好了真是谢谢啊

# 停用词
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our',
              'ours', 'ourselves', 'you', 'your', 'yours',
              'yourself', 'yourselves', 'he', 'him', 'his',
              'himself', 'she', 'her', 'hers', 'herself',
              'it', 'its', 'itself', 'they', 'them', 'their',
              'theirs', 'themselves', 'what', 'which', 'who',
              'whom', 'this', 'that', 'these', 'those', 'am',
              'is', 'are', 'was', 'were', 'be', 'been', 'being',
              'have', 'has', 'had', 'having', 'do', 'does', 'did',
              'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or',
              'because', 'as', 'until', 'while', 'of', 'at',
              'by', 'for', 'with', 'about', 'against', 'between',
              'into', 'through', 'during', 'before', 'after',
              'above', 'below', 'to', 'from', 'up', 'down', 'in',
              'out', 'on', 'off', 'over', 'under', 'again',
              'further', 'then', 'once', 'here', 'there', 'when',
              'where', 'why', 'how', 'all', 'any', 'both', 'each',
              'few', 'more', 'most', 'other', 'some', 'such', 'no',
              'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too',
              'very', 's', 't', 'can', 'will', 'just', 'don',
              'should', 'now', '']


# 清理文本
def get_only_chars(line):
    clean_line = ""

    line = line.replace("’", "")
    line = line.replace("'", "")
    line = line.replace("-", " ")
    line = line.replace('\t', " ")
    line = line.replace("\n", " ")
    line = line.lower()

    for char in line:
        if char in 'qwertyuiopasdfghjklzxcvbnm ':
            clean_line += char
        else:
            clean_line += ' '

    clean_line = re.sub(' +', ' ', clean_line)
    if clean_line[0] == ' ':
        clean_line = clean_line[1:]
    return clean_line


# Random prediction 随机预测：对一句话生成mask随机掩蔽再预测mask位置
def random_prediction(words, n):
    new_words = words.copy()
    # 取出所有非停用词
    random_num_list = []
    for i in range(len(new_words)):
        if new_words[i] not in stop_words:
            random_num_list.append(i)
    if len(random_num_list) == 0:
        random_num_list.append(random.randint(0, len(new_words) - 1))
    shuffle(random_num_list)
    # 将非停用词随机替换为<mask>
    # 有可能存在停用词过多，替换<mask>不够的情况，这种情况下能换多少换多少，如果全是停用词就随机mask掉一个结构
    num_replaced = 0
    for i in random_num_list:
        new_words[i] = "<mask>"
        num_replaced += 1
        if num_replaced == n:
            break
    # 先把所有需要<mask>预测的句子生成好，避免重复调用多次模型
    sentence = ' '.join(new_words)
    return sentence


# Random insertion 随机插入：随机将n个mask预测结果插入句子
def random_insertion(words, n):
    new_words = words.copy()
    # 插入n次
    for _ in range(n):
        add_word(new_words)
    return new_words


# 每次只mask一个，然后插入随机位置
def add_word(words):
    if len(words) == 1:
        words.insert(0, words[0])
    else:
        new_words = words.copy()
        # 取出所有非停用词，随机选择一个<mask>掉，如果全是停用词就随机选择一个结构mask
        rand_mask = random.randint(0, len(new_words) - 1)
        random_num_list = []
        for i in range(len(new_words)):
            if new_words[i] not in stop_words:
                random_num_list.append(i)
        if len(random_num_list) != 0:
            shuffle(random_num_list)
            rand_mask = random_num_list[0]
        new_words[rand_mask] = "<mask>"
        sentence = ' '.join(new_words)
        res = get_only_chars(BART_prediction([sentence])[0])
        # 将预测出来的<mask>塞到原结构中
        mask = get_mask(words, res, rand_mask)
        random_idx = random.randint(0, len(words) - 1)
        words.insert(random_idx, mask)


# 获取<mask>
def get_mask(mask_sen, new_sen, mask_pos):
    before_sen = ' '.join(mask_sen.copy()[:mask_pos])
    after_sen = ' '.join(mask_sen.copy()[mask_pos + 1:])
    mask = new_sen[new_sen.find(before_sen) + len(before_sen):new_sen.rfind(after_sen)].strip()
    return mask


# Random swap 随机交换：随机交换句子中的2个结构n次
def random_swap(words, n):
    new_words = words.copy()
    # 交换n次，每次选择两个不同的结构
    for _ in range(n):
        swap_word(new_words)
    return new_words


def swap_word(words):
    random_num_list = [_ for _ in range(len(words))]
    shuffle(random_num_list)
    random_idx_1 = random_num_list[0]
    random_idx_2 = random_idx_1 if len(words) == 1 else random_num_list[1]
    # 交换二者位置
    words[random_idx_1], words[random_idx_2] = words[random_idx_2], words[random_idx_1]
    return words


# Random deletion 随机删除：句子里的每个结构都有p的概率被删除
def random_deletion(words, p):
    # 如果剩一个结构，不删
    if len(words) == 1:
        return words
    # randomly delete words with probability p
    new_words = []
    for word in words:
        r = random.uniform(0, 1)  # 随机下看删不删
        if r > p:
            new_words.append(word)
    # 要是结构都删没了就随机填回来一个结构
    if len(new_words) == 0:
        rand_int = random.randint(0, len(words) - 1)
        return [words[rand_int]]

    return new_words


def pwda(sentences, alpha_rp, alpha_ri, alpha_rs, p_rd, num_aug):
    origin_sentence = ' '.join(sentences[0])
    num_per_tech = int(num_aug / 4) + 1  # 每种方法增加句子的个数，均相同
    # 各方法待增广的句子
    sentence_rp = sentences[:num_per_tech]
    sentence_ri = sentences[num_per_tech:2 * num_per_tech]
    sentence_rs = sentences[2 * num_per_tech:3 * num_per_tech]
    sentence_rd = sentences[3 * num_per_tech:]
    augmented_sentences = []

    # rp
    if alpha_rp > 0:
        mask_sentences = []
        flag = len(sentence_rp[0]) == 1  # 只有一个结构时
        for words in sentence_rp:
            if flag:
                augmented_sentences.extend(words)
            else:
                n_rp = max(1, int(alpha_rp * len(words)))  # n_rp是要更改的结构数，当不足1个时只改一个
                mask_sentences.append(random_prediction(words, n_rp))
        if not flag:
            augmented_sentences.extend(BART_prediction(mask_sentences))  # <mask>预测

    # ri
    if alpha_ri > 0:
        for words in sentence_ri:
            n_ri = max(1, int(alpha_ri * len(words)))
            a_words = random_insertion(words, n_ri)
            augmented_sentences.append(' '.join(a_words))

    # rs
    if alpha_rs > 0:
        for words in sentence_rs:
            n_rs = max(1, int(alpha_rs * len(words)))
            a_words = random_swap(words, n_rs)
            augmented_sentences.append(' '.join(a_words))

    # rd
    if p_rd > 0:
        for words in sentence_rd:
            a_words = random_deletion(words, p_rd)
            augmented_sentences.append(' '.join(a_words))
    augmented_sentences = [get_only_chars(sentence) for sentence in augmented_sentences]

    # 随机从所有增广的句子中取出num_aug个句子
    if num_aug >= 1:
        augmented_sentences = augmented_sentences[:num_aug]
    else:
        keep_prob = num_aug / len(augmented_sentences)
        augmented_sentences = [s for s in augmented_sentences if random.uniform(0, 1) < keep_prob]

    # append the original sentence
    augmented_sentences.append(origin_sentence)  # 加入原句一起训练
    return augmented_sentences
