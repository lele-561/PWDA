# 说明：以不同粒度分割句子的各结构，短语级标签为NP, VP, ADVP, ADJP, PP, DP；词级标签为WORD
from itertools import product

import benepar
import spacy

# 引入benepar分析器
nlp = spacy.load('zh_core_web_sm')  # 中文
if spacy.__version__.startswith('2'):
    nlp.add_pipe(benepar.BeneparComponent("benepar_zh2"))
else:  # 走这个
    nlp.add_pipe("benepar", config={"model": "benepar_zh2"})  # 中文


# sent._.parse_string: 语法结构
# sent._.labels: 该语法结构的Tag
# list(sent._.children): 该语法结构的子结构，子结构和父结构类型相同
# sent.text是其内容，为string类型

# 获取不同粒度的结构
def get_structures(sent):
    res_list = []
    if len(list(sent._.children)) == 0:  # 只有一个单词时
        res_list = [[("WORD", sent.text)]]
    else:  # 有多个单词时
        tag = sent._.labels[0]
        subsent_list = []
        for subsent in list(sent._.children):
            subsent_list.append(get_structures(subsent))  # 得到不同的子句结构列表
        cartesian_product = list(product(*subsent_list))  # 子列表内容做笛卡尔积
        for _ in cartesian_product:  # 去除列表外框，统一成tuple结构
            tmp_list = []
            for __ in list(_):
                tmp_list.extend(__)
            res_list.append(tmp_list)
        res_list.append([(tag, sent.text)])
    return res_list


def split_to_phrase(sentence):
    # 基本处理
    doc = nlp(sentence)
    all_res = []
    res = []
    for sent in list(doc.sents):
        sent_res = get_structures(sent)  # 所有划分好的句子
        # 按需处理
        # 去除从句级结构（Tag为S, SBAR, SBARQ, SINV, SQ）的句子和超长短语级结构（超过5个词）
        sent_tag = {"S", "SBAR", "SBARQ", "SINV", "SQ"}
        tmp_res = []
        max_phrase_len = 5
        for _ in sent_res:
            flag = False  # 判断该句是否需要被去除
            noTag_sent = []
            if len(sent_res) == 1:  # 如果只有一个单词
                noTag_sent.append(_[0][1])
            else:
                for __ in _:
                    # 从所有划分好结构的句子中去除从句级结构 or 超过10个词的短语 or 只有一个结构的短语
                    if __[0] in sent_tag or len(__[1]) > max_phrase_len or len(_) == 1:
                        flag = True
                        break
                    noTag_sent.append(__[1])  # 剥离Tag
            if flag:  # 需要被去除
                continue
            tmp_res.append(noTag_sent)
        all_res.append(tmp_res)
    cartesian_product = list(product(*all_res))  # 子列表内容做笛卡尔积，此处针对一条文本中有多句话的情况
    for _ in cartesian_product:  # 每个tuple
        tmp_res = []
        for __ in _:  # tuple内每个列表
            tmp_res.extend(__)
        res.append(tmp_res)
    return res
