import json


cityList = []
outstr = ""
for line in open('/Users/raymondyuan/Documents/Projects/globalweather/public/cityList.txt', 'r'):
    cityList.append(json.loads(line))

for cityInfo in cityList:
    outstr += str(cityInfo["_id"]) + ","

outstr = outstr[:-1]
textFile = open("Output.txt", "w")
textFile.write(outstr)
textFile.close()

# with open('/Users/raymondyuan/Documents/Projects/globalweather/public/city.list.json') as json_data:
# 	cityData = json.load(json_data)

print "finished"
