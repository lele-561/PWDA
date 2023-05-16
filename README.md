# PWDA: Phrase-level and Word-level Data Augmentation for Text Classification Tasks

## Introduction

本文针对文本分类任务，研究如何利用数据增广方法来提高文本分类任务中常用模型的泛化性和鲁棒性，提出了一种基于短语级别和词级别的数据增广方法PWDA。该方法将文本划分并重组为短语级和单词级结构组合的不同表示，使用随机预测、随机插入、随机交换和随机删除四种不同的操作分别处理结构不同的表示得到增广数据，并根据原数据训练一个分类器，重新判断增广数据的标签，从而实现增广数据的自动化生成。生成的多样性数据可以有效提升模型的泛化性，此外，PWDA的四种操作能向数据中有效引入噪声，以模拟文本分类模型在实际应用中可能遇到的干扰，例如对抗性文本等。通过学习这些噪声和干扰信息，模型可以在应对新数据和不同的场景时具有更好的鲁棒性。

## Usage

### Environment

| 配置           | 说明        |
| -------------- | ----------- |
| Python         | 3.8         |
| PyTorch        | 1.8.1+cu101 |
| spaCy          | 3.5.0       |
| transformers   | 4.26.1      |
| benepar        | 0.2.0       |
| en_core_web_md | 3.5.0       |
| TextFlint      | 0.1.0       |

#### Install

**Berkeley Neural Parser**

在线使用：https://parser.kitaev.io/

Github：https://github.com/nikitakit/self-attentive-parser#available-models

简单代码示例：https://spacy.io/universe/project/self-attentive-parser

- 下载benepar和模型

  下载benepar：

  ```shell
  pip install benepar
  ```

  下载模型，这里下载`benepar_en3`英文模型：

  ```python
  import benepar
  benepar.download('benepar_en3')		# 英文
  nlp = spacy.load('zh_core_web_sm')  # 中文
  ```

  如果太卡，直接从官方github：https://github.com/nikitakit/self-attentive-parser/releases
  下载对应模型，解压后放在下载的文件夹`C:\Users\lele\AppData\Roaming\nltk_data\models`
  下即可（路径会显示）


- 下载spacy和模型

  教程参见：https://blog.csdn.net/qq_45520647/article/details/123536812

  下载spacy：

  ```shell
  pip install -U spacy -i https://pypi.tuna.tsinghua.edu.cn/simple
  ```

  安装模型：和spcay版本对应，这里是3.5版本，从官方github：https://github.com/explosion/spacy-models/releases 中选择模型提前下载到本地，否则会失败

  ```shell
  # 英文
  pip install D:\SpacyModels\en_core_web_md-3.5.0.tar.gz -i https://pypi.tuna.tsinghua.edu.cn/simple/
  # 中文
  pip install D:\SpacyModels\zh_core_web_trf-3.5.0.tar.gz -i https://pypi.tuna.tsinghua.edu.cn/simple/
  ```

**TextFlint**

```shell
pip install textflint
```

参见官方主页：https://github.com/textflint/textflint

### Run PWDA

#### Step 0

将数据处理为如下形式txt文件

```
内容 + tab + label
there is no way the battery supplied lasts hours	0
```

#### Step 1

在`code/pwda-en/augment.py`中38~40行设置数据集、增广句子数、修改率以及输入输出文件名，运行`augment.py`，得到未纠正标签的数据`pwda-noLC-xx.txt`

```Python
dataset = 'SST-2'  # 英文数据集
num_aug = 16  # 增广句子数
alphas = [0.1, 0.2, 0.3, 0.4, 0.5]  # 修改率
```

#### Step 2

如果需要得到纠正标签的数据，在`code/pwda-en/repredict_label.py`中106~107行设置数据集、修改率以及输入输出文件名，运行`repredict_label.py`
，得到纠正标签的最终数据`pwda-xx.txt`

```Python
dataset = 'SST-2'  # 英文数据集
alpha = 0.5  # 修改率
```

## Experiments

数据集及预处理详细信息参看data目录下[README](data/README.md)

### TextCNN

