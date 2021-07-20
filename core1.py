import csv
import numpy as np
from numpy.lib.function_base import corrcoef

def getDataSource(dataPath):
    size = []

    ats = []

    with open(dataPath) as file:
        frame = csv.DictReader(file)

        for r in frame:
            size.append(float(r["Marks In Percentage"]))
            ats.append(float(r["Days Present"]))




    return {
        "x":size,
        "y":ats
    }


def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])

    print(correlation[0] , " " , correlation[1])

def setup():
    dataPath = "./3.csv"

    dataSource = getDataSource(dataPath)

    findCorrelation(dataSource)

setup()
