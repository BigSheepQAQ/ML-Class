import csv
import copy


class DataLoder:
    @staticmethod
    def getDataFromCsv(path: str, fileName: str):
        with open(path + '/' + fileName) as csvfile:
            csvReader = csv.reader(csvfile)

            dataSet = []
            for row in csvReader:
                dataSet.append(row)

            dataSet = dataSet[1:]
            DataLoder.strToFloat(dataSet)

            return dataSet

    @staticmethod
    def splitXAndY(dataSet: list):
        XIndex = len(dataSet) - 1
        YIndex = len(dataSet[0]) - 1

        X, Y, Z, result = [], [], [], []
        # 通过修改系数达到修改分配比例
        for i in range(0, XIndex // 10):
            temp = copy.deepcopy(dataSet[i])
            result.append(temp[YIndex])
            del temp[YIndex]
            Z.append(temp)
            del dataSet[i]
        for datum in dataSet:
            Y.append(datum[YIndex])
            del datum[YIndex]
            X.append(datum)

        return X, Y, Z, result

    @staticmethod
    def strToFloat(dataSet: list):
        N, M = len(dataSet), len(dataSet[0])
        for i in range(0, N):
            for j in range(0, M):
                dataSet[i][j] = float(dataSet[i][j])
