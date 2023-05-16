# Datasets Info

## Datasets

| 数据集                                 | 说明     | 论文                                                         | 标签                                                         | 下载                                                         |
| :------------------------------------- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| SST-2<br />Stanford Sentiment Treebank | 情感分析 | Richard Socher, Alex Perelygin, Jean Wu, Jason Chuang, Christopher Manning, Andrew Ng, and Christopher Potts. 2013. Parsing With Compositional Vector Grammars. | 二分类<br />积极-消极<br />0=negative<br /> 1=positive       | [下载](https://nlp.stanford.edu/sentiment/)                  |
| CR<br />Customer Review                | 顾客评论 | Minqing Hu and Bing Liu. 2004. Mining and summarizing customer reviews.<br />Qian Liu, Zhiqiang Gao, Bing Liu, and Yuanlin Zhang. 2015. Automated rule selection for aspect extraction in opinion mining. | 二分类<br />积极-消极<br />0=negative<br /> 1=positive       | [下载](https://www.cs.uic.edu/~liub/FBS/CustomerReviewData.zip) |
| TREC<br />Question Type Dataset        | 问题分类 | Xin Li and Dan Roth. 2002. Learning question classifiers.<br />Hovy, Eduard and Gerber, Laurie and Hermjakob, Ulf and Lin, Chin-Yew and Ravichandran, Deepak. 2001. Toward Semantics-Based Answer Pinpointing. | 六分类<br />0=DESCRIPTION<br />1=ENTITY<br />2=ABBREVIATION<br />3=HUMAN<br />4=LOCATION<br />5=NUMERIC | [下载](https://www.tensorflow.org/datasets/catalog/trec)     |

## Preprocess

raw -①-> origin -②-> experiment

①: clean_xx.py

②: get_train_xx.py

## Structure

以CR数据集为例，其他数据集的文件结构均相同。

```text
│  embedding_glove6B-300d.npz                   # 词向量
│  README.md
│  vocab.pkl                                    # 词表
│  
├─CR                                            # CR数据集
│  ├─experiment                                 # 实验用数据
│  │  │  class.txt                              # 标签类别        
│  │  │  
│  │  ├─backTran                                # 往返翻译训练数据
│  │  │      backTran-train-100.txt             # 数量为100
│  │  │      backTran-train-1472.txt            # 数量为1472
│  │  │      backTran-train-500.txt             # 数量为500
│  │  │      backTran-train.txt                 # 全部训练数据
│  │  │      
│  │  ├─eda-0.1                                 # eda方法训练数据，修改率为0.1
│  │  │      eda-train-0.1.txt                  # 全部训练数据
│  │  │      eda-train-0.1_100_1.txt            # 原始数量为100，对每条文本增广1条
│  │  │      eda-train-0.1_100_16.txt           # 原始数量为100，对每条文本增广16条
│  │  │      eda-train-0.1_100_2.txt            # 原始数量为100，对每条文本增广2条
│  │  │      eda-train-0.1_100_4.txt            # 原始数量为100，对每条文本增广4条
│  │  │      eda-train-0.1_100_8.txt            # 原始数量为100，对每条文本增广8条
│  │  │      eda-train-0.1_1472_1.txt           # 原始数量为1472，对每条文本增广1条
│  │  │      eda-train-0.1_1472_16.txt          # 原始数量为1472，对每条文本增广16条
│  │  │      eda-train-0.1_1472_2.txt           # 原始数量为1472，对每条文本增广2条
│  │  │      eda-train-0.1_1472_4.txt           # 原始数量为1472，对每条文本增广4条
│  │  │      eda-train-0.1_1472_8.txt           # 原始数量为1472，对每条文本增广8条
│  │  │      eda-train-0.1_500_1.txt            # 原始数量为500，对每条文本增广1条
│  │  │      eda-train-0.1_500_16.txt           # 原始数量为500，对每条文本增广16条
│  │  │      eda-train-0.1_500_2.txt            # 原始数量为500，对每条文本增广2条
│  │  │      eda-train-0.1_500_4.txt            # 原始数量为500，对每条文本增广4条
│  │  │      eda-train-0.1_500_8.txt            # 原始数量为500，对每条文本增广8条
│  │  │      
│  │  ├─pwda-0.1                                # PWDA方法训练数据，修改率为0.1
│  │  │      pwda-train-0.1.txt                 # 全部训练数据
│  │  │      pwda-train-0.1_100_1.txt           # 原始数量为100，对每条文本增广1条
│  │  │      pwda-train-0.1_100_16.txt          # 原始数量为100，对每条文本增广16条
│  │  │      pwda-train-0.1_100_2.txt           # 原始数量为100，对每条文本增广2条
│  │  │      pwda-train-0.1_100_4.txt           # 原始数量为100，对每条文本增广4条
│  │  │      pwda-train-0.1_100_8.txt           # 原始数量为100，对每条文本增广8条
│  │  │      pwda-train-0.1_1472_1.txt          # 原始数量为1472，对每条文本增广1条
│  │  │      pwda-train-0.1_1472_16.txt         # 原始数量为1472，对每条文本增广16条
│  │  │      pwda-train-0.1_1472_2.txt          # 原始数量为1472，对每条文本增广2条
│  │  │      pwda-train-0.1_1472_4.txt          # 原始数量为1472，对每条文本增广4条
│  │  │      pwda-train-0.1_1472_8.txt          # 原始数量为1472，对每条文本增广8条
│  │  │      pwda-train-0.1_500_1.txt           # 原始数量为500，对每条文本增广1条
│  │  │      pwda-train-0.1_500_16.txt          # 原始数量为500，对每条文本增广16条
│  │  │      pwda-train-0.1_500_2.txt           # 原始数量为500，对每条文本增广2条
│  │  │      pwda-train-0.1_500_4.txt           # 原始数量为500，对每条文本增广4条
│  │  │      pwda-train-0.1_500_8.txt           # 原始数量为500，对每条文本增广8条
│  │  │      pwda-train-0.1_RD_100_1.txt        # 原始数量为100，使用随机删除操作，对每条文本增广1条
│  │  │      pwda-train-0.1_RD_100_2.txt        # 原始数量为100，使用随机删除操作，对每条文本增广2条
│  │  │      pwda-train-0.1_RD_100_4.txt        # 原始数量为100，使用随机删除操作，对每条文本增广4条
│  │  │      pwda-train-0.1_RD_1472_1.txt       # 原始数量为1472，使用随机删除操作，对每条文本增广1条
│  │  │      pwda-train-0.1_RD_1472_2.txt       # 原始数量为1472，使用随机删除操作，对每条文本增广2条
│  │  │      pwda-train-0.1_RD_1472_4.txt       # 原始数量为1472，使用随机删除操作，对每条文本增广4条
│  │  │      pwda-train-0.1_RD_500_1.txt        # 原始数量为500，使用随机删除操作，对每条文本增广1条
│  │  │      pwda-train-0.1_RD_500_2.txt        # 原始数量为500，使用随机删除操作，对每条文本增广2条
│  │  │      pwda-train-0.1_RD_500_4.txt        # 原始数量为500，使用随机删除操作，对每条文本增广4条
│  │  │      pwda-train-0.1_RI_100_1.txt        # 原始数量为100，使用随机插入操作，对每条文本增广1条
│  │  │      pwda-train-0.1_RI_100_2.txt        # 原始数量为100，使用随机插入操作，对每条文本增广2条
│  │  │      pwda-train-0.1_RI_100_4.txt        # 原始数量为100，使用随机插入操作，对每条文本增广4条
│  │  │      pwda-train-0.1_RI_1472_1.txt       # 原始数量为1472，使用随机插入操作，对每条文本增广1条
│  │  │      pwda-train-0.1_RI_1472_2.txt       # 原始数量为1472，使用随机插入操作，对每条文本增广2条
│  │  │      pwda-train-0.1_RI_1472_4.txt       # 原始数量为1472，使用随机插入操作，对每条文本增广4条
│  │  │      pwda-train-0.1_RI_500_1.txt        # 原始数量为500，使用随机插入操作，对每条文本增广1条
│  │  │      pwda-train-0.1_RI_500_2.txt        # 原始数量为500，使用随机插入操作，对每条文本增广2条
│  │  │      pwda-train-0.1_RI_500_4.txt        # 原始数量为500，使用随机插入操作，对每条文本增广4条
│  │  │      pwda-train-0.1_RP_100_1.txt        # 原始数量为100，使用随机预测操作，对每条文本增广1条
│  │  │      pwda-train-0.1_RP_100_2.txt        # 原始数量为100，使用随机预测操作，对每条文本增广2条
│  │  │      pwda-train-0.1_RP_100_4.txt        # 原始数量为100，使用随机预测操作，对每条文本增广4条
│  │  │      pwda-train-0.1_RP_1472_1.txt       # 原始数量为1472，使用随机预测操作，对每条文本增广1条
│  │  │      pwda-train-0.1_RP_1472_2.txt       # 原始数量为1472，使用随机预测操作，对每条文本增广2条
│  │  │      pwda-train-0.1_RP_1472_4.txt       # 原始数量为1472，使用随机预测操作，对每条文本增广4条
│  │  │      pwda-train-0.1_RP_500_1.txt        # 原始数量为500，使用随机预测操作，对每条文本增广1条
│  │  │      pwda-train-0.1_RP_500_2.txt        # 原始数量为500，使用随机预测操作，对每条文本增广2条
│  │  │      pwda-train-0.1_RP_500_4.txt        # 原始数量为500，使用随机预测操作，对每条文本增广4条
│  │  │      pwda-train-0.1_RS_100_1.txt        # 原始数量为100，使用随机交换操作，对每条文本增广1条
│  │  │      pwda-train-0.1_RS_100_2.txt        # 原始数量为100，使用随机交换操作，对每条文本增广2条
│  │  │      pwda-train-0.1_RS_100_4.txt        # 原始数量为100，使用随机交换操作，对每条文本增广4条
│  │  │      pwda-train-0.1_RS_1472_1.txt       # 原始数量为1472，使用随机交换操作，对每条文本增广1条
│  │  │      pwda-train-0.1_RS_1472_2.txt       # 原始数量为1472，使用随机交换操作，对每条文本增广2条
│  │  │      pwda-train-0.1_RS_1472_4.txt       # 原始数量为1472，使用随机交换操作，对每条文本增广4条
│  │  │      pwda-train-0.1_RS_500_1.txt        # 原始数量为100，使用随机交换操作，对每条文本增广1条
│  │  │      pwda-train-0.1_RS_500_2.txt        # 原始数量为100，使用随机交换操作，对每条文本增广2条
│  │  │      pwda-train-0.1_RS_500_4.txt        # 原始数量为100，使用随机交换操作，对每条文本增广4条
│  │  ├─pwda-0.2                                # PWDA方法数据，修改率为0.2
│  │  │      ...
│  │  ├─pwda-0.3                                # PWDA方法数据，修改率为0.3
│  │  │      ...
│  │  ├─pwda-0.4                                # PWDA方法数据，修改率为0.4
│  │  │      ...
│  │  ├─pwda-0.5                                # PWDA方法数据，修改率为0.5
│  │  │      ...
│  │  │      
│  │  ├─pwda-noLC-0.1                           # 未纠正标签的PWDA方法数据，修改率为0.1
│  │  │      pwda-noLC-train-0.1.txt            # 全部训练数据
│  │  │      pwda-noLC-train-0.1_100_1.txt      # 原始数量为100，对每条文本增广1条
│  │  │      pwda-noLC-train-0.1_100_16.txt     # 原始数量为100，对每条文本增广16条
│  │  │      pwda-noLC-train-0.1_100_2.txt      # 原始数量为100，对每条文本增广2条
│  │  │      pwda-noLC-train-0.1_100_4.txt      # 原始数量为100，对每条文本增广4条
│  │  │      pwda-noLC-train-0.1_100_8.txt      # 原始数量为100，对每条文本增广8条
│  │  │      pwda-noLC-train-0.1_1472_1.txt     # 原始数量为1472，对每条文本增广1条
│  │  │      pwda-noLC-train-0.1_1472_16.txt    # 原始数量为1472，对每条文本增广16条
│  │  │      pwda-noLC-train-0.1_1472_2.txt     # 原始数量为1472，对每条文本增广2条
│  │  │      pwda-noLC-train-0.1_1472_4.txt     # 原始数量为1472，对每条文本增广4条
│  │  │      pwda-noLC-train-0.1_1472_8.txt     # 原始数量为1472，对每条文本增广8条
│  │  │      pwda-noLC-train-0.1_500_1.txt      # 原始数量为500，对每条文本增广1条
│  │  │      pwda-noLC-train-0.1_500_16.txt     # 原始数量为500，对每条文本增广16条
│  │  │      pwda-noLC-train-0.1_500_2.txt      # 原始数量为500，对每条文本增广2条
│  │  │      pwda-noLC-train-0.1_500_4.txt      # 原始数量为500，对每条文本增广4条
│  │  │      pwda-noLC-train-0.1_500_8.txt      # 原始数量为500，对每条文本增广8条
│  │  ├─pwda-noLC-0.2                           # 未纠正标签的PWDA方法数据，修改率为0.2
│  │  │      ...
│  │  ├─pwda-noLC-0.3                           # 未纠正标签的PWDA方法数据，修改率为0.3
│  │  │      ...
│  │  ├─pwda-noLC-0.4                           # 未纠正标签的PWDA方法数据，修改率为0.4
│  │  │      ...
│  │  ├─pwda-noLC-0.5                           # 未纠正标签的PWDA方法数据，修改率为0.5
│  │  │      ...
│  │  ├─test                                    # 测试数据
│  │  │      dev.txt                            # 验证集
│  │  │      test.txt                           # 测试集
│  │  │      textflint-InsertAdv-test.txt       # 对抗测试集，InsertAdv
│  │  │      textflint-Ocr-test.txt             # 对抗测试集，OCR
│  │  └─train                                   # 训练数据
│  │          train-100.txt                     # 数量为100
│  │          train-1472.txt                    # 数量为1472
│  │          train-500.txt                     # 数量为500
│  │          train.txt                         # 全部训练数据
│  ├─origin                                     # 预处理后数据
│  │      negative.txt                          # 标签为negative数据
│  │      positive.txt                          # 标签为positive数据
│  └─raw                                        # 原始数据
│          Canon_G3.txt
│          Computer.txt
│          DVD.txt
│          Nikon_4300.txt
│          Nokia_6610.txt
│          Router.txt
│          Speaker.txt
│          Zen_Xtra.txt
│          
├─SST-2
│  ├─experiment
│  │     ...       
│  ├─origin
│  │     ...
│  └─raw
│        ...   
└─TREC-6
   ├─experiment
   │     ...       
   ├─origin
   │     ...       
   └─raw
         ...
```