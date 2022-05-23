function showCont1(){
    document.querySelector("#move-cont1").style.display="block"
    document.querySelector("#move-cont3").style.display="none"
}
function showCont3(){
    document.querySelector("#move-cont1").style.display="none"
    document.querySelector("#move-cont3").style.display="block"
    $.ajax({
        url:"/seoul/chartshow",
        type:"get",
        data:{},
        dataType:"json",
        success:function(data){
            // barChart();

                shapeChartData = {
                labels: ['강남구','강동구','강북구','강서구','관악구','광진구','구로구','금천구','노원구','도봉구','동대문구','동작구','마포구','서대문구','서초구','성동구','성북구','송파구','양천구','영등포구','용산구','은평구','종로구','중구','중랑구'],
                // labels: ['강남구','강동구','강북구'],
                datasets: [{
                    label: '코로나 확진자',
                    data: data.dailydata,
                    // data: [500,300,200],
                    borderColor: 'rosybrown',
                    backgroundColor: 'rosybrown',
                    borderWidth: 4
                }]
            }
            barChart()
        },
        error:function(){
            alert(data);
        }})
}



function barChart() {
    // id myChart의 html 삭제
    // $('#canvas2').remove(); 
    // id fchart의 자식으로 <canvas id="myChart"><canvas> 생성
    // $('#canvas2').append('<canvas id="canvas2"></canvas>');
    // var ctx = document.getElementById('canvas2').getContext('2d');
    var ctx = document.getElementById('canvas3');
    var myChart = new Chart(ctx, {
    type: 'bar',
    data: shapeChartData,
        options:  {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}//createChart 
