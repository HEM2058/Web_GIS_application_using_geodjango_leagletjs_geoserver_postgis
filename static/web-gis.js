//map print
// $('#map-print').click(function(){
//     window.print();
// });
L.control.browserPrint({position:'topright'}).addTo(map);

//adding fullscreen function
var mapid=document.getElementById('map');
function fullScreenView(){
    if(document.fullscreenElement)
    document.exitFullscreen();
    else
    mapid.requestFullscreen();
}

// measure in map
L.control.measure({
    primaryLengthUnit: 'kilometers',
    secondaryLengthUnit: 'meters',
    primaryAreaUnit: 'sqmeters',
    secondaryAreaUnit: undefined 
}).addTo(map);

//adding search bar
L.Control.geocoder().addTo(map);

//adding zoom to layer

$('#zoomToLayer').click(function(){
    map.setView([38.8610,  71.2761],7)
    })