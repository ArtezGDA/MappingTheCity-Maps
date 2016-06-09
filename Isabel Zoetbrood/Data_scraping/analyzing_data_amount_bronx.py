import json 
jsonFile = "bronx.json"

with open(jsonFile, 'r') as inputFile:
		data = json.load(inputFile)
print "%d crimes in %s" % (len(data), jsonFile)


hourofoccurence = []
HourOccurenceAndTheirCount = []

for crime in data:
    HourOfO = hour["Occurrence Hour"]
    if HourOfO in  hourofoccurence:
        indexOfOccurence = hourofoccurence.index(HourOfO)
        hourtype = HourOccurenceAndTheirCount [indexOfOccurence]
        hourtype['count'] = hourtype['count'] +1		
    else: 
		offenseType = {}
		offenseType['name'] = typeOfO
		offenseType['count'] = 1
		OffensesAndTheirCount.append(offenseType)
		typeofoffense.append(typeOfO)


print OffensesAndTheirCount
print HourOccurenceAndTheirCount


