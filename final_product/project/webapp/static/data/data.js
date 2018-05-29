var used_label = ['27.03.2018', '27.03.2018', '27.03.2018']
var used_data = [37.0, 38.0, 37.0]
 
var ctx = document.getElementById("myChart0"); 
var myChart = new Chart(ctx, { 
  type: 'line', 
  data: { 
    labels: used_label, 
    datasets: [ 
      {  
        borderColor: "#D9EDF7", 
        pointBorderColor: "#D9EDF7",
        pointBackgroundColor: "#D9EDF7",
        fill: true,
        backgroundColor: "rgba(217, 237, 247, 0.65)",
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
