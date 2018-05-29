var used_label = ['27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018', '27.03.2018']
var used_data = [40.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 52.0, 55.0]
 
var ctx = document.getElementById("myChart4"); 
var myChart = new Chart(ctx, { 
  type: 'line', 
  data: { 
    labels: used_label, 
    datasets: [ 
      {  
        borderColor: "#DFF0D8", 
        pointBorderColor: "#DFF0D8",
        pointBackgroundColor: "#DFF0D8",
        fill: true,
        backgroundColor: "rgba(223, 240, 216, 0.65)",
        label: 'Value',
        data: used_data 
      } 
    ] 
  }, 
  options: { 
      scales: {
          yAxes: [{
              ticks: {
                  beginAtZero: true
              }
          }]
      }
  }
}); 
