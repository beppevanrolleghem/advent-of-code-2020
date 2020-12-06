# python again :^P
import string


groups = []
lines = open("input.txt").read().split("\n")
groupIndex = 0
personIndex = 0

tline = ""

for line in lines:
    tline += line
    if len(line) == 0:
        groups.append(tline)
        tline = ""

groups.append(tline)

def scoreGroup(group):
    gscore = 0
    qs = "abcdefghijklmnopqrstuvwxyz"
    for char in qs:
        if char in group:
            gscore += 1
    return gscore

score = 0
for group in groups:
    score += scoreGroup(group)

print(score)
