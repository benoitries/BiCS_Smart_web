var used_label = ['27.03.2018', '27.03.2018']
var used_data = [65.0, 65.0]
 
var ctx = document.getElementById("myChart2"); 
var myChart = new Chart(ctx, { 
  type: 'line', 
  data: { 
    labels: used_label, 
    datasets: [ 
      {  
        borderColor: "#F2DEDE", 
        pointBorderColor: "#F2DEDE",
        pointBackgroundColor: "#F2DEDE",
        fill: true,
        backgroundColor: "rgba(242, 222, 222, 0.65)",
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
