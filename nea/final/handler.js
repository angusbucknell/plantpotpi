//temp --> humidity --> soil moisture --> light
//Globally declares the mean measure to be integers

window.onload = function () {
    //Executes the function once the page has loaded
    temp_dyn = new Array();
    humidity_dyn = new Array();
    moisture_dyn = new Array();
    date_dyn = new Array();
    lux_dyn = new Array();
    avgTemp = 0;
    avgHum = 0;
    avgMoist = 0;
    avgLux = 0; 
    $.get("testdata3.txt", function (raw) {
    //Uses jQuery to pass data from local text file onto website
    info = raw.split("\n");
    //Constructs array by separating the data within the text file by new line
    for (i = 0; i < info.length - 1; i++) {
      //Constructs FOR loop spanning the length of the array
      info[i] = info[i].split(",");
    }
    //Splits each section of each line into subarrays separated by commas
    document.getElementById("tempdata").innerHTML = info[info.length - 2][0] + "°C";
    document.getElementById("humdata").innerHTML = info[info.length - 2][1] + "%";
    document.getElementById("moistdata").innerHTML = info[info.length - 2][2] + "%";
    document.getElementById("luxdata").innerHTML = info[info.length - 2][3] + " lux";
    //Overrides the HTML content of all templates with respective identifiers with the correct element of the subarray,
    //within the last (most frequent) element of the parent array
    for (k = 0; k < info.length - 1; k++) {
      avgTemp += parseInt(info[k][0]);
      temp_dyn.push(info[k][0])
      avgHum += parseInt(info[k][1]);
      humidity_dyn.push(info[k][1])
      avgMoist += parseInt(info[k][2]);
      moisture_dyn.push(info[k][2])
      avgLux += parseInt(info[k][3]);
      lux_dyn.push(info[k][3])

      date = info[k][4].split("");
      months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "Decmeber"];
      month = months[parseInt(date[5] + date[6]) - 1];
      day = date[8]+date[9];
      year = date[0]+date[1]+date[2]+date[3];
      date_dyn.push(day+" "+month+" "+year);

    }
    //Calculates the total values for each measurement from all separate data records, used for calculating the mean
    //Also appends each data value to the arrays needed to generate the graph
    document.getElementById("avgTemp").innerHTML = Math.round(avgTemp / (info.length - 1)) + "°C";
    document.getElementById("avgHum").innerHTML = Math.round(avgHum / (info.length - 1)) + "%";
    document.getElementById("avgMoist").innerHTML = Math.round(avgMoist / (info.length - 1)) + "%";
    document.getElementById("avgLux").innerHTML = Math.round(avgLux / (info.length - 1)) + " lux";
    //Overrides HTML content with templates for mean data identifiers, correct to nearest integer
  }, "text");
  /*Below is all for generating the static chart, for now static data is used
  temp = [19, 19, 19, 20, 21, 21, 22, 20, 19, 16, 15, 14];
  humidity = [40, 40, 40, 60, 50, 40, 30, 20, 10, 100, 70, 60];
  moisture = [90, 80, 70, 60, 50, 40, 30, 20, 10, 80, 70, 80];
  lux = [60, 60, 60, 70, 70, 70, 80, 80, 70, 70, 60, 50];
  dates = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];*/
  //Defines static arrays of data to display on the graph
  temperature_Chart = new Chart(document.getElementById("temperatureChart"), {
  //Defines a new chart for the HTML canvas region using Chart.js
    type: "line",
  //Specifies it is a line chart, rather than bar or pie or other types
    data: {
      labels: date_dyn,
      //Specifies that the dates array will be used for x-axis
      datasets: [{
          data: temp_dyn,
          label: "Temeprature",
          borderColor: "#3e95cd",
          fill: false
        }]
      //Specifies the lines needed to be drawn, where the data is held, and cosmetic values
    }
  });
  humidity_Chart = new Chart(document.getElementById("humidityChart"), {
    type: "line",
    data: {
      labels: date_dyn,
      datasets: [{
        data: humidity_dyn,
        label: "Humidity",
        borderColor:"#8e5ea2",
        fill: false
      },{
        data: moisture_dyn,
        label: "Soil Moisture",
        borderColor: "#3cba9f",
        fill: false
      },{
        data: lux_dyn,
        label: "Light",
        borderColor: "#e8c3b9",
        fill: false
      }]
    }
  });

}