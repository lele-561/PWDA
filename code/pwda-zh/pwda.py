import random
import re
from random import shuffle

from transformers import BertTokenizer, BartForConditionalGeneration, Text2TextGenerationPipeline
from zhon.hanzi import punctuation


# 预测连续位置
def BART_prediction(sentences):
    tokenizer = BertTokenizer.from_pretrained(r"D:\Transformers\models\bart-base-chinese")
    model = BartForConditionalGeneration.from_pretrained(r"D:\Transformers\models\bart-base-chinese")
    text2text_generator = Text2TextGenerationPipeline(model, tokenizer)
    res = []

    for _ in sentences:
        res.append(text2text_generator(_, max_length=300, do_sample=False)[0]['generated_text'].replace(" ", ""))
    return res


random.seed(1)

# 停用词
stop_words = []
with open('stopwords/hit_stopwords.txt', 'r', encoding='UTF-8') as f:
    for stop_word in f.readlines():
        stop_words.append(stop_word[:-1])


# 清理文本，空格不用去除
def get_only_characters(line):
    return re.sub(r"[%s]+" % punctuation, "", line)


# Random prediction 随机预测：对一句话生成mask随机掩蔽再预测mask位置
def random_prediction(words, n):
    # 对一句话生成mask随机遮盖
    new_words = words.copy()
    # 取出所有非停用词
    random_num_list = []
    for i in range(len(new_words)):
        if new_words[i] not in stop_words:
            random_num_list.append(i)
    shuffle(random_num_list)
    # 将非停用词随机替换为[MASK]
    # 有可能存在停用词过多，替换[MASK]不够的情况，这种情况目前先不处理，考虑到如果向其中插入[MASK]就变成了RI方法
    num_replaced = 0
    for i in random_num_list:
        new_words[i] = "[MASK]"
        num_replaced += 1
        if num_replaced == n:
            break
    # 先把所有需要[MASK]预测的句子生成好，避免重复调用多次模型
    sentence = ''.join(new_words)
    return sentence


# Random insertion 随机插入：随机将n个单词插入句子
def random_insertion(words, n):
    new_words = words.copy()
    # 插入n次
    for _ in range(n):
        add_word(new_words)
    return new_words


# 每次只mask一个，然后随机插入随机位置
def add_word(words):
    new_words = words.copy()
    # 取出所有非停用词，随机选择一个[MASK]掉
    random_num_list = []
    for i in range(len(new_words)):
        if new_words[i] not in stop_words:
            random_num_list.append(i)
    shuffle(random_num_list)
    new_words[random_num_list[0]] = "[MASK]"
    sentence = ''.join(new_words)
    res = get_only_characters(BART_prediction([sentence])[0])
    # 将预测出来的[MASK]塞到原结构中
    mask = get_mask(words, res, random_num_list[0])
    random_idx = random.randint(0, len(words) - 1)
    words.insert(random_idx, mask)


# 获取[MASK]
def get_mask(mask_sen, new_sen, mask_pos):
    before_sen = ''.join(mask_sen.copy()[:mask_pos])
    after_sen = ''.join(mask_sen.copy()[mask_pos + 1:])
    mask = new_sen[new_sen.find(before_sen) + len(before_sen):new_sen.rfind(after_sen)].strip()
    return mask


# Random swap 随机交换：随机交换句子中的2个词n次
def random_swap(words, n):
    new_words = words.copy()
    # 交换n次，每次选择两个不同的词
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


# Random deletion 随机删除：句子里的每个词都有p的概率被删除
def random_deletion(words, p):
    # 如果剩一个词，不删
    if len(words) == 1:
        return words
    # randomly delete words with probability p
    new_words = []
    for word in words:
        r = random.uniform(0, 1)  # 随机下看删不删
        if r > p:
            new_words.append(word)
    # 要是词都删没了就随机填回来一个词
    if len(new_words) == 0:
        rand_int = random.randint(0, len(words) - 1)
        return [words[rand_int]]

    return new_words


# 增广数据主体函数
def pwda(sentences, alpha_rp=0.1, alpha_ri=0.1, alpha_rs=0.1, p_rd=0.1, num_aug=9):
    origin_sentence = ''.join(sentences[0])
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
        flag = len(sentence_rp[0]) == 1  # 只有一个词时
        for words in sentence_rp:
            if flag:
                augmented_sentences.extend(words)
            else:
                n_rp = max(1, int(alpha_rp * len(words)))  # n_rp是要更改的结构数，当不足1个时只改一个
                mask_sentences.append(random_prediction(words, n_rp))
        if flag:
            augmented_sentences.extend(BART_prediction(mask_sentences))  # <mask>预测

    # ri
    if alpha_ri > 0:
        for words in sentence_ri:
            n_ri = max(1, int(alpha_ri * len(words)))
            a_words = random_insertion(words, n_ri)
            augmented_sentences.append(''.join(a_words))

    # rs
    if alpha_rs > 0:
        for words in sentence_rs:
            n_rs = max(1, int(alpha_rs * len(words)))
            a_words = random_swap(words, n_rs)
            augmented_sentences.append(''.join(a_words))

    # rd
    if p_rd > 0:
        for words in sentence_rd:
            a_words = random_deletion(words, p_rd)
            augmented_sentences.append(''.join(a_words))

    augmented_sentences = [get_only_characters(sentence) for sentence in augmented_sentences]
    shuffle(augmented_sentences)

    # 随机从增广的句子中取出num_aug个
    if num_aug >= 1:
        augmented_sentences = augmented_sentences[:num_aug]
    else:
        keep_prob = num_aug / len(augmented_sentences)
        augmented_sentences = [s for s in augmented_sentences if random.uniform(0, 1) < keep_prob]

    augmented_sentences.append(origin_sentence)  # 加入原句一起训练
    return augmented_sentences
