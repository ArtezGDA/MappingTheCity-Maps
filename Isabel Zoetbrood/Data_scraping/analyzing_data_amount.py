import json 
jsonFile = "bronx.json"

with open(jsonFile, 'r') as inputFile:
		data = json.load(inputFile)
print "%d crimes in %s" % (len(data), jsonFile)

# Analyze the types of offenses

typeofoffense = []
# list of strings
OffensesAndTheirCount = []
# list of dictionairies

for crime in data:
	typeOfO = crime["Offense"]
	if typeOfO in typeofoffense:
		indeOfType = typeofoffense.index(typeOfO)
		offenseType = OffensesAndTheirCount[indeOfType]
		offenseType['count'] = offenseType['count'] + 1
	else: 
		offenseType = {}
		offenseType['name'] = typeOfO
		offenseType['count'] = 1
		OffensesAndTheirCount.append(offenseType)
		typeofoffense.append(typeOfO)

# print result
print OffensesAndTheirCount

