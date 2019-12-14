from sklearn import svm
from DataLoder import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = DataLoder.getDataFromCsv('.', 'BCW.csv')
    dataSet, labelSet, testSet, result = DataLoder.splitXAndY(data)

    clf = svm.SVC()
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
