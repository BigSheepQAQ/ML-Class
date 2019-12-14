from sklearn import svm
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as ply
from DataLoder import *

if __name__ == '__main__':
    data = DataLoder.getDataFromCsv('/Users/bigsheep/github/ML-Class', 'wine.csv')
    dataSet, labelSet, testSet, result = DataLoder.splitXAndY(data)

    clf = svm.SVC()
    clf.fit(dataSet, labelSet)
    predict = clf.predict(testSet)

    print(predict)
    print(result)

    tot = len(result)
    f11 = f12 = f13 = f21 = f22 = f23 = f31 = f32 = f33 = 0

    for i in range(0, tot):
        if result[i] == 1 and predict[i] == 1:
            f11 += 1
        if result[i] == 1 and predict[i] == 2:
            f12 += 1
        if result[i] == 1 and predict[i] == 3:
            f13 += 1

        if result[i] == 2 and predict[i] == 1:
            f21 += 1
        if result[i] == 2 and predict[i] == 2:
            f22 += 1
        if result[i] == 2 and predict[i] == 3:
            f23 += 1

        if result[i] == 3 and predict[i] == 1:
            f31 += 1
        if result[i] == 3 and predict[i] == 2:
            f32 += 1
        if result[i] == 3 and predict[i] == 3:
            f33 += 1

    print((f11 + f22 + f33) / tot)  # 预测正确
    print((tot - f11 - f22 - f33) / tot)  # 预测错误
    print()

    print(f11 / tot)
    print(f12 / tot)
    print(f13 / tot)
    print()

    print(f21 / tot)
    print(f22 / tot)
    print(f23 / tot)
    print()

    print(f31 / tot)
    print(f32 / tot)
    print(f33 / tot)
    print()

    fpr, tpr, thresholds = roc_curve(predict, result, pos_label=3)
    auc = auc(fpr, tpr)
    print(auc)

    ply.plot(fpr, tpr)
    x = [0.0, 1.0]
    y = x
    ply.plot(x, y)
    ply.show()