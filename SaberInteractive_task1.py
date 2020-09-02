import plotly.express as px

stage = open("FirstEnter.txt", "r", encoding="utf8")
empty = []
emptyDict = {}
for line in stage:
    empty.extend(line.split())
empty = empty[1::3]
print(len(empty))  # all
for i in empty:
    emptyDict[i] = emptyDict.get(i, 0) + 1  # numbers of meetings
print(emptyDict)


data = dict(
    number=[1192, 554, 269, 158, 90, 28, 28, 27, 22, 16],
    stage=["All users", "Stage 8", "Stage 0", "Stage 1",
           "Stage 6", "Stage 2", "Stage 4", "Stage 3", "Stage 7", "Stage 5"])
fig = px.funnel(data, x='number', y='stage')
fig.show()
