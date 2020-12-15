lines = open("input.txt").read().split("\n")

bagTypes = {}


# basically "depluralizes"
def checkName(string):
    if string[-1] == "s":
        return string[:-1]
    else:
        return string


for line in lines:
    if (len(line) == 0): 
        continue
    lineParts = line.split(" ")
    bagName = checkName(lineParts[0] + " " + lineParts[1] + " " + lineParts[2])
    bagContents = " ".join(lineParts[lineParts.index("contain")+1:]).replace(".","").split(", ")
    bagObj = {}
    for bagContent in bagContents:
        if (bagContent == "no other bags"):
            continue
        splitContent = bagContent.split(" ")
        bagCount = int(splitContent[0])
        bagContentName = checkName(" ".join(splitContent[1:]))
        bagObj[bagContentName] = bagCount
    bagTypes[bagName] = bagObj
    
    #print(bagContents)

filledBags = {}

def filBags(bagType):
	if len(bagTypes[bagType]) == 0:
		return bagType
	else:
		subBagList = []
		for subBagType in bagTypes[bagType]:
			for x in range(0, bagTypes[bagType][subBagType]):
				subBagList.append(filBags(subBagType))
		return subBagList

def checkAmount(bagType, fbag, level=0):
	if type(fbag) is list or type(fbag) is dict:
		for item in fbag:
			tlevel = checkAmount(bagType, item, level)
			if (tlevel >= level):
				return tlevel +1
		return level
	else:
		if bagType == fbag:
			return 1
		else:
			return 0

bigx=0
for bag in bagTypes:
	filledBags[bag] = filBags(bag)
	x = (checkAmount("shiny gold bag", filledBags[bag]))
	if x > bigx:
		bigx=x
