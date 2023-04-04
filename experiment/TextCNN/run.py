# coding: UTF-8
import time

from TextCNN import *
from train_eval import train, init_network
from utils import build_dataset, build_iterator, get_time_dif

if __name__ == '__main__':
    datasets = ['SST-2', 'CR', 'TREC-6']  # 数据集
    aug_nums = [1, 2, 4, 8, 16]  # 增广句子数
    alphas = [0.1, 0.2, 0.3, 0.4, 0.5]  # 修改率
    all_nums = []
    # 总数据量
    for dataset in datasets:
        if dataset == 'CR':
            all_nums = [100, 500, 1472]
        elif dataset == 'SST-2':
            all_nums = [100, 500, 2000, 5484]
        elif dataset == 'TREC-6':
            all_nums = [100, 500, 2000, 3569]
        for alpha in alphas:
            for all_num in all_nums:
                for aug_num in aug_nums:
                    train_path = 'pwda-' + str(alpha) + '/pwda-train-' + str(alpha) + '_' + str(all_num) + '_' + str(
                        aug_num)

                    embedding = 'embedding_glove6B-300d.npz'  # 词向量
                    model_name = 'TextCNN'

                    config = Config(dataset, embedding, train_path)
                    np.random.seed(1)
                    torch.manual_seed(1)
                    torch.cuda.manual_seed_all(1)
                    torch.backends.cudnn.deterministic = True  # 保证每次结果一样

                    start_time = time.time()
                    print("Loading experiment...")
                    vocab, train_data, dev_data, test_data = build_dataset(config, True)  # True为word，False为char
                    train_iter = build_iterator(train_data, config)
                    dev_iter = build_iterator(dev_data, config)
                    test_iter = build_iterator(test_data, config)
                    time_dif = get_time_dif(start_time)
                    print("Time usage:", time_dif)

                    # train
                    config.n_vocab = len(vocab)
                    model = Model(config).to(config.device)
                    init_network(model)
                    print(model.parameters)
                    train(config, model, train_iter, dev_iter, test_iter)
