var used_label = ['27.03.2018', '27.03.2018']
var used_data = [6.0, 6.0]
 
var ctx = document.getElementById("myChart1"); 
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
