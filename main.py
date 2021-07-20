import plotly.express as exp
import csv


with open("2.csv") as tv:
    data = csv.DictReader(tv)

    sc = exp.scatter(data,x="Size of TV",y="\tAverage time spent watching TV in a week (hours)")

    sc.show()

