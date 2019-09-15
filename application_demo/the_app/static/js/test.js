//alert("Hello World")

var responseData = {}

async function axiosResponse() {
    let res = await axios.get('http://localhost:8000/api/v1/airlines')
    // .then(function (response) {
    //     console.log(response.data)
    //     responseData = response.data;
    //     console.log(responseData)
    // })
    this.responseData = res.data
    return this.responseData
}
// console.log(responseData)
//debug.log("THe response data -->> " + responseData)
//alert("H");

// var theResponse = {}
// async function result() {
//     theResponse = await axiosResponse()
//     //console.log(theResponse)

// }

// asynget = async () => {
//     let res = await axios.get('http://localhost:8000/api/v1/airlines')
//         .then(function (response) {
//             console.log(response.data)
//             responseData = response.data;
//             console.log(responseData)
//         })
// }
// console.log(asyncget)
// asyncget()
// // result()
// console.log(theResponse)
// console.log(theResponse)
// console.log(responseData)
// console.log(responseData.length)

// let d = {}

// function jqueryget() {
//     $.when(
//         $.ajax({
//             url: 'http://localhost:8000/api/v1/airlines',
//             dataType: 'json',
//             type: 'get',
//             cache: false,
//             success: function (data) {
//                 console.log("this is jquery")
//                 console.log(data)
//                 //console.log(raspi_time);
//                 //onsole.log(raspi_value);
//                 d = data

//             }
//         })
//     )
// }
// console.log("D")
// console.log(d)
let result = {}
// axiosResponse().then(res => console.log(res))
document.addEventListener("DOMContentLoaded", function (event) {
    var ctx_first = document.getElementById("firstChart").getContext('2d');
    var ctx_second = document.getElementById("secondChart").getContext('2d');
    var ctx_third = document.getElementById("thirdChart").getContext('2d');

    let chart_options = {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                }
            }],
            xAxes: [{}]
        },
        animation: false,
    }

    axiosResponse().then(res => {
        let airlines = []
        let incidents_85_99 = []
        let incidents_00_14 = []
        let avail_set_km_per_week = []
        for (let i = 0; i < res.length; i++) {
            let obj = res[i]
            airlines.push(res[i].airline)
            incidents_85_99.push(res[i].incidents_85_99)
            incidents_00_14.push(res[i].incidents_00_14)
            avail_set_km_per_week.push(res[i].avail_set_km_per_week)
        }
        var chart_a = new Chart(ctx_first, {
            type: 'bar',
            data: {
                labels: airlines,
                datasets: [{
                    label: 'Total number of incidents, 1985–1999',
                    data: incidents_85_99,
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderWidth: 1
                }]
            },
            options: chart_options
        })

        var chart_b = new Chart(ctx_second, {
            type: 'line',
            data: {
                labels: airlines,
                datasets: [{
                    label: 'Total number of incidents, 1985–1999',
                    data: incidents_85_99,
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderWidth: 1
                }, {
                    label: 'Total number of incidents, 2000–2014',
                    data: incidents_00_14,
                    backgroundColor: 'rgba(255, 0, 0, 0.5)',
                    borderWidth: 1
                }]
            },
            options: chart_options
        })

        var chart_c = new Chart(ctx_third, {
            type: 'line',
            data: {
                labels: airlines,
                datasets: [{
                    label: 'Available seat kilometers flown every week per airline',
                    data: avail_set_km_per_week,
                    backgroundColor: 'rgba(0, 51, 0, 0.7)',
                    borderWidth: 1,
                }]
            },
            options: chart_options
        })
    })
})


console.log(result)