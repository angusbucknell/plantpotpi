//File switched to CSV, perhaps use https://www.papaparse.com/ to handle CSV to JSON?

//temp --> humidity --> soil moisture --> light
//Globally declares the mean measurements to be integers
avgTemp=0;
avgHum=0;
avgMoist=0;
avgLux=0;
$.get("testdata.txt",function(raw){//Uses the jQuery library to pass data from local text file to be processed as text
    data=raw.split("\n");//Constructs an array by separating the information within the file using new lines
    for(i=0;i<data.length-1;i++){//Constructs FOR loop spanning the length of the array of text data
        data[i]=data[i].split(",");//Splits each line into another array based on indentation
        /*data[i][3]=data[i][3].replace(/\r/gm,"")*/;}
    for(k=0;k<data.length-1;k++){//Finds the total values for each individual measurement from all the separate data records to later use in finding mean
        avgTemp+=parseInt(data[k][0]);
        avgHum+=parseInt(data[k][1]);
        avgMoist+=parseInt(data[k][2]);
        avgLux+=parseInt(data[k][3]);}},"text");
// Each new line of the text file represents a new record of data, including temperature, humidity, soil moisture, and lux
//Simulates records of a database
window.onload = function(){//When the page loads, and after the above is executed runs the function
    document.getElementById("tempdata").innerHTML=data[data.length-2][0]+"°C";
    //Chanages the HTML content of all elements with the ID of 'tempdata' with the data from the first index of the first subarray from the text file data
    document.getElementById("humdata").innerHTML=data[data.length-2][1]+"%";
    //Chanages the HTML content of all elements with the ID of humdata' with the data from the second index of the first subarray from the text file data
    document.getElementById("moistdata").innerHTML=data[data.length-2][2]+"%";
    //Chanages the HTML content of all elements with the ID of moistdata' with the data from the third index of the first subarray from the text file data
    document.getElementById("luxdata").innerHTML=data[data.length-2][3]+" lux";
    //Chanages the HTML content of all elements with the ID of 'luxdata' with the data from the fourth index of the first subarray from the text file data
    //The values of the parent array represent the different records of data input, with the top (0) being the most recent, so displays most recent statistics
    document.getElementById("avgTemp").innerHTML=Math.round(avgTemp / (data.length-1))+"°C";/*Calculates mean temperature using previously calculated total
                                                                                        and length of parent array, indicating how many sets of data*/

    document.getElementById("avgHum").innerHTML=Math.round(parseInt(avgHum) / (data.length-1))+"%";/*Calculates mean humidity using previously calculated total
                                                                                        and length of parent array, indicating how many sets of data*/
    document.getElementById("avgMoist").innerHTML=Math.round(avgMoist / (data.length-1))+"%";/*Calculates mean moisture level using previously calculated total
                                                                                        and length of parent array, indicating how many sets of data*/
    document.getElementById("avgLux").innerHTML=Math.round(avgLux / (data.length-1))+" lux";}/*Calculates mean light level using previously calculated total
                                                                                        and length of parent array, indicating how many sets of data*/
