window.onload = function() {
  var temp = [19,19,19,20,21,21,22,20,19,16,15,14];
  var humidity = [40,40,40,60,50,40,30,20,10,100,70,60];
  var moisture = [90,80,70,60,50,40,30,20,10,80,70,80];
  var lux = [60,60,60,70,70,70,80,80,70,70,60,50];
  var dates = ["January","February","March","April","May","June","July","August","September","October","November","December"];
  
  var context = document.getElementbyId("myChart");
  var myChart = new Chart(context, {
    type: "line",
    data:{
      labels:dates,
      datasets:[
        {
          data:temp,
          label:"Temeprature",
          borderColor:"#3e95cd",
          fill:false,
          yAxisID:"Num"
        },
        {
          data:humidity,
          label:"Humidity",
          borderColor:"#8e5ea2",
          fill:false,
          yAxisID:"Per"
        },
        {
          data:moisture,
          label:"Soil Moisture",
          borderColor:"#3cba9f",
          fill:false,
          yAxisID:"Per"
        },
        {
          data:lux
          label:"Light",
          borderColor:"#e8c3b9",
          fill:false,
          yAxisID:"Per"
        }
      ]
    },
    options:{
      scales:{
        yAxes: [{
          id:"Num",
          type:"linear",
          position:"left"
        },
        {
          id:"Per",
          type:"linear",
          position:"left"
        }]
      }
    }
  });
}
