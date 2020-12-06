# python again :^P
import string


groups = []
lines = open("input.txt").read().split("\n")
groupIndex = 0
personIndex = 0

tline = ""

tObject = {}
tIndex = 0


for line in lines:
    if len(line) == 0:
        if len(tObject.keys()) > 0:
            groups.append(tObject)
        tObject = {}
        tIndex = 0
        continue
    tObject[tIndex] = line
    tIndex += 1

       
#print(groups)

groups.append(tline)

def scoreGroup(group):
    gscore = 0
    qs = "abcdefghijklmnopqrstuvwxyz"
    if isinstance(group, str):
        #print("this one is a str for some reason, so score 0")
        return gscore
    
    for char in qs:
        valid = True
        for key in group.keys():
            if char not in group[key]:
                valid = False
        if valid:
            gscore += 1
    return gscore

score = 0
for group in groups:
    score += scoreGroup(group)

print(score)
