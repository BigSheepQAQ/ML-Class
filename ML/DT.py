from sklearn import tree
from DataLoder import *

if __name__ == '__main__':
    data = DataLoder.getDataFromCsv('.', 'BCW.csv')
    dataSet, labelSet,testSet,result = DataLoder.splitXAndY(data)

    clf = tree.DecisionTreeClassifier()
    clf.fit(dataSet, labelSet)

    print(clf.predict(testSet))
    print(result)