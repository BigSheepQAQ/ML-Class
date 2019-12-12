from sklearn import svm
from DataLoder import *

if __name__ == '__main__':
    data = DataLoder.getDataFromCsv('.', 'BCW.csv')
    dataSet, labelSet, testSet, result = DataLoder.splitXAndY(data)

    clf = svm.SVC()
    clf.fit(dataSet,labelSet)

    print(clf.predict(testSet))
    print(result)