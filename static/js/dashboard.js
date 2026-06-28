// -----------------------------
// Socket Connection
// -----------------------------

const socket = io();

socket.on("connect", () => {
    console.log("✅ Socket Connected");
});

// -----------------------------
// Revenue Line Chart
// -----------------------------

const revenueCtx = document
    .getElementById("revenueChart")
    .getContext("2d");

const revenueChart = new Chart(revenueCtx, {

    type: "line",

    data: {

        labels: [...labels],

        datasets: [

            {

                label: "Revenue",

                data: [...revenueData],

                borderColor: "#4F46E5",

                backgroundColor: "rgba(79,70,229,0.15)",

                fill: true,

                borderWidth: 3,

                tension: 0.35,

                pointRadius: 5,

                pointHoverRadius: 7

            }

        ]

    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        plugins: {

            legend: {

                display: true

            }

        },

        scales: {

            y: {

                beginAtZero: true

            }

        }

    }

});

// -----------------------------
// Visitors vs Orders
// -----------------------------

const comparisonCtx = document
    .getElementById("comparisonChart")
    .getContext("2d");

const comparisonChart = new Chart(comparisonCtx, {

    type: "bar",

    data: {

        labels: [...labels],

        datasets: [

            {

                label: "Visitors",

                data: [...visitorsData],

                backgroundColor: "#06B6D4"

            },

            {

                label: "Orders",

                data: [...ordersData],

                backgroundColor: "#10B981"

            }

        ]

    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        plugins: {

            legend: {

                display: true

            }

        }

    }

});

// -----------------------------
// Live Socket Updates
// -----------------------------

socket.on("new_metric", function(data){

    console.log("📊 New Metric", data);

    // KPI Cards

    document.getElementById("revenue").innerHTML =
        "₹" + Number(data.revenue).toLocaleString();

    document.getElementById("visitors").innerHTML =
        data.visitors;

    document.getElementById("orders").innerHTML =
        data.orders;

    document.getElementById("profit").innerHTML =
        "₹" + Number(data.profit).toLocaleString();

    // Revenue Chart

    revenueChart.data.labels.push("Now");

    revenueChart.data.datasets[0].data.push(data.revenue);

    revenueChart.update();

    // Comparison Chart

    comparisonChart.data.labels.push("Now");

    comparisonChart.data.datasets[0].data.push(data.visitors);

    comparisonChart.data.datasets[1].data.push(data.orders);

    comparisonChart.update();

    // Metrics Table

    const tbody = document.getElementById("metricsTable");

    if(tbody){

        const row = document.createElement("tr");

        row.innerHTML = `

            <td>${new Date().toLocaleString()}</td>

            <td>${data.revenue}</td>

            <td>${data.visitors}</td>

            <td>${data.orders}</td>

            <td>${data.profit}</td>

        `;

        tbody.prepend(row);

    }

});

// -----------------------------
// Search Table
// -----------------------------

const search = document.getElementById("search");

if(search){

    search.addEventListener("keyup", function(){

        const filter = this.value.toLowerCase();

        const rows =
            document.querySelectorAll("#metricsTable tr");

        rows.forEach((row)=>{

            row.style.display =
                row.innerText.toLowerCase().includes(filter)
                ? ""
                : "none";

        });

    });

}

// -----------------------------
// Counter Animation
// -----------------------------

document.querySelectorAll(".card h2").forEach((card)=>{

    let original = card.innerText;

    let numeric = Number(
        original.replace(/[^0-9.]/g,"")
    );

    if(isNaN(numeric))
        return;

    let current = 0;

    let increment = numeric / 50;

    function animate(){

        current += increment;

        if(current >= numeric){

            card.innerText = original;

            return;

        }

        if(original.includes("₹")){

            card.innerText =
                "₹" +
                Math.floor(current).toLocaleString();

        }

        else{

            card.innerText =
                Math.floor(current).toLocaleString();

        }

        requestAnimationFrame(animate);

    }

    animate();

});

// -----------------------------
// Greeting
// -----------------------------

const hour = new Date().getHours();

let greeting = "Welcome";

if(hour < 12)

    greeting = "Good Morning";

else if(hour < 17)

    greeting = "Good Afternoon";

else

    greeting = "Good Evening";

const heading =
document.querySelector(".topbar h2");

if(heading){

    heading.innerHTML =
        greeting +
        ", " +
        heading.innerHTML.replace("Welcome,", "");

}