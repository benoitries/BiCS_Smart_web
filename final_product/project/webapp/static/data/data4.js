var used_label = ['27.03.2018', '27.03.2018']
var used_data = [33.0, 46.0]
 
var ctx = document.getElementById("myChart3"); 
var myChart = new Chart(ctx, { 
  type: 'line', 
  data: { 
    labels: used_label, 
    datasets: [ 
      {  
        borderColor: "#FCF8E3", 
        pointBorderColor: "#FCF8E3",
        pointBackgroundColor: "#FCF8E3",
        fill: true,
        backgroundColor: "rgba(252, 248, 227, 0.65)",
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
