from sklearn.neural_network import MLPClassifier
from DataLoder import *

if __name__ == '__main__':
    data = DataLoder.getDataFromCsv('.', 'BCW.csv')
    dataSet, labelSet, testSet, result = DataLoder.splitXAndY(data)

    clf = MLPClassifier()
    clf.fit(dataSet, labelSet)

    predict = clf.predict(testSet)
    print(predict)
    print(result)
    right = 0
    tot = len(result)
    for i in range(0, tot):
        if result[i] // predict[i] == 1:
            right += 1
    print(right / tot)