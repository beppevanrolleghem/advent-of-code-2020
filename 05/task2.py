# doing python again because i want to :^)
# i dont know why some others show up. it's something to do with binary i just dont understand
#
#
lines = open("input.txt").read().split("\n")


#i will use this if i ever need it, for now it's faster to not use it
#scores = []

lastScore = 0


# its binary, time to understand bitshifting
l = {}


for line in lines:
    if len(line) > 3: #idk i picked 3 just cuz, sometimes python just has empty string after split
        b = int(line.lower().replace("f", "0").replace("b","1").replace("l","0").replace("r","1"), 2)
        if "{0:b}".format(b)[:7] == "0000000" or "{0:b}".format(b)[:7] == "1111111":
            #print("{0:b}".format(b))
            print("first-line")
        else:
            row = b >> 3
            col = b & int("0000000111",2)
            score = row * 8 + col
            l[score] = {"line": line, "row": row, "col":col, "score":score}
            #print("{0:b}".format(b))
#        row = b >> 3
#        col = b & int("0000000111", 2) # idk if you can do this with bitshifting too, this felt kinda cheap
#        score = row * 8 + col
#        print(score)
#        if score > lastScore:
#            lastScore = score

#print(l.keys())
lastk = l.keys()[0]
print(lastk)
for k in l.keys():
    #print("started loop for " + str(k))
    if k == lastk:
        continue
    elif k -1 == lastk:
        lastk = k
    else:
        print(k)
        print(lastk)
        print(l[k])
        print(l[lastk])
        lastk = k
