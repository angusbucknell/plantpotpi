//Data is inputed as: temp, humidity, moisture, lux
//Each new line of the text file represents a new record of data from a different time
avgTemp = 0;
avgHum = 0;
avgMoist = 0;
avgLux = 0;
//Lines 2 - 5 declares average vars globally
$.get("testdata.txt", function(raw){
//Uses jQuery to pass data from local text file to function
  data = raw.split("\n");
//Constructs an array by separating the information within the file using new lines
  for(i = 0, i < data.length - 1; i++){
//FOR loop spanning length of text data arrat
    data[i] = data[i].split("\t");}
//Splits each line of data into subarrays based on indentation
  for(k = 0; k < data.length - 1; k++){
//Finds the total value of each individual measurement from all records
    avgTemp += parseInt(data[k][0]);
    avgHum += parseInt(data[k][1]);
    avgMoist += parseInt(data[k][2]);
    avgLux += parseInt(data[k][3]);}}, "test");

window.onload = function(){
//Executes function once the HTML webpage has loaded
  document.getElementById("tempdata").innerHTML = data[data.length-2][0]+"°C";
//Changes HTML element to show the temperature from the most recent record
  document.getElementById("humdata").innerHTML = data[data.length-2][1]+"%";
//Changes HTML element to show the humidity from the most recent record
  document.getElementById("moistdata").innerHTML = data[data.length-2][2]+"%";
//Changes HTML element to show the soil moisture from the most recent record
  document.getElementById("luxdata").innerHTML = data[data.length-2][3]+" lux";
//Changes HTML element to show the light data from the most recent record
  
  document.getElementById("avgTemp").innerHTML = Math.round(avgTemp / (data.length-1))+"°C";
//Calculates mean temperature from previously calculated sum and switches it from blank placeholder
  document.getElementById("avgHum").innerHTML = Math.round(avgHum / (data.length-1))+"%";
//Calculates mean humidity from previously calculated sum and switches it from blank placeholder
  document.getElementById("avgMoist").innerHTML = Math.round(avgMoist / (data.length-1))+"%";
//Calculates mean moisture from previously calculated sum and switches it from blank placeholder
  document.getElementById("avgLux").innerHTML = Math.round(avgLux / (data.length-1))+" lux";
//Calculates mean lux value from previously calculated sum and switches it from blank placeholder
}
