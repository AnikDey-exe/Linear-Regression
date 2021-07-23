import csv
import random
import plotly_express as px
import pandas as pd
import statistics as st
import numpy as np

# df = pd.read_csv("heightweight.csv")
# heightList = df["Height"].to_list()
# weightList = df["Weight"].to_list()

df2 = pd.read_csv("school.csv")
greList = df2["TOEFL Score"].to_list()
chanceList = df2["ChanceofAdmit "].to_list()

# heightArray = np.array(heightList)
# weightArray = np.array(weightList)

greArray = np.array(greList)
chanceArray = np.array(chanceList)

# b, a = np.polyfit(heightArray, weightArray, 1)
b2, a2 = np.polyfit(greArray, chanceArray, 1)

# with open("heightweight.csv", newline='') as f:
#     reader = csv.reader(f)
#     data = list(reader)

# a = 0
# b = 1

y = []

y2 = []

# for x in heightArray:
#     y_value = b*x + a
#     y.append(y_value)

for x in greArray:
    y2_value = b2*x + a2
    y2.append(y2_value)

x2 = float(input("TOEFL Score: "))
y3_value = b2*x2 + a2
print(f"Chance of Admission With Score of {x2} is {y3_value * 100}%")

# fig = px.scatter(df, x = heightArray, y = weightArray, title = "Height and Weight")
# fig.update_layout(shapes = [
#     dict(
#         type = 'line',
#         y0 = min(weightArray),
#         y1 = max(weightArray),
#         x0 = min(heightArray),
#         x1 = max(heightArray)
#     )
#                                                                                                                                                                                                                                                                 ]
# )

# fig.show()

fig2 = px.scatter(df2, x = greArray, y = chanceArray, title = "TOEFL Score and Chances of Admission")
fig2.update_layout(shapes = [
    dict(
        type = 'line',
        y0 = min(y2),
        y1 = max(y2),
        x0 = min(greArray),
        x1 = max(greArray)
    )
])

fig2.show()
