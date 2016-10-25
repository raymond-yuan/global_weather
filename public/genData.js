var cityData;

var oReq = new XMLHttpRequest();
oReq.onload = reqListener;
oReq.open("get", "city.list.json", true);
oReq.send();

function reqListener(e) {
    cityData = JSON.parse(this.responseText);
}
