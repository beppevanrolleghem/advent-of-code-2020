lines = open("input.txt").read().split("\n")

def checkTrees(xd, yd, lines):
    x = 0
    y = 0
    trees = 0
    ln = len(lines[0])
    while y < len(lines):
        try:
            x += xd
            y += yd
            if y >= len(lines)-1:
                break
            if (len(lines[y]) != ln):
                continue #sometimes there is a line with nothing on. idk why
            if x >= len(lines[y]):
                x = x - len(lines[y])
            if lines[y][x] == "#":
                trees+=1
        except:
            print(x)
            print(y)
            print(len(lines))
            print(lines[y])
    return trees

one = checkTrees(1,1,lines)
two = checkTrees(3,1,lines)
three = checkTrees(5,1,lines)
four = checkTrees(7,1,lines)
five = checkTrees(1,2,lines)

print(one)
print(two)
print(three)
print(four)
print(five)
print(one*two*three*four*five)
