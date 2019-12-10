import pandas, argparse
from sklearn.model_selection import KFold, train_test_split

def main1():
    parser = argparse.ArgumentParser(description='Train Hyperbolic Embeddings')
    parser.add_argument('-dset', type=str, required=True,
                        help='Dataset identifier')
    parser.add_argument('-out', type=str, required=True,
                        help='out path')
    opt = parser.parse_args()

    df = pandas.read_csv(opt.dset, usecols=['id1', 'id2', 'weight'], engine='c')
    idx = KFold(n_splits = 5, shuffle = True).split(df) #5-way split

    count = 0

    train_csv = "resources/" + opt.out + "/train_{}.csv"

    test_csv = "resources/" + opt.out + "/test_{}.csv"

    for train_index, test_index in idx:
        df.iloc[train_index].to_csv(train_csv.format(count), index=False)
        df.iloc[test_index].to_csv(test_csv.format(count), index=False)
        count += 1

def main():
    parser = argparse.ArgumentParser(description='Train Hyperbolic Embeddings')
    parser.add_argument('-dset', type=str, required=True,
                        help='Dataset identifier')
    parser.add_argument('-out', type=str, required=True,
                        help='out path')
    opt = parser.parse_args()

    df = pandas.read_csv(opt.dset, usecols=['id1', 'id2', 'weight'], engine='c')

    for split in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]:
        X_train, X_test = train_test_split(df, test_size = split, random_state = 42)

        train_csv = "resources/" + opt.out + "/train_{}.csv"
        test_csv = "resources/" + opt.out + "/test_{}.csv"

        X_train.to_csv(train_csv.format(split*100), index=False)
        X_test.to_csv(test_csv.format(split*100), index=False)

if __name__ == '__main__':
    main()
