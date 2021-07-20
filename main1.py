import plotly.express as exp
import csv


with open("3.csv") as tv:
    data = csv.DictReader(tv)

    sc = exp.scatter(data,x="Days Present",y="Marks In Percentage")

    sc.show()

