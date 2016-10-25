import requests
import json


with open("Output.txt", "r") as cityIdTxt:
    data = cityIdTxt.read()

cityArray = data.split(",")
city100Array = []
outstr = ""
for i in range(len(cityArray)):
    if ((i + 1) % 100) == 0:
        outstr = outstr[:-1]
        city100Array.append(outstr)
        outstr = ""
    else:
        outstr += cityArray[i] + ","


# cityIdList = "1463749,295582,295582,295582,295582,295582,295582,295582,295582,2878044,524901,703448,2643743"
appId = "9402dfca6e52269cf255dce61e9ad819"
cityList = []

for cityGrp in city100Array:
    response = requests.get("http://api.openweathermap.org/data/2.5/group?id="+ cityGrp +"&units=imperial&appid=" + appId)
    print response.status_code
    if response.status_code == 200:
        outJson = json.loads(response.content)
        cityList.extend(outJson["list"])

worldArray = []
for city in cityList:
    worldArray.append(city["coord"]["lat"])
    worldArray.append(city["coord"]["lon"])
    worldArray.append(city["main"]["temp"])

textFile = open("allTemp.txt", "w")
textFile.write(str(worldArray))
textFile.close()
