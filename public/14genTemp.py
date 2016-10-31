import json
import numpy as np

cityList = []
outJson = []
temp = []
for line in open('/Users/raymondyuan/Documents/Projects/globalweather/public/weather_14.json', 'r'):
    cityList.append(json.loads(line))

print cityList[0]["main"]

for cityInfo in cityList:
    val = (cityInfo["main"]["temp"] - 273.15)/200.0
    if (val) < 1 :
        outJson.append(cityInfo["city"]["coord"]["lat"])
        outJson.append(cityInfo["city"]["coord"]["lon"])
        outJson.append(val)
        temp.append(val)

minTemp = min(temp)
maxTemp = max(temp)

divs = (maxTemp - minTemp)/11.0
tempBins = []
for i in range(12):
    tempBins.append(minTemp + i*divs)

def digitize(num, inList):
    for i in range(len(inList) - 1):
        if num > inList[i] and num <= inList[i + 1]:
            return i + 1
    return len(inList)

for i in range(len(outJson), 2, -1):
    if i % 3 == 0:
        # print np.array(outJson[i - 1])
        # print np.digitize(np.array(outJson[i - 1]), tempBins)
        val = digitize(outJson[i-1], tempBins)#list(np.digitize(np.array(outJson[i - 1]), tempBins))[0]
        outJson.insert(i, val)


with open('14Temp.json', 'w') as f:
     json.dump(outJson, f)
# textFile = open("14Temp.txt", "w")
# textFile.write(str(outJson))
# textFile.close()

# with open('/Users/raymondyuan/Documents/Projects/globalweather/public/city.list.json') as json_data:
# 	cityData = json.load(json_data)

print "finished"
