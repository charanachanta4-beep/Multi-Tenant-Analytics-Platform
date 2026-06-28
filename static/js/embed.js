const socket = io();

const ctx=document
.getElementById("revenueChart")
.getContext("2d");

const revenueChart=new Chart(ctx,{

    type:"line",

    data:{

        labels:labels,

        datasets:[{

            label:"Revenue",

            data:revenueData,

            borderWidth:3

        }]

    }

});

socket.on("new_metric",(data)=>{

    document.getElementById("revenue").innerHTML=
    "₹"+data.revenue;

    document.getElementById("visitors").innerHTML=
    data.visitors;

    document.getElementById("orders").innerHTML=
    data.orders;

    document.getElementById("profit").innerHTML=
    "₹"+data.profit;

    revenueChart.data.labels.push("Now");

    revenueChart.data.datasets[0].data.push(data.revenue);

    revenueChart.update();

});