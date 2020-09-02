stage = open("RetentionRate.txt", "r", encoding="utf8")
empty = []
emptyDict = {}
visits = []
god = {}
j = 0
for line in stage:
    empty.extend(line.split())
empty1 = empty[0::3]  # id
empty2 = empty[1::3]  # dates
for i in empty1:
    emptyDict[i] = emptyDict.get(i, 0) + 1  # numbers of meetings
for i in empty1:    # unique ID's with 2+ visits
    if empty1.count(i) >= 2:
        visits.append(i)
visits = set(visits)
answer = len(visits) / len(set(empty1))
print(answer)
