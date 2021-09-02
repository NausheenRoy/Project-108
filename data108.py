import csv
import plotly.express as px
import pandas as pd
import plotly.figure_factory as pff

df = pd.read_csv("C:\\Users\\TRUSTANA MARKETING\\OneDrive\\Desktop\\Whitehat jr\\Python_Class\\project108.csv")
fig = pff.create_distplot([df["Avg Rating"].tolist()],["Rating"], show_hist=False)
fig.show()