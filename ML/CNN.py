from sklearn.neural_network import MLPClassifier
from DataLoder import *

if __name__ == '__main__':
    data = DataLoder.getDataFromCsv('.', 'BCW.csv')
    dataSet, labelSet, testSet, result = DataLoder.splitXAndY(data)

    clf = MLPClassifier()
    clf.fit(dataSet, labelSet)

    print(clf.predict(testSet))
    print(result)