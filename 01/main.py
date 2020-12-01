lines = open("input.txt", "r").read().split("\n")



# number, array, offset, target
def checkIfCanAdd(num, arr, trg):
    for num2 in arr:
        try:
            num2 = int(num2)
            if num + num2 < trg: 
                for num3 in arr:
                    try:
                        num3 = int(num3)
                    except:
                        continue
                    if num3 + num2 + num == 2020:
                        return num3 * num2 * num
        except:
            continue
    return False


def mainLoop():
    for i, line in enumerate(lines, start=0):
        try:
            num = int(line)
        except:
            continue
        if num > 2020:
            continue
#        print(len(lines[i:]))
        num = checkIfCanAdd(num, lines, 2020)
        if num != False:
            return num

    return "nothing found"

print(mainLoop())
        
    
