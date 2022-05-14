var totalYears;
var startYear;
let endYear;
var difference;
var newCarsBox;
var txtNewInputBox;
var divTag;
var inputOfCars = [];
var index = 0;
var values;
let dataToBeSend;
var names;
var checkedValues;
var namesofcheck;
var totalSteel = [];



function createNewElement() {
    
    // totalYears=difference;
    startYear = parseInt(document.getElementById('Starting_Year').value);
    endYear = parseInt(document.getElementById('Ending_Year').value);
    console.log("Starting Year is"+startYear);
    console.log("Ending Year is"+endYear);
    if( endYear  <  startYear ) {
        alert("You Have Not Entered Valid Year");
    } else {

    difference = parseInt(endYear) - parseInt(startYear);
    console.log("Total Number of Column is"+difference);
     totalYears = difference;

    for(var i=0;i<difference;i++) { 
    // newCarsBox = document.createElement('input');
    // txtNewInputBox = document.createElement('input');
   
    divTag = document.createElement('div');
    // if (! /^[0-9]{11}$/.test(divTag)) {
    //     alert("Please input exactly 11 numbers!");
    //     return false;
    //   }
    
    
    console.log("Total NO Of Years is "+totalYears);
    // For Year
	// txtNewInputBox.innerHTML = " <input type='number' id='newInputBox' >";
    // For Number of cars


    // newCarsBox.innerHTML = " <input type='number'  id=index > "
    
    $('#data').append('<input type="number" placeholder="Enter Number Of Cars" name="value'+ i +'" pattern="[1-9]{1}[0-9]{7}"  id="carinput'+ i +'" />  ');
   
    
	// document.getElementById("data").appendChild(txtNewInputBox).placeholder=startYear++;

    // document.getElementById("data").appendChild(newCarsBox).placeholder=" Enter No Of Vehicle Here ";
    
    document.getElementById("data").appendChild(divTag);
   
    }

}

}



function TotalYears() {
    for(var i=0;i<=difference;i++){
        values = 'carinput' + i;
        inputOfCars[i] = parseInt(document.getElementById(values).value);
    }
    for(var j=0;j<i;j++) {
    console.log(inputOfCars[j]);
    }
}



function  checkingValues() {
    var checkboxSteel = document.getElementById("materialSteel")
    var checkboxPlastic = document.getElementById("materialPlastic")
    var checkboxIron  = document.getElementById("materialIron")
    var checkboxRubber = document.getElementById("materialRubber")
    var checkboxAluminium = document.getElementById("materialAluminium")
    var checkboxCopper = document.getElementById("materialCopper")
    var checkboxGlass = document.getElementById("materialGlass")

    var sch1 = document.getElementById("steelColHead")
    var pch1 = document.getElementById("plasticColHead")
    var ich1 = document.getElementById("ironColHead")
    var rch1 = document.getElementById("rubberColHead")
    var ach1 = document.getElementById("aluminiumColHead")
    var gch1 = document.getElementById("glassColHead")
    var cch1 = document.getElementById("copperColHead")

    var sch2 = document.getElementById("steelCol")
    var pch2 = document.getElementById("plasticCol")
    var ich2 = document.getElementById("ironCol")
    var rch2 = document.getElementById("rubberCol")
    var ach2 = document.getElementById("aluminiumCol")
    var gch2 = document.getElementById("glassCol")
    var cch2 = document.getElementById("copperCol")


    // steel
    if(checkboxSteel.checked == true) {
        sch1.style.display = "table-cell";
        sch2.style.display = "table-cell";
        sch2.style.width = "85px";
    } else {
        sch1.style.display = "none";
        sch2.style.display = "none";
    }




    if(checkboxPlastic.checked == true) {
        pch1.style.display = "table-cell";
        pch2.style.display = "table-cell" ;
        pch2.style.width = "85px";    
    } else {
        pch1.style.display = "none";
        pch2.style.display = "none";
    }




    // iron
    if(checkboxIron.checked == true) {
        ich1.style.display = "table-cell";
        ich2.style.display = "table-cell";
        ich2.style.width = "85px";
    } else {
        ich1.style.display = "none";
        ich2.style.display = "none";
    }
    
    // rubber
    if(checkboxRubber.checked == true) {
        rch1.style.display = "table-cell";
        rch2.style.display = "table-cell";
        rch2.style.width = "85px";
    } else {
        rch1.style.display = "none";
        rch2.style.display = "none";
    }

    // aluminium
    if(checkboxAluminium.checked == true) {
        ach1.style.display = "table-cell";
        ach2.style.display = "table-cell";
        ach2.style.width = "85px";
    } else {
        ach1.style.display = "none";
        ach2.style.display = "none";
    }
    
    // glass
    if(checkboxGlass.checked == true) {
        gch1.style.display = "table-cell";
        gch2.style.display = "table-cell";
        gch2.style.width = "85px";
    } else {
        gch1.style.display = "none";
        gch2.style.display = "none";
    }
    
    // copper
    if(checkboxCopper.checked == true) {
        cch1.style.display = "table-cell";
        cch2.style.display = "table-cell";
        cch2.style.width = "85px";
    } else {
        cch1.style.display = "none";
        cch2.style.display = "none";
    }

}


// document.addEventListener('DOMContentLoaded', function () {
//     const chart = Highcharts.chart('container-block', {
//         chart: {
//             type: 'bar'
//         },
//         title: {
//             text: 'Raw Material Consumption'
//         },
//         xAxis: {
//             categories: ['Steels', 'Platics', 'Iron', 'Rubber', 'Aluminium', 'Glass', 'Copper']
//         },
//         yAxis: {
//             title: {
//                 text: 'Demand over the Years'
//             }
//         },
//         series: [{
//             name: '2001-2002',
//             data: [2154365, 2543655, 3054365, 3600000]
//         }, {
//             name: '2002-2003',
//             data: [2400000, 2700000, 3000000]
//         }]
//     });
// });




// var username='{{Years}}'




// google.load('visualization', '1', {packages: ['corechart', 'bar']});
// google.setOnLoadCallback(drawBasic);

// function drawBasic() {

//     var data = google.visualization.arrayToDataTable([
//         ['Year', 'Population',],
//         ['2000-01', 2000],
    
//     ]);

//     var options = {
//         title: 'Population of People with Disabilities',
//         chartArea: {width: '50%'},
//         hAxis: {
//             title: 'Total Population',
//             minValue: 0
//         },
//         vAxis: {
//             title: 'Year'
//         }
//     };

//     var chart = new google.visualization.BarChart(document.getElementById('chart_div'));

//     chart.draw(data, options);
// }





//     class MyCharts{

//       constructor(XData, YData)
//       {
//         this.XData = XData;
//         this.YData = YData;
//       }

//       createGraph()
//       {
//         var data =
//                 {
//                   labels: this.XData,
//                   series:[
//                           this.YData
//                   ]
//                 }
//         new Chartist.Line('.ct-chart', data);
//       }
//     }

//   var XData= ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'];
//     var YData = [5, 2, 4, 2, 0];
//     var data = $.get('steel_chart');
//     var tm = data.done(function (resp) {
//       console.log("JSON DATA", resp.steel_chart);
//       var obj = new MyCharts(XData, resp.steel_chart);
//       obj.createGraph();

//     })
