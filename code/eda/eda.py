'''EDA方法'''
# Easy data augmentation techniques for text classification
# Jason Wei and Kai Zou

import random
from random import shuffle

random.seed(1)

# stop words list
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

# cleaning up text
import re


def get_only_chars(line):
    clean_line = ""

    line = line.replace("’", "")
    line = line.replace("'", "")
    line = line.replace("-", " ")  # replace hyphens with spaces
    line = line.replace('\t', " ")
    line = line.replace("\n", " ")
    line = line.lower()

    for char in line:
        if char in 'qwertyuiopasdfghjklzxcvbnm ':
            clean_line += char
        else:
            clean_line += ' '

    clean_line = re.sub(' +', ' ', clean_line)  # delete extra spaces
    if clean_line[0] == ' ':
        clean_line = clean_line[1:]
    return clean_line


########################################################################
# Synonym replacement 同义词替换，从近义词表中随机替换句子中的n个词
# Replace n words in the sentence with synonyms from wordnet
########################################################################

# for the first time you use wordnet
# import nltk
# nltk.download('wordnet')
from nltk.corpus import wordnet


# params: words句子单词列表; n要替换的单词数:
def synonym_replacement(words, n):
    new_words = words.copy()
    # 取出所有非停用词
    random_word_list = list(set([word for word in words if word not in stop_words]))
    # 将所有非停用词随机排列
    random.shuffle(random_word_list)
    num_replaced = 0
    # 对随机非停用词中的每个词选出一个同义词
    for random_word in random_word_list:
        synonyms = get_synonyms(random_word)  # 选出的一组同义词
        if len(synonyms) >= 1:  # 如果同义词不止一个
            synonym = random.choice(list(synonyms))  # 随机选择一个同义词
            # 下面这个简写是把为真的结果提前了，实际为
            # for word in new_words:
            #   if word == random_word: synonym
            #   else: word
            new_words = [synonym if word == random_word else word for word in new_words]
            # print("replaced", random_word, "with", synonym)
            num_replaced += 1
        if num_replaced >= n:  # only replace up to n words
            break

    # this is stupid but we need it, trust me
    sentence = ' '.join(new_words)
    new_words = sentence.split(' ')

    return new_words


# 获取同义词
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        # syn.lemmas()是一堆列表的集合，形如[[Lemma('strong.a.01.strong')], ...]
        # l是其中的一个列表，形如Lemma('strong.a.01.strong')
        # l.name是这个单词，如strong
        for l in syn.lemmas():
            # 这步是因为同义词有的是短语，是由几个词用_或-连起来的，要把这些去掉
            synonym = l.name().replace("_", " ").replace("-", " ").lower()
            # 这步没整明白，可能存在非26个字母的字符？？
            synonym = "".join([char for char in synonym if char in ' qwertyuiopasdfghjklzxcvbnm'])
            synonyms.add(synonym)
    if word in synonyms:  # 如果同义词找到本身了，就去掉
        synonyms.remove(word)
    return list(synonyms)


########################################################################
# Random deletion 随机删除：句子里的每个词都有p的概率被删除
# Randomly delete words from the sentence with probability p
########################################################################
def random_deletion(words, p):
    # obviously, if there's only one word, don't delete it 剩一个词了不删
    if len(words) == 1:
        return words

    # randomly delete words with probability p
    new_words = []
    for word in words:
        r = random.uniform(0, 1)  # 随机下看删不删
        if r > p:
            new_words.append(word)

    # if you end up deleting all words, just return a random word
    # 要是都删没了就随机填回来一个词
    if len(new_words) == 0:
        rand_int = random.randint(0, len(words) - 1)
        return [words[rand_int]]

    return new_words


########################################################################
# Random swap 随机交换：随机交换句子中的2个词n次
# Randomly swap two words in the sentence n times
########################################################################

def random_swap(words, n):
    new_words = words.copy()
    # 交换n次，每次选择两个不同的词
    for _ in range(n):
        new_words = swap_word(new_words)
    return new_words


def swap_word(new_words):
    random_idx_1 = random.randint(0, len(new_words) - 1)
    random_idx_2 = random_idx_1
    counter = 0
    while random_idx_2 == random_idx_1:
        random_idx_2 = random.randint(0, len(new_words) - 1)
        counter += 1
        if counter > 3:  # 这里设置counter是？如果二者一直随机到相等呢？
            return new_words
    # 交换二者位置
    new_words[random_idx_1], new_words[random_idx_2] = new_words[random_idx_2], new_words[random_idx_1]
    return new_words


########################################################################
# Random insertion 随机插入：随机将n个单词插入句子
# Randomly insert n words into the sentence
########################################################################

def random_insertion(words, n):
    new_words = words.copy()
    # 插入n次
    for _ in range(n):
        add_word(new_words)
    return new_words


def add_word(new_words):
    synonyms = []
    counter = 0
    # 随机找出一个单词的一组同义词，循环n次
    while len(synonyms) < 1:
        random_word = new_words[random.randint(0, len(new_words) - 1)]
        synonyms = get_synonyms(random_word)  # 找出一组同义词
        counter += 1
        if counter >= 10:  # 循环的目的是一直找同义词，要是一个句子中的每个词都一直找不到同义词且达到循环次数就退出
            return
    random_synonym = synonyms[0]  # 随机取一个同义词第一个插入到随机位置
    random_idx = random.randint(0, len(new_words) - 1)
    new_words.insert(random_idx, random_synonym)  # 这是指针？？不用返回值的？？


########################################################################
# main data augmentation function
########################################################################

def eda(sentence, alpha_sr, alpha_ri, alpha_rs, p_rd, num_aug):
    sentence = get_only_chars(sentence)
    words = sentence.split(' ')
    words = [word for word in words if word != '']
    num_words = len(words)

    augmented_sentences = []
    num_new_per_technique = int(num_aug / 4) + 1  # 每种方法增加句子的个数，均相同

    # sr
    if alpha_sr > 0:
        n_sr = max(1, int(alpha_sr * num_words))  # n_sr是要更改的单词数，当不足1个时只改一个
        for _ in range(num_new_per_technique):
            a_words = synonym_replacement(words, n_sr)
            augmented_sentences.append(' '.join(a_words))

    # ri
    if alpha_ri > 0:
        n_ri = max(1, int(alpha_ri * num_words))
        for _ in range(num_new_per_technique):
            a_words = random_insertion(words, n_ri)
            augmented_sentences.append(' '.join(a_words))

    # rs
    if alpha_rs > 0:
        n_rs = max(1, int(alpha_rs * num_words))
        for _ in range(num_new_per_technique):
            a_words = random_swap(words, n_rs)
            augmented_sentences.append(' '.join(a_words))

    # rd
    if p_rd > 0:
        for _ in range(num_new_per_technique):
            a_words = random_deletion(words, p_rd)
            augmented_sentences.append(' '.join(a_words))

    augmented_sentences = [get_only_chars(sentence) for sentence in augmented_sentences]
    shuffle(augmented_sentences)

    # trim so that we have the desired number of augmented sentences
    # 随机从增广的句子中取出之前定好的num_aug个
    if num_aug >= 1:
        augmented_sentences = augmented_sentences[:num_aug]
    else:
        keep_prob = num_aug / len(augmented_sentences)
        augmented_sentences = [s for s in augmented_sentences if random.uniform(0, 1) < keep_prob]

    # append the original sentence
    augmented_sentences.append(sentence)

    return augmented_sentences
