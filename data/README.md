# 数据集

| 数据集                                 | 说明     | 论文                                                         | 标签                                                         | 下载                                                         |
| :------------------------------------- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| SST-2<br />Stanford Sentiment Treebank | 情感分析 | Richard Socher, Alex Perelygin, Jean Wu, Jason Chuang, Christopher Manning, Andrew Ng, and Christopher Potts. 2013. Parsing With Compositional Vector Grammars. | 二分类<br />积极-消极<br />0=negative<br /> 1=positive       | [下载](https://nlp.stanford.edu/sentiment/)                  |
| CR<br />Customer Review                | 顾客评论 | Minqing Hu and Bing Liu. 2004. Mining and summarizing customer reviews.<br />Qian Liu, Zhiqiang Gao, Bing Liu, and Yuanlin Zhang. 2015. Automated rule selection for aspect extraction in opinion mining. | 二分类<br />积极-消极<br />0=negative<br /> 1=positive       | [下载](https://www.cs.uic.edu/~liub/FBS/CustomerReviewData.zip) |
| TREC<br />Question Type Dataset        | 问题分类 | Xin Li and Dan Roth. 2002. Learning question classifiers.<br />Hovy, Eduard and Gerber, Laurie and Hermjakob, Ulf and Lin, Chin-Yew and Ravichandran, Deepak. 2001. Toward Semantics-Based Answer Pinpointing. | 六分类<br />0=DESCRIPTION<br />1=ENTITY<br />2=ABBREVIATION<br />3=HUMAN<br />4=LOCATION<br />5=NUMERIC | [下载](https://www.tensorflow.org/datasets/catalog/trec)     |

# 文件结构

| 文件夹名称                | 说明                                                         |
| ------------------------- | ------------------------------------------------------------ |
| raw                       | 未处理的原数据                                               |
| origin                    | raw -> origin：经过clean处理后由\[label sentence\]组成的数据 |
| experiment                | origin -> experiment：实验用数据                 |
