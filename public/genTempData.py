import requests
import json


with open("Output.txt", "r") as cityIdTxt:
    data = cityIdTxt.read()

cityArray = data.split(",")
city100Array = []
outstr = ""
for i in range(len(cityArray)):
    if ((i + 1) % 25) == 0:
        outstr = outstr[:-1]
        city100Array.append(outstr)
        outstr = ""
    else:
        outstr += cityArray[i] + ","
n = len(city100Array)
print n
# print city100Array[1], city100Array[n/4], city100Array[n/2], city100Array[3*n/4]

def checkFunc(response_in, cityList):
    if response_in.status_code == 200:
        try:
            outJson = json.loads(response_in.content)
            cityList.extend(outJson["list"])

        except:
            print "unknown error occured!"
            worldArray = []
            for city in cityList:
                worldArray.append(city["coord"]["lat"])
                worldArray.append(city["coord"]["lon"])
                worldArray.append(city["main"]["temp"])

            textFile = open("allTemp.txt", "w")
            textFile.write(str(worldArray))
            textFile.close()

# cityIdList = "1463749,295582,295582,295582,295582,295582,295582,295582,295582,2878044,524901,703448,2643743"
appId = "9402dfca6e52269cf255dce61e9ad819"
appId2 = "ad57368f1e9e14a380336923d305e431"
appId3 = "164c9b25b082a4ec251f44d0038621a1"
appId4 = "fdbfa83f04042c038b40b1b6b2585a52"

cityList = []
count = 0
for cityGrp in city100Array:
    try:
        response = requests.get("http://api.openweathermap.org/data/2.5/group?id="+ cityGrp+"&units=imperial&appid=" + appId)
        print response.status_code
        checkFunc(response, cityList)
    except:
        print "broken shit"


# for i in range(n/4):
#     count += 1
#     try:
#         response = requests.get("http://api.openweathermap.org/data/2.5/group?id="+ city100Array[i] +"&units=imperial&appid=" + appId)
#     except:
#         print "response broke "
#     try:
#         response2 = requests.get("http://api.openweathermap.org/data/2.5/group?id="+ city100Array[i + n/4] +"&units=imperial&appid=" + appId2)
#     except:
#         print "response2 broke "
#     try:
#         response3 = requests.get("http://api.openweathermap.org/data/2.5/group?id="+ city100Array[i + n/2] +"&units=imperial&appid=" + appId3)
#     except:
#         print "response3 broke "
#     try:
#         response4 = requests.get("http://api.openweathermap.org/data/2.5/group?id="+ city100Array[i + 3*n/4] +"&units=imperial&appid=" + appId4)
#     except:
#         print "response4 broke "
#     print response.status_code, response2.status_code, response3.status_code, response4.status_code
#     checkFunc(response, cityList)
#     checkFunc(response2, cityList)
#     checkFunc(response3, cityList)
#     checkFunc(response4, cityList)


worldArray = []
for city in cityList:
    worldArray.append(city["coord"]["lat"])
    worldArray.append(city["coord"]["lon"])
    worldArray.append(city["main"]["temp"])

textFile = open("allTemp.txt", "w")
textFile.write(str(worldArray))
textFile.close()
