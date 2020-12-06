# doing python again because i want to :^)

lines = open("input.txt").read().split("\n")


#i will use this if i ever need it, for now it's faster to not use it
#scores = []

lastScore = 0


# its binary, time to understand bitshifting



for line in lines:
    if len(line) > 3: #idk i picked 3 just cuz, sometimes python just has empty string after split
        b = int(line.lower().replace("f", "0").replace("b","1").replace("l","0").replace("r","1"), 2)
        row = b >> 3
        col = b & int("0000000111", 2) # idk if you can do this with bitshifting too, this felt kinda cheap
        score = row * 8 + col
        print(score)
        if score > lastScore:
            lastScore = score

print(lastScore)