在```experiment/TextCNN/run.py```中9~11行设置数据集等参数，使用不同数据对模型进行训练

```Python
datasets = ['SST-2', 'CR', 'TREC-6']  # 数据集
aug_nums = [1, 2, 4, 8, 16]  # 增广句子数
alphas = [0.1, 0.2, 0.3, 0.4, 0.5]  # 修改率
```

### RoBERTa & XLNet

由于算力问题，RoBERTa和XLNet模型实验均在Goggle Colab上进行，将`experiment/XLNet/XLNet_2.ipynb`和`experiment/RoBERTa/RoBERTa_6.ipynb`
两个文件直接上传至Colab，修改数据集等参数，直接运行即可执行实验

## Structure

项目整体结构如下：

```text
│  README.md
│          
├─code                            # 算法代码
│  ├─backTran                     # 对照方法：往返翻译
│  │      back_translation.py
│  ├─eda                          # 对照方法：eda
│  │      augment.py
│  │      eda.py
│  ├─pwda-en                      # PWDA方法，处理英文数据集
│  │      augment.py
│  │      pwda.py
│  │      repredict_label.py
│  │      split_phrase.py
│  └─pwda-zh                      # PWDA方法，处理中文数据集
│      │  augment.py
│      │  pwda.py
│      │  split_phrase.py
│      └─stopwords                # 停用词表
│              baidu_stopwords.txt
│              cn_stopwords.txt
│              hit_stopwords.txt
│              scu_stopwords.txt
│              
├─data                            # 数据
│  │  embedding_glove6B-300d.npz  # TextCNN词向量
│  │  README.md
│  │  vocab.pkl                   # 词表
│  │  
│  ├─CR                           # CR数据集
│  │  ├─experiment                # 实验用数据
│  │  │  │  class.txt             # 标签类别
│  │  │  ├─backTran               # 往返翻译数据
│  │  │  │      ...
│  │  │  ├─eda-0.1                # eda方法数据
│  │  │  │      ...     
│  │  │  ├─pwda-0.1               # PWDA方法数据
│  │  │  │      ...
│  │  │  ├─pwda-0.2
│  │  │  │      ...
│  │  │  ├─pwda-0.3
│  │  │  │      ...
│  │  │  ├─pwda-0.4
│  │  │  │      ...
│  │  │  ├─pwda-0.5
│  │  │  │      ...
│  │  │  ├─pwda-noLC-0.1          # PWDA方法数据，未纠正标签
│  │  │  │      ...
│  │  │  ├─pwda-noLC-0.2
│  │  │  │      ...
│  │  │  ├─pwda-noLC-0.3
│  │  │  │      ...
│  │  │  ├─pwda-noLC-0.4
│  │  │  │      ...
│  │  │  ├─pwda-noLC-0.5
│  │  │  │      ...
│  │  │  ├─test                   # 测试数据
│  │  │  │      ...
│  │  │  └─train                  # 训练数据
│  │  │         ...
│  │  ├─origin                    # 预处理后数据
│  │  │         ...
│  │  └─raw                       # 原始数据
│  │            ...
│  ├─SST-2
│  │  ├─experiment
│  │  │     ...
│  │  ├─origin
│  │  │     ...
│  │  └─raw
│  │        ...
│  └─TREC-6
│      ...
│              
├─experiment                      # 实验代码
│  ├─preprocess_dataset           # 数据预处理
│  │      clean_CR.py
│  │      clean_SST-2.py
│  │      clean_TREC-6.py
│  │      get_train_dev_test.py
│  │      get_train_set_2.py
│  │      get_train_set_mul.py
│  │      utils.py
│  ├─RoBERTa                      # RoBERTa实验
│  │      RoBERTa_6.ipynb
│  ├─TextCNN                      # TextCNN实验
│  │      run.py
│  │      TextCNN.py
│  │      train_eval.py
│  │      utils.py
│  └─XLNet                        # XLNet实验
│          XLNet_2.ipynb
│          
└─figure                          # 画图代码
        ablation_4_operations.py
        allDatasets_statistics.py
        correct_label.py
        numAug_alpha.py
        robust_ocr_insertAdv.py
```