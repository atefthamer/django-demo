alert("Hello World")

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

// matrix = async () => {
//     let res = await axios.get('http://localhost:8000/api/v1/airlines')
//         .then(function (response) {
//             console.log(response.data)
//             responseData = response.data;
//             console.log(responseData)
//         })
// }
// console.log(matrix)
// matrix()
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
axiosResponse().then(res => result = res)
console.log(result)